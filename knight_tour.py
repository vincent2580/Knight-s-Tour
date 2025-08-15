class MatrixGenerator:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]

    def trace_movement(self, x_row, y_row, contador):
        self.matrix[x_row][y_row] = contador # Mejor colocar un parametro extra que sea el contador de pasos y se cambie por ese

    def __str__(self):
        return "\n".join(str(row) for row in self.matrix)


class Horse:
    def __init__(self, x_row, y_row):
        self.x_row = x_row
        self.y_row = y_row
        # Movimientos del caballo, guardado en listas
        self.list_movement = [[-1,-2] ,[1,-2] ,[2,-1], [2,1], [-1,2] ,[1,2], [-2,-1], [-2,1]]

    def limits(self, N, x_mov, y_mov)->bool: 
        if (self.x_row + x_mov >= 0) and (self.x_row + x_mov < N) and (self.y_row + y_mov >= 0) and (self.y_row + y_mov < N):
            return True
        else: return False

    def no_step_back(self, Matrix, x_mov, y_mov)->bool:
        validation_limit = self.limits(len(Matrix.matrix), x_mov, y_mov)
        if validation_limit:
            step = Matrix.matrix[self.x_row + x_mov][self.y_row + y_mov]
            if step == 0:
                return True
        else: return False
    
    def check_movements(self, Matrix)->list:
        list_check = []
        for i in self.list_movement:
            if self.no_step_back(Matrix, i[0], i[1]):
                list_check.append([self.x_row + i[0], self.y_row + i[1]])
        return list_check


class GameLogic:

    def __init__(self, size, x_init, y_init):
        self.matrix = MatrixGenerator(size)
        self.horse = Horse(x_init, y_init)
        self.list_movements = [] # Que imprima la cadena de movimientos final
        self.max_movements = size*size # La cantidad de movimientos que tiene que hacer

    def selecionar_menor_recorrido(self, posibles_recorridos_lista)->list: #-> x,y del movimiento a seguir
        # en cada posible recorrido instanciar un caballo y ver cuantos posibles mov tendra luego y luego compararlo con el resto
        comparador_de_movimientos = float("inf")
        for i in posibles_recorridos_lista:
            new_horse = Horse(i[0],i[1])
            new_horse_movements = new_horse.check_movements(self.matrix)
            if len(new_horse_movements) < comparador_de_movimientos:
                comparador_de_movimientos = len(new_horse_movements)
                next_move = [i[0],i[1]]
        return next_move

    def start(self):
        matrix = self.matrix
        game_horse = Horse(self.horse.x_row, self.horse.y_row)
        contador = 1
        matrix.trace_movement(game_horse.x_row, game_horse.y_row, contador)
        self.list_movements.append([game_horse.x_row, game_horse.y_row])

        while contador < self.max_movements: # 
            contador += 1
            posibles_mov_iniciales = game_horse.check_movements(matrix)
            next_move = self.selecionar_menor_recorrido(posibles_mov_iniciales) # [x, y]
            # Esto podria ser un metodo lol
            # 2) Ejecutar movimiento // Esto puede ser un metodo que haga esta ejecucion 

            matrix.trace_movement(next_move[0], next_move[1], contador)
            game_horse.x_row = next_move[0]
            game_horse.y_row = next_move[1]
            self.list_movements.append(next_move)

            # 3) print tableros
            """print(f"Hemos realizado el movimiento {contador}: {next_move}")
            print(matrix)
            input("Presiona la tecla ENTER para continuar: ")"""
            # Wait for confirm, and another round

        print("Esta es la matriz final: \n")
        print(self.matrix)
        print("\nEsta es la lista de movimientos: [fila, columna]")
        print(self.list_movements)







            
