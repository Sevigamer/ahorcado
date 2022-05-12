import random


nombreJugador = " "
class juegoAhorcado:
    ESTADOS = [
        r"""
     +--+
     |  |
        |
        |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
        |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
     |  |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|  |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
    /   |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
    / \ |
        |
    ====="""]

    SALVADO = [
        r"""
     +--+
        |
        |
    \O/ |
     |  |
    / \ |
    ====="""]

    Categoria = 'FRUTAS'
    Frutas = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON MANDARINA NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()

    def jugar(self):
        global nombreJugador

        letrasIncorrectas = []
        letrasCorrectas = []
        secreto = random.choice(self.Frutas)

        print("Dime tu nombre")
        nombreJugador = input()

        while True:
            self.dibujar(letrasIncorrectas, letrasCorrectas, secreto)

            letraDicha = self.dimeLetra(letrasIncorrectas + letrasCorrectas)

            if letraDicha in secreto:

                letrasCorrectas.append(letraDicha)

                salvado = True
                for solucion in secreto:
                    if solucion not in letrasCorrectas:
                        salvado = False
                        break
                if salvado:
                    print(self.SALVADO[0])
                    print('¡Bien hecho! la palabra secreta es :', secreto)
                    print('Has ganado! ', nombreJugador)
                    break
            else:
                letrasIncorrectas.append(letraDicha)

                if len(letrasIncorrectas) == len(self.ESTADOS) - 1:
                    self.dibujar(letrasIncorrectas, letrasCorrectas, secreto)
                    print('Demasiados intentos!')
                    print('La palabra era "{}"'.format(secreto))
                    break

    def dibujar(self, letrasIncorrectas, letrasCorrectas, secreto):
        print(self.ESTADOS[len(letrasIncorrectas)])
        print('La categoría es: ', self.Categoria)
        print()

        print('Letras incorrectas: ', end='')
        print()
        print("Tienes", self.intentos(letrasIncorrectas), "intentos")
        for letra in letrasIncorrectas:
            print(letra, end=' ')
        if len(letrasIncorrectas) == 0:
            print('No hay letras incorrectas.')
        if len(letrasIncorrectas) == len(letrasIncorrectas) + 1:
            print('Letras diferentes.')
        if len(letrasIncorrectas) == len(letrasIncorrectas) + 2:
            print('No coinciden.')

        print()

        longitudPalabra = ['_'] * len(secreto)

        for i in range(len(secreto)):
            if secreto[i] in letrasCorrectas:
                longitudPalabra[i] = secreto[i]

        print(' '.join(longitudPalabra))

    def dimeLetra(self, letraDicha):
        while True:
            print('Adivina una letra.')
            adivina = input('> ').upper()
            if len(adivina) != 1:
                print('Introduce una única letra.')
            elif adivina in letraDicha:
                print('Esa letra letraDicha la sabías. Elige otra vez.')
            elif not adivina.isalpha():
                print('Introduce una LETRA.')

            else:
                return adivina

    def intentos(self,letrasIncorrectas):
        numIntentos = 6
        numIntentos -= len(letrasIncorrectas)
        return numIntentos

if __name__ == '__main__':
    juego1 = juegoAhorcado()
    juego1.jugar()
