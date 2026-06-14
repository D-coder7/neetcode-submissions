class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkrow(table, row):
            count = {}
            for num in table[row]:
                if num == '.':
                    continue
                count[num] = 1 + count.get(num, 0)
                if count[num] > 1 or not(0<int(num)<10):
                    return False
            return True
        def checkcol(table, col):
            count = {}
            for i in range(len(table)):
                num = table[i][col]
                if num == '.':
                    continue
                count[num] = 1 + count.get(num, 0)
                if count[num] > 1 or not(0<int(num)<10):
                    return False
            return True
        def checkbox(table, boxno):
            count = {}
            rowstrt = (boxno//3)*3
            colstrt = (boxno%3)*3
            for i in range(rowstrt, rowstrt+3):
                for j in range(colstrt, colstrt+3):
                    num = table[i][j]
                    if num == '.':
                        continue
                    count[num] = 1 + count.get(num, 0)
                    if count[num] > 1:
                        return False
            return True
        
        #check rows
        for r in range(len(board)):
            if not checkrow(board, r):
                return False
        for c in range(len(board[0])):
            if not checkcol(board, c):
                return False
        for i in range(9):
            if not checkbox(board, i):
                return False

        return True