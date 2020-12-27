# threding allows to perform a multiple task and functions 
import threading
# from threading import*

import time

# to store the key value and pair the data structure in python called dictionary is created
dict={}

def create(key,value,timeout=0):
    # check the existig key
    if key in dict:
        print("keys is already exists")
    else:
        # checking dictionary length and key valuse is upto to memory limit is 1gb and 16 kb 
        if len(dict)<(1024*1020*1024) and value<=(16*1024*1024):
            # time to live property
            if timeout==0:
                d=[value,timeout]
            else:
                d=[value,time.time()+timeout]

            
