import datetime
import time
import threading

def cronometro():
	
	try:
		while opcao ==1 :
			global i
			time.sleep(1)
			print('total segundos',i)
			global x
			x = datetime.timedelta(seconds=i)
			i +=1
			print(x)
			#captura(x)
		return (x)
	except KeyboardInterrupt:
	    print('concluido')

def captura (tempo):
	print(tempo)
	captura = str(input('digite c para capturar '))
	if captura == 'c':
		corta = tempo
		print(corta)
	

i=0
x = datetime.timedelta(seconds=i)
#opcao = int(input('1-CAPTURAR 2- para Cancelar a verificação: '))
#if opcao ==1:
#	th = threading.Thread(target=cronometro, args=())
#	th.start()
#	#tempo=cronometro()
#	print(th)

#else:
#	print(a)
