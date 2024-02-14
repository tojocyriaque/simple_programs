class Game:

    def __init__(self):
        self.board = [["xx", "xx", "xx", "blueR", "blueN", "blueB", "blueK", "blueQ", "blueB", "blueN", "blueR", "xx", "xx", "xx"],
                      ["xx", "xx", "xx", "blueP", "blueP", "blueP", "blueP", "blueP", "blueP", "blueP", "blueP", "xx", "xx", "xx"],
                      ["xx", "xx", "xx", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "xx", "xx", "xx"],
                      ["redR", "redP", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "yellowP", "yellowR"],
                      ["redN", "redP", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "yellowP", "yellowN"],
                      ["redB", "redP", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "yellowP", "yellowB"],
                      ["redQ", "redP", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "yellowP", "yellowQ"],
                      ["redK", "redP", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "yellowP", "yellowK"],
                      ["redB", "redP", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "yellowP", "yellowB"],
                      ["redN", "redP", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "yellowP", "yellowN"],
                      ["redR", "redP", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "yellowP", "yellowR"],
                      ["xx", "xx", "xx", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "-----", "xx", "xx", "xx"],
                      ["xx", "xx", "xx", "greenP", "greenP", "greenP", "greenP", "greenP", "greenP", "greenP", "greenP", "xx", "xx", "xx"],
                      ["xx", "xx", "xx", "greenR", "greenN", "greenB", "greenK", "greenQ", "greenB", "greenN", "greenR", "xx", "xx", "xx"]
                      ]

        self.moves = {
            "P": self.get_pawn_moves, "R": self.get_rook_moves,
            "N": self.get_knight_moves, "B": self.get_bishop_moves,
            "Q": self.get_queen_moves, "K": self.get_king_moves
        }

        self.piece_value = {"K": 10, "Q": 9, "N": 3, "B": 3, "R": 5, "P": 1}

        self.current_player = "blue"
        self.scores = {"blue": 0, "green": 0, "red": 0, "yellow": 0}

        self.moves_log = []

    def get_valid_moves(self):
        valid_moves = []
        for r in range(14):
            for c in range(14):
                piece = self.board[r][c]
                if piece not in ["xx", "-----"]:
                    color = piece[:-1]
                    piece_type = piece[-1]

                    if color == self.current_player:
                        valid_moves += self.moves[piece_type](r, c)

        return valid_moves

    def make_move(self, move):
        (iy, ix), (ey, ex) = move
        color = self.board[iy][ix][:-1]
        move = [(iy, ix), (ey, ex), self.board[iy][ix], self.board[ey][ex]]

        if self.board[ey][ex] not in ["-----", "xx"]:
            piece_type = self.board[ey][ex][-1]
            self.scores[color] += self.piece_value[piece_type]

        self.board[ey][ex] = self.board[iy][ix]
        self.board[iy][ix] = "-----"
        players = ["blue", "yellow", "green", "red"]
        self.current_player = players[(1+players.index(self.current_player)) % 4]

        self.moves_log.append(move)

    def undo(self):
        if self.moves_log:
            move = self.moves_log.pop()
            (iy, ix), (ey, ex), attack, captured = move
            self.board[iy][ix] = attack
            self.board[ey][ex] = captured

            players = ["blue", "yellow", "green", "red"]
            self.current_player = players[(players.index(self.current_player)-1) % 4]

    def get_pawn_moves(self, r, c):
        valid_moves = []
        color = self.board[r][c][:-1]
        if color == "x":
            return []

        if color == "green":
            if 0 <= r-1 < 14:
                if self.board[r-1][c] == "-----":
                    valid_moves.append([(r, c), (r-1, c)])
                if r == 12 and self.board[11][c] == self.board[10][c] == "-----":
                    valid_moves.append([(r, c), (r-2, c)])

                for col in [c-1, c+1]:
                    if 0 <= col < 14:
                        if self.board[r-1][col][:-1] not in [color, "----", "x"]:
                            valid_moves.append([(r, c), (r-1, col)])

        elif color == "blue":
            if 0 <= r+1 < 14:
                if self.board[r+1][c] == "-----":
                    valid_moves.append([(r, c), (r+1, c)])
                if r == 1 and self.board[2][c] == self.board[3][c] == "-----":
                    valid_moves.append([(r, c), (r+2, c)])

                for col in [c-1, c+1]:
                    if 0 <= col < 14:
                        if self.board[r+1][col][:-1] not in ["----", color, "x"]:
                            valid_moves.append([(r, c), (r+1, col)])

        elif color == "yellow":
            if 0 <= c-1 < 14:
                if self.board[r][c-1] == "-----":
                    valid_moves.append([(r, c), (r, c-1)])
                if c == 12 and self.board[r][11] == self.board[r][10] == "-----":
                    valid_moves.append([(r, c), (r, c-2)])
                for row in [r+1, r-1]:
                    if 0 <= row < 14:
                        if self.board[row][c-1][:-1] not in ["----", color, "x"]:
                            valid_moves.append([(r, c), (row, c-1)])

        elif color == "red":
            if 0 <= c+1 < 14:
                if self.board[r][c+1] == "-----":
                    valid_moves.append([(r, c), (r, c+1)])
                if c == 1 and self.board[r][2] == self.board[r][3] == "-----":
                    valid_moves.append([(r, c), (r, c+2)])

                for row in [r+1, r-1]:
                    if 0 <= row < 14:
                        if self.board[row][c+1][:-1] not in ["----", color, "x"]:
                            valid_moves.append([(r, c), (row, c+1)])

        return valid_moves

    def get_rook_moves(self, r, c):
        valid_moves = []
        rook_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        color = self.board[r][c][:-1]

        if color in ["x", "----"]:
            return []

        for rm in rook_moves:
            for i in range(1, 14):
                end_row = r + rm[0]*i
                end_col = c + rm[1]*i

                if 0 <= end_row < 14 and 0 <= end_col < 14:
                    end_piece = self.board[end_row][end_col]
                    if end_piece == "-----":
                        valid_moves.append([(r, c), (end_row, end_col)])
                    elif end_piece[:-1] not in [color, "x"]:
                        valid_moves.append([(r, c), (end_row, end_col)])
                        break
                    else:
                        break
                else:
                    break

        return valid_moves

    def get_bishop_moves(self, r, c):
        valid_moves = []
        bishop_moves = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        color = self.board[r][c][:-1]

        if color in ["x", "----"]:
            return []

        for bm in bishop_moves:
            for i in range(1, 14):
                end_row = r + bm[0]*i
                end_col = c + bm[1]*i

                if 0 <= end_row < 14 and 0 <= end_col < 14:
                    end_piece = self.board[end_row][end_col]
                    if end_piece == "-----":
                        valid_moves.append([(r, c), (end_row, end_col)])
                    elif end_piece[:-1] not in [color, "x"]:

                        valid_moves.append([(r, c), (end_row, end_col)])
                        break
                    else:
                        break
                else:
                    break

        return valid_moves

    def get_knight_moves(self, r, c):
        valid_moves = []
        knight_moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        color = self.board[r][c][:-1]

        if color in ["x", "----"]:
            return []

        for knm in knight_moves:
            end_row = r + knm[0]
            end_col = c + knm[1]

            if 0 <= end_row < 14 and 0 <= end_col < 14:
                end_piece = self.board[end_row][end_col]
                if end_piece[:-1] not in [color, "x"]:
                    valid_moves.append([(r, c), (end_row, end_col)])

        return valid_moves

    def get_queen_moves(self, r, c):
        return self.get_rook_moves(r, c) + self.get_bishop_moves(r, c)

    def get_king_moves(self, r, c):
        valid_moves = []
        king_moves = [(1, -1), (1, 0), (1, 1), (0, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        color = self.board[r][c][:-1]
        for km in king_moves:
            end_row = r + km[0]
            end_col = c + km[1]

            if 0 <= end_row < 14 and 0 <= end_col < 14:
                end_piece = self.board[end_row][end_col]
                if end_piece[:-1] not in [color, "x"]:
                    valid_moves.append([(r, c), (end_row, end_col)])
        return valid_moves
