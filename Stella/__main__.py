#    Stella (Development)
#    Copyright (C) 2021 - meanii (Anil Chauhan)
#    Copyright (C) 2021 - SpookyGang (Neel Verma, Anil Chauhan)

#    This program is free software; you can redistribute it and/or modify 
#    it under the terms of the GNU General Public License as published by 
#    the Free Software Foundation; either version 3 of the License, or 
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import importlib
from os.path import dirname
from sys import platform

from Stella import StellaCli, scheduler
from Stella.plugins import ALL_MODULES

IMPORTED = {}
HELPABLE = {}
SUB_MODE = {}
HIDDEN_MOD = {}

STATS = []
USER_INFO = []

if platform == "linux" or platform == "linux2":
    path_dirSec = '/'
elif platform == "win32":
    path_dirSec = '\\'

cdir = dirname(__file__) 
for mode in ALL_MODULES: 
    module = mode.replace(cdir, '').replace(path_dirSec, '.')
    imported_module = importlib.import_module('Stella' + module)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__
 
    if not imported_module.__mod_name__.lower() in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("Can't have two modules with the same name! Please change one")

    if hasattr(imported_module, "__help__") and imported_module.__help__:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module
    
    if hasattr(imported_module, "__sub_mod__") and imported_module.__sub_mod__:
        SUB_MODE[imported_module.__mod_name__.lower()] = imported_module
    
    if hasattr(imported_module, "__hidden__") and imported_module.__hidden__:
        HIDDEN_MOD[imported_module.__mod_name__.lower()] = imported_module.__hidden__

    if hasattr(imported_module, "__stats__"):
        STATS.append(imported_module)

    if hasattr(imported_module, "__user_info__"):
        USER_INFO.append(imported_module)

print(HIDDEN_MOD)

if __name__ == "__main__":
    scheduler.start()
    StellaCli.run()
