from sudoku_connections import SudokuConnections
from get_sudoku_board import getSudokuBoard
from time import time

class SudokuBoard : 
    def __init__(self, difficulty="easy", m=9) : 
        self._m = self._rows = self._cols = m # defines only square grid
        self.board, self._solution = self.getBoard(difficulty)
        
        self.sudokuGraph = SudokuConnections()
        self.mappedGrid = self.__getMappedMatrix() # Maps all the ids to the position in the matrix

    def __getMappedMatrix(self) : 
        """
        Generates the mxm grid or matrix consisting of node ids.
        
        This matrix will act as amapper of each cell with each node 
        through node ids
        """
        matrix = [[0 for _ in range(self._cols)] 
        for _ in range(self._rows)]

        count = 1
        for rows in range(self._rows) : 
            for cols in range(self._cols):
                matrix[rows][cols] = count
                count+=1
        return matrix

    def getBoard(self, difficulty="easy") : 
        board, solution = getSudokuBoard().getBoardFromAPI(difficulty=difficulty)
        if board:
            pass
        else:
            board = [
                [0,0,0,4,0,0,0,0,0],
                [4,0,9,0,0,6,8,7,0],
                [0,0,0,9,0,0,1,0,0],
                [5,0,4,0,2,0,0,0,9],
                [0,7,0,8,0,4,0,6,0],
                [6,0,0,0,3,0,5,0,2],
                [0,0,1,0,0,7,0,0,0],
                [0,4,3,2,0,0,6,0,5],
                [0,0,0,0,0,5,0,0,0]
            ]
            solution = None
        return board, solution
        

    def printBoard(self) : 

        #TODO: Replace 3 with square root of m
        
        print("    1 2 3     4 5 6     7 8 9")
        for i in range(len(self.board)) : 
            if i%3 == 0:
                print("  - - - - - - - - - - - - - - ")

            for j in range(len(self.board[i])) : 
                if j %3 == 0: 
                    print(" |  ", end = "")
                if j == self._cols-1 :
                    print(self.board[i][j]," | ", i+1)
                else : 
                    print(f"{ self.board[i][j] } ", end="")
        print("  - - - - - - - - - - - - - - ")

    def is_Blank(self) : 
        
        for row in range(len(self.board)) :
            for col in range(len(self.board[row])) : 
                if self.board[row][col] == 0 : 
                    return (row, col)
        return None

    def graphColoringInitializeColor(self):
        """
        fill the already given colors
        """
        color = [0] * (self.sudokuGraph.graph.totalV+1)
        given = [] # list of all the ids whos value is already given. Thus cannot be changed
        for row in range(self._rows) : 
            for col in range(self._cols) : 
                if self.board[row][col] != 0 : 
                    #first get the index of the position
                    idx = self.mappedGrid[row][col]
                    #update the color
                    color[idx] = self.board[row][col] # this is the main imp part
                    given.append(idx)
        return color, given

    def solveGraphColoring(self):  
        color, given = self.graphColoringInitializeColor()
        if self.__graphColorUtility(color=color, v=1, given=given):
            count = 1
            for row in range(self._rows) : 
                for col in range(self._cols) :
                    self.board[row][col] = color[count]
                    count += 1
            return color
        
        print(":(")
        return False
    
    def checkSolution(self):
        '''Check whether solution is correct'''
        for i in range(self._rows):
            for j in range(self._cols):
                if self.board[i][j] != self._solution[i][j]:
                    print("Solution incorrect :(")
                    return
        print("Solution is correct!")
        
    def __graphColorUtility(self, color, v, given) :
        '''Run graph coloring on given nodes'''
        if v == self.sudokuGraph.graph.totalV+1  : 
            return True
        for c in range(1, self._m+1) : 
            if self.__isSafe2Color(v, color, c, given) == True :
                color[v] = c
                if self.__graphColorUtility(color, v+1, given) : 
                    return True
            if v not in given : 
                color[v] = 0

        return False

    def __isSafe2Color(self, v, color, c, given) : 
        
        if v in given:
            if color[v] == c: 
                return True
            return False

        for nb in self.sudokuGraph.graph.getNeighbours(v):
            if color[nb] == c:
                return False
        return True


def main() : 
    s = SudokuBoard()
    print("BEFORE SOLVING ...")
    print("\n\n")
    s.printBoard()
    print("\nSolving ...")
    print("\n\n\nAFTER SOLVING ...")
    print("\n\n")
    # start = time()
    s.solveGraphColoring()
    # end = time()
    s.printBoard()
    # print("Execution time of Graph coloring: {}".format(end-start))
    s.checkSolution()


if __name__ == "__main__" : 
    main()
