from DibujarCuadrado import Cuadrado
if __name__ == "__main__":
    dimension = int(input("Escribe la dimensión N>= 2 del cuadrado a dibujar: "))
    if dimension >= 2:
        cuadrado = Cuadrado(dimension)
        cuadrado.dibujar()
    else:
        print("La dimensión debe ser mayor o igual a 2.")