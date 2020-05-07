# 빈 칸 채우기
def rearrange_board(board):
    t_board = list(zip(*board))
    length = len(t_board[0])
    for i in range(len(t_board)):
        n_row = ''.join(t_board[i]).replace('0', '')
        t_board[i] = '0'*(length-len(n_row)) + n_row
    
    tt_board = list(zip(*t_board))
    next_board = list(map(lambda x: ''.join(x), tt_board))
    return next_board
    
# 없애기 + 카운팅
def remove_blocks(blocks, board):
    board = list(map(lambda x: list(x), board))
    
    for (r, c) in blocks:
        board[r][c] = '0'

    return board


# 지울 수 있는 블록 탐색
def check_removable(board):
    removables = set()
    for r in range(len(board)-1):
        for c in range(len(board[0])-1):
            if board[r][c] != '0' :
                me = board[r][c]
                for i in range(3):
                    nr, nc = r+dr[i], c+dc[i]
                    if board[nr][nc] != me:
                        break
                else:
                    removables.add((r,c))
                    for i in range(3):
                        nr, nc = r+dr[i], c+dc[i]
                        removables.add((nr,nc))    
    return removables

dr = [0, 1, 1]
dc = [1, 0, 1]

def solution(m, n, board):
    answer = 0    

    removables = check_removable(board)
    while removables:
        answer += len(removables)
        removed = remove_blocks(removables, board)
        board = rearrange_board(removed)
        removables = check_removable(board)
        
    return answer


m = 4
n = 5
board = [
    'CCBDE', 
    'AAADE', 
    'AAABF', 
    'CCBBF']

solution(m, n, board)