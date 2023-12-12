import pygame

edge_color = (0, 0, 0)
red_brick = (162, 8, 0)
orange_brick = (183, 119, 0)
green_brick = (0, 127, 33)
yellow_brick = (197, 199, 37)


class Brick:
    def __init__(self, screen, screen_width, column, rows):
        self.width = screen_width / column
        self.height = 20
        self.blocks_all_wall = []  # Armazena todos os blocos da parede

        initial_y = 100
        for row in range(rows):
            block_row = []
            for col in range(column):
                brick_x = col * self.width + 10
                brick_y = row * self.height + initial_y
                rect = pygame.Rect(brick_x, brick_y, self.width, self.height)  # coordenada(x,y, largura,altura)

                if row < 2:
                    points = 7
                elif 2 <= row < 4:
                    points = 5
                elif 4 <= row < 6:
                    points = 3
                elif row >= 6:
                    points = 1

                # Adiciona o retângulo e a pontuacao à linha de blocos
                block_row.append((rect, points))
            self.blocks_all_wall.append(block_row)

    def draw_wall(self, screen):
        for row in self.blocks_all_wall:
            for brick in row:
                if brick[1] == 7:
                    brick_color = red_brick
                elif brick[1] == 5:
                    brick_color = orange_brick
                elif brick[1] == 3:
                    brick_color = green_brick
                else:
                    brick_color = yellow_brick

                pygame.draw.rect(screen, brick_color, brick[0])
                pygame.draw.rect(screen, edge_color, brick[0], 3)  # Tamanho da borda entre os tijolos

    def increase_ball_speed(self, ball):
        # Verifica se a bola atingiu tijolos verdes ou laranjas e aumenta a velocidade
        for row_cont, row in enumerate(self.blocks_all_wall):
            for brike_cont, (brike_rect, points) in enumerate(row):
                if points == 3 or points == 5:  # Verifica tijolos verdes ou laranjas
                    if ball.rect.colliderect(brike_rect):
                        ball.adjust_speed(points)  # Chama o método para ajustar a velocidade
