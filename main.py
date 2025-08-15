from knight_tour import *
import unittest

class GameTest(unittest.TestCase):
    "Test for the Horse Game"
    def test_game(self):
        ## Test 
        size = int(input("¿De que tamaño es el tablero?: "))
        x = int(input("¿En que fila(x) comienza el caballo?: "))
        y = int(input("¿En que columna(y) comienza el caballo?: "))

        game = GameLogic(size, x, y)
        game.start()

if __name__ == '__main__':
    unittest.main()

