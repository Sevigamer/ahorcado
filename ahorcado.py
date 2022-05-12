import random


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

    Categoria = 'FRUTAS JUEGOS DEPORTES'.split()
    Frutas = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON MANDARINA NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()
    Juegos = 'LOL MINECRAFT FORNITE ISAAC POKEMON BLASPHEMOUS'.split()
    Deportes = 'NATACION FUTBOL TENIS BALONMANO BALONCESTO SOCORRISMO'.split()


    def jugar(self):

        letrasIncorrectas = []
        letrasCorrectas = []
        categoria = random.choice(self.Categoria)
        if categoria == "FRUTAS":
            secreto = random.choice(self.Frutas)
        elif categoria == "JUEGOS":
            secreto = random.choice(self.Juegos)
        else:
            secreto = random.choice(self.Deportes)

        while True:
            self.dibujar(letrasIncorrectas, letrasCorrectas, secreto, categoria)

            letraDicha = self.dimeLetra(letrasIncorrectas + letrasCorrectas)

            if letraDicha == "TERMINAR":
                print(self.ESTADOS[6])
                print("La palabra era ", secreto)
                break

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
                    print('Has ganado!')
                    break
            else:
                letrasIncorrectas.append(letraDicha)

                if len(letrasIncorrectas) == len(self.ESTADOS) - 1:
                    self.dibujar(letrasIncorrectas, letrasCorrectas, secreto)
                    print('Demasiados intentos!')
                    print('La palabra era "{}"'.format(secreto))
                    break

    def dibujar(self, letrasIncorrectas, letrasCorrectas, secreto, categoria):
        print(self.ESTADOS[len(letrasIncorrectas)])
        print('La categoría es: ', categoria)
        print()

        print('Letras incorrectas: ', end='')
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
            if adivina == "TERMINAR":
               return adivina
            elif len(adivina) != 1:
                print('Introduce una única letra.')
            elif adivina in letraDicha:
                print('Esa letra letraDicha la sabías. Elige otra vez.')
            elif not adivina.isalpha():
                print('Introduce una LETRA.')

            else:
                return adivina


if __name__ == '__main__':
    juego1 = juegoAhorcado()
    juego1.jugar()
