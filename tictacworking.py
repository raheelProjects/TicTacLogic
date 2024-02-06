import numpy as np

class MatchResult:
    def __init__(self,gotFrom="",result=None,pos=-1):
        self.gotFrom = gotFrom
        self.result = result
        self.pos =pos
    def updateOwnResult(self,data: 'MatchResult'):
        self.gotFrom = data.gotFrom
        self.pos = data.pos
        self.result = True
    def getPerfectResultFrom(self,resultCross: 'MatchResult',resultRowAndCol: 'MatchResult'):
        if(resultCross.result):
            self.updateOwnResult(resultCross)
        elif(resultRowAndCol.result):
            self.updateOwnResult(resultRowAndCol)
        else:
            pass


class TicTacBoard:
    def __init__(self,size=3):
        self.board=np.full((size, size), '', dtype=str)
        self.checkSize = size
    
    def addTicOrTac(self,pos,value):
        row,col = pos
        self.board[row][col]=value

    def checkCrossPattrens(self,value):
        isLeftCrossMatch = True
        isRightCrossMatch =True
        for cross in range(len(self.board)):
            print(f"the row is ${cross} and value is ${(len(self.board)-cross)-1}")
            if(self.board[cross][cross]!=value ):
                isLeftCrossMatch=False
            if(self.board[cross][(len(self.board)-cross)-1]!=value ):
                isRightCrossMatch=False
        if(isLeftCrossMatch ):
            return MatchResult("cross",isLeftCrossMatch,0)
        elif(isRightCrossMatch):
            return MatchResult("cross",isRightCrossMatch,1)
        return MatchResult()
    
    def checkRowsPattrens(self,value):
        isRowMatch = None
        isColumnMatch=None
        no = 0
        for row in range(len(self.board)):
            if(isRowMatch==True or isColumnMatch==True):
                break
            isRowMatch =True
            isColumnMatch = True
            no = row
            for column in range(len(self.board[row])):
                if(self.board[row][column]!=value):
                    isRowMatch=False
                if(self.board[column][row]!=value):
                    isColumnMatch=False
        if(isRowMatch):
            return MatchResult("Row",isRowMatch,no)
        elif(isColumnMatch):
            return MatchResult("Col",isColumnMatch,no)
        return MatchResult()


    def checkBoard(self,value):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                print(f"at row ${row+1} and position {col+1}")

    def getBoard(self):
        print(self.board)

ticTacGame:TicTacBoard = TicTacBoard()
ticTacGame.addTicOrTac((0,2),"X")
ticTacGame.addTicOrTac((1,2),"X")
ticTacGame.addTicOrTac((2,2),"X")
# haspattren = ticTacGame.checkRowsPattrens("X")
# haspattren = ticTacGame.checkCrossPattrens("X")
# print(haspattren)
ticTacGame.getBoard()

