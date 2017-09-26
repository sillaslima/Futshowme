with open('/tmp/tempo.txt','rt') as f:
    linhas = f.readlines()
    f.close()
    ultimo_tempo = linhas[len(linhas) -1]
    print(ultimo_tempo)
