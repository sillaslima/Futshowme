import os
import signal

if os.path.exists('pidfile.txt'):
    print(type(os.path.exists('pidfile.txt')))
    print(os.getpid())
    with open('pidfile.txt','rt') as f:
        x = f.read()
        print(x)
        print(type(x))
        os.kill(int(x),signal.SIGTERM)


else:
    print('Cronometro Não Iniciado')
    raise SystemExit(1)
