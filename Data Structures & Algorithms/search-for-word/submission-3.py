class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def check(i,j,prev,n):
            print(i,j)

            if n>=len(word):
                return True

            if j > 0 and board[i][j-1] == word[n]:

                if [i,j-1] != prev and check(i,j-1,[i,j],n+1):
                    return True

            if j < len(board[i])-1 and board[i][j+1] == word[n]:

                if [i,j+1] != prev and check(i,j+1,[i,j],n+1):
                    return True

            if i > 0 and board[i-1][j] == word[n]:

                if [i-1,j] != prev and check(i-1,j,[i,j],n+1):
                    return True

            if i < len(board)-1 and board[i+1][j] == word[n]:

                if [i+1,j] != prev and check(i+1,j,[i,j],n+1):
                    return True

            return False

        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:

                    if len(word) == 1:
                        return True

                    if len(word) > len(board[i])*len(board):
                        return False

                    if j > 0 and board[i][j-1] == word[1]:

                        if check(i,j-1,[i,j],2):
                            return True

                    if j < len(board[i])-1 and board[i][j+1] == word[1]:

                        if check(i,j+1,[i,j],2):
                            return True

                    if i > 0 and board[i-1][j] == word[1]:

                        if check(i-1,j,[i,j],2):
                            return True

                    if i < len(board)-1 and board[i+1][j] == word[1]:

                        if check(i+1,j,[i,j],2):
                            return True


        return False

        