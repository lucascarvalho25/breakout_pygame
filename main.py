import sys
import pygame
from brick import Brick
from racket import Racket
from ball import Ball
from edge import Edge
import pygame.font

dozens = 0
hundreds = 0
columns = 14
rows = 8
pygame.font.init()
pygame.init()
clock = pygame.time.Clock()
black_background = (0, 0, 0)
red_message = (255, 0, 0)
score_color = (212, 210, 212)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout")
lives = 1
score = 0
game_over = False
reduction_count = 0

brick_wall = Brick(screen, screen_width - 19, columns, rows)
racket = Racket(screen_width, screen_height, columns)
initial_ball_position = (
    racket.rect.x + ((racket.width // 2) - 7.5),
    racket.rect.y - ((racket.height * 2) - 21),
)

ball = Ball(
    initial_ball_position[0],
    initial_ball_position[1],
    7,
    initial_speed=1,
    racket=racket
)

edge = Edge()

font_size = 36
game_font = pygame.font.Font("assets/font/game_font.ttf", font_size)
score_font = pygame.font.Font("assets/font/score_font.ttf", 36)

new_wall_needed = False
ball_on_racket = True

red_bricks_height = brick_wall.blocks_all_wall[0][0][0].top
reduction_done = False

def expand_racket_to_edges(racket, screen_width):
    if racket.rect.left > 0:
        expansion_left = racket.rect.left
        racket.rect.x = 0
        racket.rect.width += expansion_left

    if racket.rect.right < screen_width:
        expansion_right = screen_width - racket.rect.right
        racket.rect.width += expansion_right

def draw_final_screen(screen, brick_wall, racket, ball_on_racket):
    screen.fill(black_background)
    brick_wall.draw_wall(screen)
    racket.draw(screen)
    if ball_on_racket:
        ball.rect.x = racket.rect.x + (racket.width // 2) - 7.5
        ball.rect.y = racket.rect.y - ((racket.height * 2) - 21)
    ball.draw(screen)
    pygame.display.update()

def draw_game_over_screen(screen, brick_wall, racket):
    screen.fill(black_background)
    brick_wall.draw_wall(screen)
    racket.draw(screen)
    pygame.display.update()

def reset_game():
    global lives, score, ball_on_racket, brick_wall, racket, ball, new_wall_needed, game_over, reduction_done, dozens, hundreds
    lives = 1
    score = 0
    dozens = 0
    hundreds = 0
    ball_on_racket = True
    new_wall_needed = False
    game_over = False
    reduction_done = False
    brick_wall = Brick(screen, screen_width - 19, columns, rows)
    racket = Racket(screen_width, screen_height, columns)
    initial_ball_position = (
        racket.rect.x + ((racket.width // 2) - 7.5),
        racket.rect.y - ((racket.height * 2) - 21),
    )
    ball = Ball(
        initial_ball_position[0],
        initial_ball_position[1],
        7,
        initial_speed=1,
        racket=racket
    )


flag = True
while flag and lives > 0:
    screen.fill(black_background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    edge.edge()

    racket.update_movement(screen_width)

    if ball_on_racket:
        ball.rect.x = racket.rect.x + (racket.width // 2) - 7.5
        ball.rect.y = racket.rect.y - ((racket.height * 2) - 21)

    lost_life = ball.update_movement(screen_width, screen_height, racket, ball_on_racket)

    if ball.rect.y < red_bricks_height and not reduction_done:
        racket.width /= 2
        racket.rect.width = int(racket.width)
        racket.original_width = racket.width
        reduction_done = True


    if ball.rect.y >= red_bricks_height and reduction_count == 0:
        reduction_done = False
        reduction_count = reduction_count + 1

    if lost_life:
        lives = lives + 1
        if lives < 4 and lives >= 1:
            ball_on_racket = True
            ball.reset_position(
                racket.rect.x + (racket.width // 2) - 7.5,
                racket.rect.y - ((racket.height * 2) - 21)
            )
            racket.hits = 0
            ball.reset_ball_speed()
    else:
        ball_on_racket = False

    if ball.hits_on_racket == 4 and ball_on_racket:
        ball.current_speed_level = 2
        ball_on_racket = False

    if ball.hits_on_racket == 12 and ball_on_racket:
        ball.current_speed_level = 3
        ball.hits_on_racket = 0
        ball_on_racket = False

    ball.check_racket_collision(racket)
    ball.wall_collision(brick_wall.blocks_all_wall, racket)
    brick_wall.increase_ball_speed(ball)
    brick_wall.draw_wall(screen)
    racket.draw(screen)
    ball.draw(screen)

    lives_text = score_font.render(f"{lives}", True, score_color)
    screen.blit(lives_text, (650, 40))
    score_text = score_font.render(f"{hundreds}{dozens}{ball.score}", True, score_color)
    if ball.score > 9:
        dozens = dozens + 1
        ball.score = 0
        score_text = score_font.render(f"{hundreds}{dozens}{ball.score}", True, score_color)
        if dozens > 9:
            hundreds = hundreds + 1
            dozens = 0
            score_text = score_font.render(f"{hundreds}{dozens}{ball.score}", True, score_color)
    screen.blit(score_text, (80, 40))

    if brick_wall.blocks_all_wall and brick_wall.blocks_all_wall[0]:
        first_row_bricks = brick_wall.blocks_all_wall[0]

        for brick_rect, points in first_row_bricks:
            if isinstance(brick_rect, pygame.Rect) and racket.rect.colliderect(brick_rect):
                if (
                        racket.rect.top < brick_rect.top
                        and racket.rect.bottom > brick_rect.top
                        and racket.width > racket.original_width / 2
                ):
                    racket.width /= 2
                    racket.rect.width = int(racket.width)
                    racket.original_width = racket.width

    if all(all(brick[1] == 0 for brick in row) for row in brick_wall.blocks_all_wall):
        if new_wall_needed:
            flag = False
        else:
            new_wall_needed = True
            brick_wall = Brick(screen, screen_width, columns, rows)
            reduction_count = 0

            initial_ball_position = (
                racket.rect.x + ((racket.width // 2) - 7.5),
                racket.rect.y - ((racket.height * 2) - 21),
            )
            ball.reset_position(*initial_ball_position)

    pygame.display.update()

    if lives == 4:
        expand_racket_to_edges(racket, screen_width)
        draw_final_screen(screen, brick_wall, racket, ball_on_racket)
        lives_text = score_font.render(f" {lives}", True, score_color)
        screen.blit(lives_text, (650, 40))
        score_text = score_font.render(f"{hundreds}{dozens}{ball.score}", True, score_color)
        screen.blit(score_text, (80, 40))
        edge.edge()
        lives_text = game_font.render("PRESS SPACE TO RESTART", True, red_message)
        screen.blit(lives_text, (screen_width // 2 - 260, screen_height // 2))
        pygame.display.update()

        restart_game = False
        while not restart_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    reset_game()
                    restart_game = True
                    game_over = False

pygame.quit()
sys.exit()
