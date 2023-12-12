import pygame

class Ball:
    def __init__(self, x, y, radius, initial_speed, racket):
        self.radius = radius
        self.x = (x - (self.radius))
        self.y = (y - (self.radius))
        self.rect = pygame.Rect(x, y, self.radius * 2, self.radius * 2)
        self.x_speed = initial_speed
        self.y_speed = -initial_speed
        self.max_speed = initial_speed
        self.racket = racket
        self.lost = False
        self.score = 0
        self.current_speed_level = 1  # Nível inicial de velocidade
        self.hits_on_racket = 0



        # Adicionar efeitos sonoros
        self.racket_sound = pygame.mixer.Sound("assets/sound_effects/racket.wav")
        self.racket_sound.set_volume(0.4)

        self.brick_sound = pygame.mixer.Sound("assets/sound_effects/brick.wav")
        self.brick_sound.set_volume(0.3)

        self.wall_sound = pygame.mixer.Sound("assets/sound_effects/wall.wav")
        self.wall_sound.set_volume(0.4)

    def draw(self, screen):
        ball_color = (212, 210, 212)
        edge_ball = (0, 0, 0)
        pygame.draw.rect(screen, ball_color, self.rect)
        pygame.draw.rect(screen, edge_ball, self.rect, 2)

    def check_racket_collision(self, racket):
        colision_treesh = 5

        if self.rect.colliderect(racket.rect):
            if abs(self.rect.bottom - racket.rect.top) < colision_treesh and self.y_speed > 0:
                self.y_speed *= -1
                self.x_speed += racket.direction
                self.racket_sound.play()
                self.hits_on_racket += 1


                if self.hits_on_racket == 4:
                    # Ajusta a velocidade quando a bola tocar 4 vezes na raquete
                    self.x_speed = 1.0 if self.x_speed > 0 else -1.0
                    self.y_speed = -1.0

                if self.hits_on_racket == 12:
                    # Ajusta a velocidade quando a bola tocar 4 vezes na raquete
                    self.x_speed = 1.3 if self.x_speed > 0 else -1.3
                    self.y_speed = -1.3
                    self.hits_on_racket = 0  #Reseta o contador de toques na raquete

            if self.x_speed > self.max_speed:
                self.x_speed = self.max_speed
            elif self.x_speed < 0 and self.y_speed < -self.max_speed:
                self.x_speed = -self.max_speed

    def wall_collision(self, all_bricks, racket):
        colision_treesh = 5

        for row_cont, row in enumerate(all_bricks):
            for brike_cont, (brike_rect, points) in enumerate(row):
                if self.rect.colliderect(brike_rect):
                    if abs(self.rect.bottom - brike_rect.top) < colision_treesh and self.y_speed > 0:
                        self.y_speed *= -1
                    if abs(self.rect.top - brike_rect.bottom) < colision_treesh and self.y_speed < 0:
                        self.y_speed *= -1

                    if abs(self.rect.right - brike_rect.left) < colision_treesh and self.x_speed > 0:
                        self.x_speed *= -1
                    if abs(self.rect.left - brike_rect.right) < colision_treesh and self.x_speed < 0:
                        self.x_speed *= -1

                    self.update_score(points)
                    all_bricks[row_cont][brike_cont] = ((0, 0, 0, 0), 0)  # Tijolo destruído com um toque

    def update_score(self, points):
        if points == 7:
            self.score += 7
            self.brick_sound.play()
        elif points == 5:
            self.score += 5
            self.brick_sound.play()
        elif points == 3:
            self.score += 3
            self.brick_sound.play()
        elif points == 1:
            self.score += 1
            self.brick_sound.play()

    def update_movement(self, screen_width, screen_height, racket, on_racket):
        if on_racket:
            return False  # Retorna False se a bola ainda está na raquete

        if self.lost:
            return True  #Retorna True se a bola foi perdida

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        self.screen_boundaries(screen_width, screen_height)
        self.check_racket_collision(racket)

        return False  #Retorna False se a bola não foi perdida


    def screen_boundaries(self, screen_width, screen_height):
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.x_speed *= -1
            self.wall_sound.play()

        if self.rect.top < 0:
            self.y_speed *= -1
            self.wall_sound.play()

        if self.rect.bottom > screen_height:
            self.lost = True

    def reset_position(self, x, y):
        self.x = x - self.radius
        self.y = y - self.radius
        self.rect.x = x - self.radius
        self.rect.y = y - self.radius
        self.lost = False
        self.ball_on_racket = True
        self.reset_ball_speed()

    def reset_ball_speed(self):
        self.x_speed = 1
        self.y_speed = -1
        self.current_speed_level = 1 #Resetar o nível de velocidade ao reiniciar a bola

    def adjust_speed(self, brick_points):
        if brick_points == 5 or brick_points == 7:  # Laranja ou vermelho
            self.x_speed = 1.5 if self.x_speed > 0 else -1.5
            self.y_speed = -1.5