#!/bin/bash

captura=$1
videoCaptura="video$$"

if [ $captura = "captura" ]; then

   cronometro=`cat timeResult.txt`
fi

tempoPassado=`expr $cronometro - 5`
tempoFuturo=`expr $tempoPassado + 20`

trataCronometro() 
{
local tempo=$1

#if [ $tempo -ge 3600 ] && [ $tempo -le 7199 ]; then

#segundo=`expr $tempo % 60`
#minuto=`expr '(' $tempo '/' 60 ')' '-' 60`
#hora=`expr $tempo / 3600`

#elif [ $tempo -ge 7200 ]; then

#segundo=`expr $tempo % 60`
#minuto=`expr '(' $tempo '/' 60 ')' '-' 120`
#hora=`expr $tempo / 3600`
#
if [ $tempo -ge 3600 ]; then

hora=$(($tempo / 3600))
resto=$(($tempo % 3600))
minuto=$(($resto / 60))
segundo=$(($resto % 60))

else

segundo=`expr $tempo % 60`
minuto=`expr $tempo / 60`
hora=`expr $tempo / 3600`

fi


HORASF=$(printf '%.2d' $hora)
MINUTOSF=$(printf '%.2d' $minuto)
SEGUNDOSF=$(printf '%.2d' $segundo)

#hora="$horatrat:$minutotrat:$segundotrat"
hora="$HORASF:$MINUTOSF:$SEGUNDOSF"

export RETORNO=$hora
return

}


#sleep 20
trataCronometro $tempoPassado
horacorte=`echo $RETORNO`

trataCronometro $tempoFuturo
horaFutura=`echo $RETORNO`


sleep 16
#echo "$tempo equivale a $horatrat hora(s) $minutotrat minuto(s) $segundotrat segundo(s)"
#echo "$horatrat:$minutotrat:$segundotrat"
#horaInicio="$horatrat:$minutotrat:$segundotrat"

ffmpeg -i videoCamera.avi -vcodec copy -ss $horacorte -t $horaFutura -f avi pipe:1 | cat > /home/stp/xi/Xiaomi_Yi-master/Standalone_scripts/vide_extraido/$videoCaptura.avi

#ffmpeg -i rtsp://192.168.42.1:554/live -crf 30 -preset ultrafast -r 30 -codec:v copy saida46.avi
