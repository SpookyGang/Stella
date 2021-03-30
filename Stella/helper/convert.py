import math

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

def convert_time(given_time, time_format):
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
