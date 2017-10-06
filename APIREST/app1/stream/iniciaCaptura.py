import os, sys, shutil, time
import glob
import subprocess
from random import randint

#print(sys.argv[1])
#endPointLive = sys.argv[1]


def geraNome():
    a = randint(0, 90000)
    ext = '.mp4'
    nome_arquivo = str(a) + ext
    return nome_arquivo


def iniciaStream():
    print('----INICIO DA FUNÇÃO')
    nome_captura = geraNome()
    print('NOME DO VIDEO', nome_captura)
    # ffmpeg -i rtsp://192.168.42.1:554/live -r 30 -codec:v copy videoCamera.avi
    # ffmpeg -f v4l2 -framerate 30 -video_size 1280x720 -i /dev/video0 output1.mp4
    # ffmpeg -f v4l2 -framerate 30 -video_size 1280x720 -i /dev/video0 25765.mp4
    # inicia_captura = [
    # 'ffmpeg',
    #  '-f',
    #  'v4l2',
    #  '-framerate',
    #  '30',
    #  '-video_size',
    #  '1280x720',
    #  '-i',
    #  '/dev/video0',
    #  nome_captura
    #  ]
    #inicia_captura = [
    #    'ffmpeg',
    #    '-y',
    #    '-i',
    #    'rtsp://192.168.15.64:554',
    #    '-r',
    #    '30',
    #    '-codec:v',
    #    'copy',
    #    'videoCamera.avi'
    #]
    # command = [FFMPEG_BINARY,'-i', 'my_video.mp4', '-']
    # pipe = sp.Popen(command, stdout=sp.PIPE stderr=sp.PIPE)
    # pipe.stdout.readline()
    # pipe.terminate()
    # infos = proc.stderr.read()
    print('----------------INICIO DA CAPTURA------------------')
    #print('comando ffmpeg', inicia_captura)
    #process_captura = subprocess.Popen(inicia_captura,
    #                                   stdout=subprocess.PIPE,
    #                                   stderr=subprocess.STDOUT,
    #                                   universal_newlines=False)
    # proc = sp.Popen(cmd, **popen_params)

    #print(process_captura)
    #saida_captura = process_captura.wait()
    #print('SAIDA DO PROCESS CAPTURA', saida_captura)
    #if saida_captura == 0:
        #print('INICIO DA CAPTURA COM SUCESSO', nome_captura)

    #else:
        #print('PROBLEMAS NA CAPTURA')
    #return nome_captura
    return 'chamada com sucesso'


#iniciaCaptura()