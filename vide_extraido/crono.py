import datetime
import time
i=0  
while True :
     
    time.sleep(1)
    print('total segundos',i)
    x= datetime.timedelta(seconds=i)
    i +=1
    print(x)
