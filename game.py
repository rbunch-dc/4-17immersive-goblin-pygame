
# 1. Include pygame
# Include pygame which we got from pip
import pygame

# in order to use pygame, we have to run the init method
# 2. Init pygame
pygame.init()


# 3. Create a screen with a size
screen = {
	"height": 512,
	"width": 480
}

keys = {
	"right": 275,
	"left": 276,
	"up": 273,
	"down": 274
}

keys_down = {
	"right": False,
	"left": False,
	"up": False,
	"down": False,
}

hero = {
	"x": 100,
	"y": 100,
	"speed": 10
}

screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('./images/background.png')
hero_image = pygame.image.load('./images/hero.png')
hero_image_scaled = pygame.transform.scale(hero_image, (99,96));




# /////////////////////////////////////////////
# //////////////MAIN GAME LOOP/////////////////
# /////////////////////////////////////////////	x
game_on = True
# Create the game loop (while 1)
while game_on:
	# we are inside teh main game loop. It will run as long as game_on is true
	# ---EVENTS!!----
	for event in pygame.event.get():
		# Looping through all events that happened this game loop cycle
		# 4. Add a quit event (requires sys)
		if event.type == pygame.QUIT:
			# the user clicked on the red X to leave the game
			game_on = False
			# update our boolean, so pygame can escape the loop
		elif event.type == pygame.KEYDOWN:
			if event.key == keys['up']:
				keys_down['up'] = True
			elif event.key == keys['down']:
				keys_down['down'] = True
			elif event.key == keys['left']:
				# print "User pressed left!"
				keys_down['left'] = True
			elif event.key == keys['right']:
				# print "User pressed right!"
				keys_down['right'] = True
		elif event.type == pygame.KEYUP:
			# print "The user let go of a key"
			if event.key == keys['up']:
				# the user let go of a key... and that key was the up arrow
				keys_down['up'] = False
			if event.key == keys['down']:
				keys_down['down'] = False
			if event.key == keys['left']:
				keys_down['left'] = False
			if event.key == keys['right']:
				keys_down['right'] = False

	# Update Hero position
	if keys_down['up']:
		hero['y'] -= hero['speed']
	elif keys_down['down']:
		hero['y'] += hero['speed']
	if keys_down['left']:
		hero['x'] -= hero['speed']
	elif keys_down['right']:
		hero['x'] += hero['speed']


	# ---RENDER!---
	# blit takes 2 arguments
	# 1. What?
	# 2. Where?
	# Screen.fill (pass bg_color)
	pygame_screen.blit(background_image, [0,0])

	# draw the hero
	pygame_screen.blit(hero_image_scaled, [hero['x'],hero['y']])

	# clear the screen for next time
	pygame.display.flip()

	# Flip the screen and start ove4
