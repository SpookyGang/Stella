import importlib
from os.path import dirname
from sys import platform

from Stella import StellaCli
from Stella import scheduler
from Stella.plugins import ALL_MODULES


IMPORTED = {}
HELPABLE = {}
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
    
    if hasattr(imported_module, "__stats__"):
        STATS.append(imported_module)

    if hasattr(imported_module, "__user_info__"):
        USER_INFO.append(imported_module)
    
    

if __name__ == "__main__":
    scheduler.start()
    StellaCli.run()
