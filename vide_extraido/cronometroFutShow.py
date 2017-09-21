import time
print('enter para start e enter stop e ctrl+c para sair')
input()
print('--------START--------')
inicio = time.time()
fim = inicio
Numerovolta=1
print(fim)

try:
    while True:
        input()
        tempoVolta= round(time.time() - fim, 2)
        tempoTotal= round(time.time() - inicio, 2)
        print(Numerovolta)
        print(tempoTotal)
        print(tempoVolta)
        Numerovolta +=1
        fim=time.time()
except KeyboardInterrupt:
    print('concluido')

        
