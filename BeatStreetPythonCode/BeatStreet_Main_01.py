import pygame
import os

def load_sound(sound_filename, directory):
    """load the sound file from the given directory"""
    fullname = os.path.join(directory, sound_filename)
    sound = pygame.mixer.Sound(fullname)
    return sound

pygame.mixer.pre_init(22050, -16, 1, 512)
pygame.init()

# pygame.init()
# pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=256)

# some color tuples (r,g,b)
screen = pygame.display.set_mode([600, 400])
pygame.display.set_caption("Simple Play Wave Files")

# pick a wave (.wav) sound file you have in the given directory
directory = "C:/Users/Robert/Documents/School/PennApps/Python/sounds"

left_heel = load_sound("Synth_01.wav", directory)
left_toe = load_sound("Tom_01.wav", directory)

right_heel = load_sound("Snare_01.wav", directory)
right_toe = load_sound("Tom_02.wav", directory)

scratch_in_right = load_sound("Scratch_in_01.wav", directory)
scratch_out_right = load_sound("Scratch_out_01.wav", directory)

scratch_in_left = load_sound("Scratch_in_02.wav", directory)
scratch_out_left = load_sound("Scratch_out_02.wav", directory)

shots = load_sound("Shots_01.wav", directory)
shots_continuation = load_sound("Shots_02.wav", directory)

# optional color change

screen.fill((0,0,0))
# event loop and exit conditions
# escape key or display window x
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            raise SystemExit
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_b):
            left_heel.play()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_c):
            left_toe.play()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_d):
            right_heel.play()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_e):
            right_toe.play()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_f):
            scratch_in_right.play()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_g):
            scratch_out_right.play()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_h):
            scratch_in_left.play()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_i):
            scratch_out_left.play()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_j):
            if (pygame.mixer.get_busy() == False):
                shots.play()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_k):
            if (pygame.mixer.get_busy() == False):
                shots_continuation.play()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_l):
            right_toe.play()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_m):
            right_heel.play()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_o):
            scratch_out_right.play()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_p):
            scratch_in_right.play()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            shots_continuation.play()
