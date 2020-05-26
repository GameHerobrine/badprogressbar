#started 23.05.2020 // i currently dont remember day when i started
#updated 26.05.2020 // 
#finished 23.05.2020 //project finished, 1st succeseful run

#last version 1.0_01 //added comments
from os import system,name # import system for clear and cls and name of os
import time #importing time(for delay)
i=0 #define for progressbar
while i <= 25: #start progressbar
    i=i+4 #one step
    #print(i) #debug =D  
    print('#'*i) #printing '#'
    time.sleep(1) #delay
    if name == 'nt':  #if windows do cls
        system('cls') 
    else:  #if other os do clear
        system('clear')

        
