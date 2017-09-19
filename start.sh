#!/bin/bash

#python Camera_record_start.py 

# stauts=$?

# if [ $status != 0 ]; then
#    echo "Erro ao startar a Camera, verifique e reinicie"
#    exit 3
# else

   sh cronometro.sh &
   #Copiar fluxo de video da live para a pasta local
   #ffmpeg -i rtsp://192.168.15.64:554 -r 30 -codec:v copy videoCamera.avi
   python3 IniciaCaptura.py rtsp://192.168.15.64:554	
 
#fi

