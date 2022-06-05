import math

def convert_size_mb(bytes): 
    return round(bytes/1048576, 2)

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("b", "kb", "mb", "gb", "tb", "pb", "eb", "zb", "yb")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s%s" % (s, size_name[i])

def s_between(d1, d2):
    time_dif = d1-d2
    seconds = time_dif.total_seconds()
    return seconds