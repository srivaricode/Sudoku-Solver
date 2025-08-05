import requests

class getSudokuBoard:

    def getBoardFromAPI(self, difficulty="easy"):
        '''
        Fetches random sudoku board from YouDoSudoku.
        Rows and columns size is 9
        '''
        body = {
            "difficulty": difficulty, # "easy", "medium", or "hard" (defaults to "easy")
            "solution": True, # True or False (defaults to True)
            "array": True # True or False (defaults to False)
        }
        headers =  {"Content-Type":"application/json"}

        response = requests.post("https://youdosudoku.com/api/", json=body, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return self.__cvtToInt(data['puzzle']), self.__cvtToInt(data['solution'])
        else:
            #TODO: Handle this better
            print(f"Error: {response.status_code}")

    def __cvtToInt(self, board:list[list[int]]):
        for i, row in enumerate(board):
            board[i] = list(map(int, row))
        return board


if __name__ == "__main__":
    print(getSudokuBoard().getBoardFromAPI())