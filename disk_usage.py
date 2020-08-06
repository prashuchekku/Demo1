# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 12:10:48 2020

@author: prash
"""
import shutil

def check_disk_usage(disk,min_absolute,min_percent):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.total - du.used
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True

if not check_disk_usage("/",2,10):
    print("Error: Not enough disk space")
print("Everything ok")
    