# a program to create game boards in the command line 

import os 
import time 
import sys
import termios 
import tty
from threading import Timer 

class Board: 
    def __init__(self, height, width):
        self.height = height
        self.width = width 

        self.contents = []
        for y in range(height):
            rowList = []
            for x in range(width):
                rowList.append("🧱")
            self.contents.append(rowList)
    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width
    def clr(self): 
        for row in range(self.height):
            self.contents[row] = ["⬜️"]*self.width

    def __str__(self):
        os.system("clear")
        brdStr ="" 
        for y in range(self.height): 
            for x in range(self.width): 
                brdStr+= self.contents[y][x]
            brdStr +="\n" 
        return (brdStr)
    def updateCell(self,x, y, sprite):
        self.contents[y][x] = sprite

    def shift(self, direction):
        if direction == "up": 
            self.contents = self.contents[1:] + [self.contents[0]]
            return
        if direction == "down":  
            self.contents = [self.contents[-1]] + self.contents[0:-1]
            return
        if direction == "left":

            for row in range(self.height): 
                self.contents[row].append(self.contents[row][0])
                self.contents[row] = self.contents[row][1:]
        if direction == "right":                 
            for row in range(self.height):
                last = self.contents[row].pop()
                self.contents[row].insert(0, last)
   

    def scroll(self): 
        for col in range(self.width): 
            self.shift()
            print(self)

    def doNothing(self):
        pass
        print("moving to next iteration")
        return 0
    def vScroll(self): 
        while(True):
            t = Timer(.5, self.doNothing)
            self.shift("down")
            t.start()
            time.sleep(.5)
            ch = getch()
            if (ch == "d"): 
                self.shift("right")
            if (ch == "a"):
                self.shift("left")
            if (ch == "f"):
                break

            t.cancel()
            print(self) 

class Player: 
    def __init(self,sprite,  name, x, y):
        self.name = name
        self.x = x
        self.y =y 

    def __str__(self):
        return self.sprite
def getch():
    fd = sys.stdin.fileno()
    oldSet = termios.tcgetattr(fd)
    try: 
        tty.setraw(fd) 
        ch = sys.stdin.read(1)
    finally: 
        termios.tcsetattr(fd,termios.TCSADRAIN ,oldSet)
    return ch



class Game: 
    def __init__(self):
        self.board = Board(20,14) 
        self.active = True 
    def run(self):
        cursX = 0
        cursY =0
        while(self.active):
            
            mv = getch()
           # mv = input("What is the next move? ")
            if (mv == "y"):
                self.board.vScroll()
            if ( mv == "f"):
                self.active == False
                break
            if (mv == "w" and cursY-1 in [y for y in range(self.board.height)]):
                self.board.updateCell(cursX, cursY -1, "⬛" )
                cursY -= 1
            if (mv == "s" and cursY+1 in [y for y in range(self.board.height)]):
                self.board.updateCell(cursX, cursY +1, "⬛" )
                cursY +=1
            if (mv == "a" and cursX-1 in [x for x in range(self.board.width)]):
                self.board.updateCell(cursX-1, cursY , "⬛" )
                cursX -= 1
            if (mv == "d" and cursX+1 in [x for x in range(self.board.width)]):
                self.board.updateCell(cursX+1, cursY, "⬛" )
                cursX +=1   
            if (mv == "c"):
                self.board.clr()
            if (mv == "b"): 
                self.board.shift("down")
            if (mv == "h"):
                self.board.shift("up")
            if (mv == "n"):
                self.board.shift("right")
            if (mv == "v"):
                self.board.shift("left")
            if (mv == "z"): 
                self.board.scroll()
            print(self.board)


class shape: 
    def __init__(self, form, board): 
        self.form = form

        self.y = 0
        self.board = board
        self.width = 3
        self.height = 2
    def draw(x, y): 
        if x + self.width < self.board.getWidth():
            self.board.update(x,y, "⬛️")
            self.board.update(x+1,y, "⬛️")
            self.board.update(x,y+1, "⬛️")
            self.board.update(x+1,y+1, "⬛️")



gm = Game()

gm.run()
