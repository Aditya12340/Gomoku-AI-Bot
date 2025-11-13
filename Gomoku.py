"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 16, 2025
"""

def is_empty(board):  
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "w" or board[i][j] == "b": 
                return False 
    return True
         
#-------
def is_bounded(board, y_end, x_end, length, d_y, d_x): 
    y_origin = y_end - ((length - 1) * d_y)
    x_origin = x_end - ((length - 1) * d_x)
    size = len(board)

    def in_board(y, x):
        if y < 0 or y >= size:
            return False
        if x < 0 or x >= size:
            return False
        return True

    if y_end == len(board) - 1 or x_end == len(board) - 1:
        if y_origin == 0 or x_origin == 0:
            return "CLOSED"
        elif in_board(y_origin - d_y, x_origin - d_x) and board[y_origin - d_y][x_origin - d_x] == " ":
            return "SEMIOPEN"
        else: return "CLOSED" 
    if y_origin == len(board) - 1 or x_origin == len(board) - 1:
        if y_end == 0 or x_end == 0:
            return "CLOSED"
        elif in_board(y_end - d_y, x_end - d_x) and board[y_end - d_y][x_end - d_x] == " ":
            return "SEMIOPEN"
        else: return "CLOSED" 

    else:
        if (in_board(y_end + d_y, x_end + d_x) and board[y_end + d_y][x_end + d_x] == " ") and (in_board(y_origin - d_y, x_origin - d_x) and board[y_origin - d_y][x_origin - d_x] == " "): 
            return "OPEN"
        elif (in_board(y_end + d_y, x_end + d_x) and board[y_end + d_y][x_end + d_x] == " ") or (in_board(y_origin - d_y, x_origin - d_x) and board[y_origin - d_y][x_origin - d_x] == " "):
            return "SEMIOPEN"
        else: 
            return "CLOSED"    

def detect_row(board, col, y_start, x_start, length, d_y, d_x): 
    open_seq_count = 0
    semi_open_seq_count = 0
    counter = 0
    size = len(board)
    for i in range(size):   
        if (y_start + (i * d_y)) >= len(board) or (x_start + (i * d_x)) >= len(board):
            return (0,0)
        elif (y_start + (i * d_y)) <= len(board) and (x_start + (i * d_x)) <= len(board): 
            if board[y_start + (i * d_y)][x_start + (i * d_x)] == col: 
                counter += 1
                y_cur = y_start + (i * d_y)
                x_cur = x_start + (i * d_x)

                if counter == length and (y_cur >= size - 1 or\
                                            y_cur <= 0 or\
                                            x_cur >= size - 1 or\
                                             x_cur <= 0 or\
                                             board[y_cur + d_y ][x_cur + d_x] != col): 
                    y_end = y_start + (i * d_y)
                    x_end = x_start + (i* d_x)
                    if is_bounded(board, y_end, x_end, length, d_y, d_x) == "OPEN" :
                        open_seq_count += 1
                    if is_bounded(board, y_end, x_end, length, d_y, d_x) == "SEMIOPEN":
                        semi_open_seq_count += 1
        elif (y_start + (i * d_y)) <= len(board) and (x_start + (i * d_x)) <= len(board) and board[y_start + (i * d_y)][x_start + (i * d_x)] != col:
                counter = 0
    return (open_seq_count, semi_open_seq_count)


def detect_rows(board, col, length):
    open_seq_count = 0
    semi_open_seq_count = 0
    for i in range(len(board)): 
        (a, b) = detect_row(board, col, 0, i, length, 1, 0) # verticals
        open_seq_count += a
        semi_open_seq_count += b
        (c , d) = detect_row(board, col, i, 0, length, 0, 1) # horizontals
        open_seq_count += c 
        semi_open_seq_count += d
        (e, f) = detect_row(board, col, i, 0, length, 1, 1) # uppper left -> lower right
        open_seq_count += e 
        semi_open_seq_count += f
        (g ,h) = detect_row(board, col, i, len(board) - 1 , length, 1, -1) # upper right -> lower left
        open_seq_count += g 
        semi_open_seq_count += h
        for j in range(i+1, len(board) - 1): 
            (m ,n) = detect_row(board, col, 0, j , length, 1, 1)
            open_seq_count += m 
            semi_open_seq_count += n
            (k, l) = detect_row(board, col, 0, j , length, 1, -1)
            open_seq_count += k 
            semi_open_seq_count += l
    return(open_seq_count, semi_open_seq_count)
    
def search_max(board): #passed
    cur_max = -100000
    move_y = 0
    move_x = 0
    for i in range(len(board)): 
        for j in range(len(board)): 
            if board[i][j] == " ": 
                board[i][j] = "b"
                if cur_max < score(board):
                    cur_max = score(board)
                    move_y = i 
                    move_x = j 
                board[i][j] = " "    
    return move_y, move_x


def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])



def is_win(board):
    counter_w = 0
    counter_b = 0
    counter_e = 0
    #horizontal axis
    for j in range(4): 
        for i in range(8):
            if board[i][j] == "w":
                counter_w += 1
            elif board[i][j] == "b":
                counter_b += 1
            elif board[i][j] == " ":
                counter_e += 1
    if counter_w == 5:
        print("White won")
    elif counter_b == 5:
        print("Black won")
    elif counter_e> counter_w and counter_e>counter_b: 
        print("Continue playing")
    else: 
        pass
    
    # vertical axis 
    counter_w1 = 0
    counter_b1 = 0
    counter_e1 = 0
    for j in range(8):
        for i in range(4):
            if board[i][j] == "w":
                counter_w1 += 1
            elif board[i][j] == "b":
                counter_b1 += 1
            elif board[i][j] == " ":
                counter_e1 += 1
    if counter_w1 == 5:
        print("White won")
    elif counter_b1 == 5:
        print("Black won")
    elif counter_e1> counter_w1 and counter_e1>counter_b1: 
        print("Continue playing")
    else: 
        pass

    counter_w2 = 0
    counter_b2 = 0
    counter_e2 = 0
    for j in range(4):
        for i in range(4):
            if board[i][j] == "w":
                counter_w2 += 1
            elif board[i][j] == "b":
                counter_b2 += 1
            elif board[i][j] == " ":
                counter_e2 += 1
    if counter_w2 == 5:
        print("White won")
    elif counter_b2 == 5:
        print("Black won")
    elif counter_e2> counter_w2 and counter_e2>counter_b2: 
        print("Continue playing")
    else: 
        pass


def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
    

        
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    #play_gomoku(8)
    test_is_bounded()
    test_is_empty()
    test_detect_row()
    test_detect_rows()
    test_search_max()
    
