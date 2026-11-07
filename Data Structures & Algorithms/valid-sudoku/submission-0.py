class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(list)
        rows = defaultdict(list)
        square = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    cols[j].append(board[i][j])
                    rows[i].append(board[i][j])


        for item1,item2 in zip(cols.values(),rows.values()):

            if len(list(set(item1)))!=len(item1) or len(list(set(item2)))!=len(item2):
                return False
            

        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in square[(i//3,j//3)]:
                        return False
                    square[(i//3,j//3)].append(board[i][j])
        return True