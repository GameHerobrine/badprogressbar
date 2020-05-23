from os import system,name
import time
i=0
while i <= 25:
    i=i+4
    #print(i) debug =D
    print('#'*i)
    time.sleep(1)
    if name == 'nt': 
        system('cls') 
  
    else: 
        system('clear')

        
