# Knight's tour 

it's a mathematic problem where we try to find 'some' path in a NxN size chess board where
the Knight only step the same floor once. It's a common problem in the Theory of graphs, and one of the
optimal solution it's Warnsdorff's algorith that I try to replicate with my humble experience in coding.


# Characteristics
1 - Example of use:
We just need 3 inputs:
    · Size of the matrix(NxN)
    · X_row
    · Y_column
    X, Y = Two numbers(0,N-1), inside the matrix where the Knight's tour is starting

2 - Example of outcome:
    · Matrix resolved
    · List of every movement made by the alghorithm
    · Speed test

3 - Notes for the alghoritm:

We have 3 main objects, MatrixGenerator, Horse, GameLogic.

MatrixGenerator its used to know the size of the problem, print the Matrix and keep the record of the movements

Horse come with 2 logic methods that make the choices of the movement. He sees where he stand and check every posibilities.

GameLogic, uses Warnsdorff's rule makes the knight choose the next move where there are less posibilities of movement later, and 
if all its the samme he always choose the same direction. And, finally the start() method it's where everythong collide,
it's doing the path in O(n), as a linear algorithm, and where the path it's finished, print the matrix and the list of movement.


## Uso rápido
```bash
python main.py