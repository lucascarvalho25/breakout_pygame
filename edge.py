import pygame

edge_color = (212, 210, 212)
red_brick = (162, 8, 0)
orange_brick = (183, 119, 0)
green_brick = (0, 127, 33)
yellow_brick = (197, 199, 37)
racket_color = (0, 97, 148)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

wall_width = 10
racket_height = 20
brick_height = 20
x_gap = 7
y_gap = 5



start_pos_edge_left = [(wall_width / 2) - 1, 0]
end_pos_edge_left = [(wall_width / 2) - 1, screen_height]
start_pos_edge_right = [(screen_width - wall_width / 2) - 1, 0]
end_pos_edge_right = [(screen_width - wall_width / 2) - 1, screen_height]

start_pos_racket_left = [(wall_width / 2) - 1, 35 + screen_height - 65 + racket_height / 2 - 54 / 2]
end_pos_racket_left = [(wall_width / 2) - 1, 15 + screen_height - 65 + racket_height / 2 - 54 / 2 + 54]
start_pos_racket_right = [(screen_width - wall_width / 2) - 1, 35 + screen_height - 65 + racket_height / 2 - 54 / 2]
end_pos_racket_right = [(screen_width - wall_width / 2) - 1, 15 + screen_height - 65 + racket_height / 2 - 54 / 2 + 54]

start_pos_red_brick_left = [(wall_width / 2) - 1, 100]
end_pos_red_brick_left = [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap-121]
start_pos_red_brick_right = [(screen_width - wall_width / 2) - 1, 100]
end_pos_red_brick_right = [(screen_width - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap-121]

start_pos_orange_brick_left = [(wall_width / 2) - 1, 90 + 2 * brick_height + 2 * y_gap]
end_pos_orange_brick_left = [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap-134]
start_pos_orange_brick_right = [(screen_width - wall_width / 2) - 1, 90 + 2 * brick_height + 2 * y_gap]
end_pos_orange_brick_right = [(screen_width - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap-134]

start_pos_green_brick_left = [(wall_width / 2) - 1, 78 + 4 * brick_height + 4 * y_gap]
end_pos_green_brick_left = [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap-144]
start_pos_green_brick_right = [(screen_width - wall_width / 2) - 1, 78 + 4 * brick_height + 4 * y_gap]
end_pos_green_brick_right = [(screen_width - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap-144]

start_pos_yellow_brick_left = [(wall_width / 2) - 1, 69 + 6 * brick_height + 6 * y_gap]
end_pos_yellow_brick_left = [(wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap-154]
start_pos_yellow_brick_right = [(screen_width - wall_width / 2) - 1, 69 + 6 * brick_height + 6 * y_gap]
end_pos_yellow_brick_right = [(screen_width - wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap-154]


class Edge():
	def edge(a):
		pygame.draw.line(screen, edge_color, [0, 0], [screen_width, 0], 45) #Desenha a borda cinza do topo
		pygame.draw.line(screen, edge_color, start_pos_edge_left, end_pos_edge_left, wall_width) #Desenha a borda lateral esquerda
		pygame.draw.line(screen, edge_color, start_pos_edge_right, end_pos_edge_right, wall_width) #Desenha a borda lateral direita

		pygame.draw.line(screen, racket_color, start_pos_racket_left, end_pos_racket_left , wall_width)
		pygame.draw.line(screen, racket_color, start_pos_racket_right, end_pos_racket_right, wall_width)

		pygame.draw.line(screen, red_brick, start_pos_red_brick_left, end_pos_red_brick_left, wall_width)
		pygame.draw.line(screen, red_brick, start_pos_red_brick_right, end_pos_red_brick_right, wall_width)

		pygame.draw.line(screen, orange_brick, start_pos_orange_brick_left, end_pos_orange_brick_left, wall_width)
		pygame.draw.line(screen, orange_brick, start_pos_orange_brick_right, end_pos_orange_brick_right, wall_width)

		pygame.draw.line(screen, green_brick, start_pos_green_brick_left, end_pos_green_brick_left , wall_width)
		pygame.draw.line(screen, green_brick, start_pos_green_brick_right, end_pos_green_brick_right, wall_width)

		pygame.draw.line(screen, yellow_brick, start_pos_yellow_brick_left, end_pos_yellow_brick_left, wall_width)
		pygame.draw.line(screen, yellow_brick, start_pos_yellow_brick_right, end_pos_yellow_brick_right, wall_width)