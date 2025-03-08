# a program to create game boards in the command line 

import os 

class Board: 
    def __init__(self, height, width):
        self.height = height
        self.width = width 

        self.contents = []
        for y in range(height):
            rowList = []
            for x in range(width):
                rowList.append("⬜️")
            self.contents.append(rowList)
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

brd = Board(20, 24)

class Player: 
    def __init(self,sprite,  name, x, y):
        self.name = name
        self.x = x
        self.y =y 

    def __str__(self):
        return self.sprite




class Game: 
    def __init__(self):
        self.board = Board(10,14) 
        self.active = True 
    def run(self):
        cursX = 0
        cursY =0
        while(self.active): 
            mv = input("What is the next move? ")
            if ( mv == "fin"):
                self.active == False
                break
            if (mv == "w"):
                self.board.updateCell(cursX, cursY -1, "⬛" )
                cursY -= 1
            if (mv == "s"):
                self.board.updateCell(cursX, cursY +1, "⬛" )
                cursY +=1
            if (mv == "a"):
                self.board.updateCell(cursX-1, cursY , "⬛" )
                cursX -= 1
            if (mv == "d"):
                self.board.updateCell(cursX+1, cursY, "⬛" )
                cursX +=1

            print(self.board)

gm = Game()

gm.run()
