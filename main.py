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
            if len(key)<=32:
                dict[key]=1
        else:
            print('Memory limit exceed should be less than 1 gb')



# read operation

def read(key):
    # check the key in database
    if key not in dict:
        print("key is not present in database enter a valid key")
    else:
        a=dict[key]
        # reading the time of the key 
        if a[1]!==0:
            if time.time()<a[1]:
                # get the value in json format
                string=str(key)+":"+str(a[0])
                return string
            else:
                print("time is expired")
        else:
            string=str(key)+":"+str(a[0])
            return string


# delete operation in database

def delete(key):
    # check the key in database
    if key not in dict:
        print("key is not present in database enter a valid key")
    else:
        a=dict[key]
        if a[1]!==0:
            if time.time()<a[1]:
                del dict[key]
                
        

             


            
