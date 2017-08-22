#-*- coding: utf-8 -*-
import os,shutil,time
import glob
import subprocess
from random import randint


def geraNome():
	a = randint(0,90000)
	ext ='.avi'
	nome_arquivo = str(a)+ext
	return nome_arquivo
def retira_audio(video):
	print(video)
	sem_audio = video
	nome_audio=geraNome()
	retira_audio = ['ffmpeg', '-i',sem_audio,'-y','-an', nome_audio]
	print('----------------APLICANDO EFEITO PARA RETIRAR O AUDIO------------------')		
	an = subprocess.Popen(retira_audio,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
	saida_audio=an.wait()
	if saida_audio == 0:
		print ('AUDIO RETIRADO COM SUCESSO',nome_audio)
	else:
		print ('PROBLEMAS AO RETIRAR O AUDIO')
	return nome_audio
def gerar_slow(video_gerar_slow):
	print('----PARAMETRO RECEBIDO',video_gerar_slow)
	slow=video_gerar_slow
	nome_slow=geraNome()
	aplica_slow = [
	'ffmpeg',
	 '-i',
	 slow,
	 '-y',
	 '-filter:v',
	 'setpts=1.7*PTS',
	  nome_slow
	  ]
	print('----------------APLICANDO EFEITO PARA GERAR O SLOW MOTION------------------')		
	slow_motion = subprocess.Popen(aplica_slow,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
	saida_slow = slow_motion.wait()
	if saida_slow == 0:
		print('SLOW MOTION GERADO COM SUCESSO',nome_slow)
		
	else:
		print('PROBLEMAS COM SLOW MOTION')
	return nome_slow
def concatena_slow (video_audio, video_slow):
	print("--------VAMOS CONCATENAR O VIDEO SEM AUDIO COM SLOW MOTION--------")
	print("--------VIDEO SEM AUDIO RECEBIDO",video_audio)
	print("--------VIDEO ORIGINAL RECEBIDO",video_slow)
	nome_concatena=geraNome()
	concatenar = [
	"ffmpeg",
	 "-i",
	 video_audio,
	 "-i",
	 video_slow,
	 "-filter_complex",
	 "[0:v] [1:v] concat=n=2:v=1 [v]",
	 "-map","[v]",
	 nome_concatena]
	print(concatenar)
	print('----------------APLICANDO PARA CONCATENAR VIDEO SEM AUDO COM SLOW MOTION------------------')
	concat_video = subprocess.Popen(concatenar,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
	saida_concat = concat_video.wait()
	if saida_concat == 0:
		print('VIDEOS CONCATENADO COM SUCESSO',nome_concatena)
		
	else:
		print('PROBLEMAS AO CONCATENAR VIDEOS')
	return nome_concatena

def concatena_intro(video_intermediario):
	print("--------VAMOS CONCATENAR O VIDEO INTRO COM O SEM AUDIO E SLOW--------")
	print("--------VIDEO INTRO RECEBIDO",video_intermediario)
	#video_intro="Intro_futshow.avi"
	video_intro="/home/stp/xi/Xiaomi_Yi-master/Standalone_scripts/vide_extraido/intro/FutShow_kde10.avi"
	nome_final=geraNome()
	print(video_intro)
	concatenar_final = [
	"ffmpeg",
	 "-i",
	 video_intro,
	 "-i",
	 video_intermediario,
	 "-filter_complex",
	 "[0:v] [1:v] concat=n=2:v=1 [v]",
	 "-map","[v]",
	 nome_final]
	print('----------------APLICANDO EFEITO PARA CONCATENAR VIDEO INTRO COM INTERMEDIARIO------------------')
	concat_final = subprocess.Popen(concatenar_final,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
	saida_final = concat_final.wait()
	if saida_final == 0:
		print('VIDEOS INTRO E INTERMEDIARIO CONCATENADO COM SUCESSO',nome_final)
		
	else:
		print('PROBLEMAS AO CONCATENAR VIDEOS DE INTRODUÇÃO')
	return nome_final

print ('---------INICIANDO A VERIFICAÇÃO E EDIÇÃO DE VIDEOS---------')
roda = True

while True:
	verifica_video = int(input('1- para verificar se existe novo arquivo ou 2- para Cancelar a verificação: '))
	
	if verifica_video == 1:
		print ('----------------Verificando se existem VIDEOS na pasta-----------------')
		lista_videos_retirar_audio = glob.glob('*.avi')
		print(type(lista_videos_retirar_audio))

		if len(lista_videos_retirar_audio) > 0:
			print('Lista de videos na pasta',lista_videos_retirar_audio)
			for i in range(len(lista_videos_retirar_audio)):
				print('chamando a função para retirar o Audio',lista_videos_retirar_audio[i])
				nome_audio=retira_audio(lista_videos_retirar_audio[i])
				print('Video sem Audio Gerado',nome_audio)
				print('chamando a função para gerar o SLOW',nome_audio)
				gera_slow=gerar_slow(nome_audio)
				print('Video com Slow Motion gerado',gera_slow)
				print('chamando a função para concatenar videos',gera_slow)
				print('e',nome_audio)
				gera_concatena=concatena_slow(nome_audio,gera_slow)
				print('Video Concatenado gerado com sucesso',gera_concatena)
				print('chamando a função para concatenar video de intro',gera_concatena)
				gera_intro=concatena_intro(gera_concatena)
				print('Video Intro Concatenado  e gerado com sucesso',gera_intro)
						
		else:
			print('não existe arquivo .avi na pasta')
	else:
		if verifica_video == 2:
			roda = False
			print('saindo')
			break
			exit(1)









# lista_videos_retirar_audio = glob.glob('*.avi')
# print(type(lista_videos_retirar_audio))

# print('Lista de videos na pasta',lista_videos_retirar_audio)
# for i in range(len(lista_videos_retirar_audio)):
# 	print('chamando a função para retirar o Audio',lista_videos_retirar_audio[i])
# 	nome_audio=retira_audio(lista_videos_retirar_audio[i])
# 	print('Video sem Audio Gerado',nome_audio)
# 	print('chamando a função para gerar o SLOW',nome_audio)
# 	gera_slow=gerar_slow(nome_audio)
# 	print('Video com Slow Motion gerado',gera_slow)
# 	print('chamando a função para concatenar videos',gera_slow)
# 	print('e',nome_audio)
# 	gera_concatena=concatena_slow(nome_audio,gera_slow)
# 	print('Video Concatenado gerado com sucesso',gera_concatena)
# 	print('chamando a função para concatenar video de intro',gera_concatena)
# 	gera_intro=concatena_intro(gera_concatena)
# 	print('Video Intro Concatenado  e gerado com sucesso',gera_intro)

		