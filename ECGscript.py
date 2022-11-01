import time
import random
import matplotlib.pyplot as plt
from csv import writer

def genECG(oclock, prev):
    if oclock == 0 :
        prev -= 20
    if oclock == 8 :
        prev += 30
    if oclock == 10 :
        prev -= 5
    if oclock == 13 :
        prev += 10
    if oclock == 15 :
        prev -= 10
    if oclock == 17 :
        prev += 10
    if oclock == 21 :
        prev -= 10
    prev += random.randint(-2,2)
    print('%.2d : %d'%(oclock, prev))
    if prev <= 50 or prev >= 100 :
        print("Danger!")
        if prev <= 50 :
            prev += 10
        else :
            prev -= 10
    return(prev)

oclock = 0
prev = 80

while(1):
    prev = genECG(oclock, prev)
    oclock += 1
    if oclock == 24 :
        oclock = 0
 
    prev=[prev]
    
    with open('scriptdata.csv','a', newline = '') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(prev)
        f_object.close()
    prev = prev[0]
    time.sleep(2)
