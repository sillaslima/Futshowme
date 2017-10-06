
def consultaCronometro():
    with open('cronometro.txt','rt') as f:
        linhas = f.readlines()
        #print(linhas)
        f.close()
        ultimo_tempo = linhas[len(linhas) -1]
        print(ultimo_tempo)
    return ultimo_tempo
consultaCronometro()