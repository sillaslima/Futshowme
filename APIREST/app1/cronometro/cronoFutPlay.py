import os
import datetime
import time

def comecar():
        with open('pidfile.txt', 'w') as f:
            print(os.getpid(), file=f)
            #print(str(tempo_atual), file=f, end='\n')
        i = 0
        while True:
            time.sleep(1)
            i += 1
            tempo_atual = datetime.timedelta(seconds=i)
            print('0'+str(tempo_atual), end='\n')

            with open('cronometro.txt', 'w') as crono:
                print('0'+str(tempo_atual), file=crono, end='\n')
#comecar()
