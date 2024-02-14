import game
import pygame

WIDTH = HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN.fill("light gray")
SQ = WIDTH//14
Images = {}


def load_images(gm: game.Game):
    for i in range(14):
        for j in range(14):
            piece = gm.board[i][j]
            if piece not in ["-----", "xx"]:
                piece_type = piece[-1]
                color = piece[:-1]
                im = pygame.image.load("pieces/"+color+"/"+piece_type+".png")
                Images[piece] = pygame.transform.scale(im, (SQ*0.75, SQ*0.75))


def show_scores(screen, gm: game.Game):
    colors = ["blue", "yellow", "green", "red"]
    positions = [(0, 0), (WIDTH-SQ*3, 0), (WIDTH-SQ*3, HEIGHT-SQ*3), (0, HEIGHT-SQ*3)]

    for i in range(4):
        surface = pygame.Surface((SQ*3, SQ*3))
        surface.fill("light gray")
        screen.blit(surface, positions[i])
        font = pygame.font.SysFont("consolas", SQ)
        text = font.render(str(gm.scores[colors[i]]), True, colors[i])
        screen.blit(text, (positions[i][0]+SQ, positions[i][1]+SQ))


def highlight_ending(screen, gm: game.Game, sq):
    surf = pygame.surface.Surface((SQ, SQ))
    surf.set_alpha(120)

    r, c = sq

    if gm.board[r][c] == "xx":

        return

    surf.fill("purple")
    screen.blit(surf, (c*SQ, r*SQ))

    for move in gm.get_valid_moves():
        (iy, ix), (ey, ex) = move
        if iy == r and ix == c:
            if gm.board[ey][ex] == "-----":
                surf.fill("orange")
            else:
                surf.fill("violet")
            screen.blit(surf, (ex*SQ, ey*SQ))


def draw_board(screen, gm: game.Game):
    for r in range(14):
        for c in range(14):
            piece = gm.board[r][c]
            if piece != "xx":
                color = ["white", "dark gray"][(r+c) % 2]

                pygame.draw.rect(screen, color, pygame.Rect(c*SQ, r*SQ, SQ, SQ))
                if piece != "-----":
                    screen.blit(Images[piece], (c*SQ + 0.10*SQ, r*SQ + 0.25*SQ))

    show_scores(screen, gm)


def main(screen):
    pygame.font.init()
    g = game.Game()
    load_images(g)
    move = []
    sq = ()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    g.undo()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                x, y = mx//SQ, my//SQ

                if sq != (y, x):
                    sq = (y, x)
                    move.append(sq)
                else:
                    sq = ()
                    move = []

                if len(move) == 2:
                    if move in g.get_valid_moves():
                        g.make_move(move)
                        sq = ()
                        move = []
                    else:
                        move = [sq]

        draw_board(screen, g)
        if sq:
            highlight_ending(screen, g, sq)
        pygame.display.flip()


if __name__ == "__main__":
    main(SCREEN)
