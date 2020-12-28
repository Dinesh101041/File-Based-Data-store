# threading aloows to perfrom multiple task
import threading 
from threading import*

import time

#dictionary is data structure of python which store as key and value
dictionary={} 

# create function is to create a data

def create(key,value,timeout=0):
    if key in dictionary:
        print("The key is already exists create new value") 
    else:
        # isalpha()is to check whether the key is only alphabets
        if(key.isalpha()):
            #constraints for file size less than 1GB and Jasonobject value less than 16KB 
            if len(dictionary)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    dictionary[key]=l
            else:
                print("memorylimit exceeed ")#error message2
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3

#reading the values
            
def read(key):
    if key not in dictionary:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=dictionary[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#deleting the values

def delete(key):
    if key not in dictionary:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=dictionary[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del dictionary[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            del dictionary[key]
            print("key is successfully deleted")


# modifiying the databse
def modify(key,value):
    b=dictionary[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in dictionary:
                print("error: given key does not exist in database. Please enter a valid key") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                dictionary[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #error message5
    else:
        if key not in d:
            print("error: given key does not exist in database. Please enter a valid key") #error message6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            dictionary[key]=l
