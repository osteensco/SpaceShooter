import pygame
import os
pygame.font.init()


#game window and fonts
WIDTH, HEIGHT = 1080, 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Defense")
main_font = pygame.font.SysFont("comicsans", 50)
lost_font = pygame.font.SysFont("comicsans", 100)
#menu and in game messaging font
title_font = pygame.font.SysFont("comicsans", 60)


# variables
set_FPS = 90#handle all variables like this so that they can be adjusted in settings menu?
scroll_vel = 2
shield_base_time = 3
enemy_vel = 1
enparmove = round(enemy_vel*1.5)
enemy_laser_vel = 4
player_vel = 10
enemy_power = 10


#func to load images
def load_image(folder, image_name):
    image = pygame.image.load(os.path.join(folder, image_name))
    image = image.convert_alpha()
    return image


#background
background = pygame.transform.scale(load_image("assets", "background-black.png"), (WIDTH, HEIGHT))
bg1_img = background
bg2_img = pygame.transform.rotate(background, 180)
bg3_img = bg2_img
bg4_img = bg1_img

x_adj = background.get_width()
y_adj = background.get_height()
quadrant = int(WIDTH/4)


#Load images
#drops
health_drop = load_image("assets", "health_drop.png")
fire_rate_drop = load_image("assets", "fire_rate_drop.png")
shield_drop = load_image("assets", "shield_drop.png")
butterfly_drop = load_image("assets", "butterfly_drop.png")

#ships
red_space_ship = load_image("assets", "pixel_ship_red_small.png")
green_space_ship = load_image("assets", "pixel_ship_green_small.png")
blue_space_ship = load_image("assets", "pixel_ship_blue_small.png")
explosion = load_image("assets", "explosion.png")
explosion2 = load_image("assets", "Boom.png")
explosions = [explosion, explosion2]
blank = load_image("assets", "blank.png")


#boss stuff
drone_img = load_image("assets", "boss_minion.png")
drone_laser_img = load_image("assets", "pixel_laser_gold.png")
boss_weapon_0 = load_image("assets", "boss_weapon_0.png")
boss_weapon_1 = load_image("assets", "boss_weapon_1.png")
boss_weapon_2 = load_image("assets", "boss_weapon_2.png")
#green
boss_0 = load_image("assets", "boss_0.png")
boss_0_0 = load_image("assets", "boss_0_0.png")
boss_green = [boss_0, boss_0_0]
boss_0_shield_0 = load_image("assets", "boss_0_shield_0.png")
boss_0_shield_1 = load_image("assets", "boss_0_shield_1.png")
boss_0_shield_2 = load_image("assets", "boss_0_shield_2.png")
boss_0_shield_3 = load_image("assets", "boss_0_shield_3.png")
boss_0_shield_4 = load_image("assets", "boss_0_shield_4.png")
boss_0_shield = [boss_0_shield_0, boss_0_shield_1, boss_0_shield_2, boss_0_shield_3, boss_0_shield_4]
boss_0_flect_0 = load_image("assets", "boss_0_flect_0.png")
boss_0_flect_1 = load_image("assets", "boss_0_flect_1.png")
boss_0_flect_2 = load_image("assets", "boss_0_flect_2.png")
boss_0_flect_3 = load_image("assets", "boss_0_flect_3.png")
boss_0_flect = [boss_0_flect_0, boss_0_flect_1, boss_0_flect_2, boss_0_flect_3]
boss_0_drone_0 = load_image("assets", "boss_0_drone_0.png")
boss_0_drone_1 = load_image("assets", "boss_0_drone_1.png")
boss_0_drone = [boss_0_drone_0, boss_0_drone_1]
#blue
boss_1 = load_image("assets", "boss_1.png")
boss_1_0 = load_image("assets", "boss_1_0.png")
boss_blue = [boss_1, boss_1_0]
boss_1_shield_0 = load_image("assets", "boss_1_shield_0.png")
boss_1_shield_1 = load_image("assets", "boss_1_shield_1.png")
boss_1_shield_2 = load_image("assets", "boss_1_shield_2.png")
boss_1_shield_3 = load_image("assets", "boss_1_shield_3.png")
boss_1_shield_4 = load_image("assets", "boss_1_shield_4.png")
boss_1_shield = [boss_1_shield_0, boss_1_shield_1, boss_1_shield_2, boss_1_shield_3, boss_1_shield_4]
boss_1_flect_0 = load_image("assets", "boss_1_flect_0.png")
boss_1_flect_1 = load_image("assets", "boss_1_flect_1.png")
boss_1_flect_2 = load_image("assets", "boss_1_flect_2.png")
boss_1_flect_3 = load_image("assets", "boss_1_flect_3.png")
boss_1_flect = [boss_1_flect_0, boss_1_flect_1, boss_1_flect_2, boss_1_flect_3]
boss_1_drone_0 = load_image("assets", "boss_1_drone_0.png")
boss_1_drone_1 = load_image("assets", "boss_1_drone_1.png")
boss_1_drone = [boss_1_drone_0, boss_1_drone_1]
#red
boss_2 = load_image("assets", "boss_2.png")
boss_2_0 = load_image("assets", "boss_2_0.png")
boss_red = [boss_2, boss_2_0]
boss_2_shield_0 = load_image("assets", "boss_2_shield_0.png")
boss_2_shield_1 = load_image("assets", "boss_2_shield_1.png")
boss_2_shield_2 = load_image("assets", "boss_2_shield_2.png")
boss_2_shield_3 = load_image("assets", "boss_2_shield_3.png")
boss_2_shield_4 = load_image("assets", "boss_2_shield_4.png")
boss_2_shield = [boss_2_shield_0, boss_2_shield_1, boss_2_shield_2, boss_2_shield_3, boss_2_shield_4]
boss_2_flect_0 = load_image("assets", "boss_2_flect_0.png")
boss_2_flect_1 = load_image("assets", "boss_2_flect_1.png")
boss_2_flect_2 = load_image("assets", "boss_2_flect_2.png")
boss_2_flect_3 = load_image("assets", "boss_2_flect_3.png")
boss_2_flect = [boss_2_flect_0, boss_2_flect_1, boss_2_flect_2, boss_2_flect_3]
boss_2_drone_0 = load_image("assets", "boss_2_drone_0.png")
boss_2_drone_1 = load_image("assets", "boss_2_drone_1.png")
boss_2_drone = [boss_2_drone_0, boss_2_drone_1]



#player ship
player_space_ship = load_image("assets", "pixel_ship_yellow.png")
player_ship_shield = load_image("assets", "player_ship_shield.png")

#Lasers
red_laser = load_image("assets", "pixel_laser_red.png")
green_laser = load_image("assets", "pixel_laser_green.png")
blue_laser = load_image("assets", "pixel_laser_blue.png")
yellow_laser = load_image("assets", "pixel_laser_yellow.png")
butterfly_lasers = [red_laser, green_laser, blue_laser, yellow_laser]

