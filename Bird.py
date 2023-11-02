from pico2d import get_time, load_image, load_font, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from ball import Ball, BigBall
import game_world
import game_framework

# Bird Action Speed
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 15

#Bird Fly Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
FLY_SPEED_KMPH = 30.0  # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

BIRD_WIDTH = 183
BIRD_HEIGHT = 165

class Bird:
    def __init__(self, x, y, dir):
        self.x, self.y = x, y
        self.frame = 0
        self.dir = dir
        self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (self.frame + ACTION_PER_TIME * FRAMES_PER_ACTION * game_framework.frame_time) % 15
        if int(self.frame) == 4:
            self.frame +=1
        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time
        if self.x >= 1600 or self.x <= 50:
            self.dir *= -1

    def handle_event(self, event):
        pass

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw((int(self.frame) % 5) * BIRD_WIDTH, (int(self.frame) // 5) * BIRD_HEIGHT, BIRD_WIDTH, BIRD_HEIGHT, 0,
                                           '',
                                           self.x, self.y, BIRD_WIDTH//2, BIRD_HEIGHT//2)
        else:
            self.image.clip_composite_draw((int(self.frame) % 5) * BIRD_WIDTH, (int(self.frame) // 5) * BIRD_HEIGHT, BIRD_WIDTH, BIRD_HEIGHT, 0,
                                           'h',
                                           self.x, self.y, BIRD_WIDTH//2, BIRD_HEIGHT//2)
