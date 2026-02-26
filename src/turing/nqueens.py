'''
This module is part of the Turing course at EPFL. It provides functions to deal
with the N-Queens problem, which consists in placing N queens on an N x N
chessboard such that no two queens threaten each other. 

This module is intended to be run exlusively in WebTigerPython, which is a
Web-based Python environment based on Pyodide.
'''

import sys


if sys.platform != "emscripten":
    print("This module is intended to be run exclusively in WebTigerPython, which is a Web-based Python environment based on Pyodide.")



from collections.abc import Iterable
from gturtle import *

def draw_chess_board(solution: Iterable[int], x: int = 0, y: int = 0, size: int = 50, color="black") -> tuple[int, int]:
    '''
    Représente la solution `solution` aux coordonnées (x, y) avec des carrés
    de taille `size` pixels avec la couleur `color`.
    '''

    def square(cx: float, cy: float) -> None:
        setPos(cx - size / 2, cy - size / 2)
        for _ in range(4):
            fd(size)
            rt(90)

    def queen(cx: float, cy: float) -> None:
        setPos(cx, cy)
        dot(size * 0.7)
        
    hideTurtle()
    setPenColor(color)
    setFontSize(size * 0.95)

    n = len(solution)

    for i in range(n):
        for j in range(n):
            cx = x + i * size - size / 2
            cy = y + j * size - size / 2
            square(cx, cy)
            if solution[i] == j:
                queen(cx, cy)

    setPos(x - size, y - 2 * size)
    setHeading(0)
    label("  ".join(str(q) if q is not None else '?' for q in solution))

    return n, size

def check_constraints(q: list[int]) -> bool:
    '''

    Vérifie que toutes les contraintes du problème soient satisfaites dans
    la solution ``q`` représentant la ligne sur laquelle est placée chaque
    dames ``q[i]``.

    >>> check_constraints([0])
    True
    >>> check_constraints([1, 3, 0, 2])
    True
    >>> check_constraints([1, 3, 5, 0, 2, 4])
    True

    >>> check_constraints([0, 1, 2, 3])
    False
    >>> check_constraints([3, 2, 1, 0])
    False
    >>> check_constraints([1, 3, 0, 0])
    False
    >>> check_constraints([1, 4, 5, 2, 0, 4])
    False

    '''
    n = len(q)

    for i in range(n):
        for j in range(i + 1, n):
            if q[i] == q[j]: return False
            if q[i] - q[j] == i - j: return False
            if q[j] - q[i] == i - j: return False
    
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()