# Converts letter input to chess piece for the displayed board
def what_piece(rank,fil):
    if board[rank][fil] == 'p':
        return '♙'
    elif board[rank][fil] == 'r':
        return '♖'
    elif board[rank][fil] == 'n':
        return '♘'
    elif board[rank][fil] == 'b':
        return '♗'
    elif board[rank][fil] == 'q':
        return '♕'
    elif board[rank][fil] == 'k':
        return '♔'
    elif board[rank][fil] == 'P':
        return '♟'
    elif board[rank][fil] == 'R':
        return '♜'
    elif board[rank][fil] == 'N':
        return '♞'
    elif board[rank][fil] == 'B':
        return '♝'
    elif board[rank][fil] == 'Q':
        return '♛'
    elif board[rank][fil] == 'K':
        return '♚'
    else:
        return ' '


# Replace piece position to 0 which is displayed as ' ' and position to where piece is moving to piece letter
def move_piece(what_move):
    board[int(what_move[2])][int(what_move[1])] = '0'
    board[int(what_move[5])][int(what_move[4])] = what_move[0]


# First checks if inputed move is legal and then calls move_piece function if it is
def legal_move(side,move):
    # Inputed moves converted for 'board'
    list_move = [x for x in move]
    list_move[2] = str(8 - (int(list_move[2]) - 1))
    list_move[5] = str(8 - (int(list_move[5]) - 1))
    list_move = [l.replace('a', '0') for l in list_move]
    list_move[1:] = [l.replace('b', '1') for l in list_move[1:]]
    list_move = [l.replace('c', '2') for l in list_move]
    list_move = [l.replace('d', '3') for l in list_move]
    list_move = [l.replace('e', '4') for l in list_move]
    list_move = [l.replace('f', '5') for l in list_move]
    list_move = [l.replace('g', '6') for l in list_move]
    list_move = [l.replace('h', '7') for l in list_move]

    # White pieces made uppercase for 'board'
    if side == 'White': list_move[0] = move[0].upper()
    # Rules for pieces:
    if board[int(list_move[2])][int(list_move[1])] == list_move[0]:
        # White pawn rules
        if list_move[0] == 'P':
            if board[int(list_move[5])][int(list_move[4])] == '0' and list_move[4] == list_move[1]:
                if list_move[2] == '7' and abs(int(list_move[5]) - int(list_move[2])) <= 2:
                    move_piece(list_move)
                    return True
                elif abs(int(list_move[5]) - int(list_move[2])) == 1:
                    move_piece(list_move)
                    return True
            elif abs(int(list_move[5]) - int(list_move[2])) == 1 and abs(int(list_move[4]) - int(list_move[1])) == 1 and board[int(list_move[5])][int(list_move[4])].islower() and board[int(list_move[5])][int(list_move[4])] != '0':
                move_piece(list_move)
                return True
            elif last_move_made[0] == 'p' and abs(int(last_move_made[5]) - int(last_move_made[2])) == 2 and list_move[4] == last_move_made[4] and abs(int(list_move[5]) - int(list_move[2])) == 1 and abs(int(list_move[4]) - int(list_move[1])) == 1 and board[int(list_move[5])][int(list_move[4])] == '0':
                board[int(last_move_made[5])][int(last_move_made[4])] = '0'
                move_piece(list_move)
                return True
        # Black pawn rules
        elif list_move[0] == 'p':
            if board[int(list_move[5])][int(list_move[4])] == '0' and list_move[4] == list_move[1]:
                if list_move[2] == '2' and abs(int(list_move[5]) - int(list_move[2])) <= 2:
                    move_piece(list_move)
                    return True
                elif abs(int(list_move[5]) - int(list_move[2])) == 1:
                    move_piece(list_move)
                    return True
            elif abs(int(list_move[5]) - int(list_move[2])) == 1 and abs(int(list_move[4]) - int(list_move[1])) == 1 and board[int(list_move[5])][int(list_move[4])].isupper() and board[int(list_move[5])][int(list_move[4])] != '0':
                move_piece(list_move)
                return True
            elif last_move_made[0] == 'P' and abs(int(last_move_made[5]) - int(last_move_made[2])) == 2 and list_move[4] == last_move_made[4] and abs(int(list_move[5]) - int(list_move[2])) == 1 and abs(int(list_move[4]) - int(list_move[1])) == 1 and board[int(list_move[5])][int(list_move[4])] == '0':
                board[int(last_move_made[5])][int(last_move_made[4])] = '0'
                move_piece(list_move)
                return True
        # White rook rules:
        elif list_move[0] == 'R':
            if board[int(list_move[5])][int(list_move[4])] == '0' or board[int(list_move[5])][int(list_move[4])].islower():
                if abs(int(list_move[4]) - int(list_move[1])) == 0:
                    if abs(int(list_move[5]) - int(list_move[2])) == 1:
                        move_piece(list_move)
                        return True
                    else:
                        if int(list_move[5]) - int(list_move[2]) < 0:
                            for vert_square in range(-1, int(list_move[5]) - int(list_move[2]), -1):
                                if board[int(list_move[2]) + vert_square][int(list_move[1])] != '0': return False
                            move_piece(list_move)
                            return True
                        else:
                            for vert_square in range(1, int(list_move[5]) - int(list_move[2])):
                                if board[int(list_move[2]) + vert_square][int(list_move[1])] != '0': return False
                            move_piece(list_move)
                            return True
                elif abs(int(list_move[5]) - int(list_move[2])) == 0:
                    if abs(int(list_move[4]) - int(list_move[1])) == 1:
                        move_piece(list_move)
                        return True
                    else:
                        if int(list_move[4]) - int(list_move[1]) < 0:
                            for hor_square in range(-1, int(list_move[4]) - int(list_move[1]), -1):
                                if board[int(list_move[2])][int(list_move[1]) + hor_square] != '0': return False
                            move_piece(list_move)
                            return True
                        else:
                            for hor_square in range(1, int(list_move[4]) - int(list_move[1])):
                                if board[int(list_move[2])][int(list_move[1]) + hor_square] != '0': return False
                            move_piece(list_move)
                            return True
        # Black rook rules:
        elif list_move[0] == 'r':
            if board[int(list_move[5])][int(list_move[4])] == '0' or board[int(list_move[5])][int(list_move[4])].isupper():
                if abs(int(list_move[4]) - int(list_move[1])) == 0:
                    if abs(int(list_move[5]) - int(list_move[2])) == 1:
                        move_piece(list_move)
                        return True
                    else:
                        if int(list_move[5]) - int(list_move[2]) < 0:
                            for vert_square in range(-1, int(list_move[5]) - int(list_move[2]), -1):
                                if board[int(list_move[2]) + vert_square][int(list_move[1])] != '0': return False
                            move_piece(list_move)
                            return True
                        else:
                            for vert_square in range(1, int(list_move[5]) - int(list_move[2])):
                                if board[int(list_move[2]) + vert_square][int(list_move[1])] != '0': return False
                            move_piece(list_move)
                            return True
                elif abs(int(list_move[5]) - int(list_move[2])) == 0:
                    if abs(int(list_move[4]) - int(list_move[1])) == 1:
                        move_piece(list_move)
                        return True
                    else:
                        if int(list_move[4]) - int(list_move[1]) < 0:
                            for hor_square in range(-1, int(list_move[4]) - int(list_move[1]), -1):
                                if board[int(list_move[2])][int(list_move[1]) + hor_square] != '0': return False
                            move_piece(list_move)
                            return True
                        else:
                            for hor_square in range(1, int(list_move[4]) - int(list_move[1])):
                                if board[int(list_move[2])][int(list_move[1]) + hor_square] != '0': return False
                            move_piece(list_move)
                            return True
        # White knight rules:
        elif list_move[0] == 'N':
            if board[int(list_move[5])][int(list_move[4])] == '0' or board[int(list_move[5])][int(list_move[4])].islower():
                if abs(int(list_move[4]) - int(list_move[1])) == 1:
                    if abs(int(list_move[5]) - int(list_move[2])) == 2:
                        move_piece(list_move)
                        return True
                elif abs(int(list_move[5]) - int(list_move[2])) == 1:
                    if abs(int(list_move[4]) - int(list_move[1])) == 2:
                        move_piece(list_move)
                        return True
        # Black knight rules:
        elif list_move[0] == 'n':
            if board[int(list_move[5])][int(list_move[4])] == '0' or board[int(list_move[5])][int(list_move[4])].isupper():
                if abs(int(list_move[4]) - int(list_move[1])) == 1:
                    if abs(int(list_move[5]) - int(list_move[2])) == 2:
                        move_piece(list_move)
                        return True
                elif abs(int(list_move[5]) - int(list_move[2])) == 1:
                    if abs(int(list_move[4]) - int(list_move[1])) == 2:
                        move_piece(list_move)
                        return True
        # White bishop rules:
        elif list_move[0] == 'B':
            if board[int(list_move[5])][int(list_move[4])] == '0' or board[int(list_move[5])][int(list_move[4])].islower():
                if abs(int(list_move[4]) - int(list_move[1])) == abs(int(list_move[5]) - int(list_move[2])):
                    if int(list_move[5]) - int(list_move[2]) < 0:
                        if int(list_move[4]) - int(list_move[1]) < 0:
                            for diag_square in range(-1, int(list_move[5]) - int(list_move[2]), -1):
                                if board[int(list_move[2]) + diag_square][int(list_move[1]) + diag_square] != '0': return False
                            move_piece(list_move)
                            return True
                        elif int(list_move[4]) - int(list_move[1]) > 0:
                            for diag_square in range(-1, int(list_move[5]) - int(list_move[2]), -1):
                                if board[int(list_move[2]) + diag_square][int(list_move[1]) - diag_square] != '0': return False
                            move_piece(list_move)
                            return True
                    elif int(list_move[5]) - int(list_move[2]) > 0:
                        if int(list_move[4]) - int(list_move[1]) < 0:
                            for diag_square in range(1, int(list_move[5]) - int(list_move[2])):
                                if board[int(list_move[2]) + diag_square][int(list_move[1]) - diag_square] != '0': return False
                            move_piece(list_move)
                            return True
                        elif int(list_move[4]) - int(list_move[1]) > 0:
                            for diag_square in range(1, int(list_move[5]) - int(list_move[2])):
                                if board[int(list_move[2]) + diag_square][int(list_move[1]) + diag_square] != '0': return False
                            move_piece(list_move)
                            return True
        # Black bishop rules:
        elif list_move[0] == 'b':
            if board[int(list_move[5])][int(list_move[4])] == '0' or board[int(list_move[5])][int(list_move[4])].isupper():
                if abs(int(list_move[4]) - int(list_move[1])) == abs(int(list_move[5]) - int(list_move[2])):
                    if int(list_move[5]) - int(list_move[2]) < 0:
                        if int(list_move[4]) - int(list_move[1]) < 0:
                            for diag_square in range(-1, int(list_move[5]) - int(list_move[2]), -1):
                                if board[int(list_move[2]) + diag_square][int(list_move[1]) + diag_square] != '0': return False
                            move_piece(list_move)
                            return True
                        elif int(list_move[4]) - int(list_move[1]) > 0:
                            for diag_square in range(-1, int(list_move[5]) - int(list_move[2]), -1):
                                if board[int(list_move[2]) + diag_square][int(list_move[1]) - diag_square] != '0': return False
                            move_piece(list_move)
                            return True
                    elif int(list_move[5]) - int(list_move[2]) > 0:
                        if int(list_move[4]) - int(list_move[1]) < 0:
                            for diag_square in range(1, int(list_move[5]) - int(list_move[2])):
                                if board[int(list_move[2]) + diag_square][int(list_move[1]) - diag_square] != '0': return False
                            move_piece(list_move)
                            return True
                        elif int(list_move[4]) - int(list_move[1]) > 0:
                            for diag_square in range(1, int(list_move[5]) - int(list_move[2])):
                                if board[int(list_move[2]) + diag_square][int(list_move[1]) + diag_square] != '0': return False
                            move_piece(list_move)
                            return True
        # White Queen rules:
        elif list_move[0] == 'Q':
            if board[int(list_move[5])][int(list_move[4])] == '0' or board[int(list_move[5])][int(list_move[4])].islower():
                if abs(int(list_move[4]) - int(list_move[1])) == abs(int(list_move[5]) - int(list_move[2])):
                    if int(list_move[5]) - int(list_move[2]) < 0:
                        if int(list_move[4]) - int(list_move[1]) < 0:
                            for diag_square in range(-1, int(list_move[5]) - int(list_move[2]), -1):
                                if board[int(list_move[2]) + diag_square][int(list_move[1]) + diag_square] != '0': return False
                            move_piece(list_move)
                            return True
                        elif int(list_move[4]) - int(list_move[1]) > 0:
                            for diag_square in range(-1, int(list_move[5]) - int(list_move[2]), -1):
                                if board[int(list_move[2]) + diag_square][int(list_move[1]) - diag_square] != '0': return False
                            move_piece(list_move)
                            return True
                    elif int(list_move[5]) - int(list_move[2]) > 0:
                        if int(list_move[4]) - int(list_move[1]) < 0:
                            for diag_square in range(1, int(list_move[5]) - int(list_move[2])):
                                if board[int(list_move[2]) + diag_square][int(list_move[1]) - diag_square] != '0': return False
                            move_piece(list_move)
                            return True
                        elif int(list_move[4]) - int(list_move[1]) > 0:
                            for diag_square in range(1, int(list_move[5]) - int(list_move[2])):
                                if board[int(list_move[2]) + diag_square][int(list_move[1]) + diag_square] != '0': return False
                            move_piece(list_move)
                            return True
                elif abs(int(list_move[4]) - int(list_move[1])) == 0:
                    if abs(int(list_move[5]) - int(list_move[2])) == 1:
                        move_piece(list_move)
                        return True
                    else:
                        if int(list_move[5]) - int(list_move[2]) < 0:
                            for vert_square in range(-1, int(list_move[5]) - int(list_move[2]), -1):
                                if board[int(list_move[2]) + vert_square][int(list_move[1])] != '0': return False
                            move_piece(list_move)
                            return True
                        else:
                            for vert_square in range(1, int(list_move[5]) - int(list_move[2])):
                                if board[int(list_move[2]) + vert_square][int(list_move[1])] != '0': return False
                            move_piece(list_move)
                            return True
                elif abs(int(list_move[5]) - int(list_move[2])) == 0:
                    if abs(int(list_move[4]) - int(list_move[1])) == 1:
                        move_piece(list_move)
                        return True
                    else:
                        if int(list_move[4]) - int(list_move[1]) < 0:
                            for hor_square in range(-1, int(list_move[4]) - int(list_move[1]), -1):
                                if board[int(list_move[2])][int(list_move[1]) + hor_square] != '0': return False
                            move_piece(list_move)
                            return True
                        else:
                            for hor_square in range(1, int(list_move[4]) - int(list_move[1])):
                                if board[int(list_move[2])][int(list_move[1]) + hor_square] != '0': return False
                            move_piece(list_move)
                            return True
        # Black Queen rules:
        elif list_move[0] == 'q':
            if board[int(list_move[5])][int(list_move[4])] == '0' or board[int(list_move[5])][int(list_move[4])].isupper():
                if abs(int(list_move[4]) - int(list_move[1])) == abs(int(list_move[5]) - int(list_move[2])):
                    if int(list_move[5]) - int(list_move[2]) < 0:
                        if int(list_move[4]) - int(list_move[1]) < 0:
                            for diag_square in range(-1, int(list_move[5]) - int(list_move[2]), -1):
                                if board[int(list_move[2]) + diag_square][int(list_move[1]) + diag_square] != '0': return False
                            move_piece(list_move)
                            return True
                        elif int(list_move[4]) - int(list_move[1]) > 0:
                            for diag_square in range(-1, int(list_move[5]) - int(list_move[2]), -1):
                                if board[int(list_move[2]) + diag_square][int(list_move[1]) - diag_square] != '0': return False
                            move_piece(list_move)
                            return True
                    elif int(list_move[5]) - int(list_move[2]) > 0:
                        if int(list_move[4]) - int(list_move[1]) < 0:
                            for diag_square in range(1, int(list_move[5]) - int(list_move[2])):
                                if board[int(list_move[2]) + diag_square][int(list_move[1]) - diag_square] != '0': return False
                            move_piece(list_move)
                            return True
                        elif int(list_move[4]) - int(list_move[1]) > 0:
                            for diag_square in range(1, int(list_move[5]) - int(list_move[2])):
                                if board[int(list_move[2]) + diag_square][int(list_move[1]) + diag_square] != '0': return False
                            move_piece(list_move)
                            return True
                elif abs(int(list_move[4]) - int(list_move[1])) == 0:
                    if abs(int(list_move[5]) - int(list_move[2])) == 1:
                        move_piece(list_move)
                        return True
                    else:
                        if int(list_move[5]) - int(list_move[2]) < 0:
                            for vert_square in range(-1, int(list_move[5]) - int(list_move[2]), -1):
                                if board[int(list_move[2]) + vert_square][int(list_move[1])] != '0': return False
                            move_piece(list_move)
                            return True
                        else:
                            for vert_square in range(1, int(list_move[5]) - int(list_move[2])):
                                if board[int(list_move[2]) + vert_square][int(list_move[1])] != '0': return False
                            move_piece(list_move)
                            return True
                elif abs(int(list_move[5]) - int(list_move[2])) == 0:
                    if abs(int(list_move[4]) - int(list_move[1])) == 1:
                        move_piece(list_move)
                        return True
                    else:
                        if int(list_move[4]) - int(list_move[1]) < 0:
                            for hor_square in range(-1, int(list_move[4]) - int(list_move[1]), -1):
                                if board[int(list_move[2])][int(list_move[1]) + hor_square] != '0': return False
                            move_piece(list_move)
                            return True
                        else:
                            for hor_square in range(1, int(list_move[4]) - int(list_move[1])):
                                if board[int(list_move[2])][int(list_move[1]) + hor_square] != '0': return False
                            move_piece(list_move)
                            return True
    return False


# Displays the board for the orientation of the side playing
def chess_board(orientation):
    if orientation == 'White':
        return f"""
    {board[0][0]}   {board[0][1]}   {board[0][2]}   {board[0][3]}   {board[0][4]}   {board[0][5]}   {board[0][6]}   {board[0][7]}
   --- --- --- --- --- --- --- --- 
8 | {what_piece(1,0)} | {what_piece(1,1)} | {what_piece(1,2)} | {what_piece(1,3)} | {what_piece(1,4)} | {what_piece(1,5)} | {what_piece(1,6)} | {what_piece(1,7)} | 8
   --- --- --- --- --- --- --- --- 
7 | {what_piece(2,0)} | {what_piece(2,1)} | {what_piece(2,2)} | {what_piece(2,3)} | {what_piece(2,4)} | {what_piece(2,5)} | {what_piece(2,6)} | {what_piece(2,7)} | 7
   --- --- --- --- --- --- --- --- 
6 | {what_piece(3,0)} | {what_piece(3,1)} | {what_piece(3,2)} | {what_piece(3,3)} | {what_piece(3,4)} | {what_piece(3,5)} | {what_piece(3,6)} | {what_piece(3,7)} | 6
   --- --- --- --- --- --- --- --- 
5 | {what_piece(4,0)} | {what_piece(4,1)} | {what_piece(4,2)} | {what_piece(4,3)} | {what_piece(4,4)} | {what_piece(4,5)} | {what_piece(4,6)} | {what_piece(4,7)} | 5
   --- --- --- --- --- --- --- --- 
4 | {what_piece(5,0)} | {what_piece(5,1)} | {what_piece(5,2)} | {what_piece(5,3)} | {what_piece(5,4)} | {what_piece(5,5)} | {what_piece(5,6)} | {what_piece(5,7)} | 4
   --- --- --- --- --- --- --- --- 
3 | {what_piece(6,0)} | {what_piece(6,1)} | {what_piece(6,2)} | {what_piece(6,3)} | {what_piece(6,4)} | {what_piece(6,5)} | {what_piece(6,6)} | {what_piece(6,7)} | 3
   --- --- --- --- --- --- --- --- 
2 | {what_piece(7,0)} | {what_piece(7,1)} | {what_piece(7,2)} | {what_piece(7,3)} | {what_piece(7,4)} | {what_piece(7,5)} | {what_piece(7,6)} | {what_piece(7,7)} | 2
   --- --- --- --- --- --- --- --- 
1 | {what_piece(8,0)} | {what_piece(8,1)} | {what_piece(8,2)} | {what_piece(8,3)} | {what_piece(8,4)} | {what_piece(8,5)} | {what_piece(8,6)} | {what_piece(8,7)} | 1
   --- --- --- --- --- --- --- --- 
    {board[0][0]}   {board[0][1]}   {board[0][2]}   {board[0][3]}   {board[0][4]}   {board[0][5]}   {board[0][6]}   {board[0][7]}
"""
    else:
        return f"""
    {board[0][7]}   {board[0][6]}   {board[0][5]}   {board[0][4]}   {board[0][3]}   {board[0][2]}   {board[0][1]}   {board[0][0]}
   --- --- --- --- --- --- --- --- 
1 | {what_piece(8,7)} | {what_piece(8,6)} | {what_piece(8,5)} | {what_piece(8,4)} | {what_piece(8,3)} | {what_piece(8,2)} | {what_piece(8,1)} | {what_piece(8,0)} | 1
   --- --- --- --- --- --- --- --- 
2 | {what_piece(7,7)} | {what_piece(7,6)} | {what_piece(7,5)} | {what_piece(7,4)} | {what_piece(7,3)} | {what_piece(7,2)} | {what_piece(7,1)} | {what_piece(7,0)} | 2
   --- --- --- --- --- --- --- --- 
3 | {what_piece(6,7)} | {what_piece(6,6)} | {what_piece(6,5)} | {what_piece(6,4)} | {what_piece(6,3)} | {what_piece(6,2)} | {what_piece(6,1)} | {what_piece(6,0)} | 3
   --- --- --- --- --- --- --- --- 
4 | {what_piece(5,7)} | {what_piece(5,6)} | {what_piece(5,5)} | {what_piece(5,4)} | {what_piece(5,3)} | {what_piece(5,2)} | {what_piece(5,1)} | {what_piece(5,0)} | 4
   --- --- --- --- --- --- --- --- 
5 | {what_piece(4,7)} | {what_piece(4,6)} | {what_piece(4,5)} | {what_piece(4,4)} | {what_piece(4,3)} | {what_piece(4,2)} | {what_piece(4,1)} | {what_piece(4,0)} | 5
   --- --- --- --- --- --- --- --- 
6 | {what_piece(3,7)} | {what_piece(3,6)} | {what_piece(3,5)} | {what_piece(3,4)} | {what_piece(3,3)} | {what_piece(3,2)} | {what_piece(3,1)} | {what_piece(3,0)} | 6
   --- --- --- --- --- --- --- --- 
7 | {what_piece(2,7)} | {what_piece(2,6)} | {what_piece(2,5)} | {what_piece(2,4)} | {what_piece(2,3)} | {what_piece(2,2)} | {what_piece(2,1)} | {what_piece(2,0)} | 7
   --- --- --- --- --- --- --- --- 
8 | {what_piece(1,7)} | {what_piece(1,6)} | {what_piece(1,5)} | {what_piece(1,4)} | {what_piece(1,3)} | {what_piece(1,2)} | {what_piece(1,1)} | {what_piece(1,0)} | 8
   --- --- --- --- --- --- --- --- 
    {board[0][7]}   {board[0][6]}   {board[0][5]}   {board[0][4]}   {board[0][3]}   {board[0][2]}   {board[0][1]}   {board[0][0]}
"""


# Stores the last move made. Used for en passant and check
def last_move(last_side, latest_move):
    global last_move_made
    last_move_made = [x for x in latest_move]
    last_move_made[2] = str(8 - (int(last_move_made[2]) - 1))
    last_move_made[5] = str(8 - (int(last_move_made[5]) - 1))
    last_move_made = [l.replace('a', '0') for l in last_move_made]
    last_move_made = [l.replace('b', '1') for l in last_move_made]
    last_move_made = [l.replace('c', '2') for l in last_move_made]
    last_move_made = [l.replace('d', '3') for l in last_move_made]
    last_move_made = [l.replace('e', '4') for l in last_move_made]
    last_move_made = [l.replace('f', '5') for l in last_move_made]
    last_move_made = [l.replace('g', '6') for l in last_move_made]
    last_move_made = [l.replace('h', '7') for l in last_move_made]
    if last_side == 'White': last_move_made[0] = latest_move[0].upper()
    return last_move_made


# Background board needed for move checks
board = [
    ['a','b','c','d','e','f','g','h'],
    ['r','n','b','q','k','b','n','r'],
    ['p','p','p','p','p','p','p','p'],
    ['0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0'],
    ['P','P','P','P','P','P','P','P'],
    ['R','N','B','Q','K','B','N','R']
]

last_move_made = []