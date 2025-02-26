#Time Complexity: O(mn)
#Space Complexity: O(1)
#Accepted successfully in leetcode: yes

class Solution:
    def countLiving(self,board,row,col):
        n = len(board)
        m = len(board[0])
        count = 0

        neigh = [[-1,0],[1,0],[0,-1],[0,1],[1,1],[1,-1],[-1,1],[-1,-1]]

        for i in neigh:
            currRow = row + i[0]
            currCol = col + i[1]

            if 0 <= currRow < n and 0 <= currCol < m:
                if board[currRow][currCol] == 1 or board[currRow][currCol] == 6:
                    count += 1
        return count
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        n = len(board)
        m = len(board[0])

        for row in range(n):
            for col in range(m):
                count = self.countLiving(board,row,col)

                if  board[row][col] == 1:
                    if 2 > count or count > 3:
                        board[row][col] = 6
                else:
                    if count == 3:
                        board[row][col] = 5

        for row in range(n):
            for col in range(m):
                if board[row][col] == 5:
                    board[row][col] = 1
                elif board[row][col] == 6:
                    board[row][col] = 0

        return board