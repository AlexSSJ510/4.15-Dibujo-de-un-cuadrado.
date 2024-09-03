class Cuadrado:
    def __init__(self, N: int):
        self.N = N

    def dibujar(self):
        for i in range(self.N + 1):
            print('* ', end='')
        print()

        j = 1
        while j < self.N - 2:
            for k in range(self.N):
                if k == 0:
                    print('* ', end='')
                elif k == self.N - 1:
                    print('  *', end='')
                else:
                    print('  ', end='')
            print()
            j += 1

        i = 0
        while i < self.N + 1:
            print('* ', end='')
            i += 1
        print()