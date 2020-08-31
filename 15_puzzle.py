import os.path
import random
import time
from functools import partial

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow

from Ui_Npuzzle import Ui_MainWindow
from search import astar_search, NPuzzle,best_first_graph_search
import math as m
from PyQt5.Qt import QFont, QObject
from PyQt5.QtCore import QEventLoop, QTimer


N= 15
state = list(range(1,N+1))+[0]
puzzle = NPuzzle(tuple(state),tuple(state))
solution = None

b = [None] * (N+1)


# TODO: refactor into OOP, remove global variables

def scramble():
    """Scrambles the puzzle starting from the goal state"""

    global state
    global puzzle
    global N
    possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    scramble = []
    for _ in range(60):
        scramble.append(random.choice(possible_actions))

    for move in scramble:
        if move in puzzle.actions(state):
            state = list(puzzle.result(state, move))
    
    puzzle = NPuzzle(tuple(state),tuple(list(range(1,N+1))+[0]))

    
def solve():
    """Solves the puzzle using astar_search"""

    return best_first_graph_search(puzzle).solution()


class NpuzzleWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,N):
        super(NpuzzleWindow,self).__init__()
        self.N = N
        self.width = int(m.sqrt(self.N+1))
        self.setupUi(self)
        self.buttons = []
        self.generate_buttons()
        self.pushButton_restart.clicked.connect(self.refresh)
        self.pushButton_solve.clicked.connect(self.solvepuzzle)
        
    def refresh(self):
        scramble()
        self.generate_buttons()
        
    def generate_buttons(self):
        self.buttons = []
        self.GameName.setText(str(self.N)+'-Puzzle')
        width = int(m.sqrt(self.N+1))
        for i in range(width):
            for j in range(width):
                button = QtWidgets.QPushButton(self.widget)
                button.setMaximumHeight(120)
                button.setMaximumWidth(120)
                button.setObjectName(str(i*width+j))
                
                font = QFont()
                font.setPointSize(14)
                font.setBold(1)
                button.setFont(font)
                
                
                button.setText(str(state[i*width+j]))
                button.clicked.connect(lambda x:self.push_button(int(self.sender().objectName())))
                
                self.buttons.append(button)
                self.ButtonLayout.addWidget(button, i, j)
                
    def push_button(self,number):
        global state,puzzle
        
        if number-1>=0 and state[number-1] == 0:
            state[number],state[number-1] = 0,state[number]

        if number+1<=self.N and state[number+1] == 0:
            state[number],state[number+1] = 0,state[number]

        if number-self.width>=0 and state[number-self.width] == 0:
            state[number],state[number-self.width] = 0,state[number]

        if number+self.width<=self.N and  state[number+self.width] == 0:
            state[number],state[number+self.width] = 0,state[number]
        
        self.generate_buttons()
        puzzle = NPuzzle(tuple(state),tuple(list(range(1,N+1))+[0]))
        return
    
    def solvepuzzle(self):
        global puzzle
        global state
        global solution
        
        solution = solve()
        print(solution)

        for move in solution:
            state = list(puzzle.result(state, move))
            loop = QEventLoop()
            QTimer.singleShot(300, loop.quit)
            loop.exec_()
            self.generate_buttons()
            
    
    
        
if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    Window = NpuzzleWindow(N)
    Window.show()
    sys.exit(app.exec_())
