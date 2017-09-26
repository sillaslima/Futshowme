import time

import datetime
class Vai_crono:
    def __init__(self):
        self.contador = 0
        self.start = None
    def inicia(self):
        if self.start is not None:
            raise RuntimeError('Already started')
        while True:
            time.sleep(1)
            print('total segundos', self.contador)
            self.duracao = datetime.timedelta(seconds=self.contador)
            self.contador += 1
            print(self.duracao)
    def end(self):
        if self.start is None:
            raise RuntimeError('Not started')
        end = self.duracao
        self.elapsed += end - self._start
        self._start = None

class Timer:
    def __init__(self):
        self.duracao = 0

        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self.x1(4)

    def end(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self.x1(5)
        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.end()


if __name__ == '__main__':
    comeca = Vai_crono()
    comeca.inicia()
    #def countdown(n):
    #    while n > 0:
    #        n -= 1

    #t = Timer(10)
    #t.start()
    #countdown(1000000)
#    t.end()
 #   print(t.elapsed)

    #with t:
    #    countdown(1000000)
  #  print(t.elapsed)
