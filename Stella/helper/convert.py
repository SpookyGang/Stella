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


import math

def convert_time(given_time: int, time_format: str):
    week = 518400 # 518400 seconds in a week
    day = 86400 # 86400 seconds in a day
    hour = 3600 # 3600 seconds in a hour
    minute = 60 # 60 seconds in a minute

    if time_format == 'w':
        cal_time = given_time * week 
    elif time_format == 'd':
        cal_time = given_time * day 
    elif time_format == 'h':
        cal_time = given_time * hour
    elif time_format == 'm':
        cal_time = given_time * minute
    
    return cal_time

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])