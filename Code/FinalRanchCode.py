import pygame, math, sys, csv, eztext, inputbox
from pygame.locals import *
from random import randint



pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()

running_program = True
start_page = True
enter_initals_page = False
game_play = False
playing_game = False
game_over = False

def end_program():
	print("End of Game")


class BackgroundSprite(pygame.sprite.Sprite):
	def __init__(self, position, flip_image=False):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.src_image =  pygame.image.load('../Sprites/RanchBackground.png')
		self.src_image = pygame.transform.scale(self.src_image, (1600,500))
		if flip_image: self.src_image = pygame.transform.flip(self.src_image, True, False)
		self.speed = self.direction = 0

	def update(self, deltat):
		if self.position[0]>= -1100:
			self.position = (self.position[0] - eric.MOVEMENT_SPEED + 5, self.position[1])
			self.image = pygame.transform.rotate(self.src_image, self.direction)
			self.rect = self.image.get_rect()
			self.rect.center = self.position
		else:
			self.position = (1600,250)


class EricSprite(pygame.sprite.Sprite):
	MOVEMENT_SPEED = 7

	START_HEIGHT = 340
	APEX_HEIGHT = 150

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.pos_x = 10
		self.pos_y = self.START_HEIGHT
		self.position = self.pos_x, self.pos_y
		self.src_image = pygame.image.load("../Sprites/EricHorse–Standing.png")
		self.src_image = pygame.transform.scale(self.src_image, (100, 105))
		self.rect = pygame.rect.Rect((self.position[0], self.position[1]), (100, 50))
		self.rect.topleft = self.position
		self.speed = self.MOVEMENT_SPEED
		self.walking_images = ["../Sprites/EricHorse–Standing.png", "../Sprites/EricHorse-walking1.png", "../Sprites/EricHorse-walking2.png"]

		self.ranch_collected = 0
		self.distance = 0
		self.level = 1

		
		self.standing = True
		self.ducking = False
		self.jumping = False
		self.jump_acel = 2

		# print(self.ranch_collected)

	def move_left(self):
		self.pos_x -= self.MOVEMENT_SPEED
		self.position = self.pos_x, self.pos_y

	def move_right(self):
		self.pos_x += self.MOVEMENT_SPEED
		self.position = self.pos_x, self.pos_y

	def jump(self):
		self.jumping = True
		self.standing = False
		self.ducking = False

	def duck(self):
		self.jumping = False
		self.standing = False
		self.ducking = True

	def add_ranch(self):
		self.ranch_collected += 1
		# print(self.ranch_collected)

	def new_level(self):
		self.level += 1
		#*** NEW ITERATION: New level Panel, wait time, and reset

	def update(self):
		self.distance += 1
		self.MOVEMENT_SPEED = 7 + ((self.level - 1) * 3)
		'''Sprite Boundaries'''
		if self.pos_x <= 0:
			self.pos_x = 0
		elif self.pos_x >= 915:
			self.pos_x = 915 
		'''Deals with jumps'''
		if self.standing:
			self.JUMP_VELOCITY = -25
			self.src_image = pygame.image.load(self.walking_images[(self.distance % 3) - 1])
			self.src_image = pygame.transform.scale(self.src_image, (100, 105))
			if self.pos_y >= self.START_HEIGHT:
				self.pos_y = self.START_HEIGHT
		elif self.jumping:
			self.src_image = pygame.image.load("../Sprites/EricHorse-jumping.png")
			self.src_image = pygame.transform.scale(self.src_image, (100, 105))
			self.JUMP_VELOCITY += self.jump_acel
			self.pos_y += self.JUMP_VELOCITY
			if self.pos_y >= self.START_HEIGHT:
				self.standing = True
				self.jumping = False
				self.ducking = False
				self.pos_y = self.START_HEIGHT
		elif self.ducking:
			# self.move_left()
			key = pygame.key.get_pressed()
			if not(key[pygame.K_DOWN]):
				self.standing = True
				self.jumping = False
				self.ducking = False
				self.pos_y = self.START_HEIGHT
			self.src_image = pygame.image.load("../Sprites/EricHorse–Ducking.png")
			self.src_image = pygame.transform.scale(self.src_image, (90, 80))
			self.pos_y = self.START_HEIGHT + 30
		self.position = self.pos_x, self.pos_y
		self.rect = pygame.rect.Rect((self.position[0], self.position[1]), (100, 50))
		self.rect.topleft = self.position


class CopSprite(pygame.sprite.Sprite):
	MAX_SPEED =  10
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.position = 1000, 320
		self.src_image =  pygame.image.load("../Sprites/HannableCop.png")
		self.src_image = pygame.transform.scale(self.src_image, (75,105))
		self.speed = self.direction = 0
		# self.rect = self.src_image.get_rect()
		self.rect = pygame.rect.Rect((self.position[0], self.position[1]), (25, 100))
		self.rect.topleft = self.position
		

	def update(self, deltat):
		# print(self.src_image.get_size())
		
		# if self.position[0] >=0:
		self.position = (self.position[0] - eric.MOVEMENT_SPEED, self.position[1])
		self.image = pygame.transform.rotate(self.src_image, self.direction)
			# self.rect = self.src_image.get_rect()
			# self.rect = pygame.rect.Rect((self.position[0] + 500, self.position[1]), (25, 100))
			# self.rect.topleft = self.position
			# pygame.draw.rect(self.rect, "")
		if self.position[0] <= 0:
			self.position = (1000, 320)
			while abs(self.position[0] - kraft_punk.position[0]) < 350:
				self.position = (randint(1000, 2000),320)
		self.rect = pygame.rect.Rect((self.position[0], self.position[1]), (25, 100))
		self.rect.topleft = self.position

class KraftSprite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.position = 1000, 292
		while abs(self.position[0] - cop.position[0]) < 350:
			self.position = (randint(1200, 2000), 292)
		self.src_image =  pygame.image.load('../Sprites/KraftPunk.png')
		self.src_image = pygame.transform.scale(self.src_image, (175,100))
		self.speed = self.direction = 0
		self.rect = pygame.rect.Rect((self.position[0], self.position[1]), (150, 50))
		self.rect.topleft = self.position

	def update(self, deltat):
		if self.position[0] >=0:
			self.position = (self.position[0] - eric.MOVEMENT_SPEED, self.position[1])
			self.image = pygame.transform.rotate(self.src_image, self.direction)
			
		else:
			self.position = (1200,292)
			while abs(self.position[0] - cop.position[0]) < 350:
				self.position = (randint(1200, 2000), 292)
		self.rect = pygame.rect.Rect((self.position[0], self.position[1]), (150, 50))
		self.rect.topleft = self.position


class RanchSprite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.position = (randint(1200, 1500),300)
		while abs(self.position[0] - cop.position[0]) < 150:
			self.position = (randint(1200, 1500),300)
		self.ranch_images = ['../Sprites/Ranch.png', '../Sprites/SirachaRanch.png']
		self.src_image =  pygame.image.load(self.ranch_images[randint(0, 1)])
		self.src_image = pygame.transform.scale(self.src_image, (45,75))
		self.speed = self.direction = 0

		self.rect = pygame.rect.Rect((self.position[0], self.position[1]), self.src_image.get_size())
		self.rect.topleft = self.position

	def update(self, deltat):
		if self.position[0] >=0:
			self.position = (self.position[0] - eric.MOVEMENT_SPEED, self.position[1] - randint(-3,3))
			self.image = pygame.transform.rotate(self.src_image, self.direction)
			
		else:
			self.position = (randint(1200, 1500),300)
			while abs(self.position[0] - cop.position[0]) < 150:
				self.position = (randint(1200, 1500),300)
			self.src_image =  pygame.image.load(self.ranch_images[randint(0, 1)])
			self.src_image = pygame.transform.scale(self.src_image, (45,75))
		self.rect = pygame.rect.Rect((self.position[0], self.position[1]), self.src_image.get_size())
		self.rect.topleft = self.position

def update_highscore(name, score):
	file_name = '../ReadWriteFiles/highscore.csv'
	highscorefile_read = open(file_name, "r")
	# Adding
	file_handler = csv.reader(highscorefile_read, delimiter=",")
	scores_array = []
	for row in file_handler:
		scores_array.append((row[0], int(row[1])))
	scores_array.append((name, score))
	organized_by_score_array = sorted(scores_array, key=lambda x: x[1])[::-1]
	organized_by_score_array = organized_by_score_array[0: 10]
	highscorefile_read.close()

	highscorefile_write = open(file_name, 'w+')
	spamwriter = csv.writer(highscorefile_write, delimiter=',')
	for player_score in organized_by_score_array:
		spamwriter.writerow([player_score[0]] + [player_score[1]])
	highscorefile_write.close()

def check_highscore():
	file_name = '../ReadWriteFiles/highscore.csv'
	highscorefile_read = open(file_name, "r")
	file_handler = csv.reader(highscorefile_read, delimiter=",")
	scores_array = []
	for row in file_handler:
		scores_array.append((row[0], int(row[1])))
	highscorefile_read.close()
	return scores_array

def check_key():
	key = pygame.key.get_pressed()
	if key[pygame.K_a]:
		return "A"
	if key[pygame.K_b]:
		return "B"
	if key[pygame.K_c]:
		return "C"
	if key[pygame.K_d]:
		return "D"
	if key[pygame.K_e]:
		return "E"
	if key[pygame.K_f]:
		return "F"
	if key[pygame.K_g]:
		return "G"
	if key[pygame.K_h]:
		return "H"
	if key[pygame.K_i]:
		return "I"
	if key[pygame.K_j]:
		return "J"
	if key[pygame.K_k]:
		return "K"
	if key[pygame.K_l]:
		return "L"
	if key[pygame.K_m]:
		return "M"
	if key[pygame.K_n]:
		return "N"
	if key[pygame.K_o]:
		return "O"
	if key[pygame.K_p]:
		return "P"
	if key[pygame.K_q]:
		return "Q"
	if key[pygame.K_r]:
		return "R"
	if key[pygame.K_s]:
		return "S"
	if key[pygame.K_t]:
		return "T"
	if key[pygame.K_u]:
		return "U"
	if key[pygame.K_v]:
		return "V"
	if key[pygame.K_w]:
		return "W"
	if key[pygame.K_x]:
		return "X"
	if key[pygame.K_y]:
		return "Y"
	if key[pygame.K_z]:
		return "Z"
	return ""
	

#NEED TO CHANGE TO A PAGE INPUT ****
player_name_input = ""

while running_program:
	while start_page:
		# pygame.init()
		# pygame.mixer.init()
		
		start_music_srcs = ["../Audio/StartPage_DabOfRanch.wav", "../Audio/StartPage_Roley.wav"]
		if not(pygame.mixer.music.get_busy()):
			pygame.mixer.music.load(start_music_srcs[randint(0, 1)])
			pygame.mixer.music.play(1)
		
		screen.fill((255, 255, 255))
		start_background_image =  pygame.image.load("../Pages/startPageBackground.jpg")
		start_background_image = pygame.transform.scale(start_background_image, (1000,500))
		screen.blit(start_background_image, (0, 0))
		pygame.display.flip()

		for event in pygame.event.get():
				if not hasattr(event, 'key'): continue
		key = pygame.key.get_pressed()
		if key[pygame.K_ESCAPE]:
				end_program()
				sys.exit()
		if key[pygame.K_RETURN]:
			start_page = False
			game_play = False
			playing_game = False
			enter_initals_page = True

	while enter_initals_page:
		screen.fill((255, 255, 255))
		enter_initals_page_image =  pygame.image.load("../Pages/enterInitialsPage.jpg")
		enter_initals_page_image = pygame.transform.scale(enter_initals_page_image, (1000,500))
		screen.blit(enter_initals_page_image, (0, 0))
		
		
		new_letter = check_key()
		if not(new_letter == "") and len(player_name_input) < 3:
			player_name_input += new_letter
			print(player_name_input)
			name_font = pygame.font.SysFont("comicsansms", 50)
			player_name_input_render = []
			for letter in player_name_input:
				player_name_input_render.append(name_font.render(letter, True, (255, 0, 0)))
			pygame.time.delay(250)

		
		if len(player_name_input) > 0:
			print("screen is rending")
			index = 0
			for letter_render in player_name_input_render:
				screen.blit(letter_render, (335 + (95 * index), 260))
				index +=1
			
		pygame.display.flip()

		for event in pygame.event.get():
			if not hasattr(event, 'key'): continue
		key = pygame.key.get_pressed()
		if key[pygame.K_ESCAPE]:
				end_program()
				sys.exit()
		if key[pygame.K_BACKSPACE]:
			player_name_input = player_name_input[0: len(player_name_input) - 1]
			player_name_input_render = []
			for letter in player_name_input:
				player_name_input_render.append(name_font.render(letter, True, (255, 0, 0)))
			index = 0
			for letter_render in player_name_input_render:
				screen.blit(letter_render, (335 + (95 * index), 260))
				index +=1
		if key[pygame.K_RETURN] and len(player_name_input) == 3:
			print(player_name_input)
			start_page = False
			enter_initals_page = False
			game_play = True
			playing_game = True

	while game_play:
		pygame.display.set_caption('Ranch It up')

		cop = CopSprite()
		cop_group = pygame.sprite.Group(cop)

		kraft_punk = KraftSprite()
		kraft_group = pygame.sprite.Group(kraft_punk)

		ranch = RanchSprite()
		ranch_group = pygame.sprite.Group(ranch)

		background1 = BackgroundSprite((800,250))
		background2 = BackgroundSprite((2100,250), True)
		background_group = pygame.sprite.Group(background1)
		background_group.add(background2)

		eric = EricSprite()
		screen.fill((255, 255, 255))
		screen.blit(eric.src_image, eric.position)
		pygame.display.flip()

		# pygame.init()
		score_font = pygame.font.SysFont("comicsansms", 15)
		score = score_font.render("Ranch Collected: " + str(eric.ranch_collected), True, (255, 255, 255))


		level_font = pygame.font.SysFont("comicsansms", 15)
		level_board = level_font.render("Level: " + str(eric.level), True, (255, 255, 255))

		# pygame.mixer.init()
		pygame.mixer.music.load("../Audio/RanchItUp.wav")
		pygame.mixer.music.play(1)

		ranch_sounds_src = ["../Audio/SupMelo.wav", "../Audio/BuzzMeMullato.wav", "../Audio/RANCH.wav"]

		while playing_game:
			# print(cop.position[0], kraft_punk.position[0])
			'''Eric Andre Movement'''
			for event in pygame.event.get():
				if not hasattr(event, 'key'): continue
			key = pygame.key.get_pressed()
			if key[pygame.K_LEFT]:
				eric.move_left()
			if key[pygame.K_RIGHT]:
				eric.move_right()
			if key[pygame.K_SPACE] or key[pygame.K_UP]:
				if eric.standing:
					eric.jump()
			if key[pygame.K_DOWN]:
				eric.duck()
			if key[pygame.K_ESCAPE]:
				end_program()
				sys.exit()

			'''Collision Detection'''
			if pygame.sprite.spritecollide(eric, cop_group, True) or pygame.sprite.spritecollide(eric, kraft_group, True):
				pygame.time.delay(1000)
				update_highscore(player_name_input, eric.ranch_collected)
				playing_game = False
				game_play = False
				game_over = True
			if pygame.sprite.spritecollide(eric, ranch_group, True):
				pygame.mixer.music.load(ranch_sounds_src[randint(0, 2)])
				pygame.mixer.music.play(1)
				eric.add_ranch()
				# Add new ranch object
				ranch = RanchSprite()
				ranch_group.add(ranch)
				score = score_font.render("Ranch Collected: " + str(eric.ranch_collected), True, (255, 255, 255))


			'''Movement Updates'''
			deltat = clock.tick(30)
			background_group.update(deltat)
			cop_group.update(deltat)
			if eric.level > 2:
				kraft_group.update(deltat)
			ranch_group.update(deltat)
			eric.update()

			'''RENDERING'''
			screen.fill((255, 255, 255))
			background_group.draw(screen)

			pygame.draw.rect(screen, (0, 0, 0), (390, 22, 250, 22))

			screen.blit(score, (500, 22))


			if eric.distance % 200 == 0:
					eric.new_level()
					level_board = level_font.render("Level: " + str(eric.level), True, (255, 255, 255))


			screen.blit(level_board, (400, 22))


			# kraft_group.draw(screen)
			screen.blit(kraft_punk.src_image, (kraft_punk.position[0], kraft_punk.position[1] - 40))
			# pygame.draw.rect(screen, (255, 0, 0), kraft_punk.rect)

			# cop_group.draw(screen)
			screen.blit(cop.src_image, (cop.position[0] - 35, cop.position[1]))
			# pygame.draw.rect(screen, (255, 0, 0), cop.rect)
			
			# ranch_group.draw(screen)
			screen.blit(ranch.src_image, (ranch.position[0], ranch.position[1]))
			# pygame.draw.rect(screen, (255, 0, 0), ranch.rect)

			screen.blit(eric.src_image, (eric.position[0], eric.position[1] - 20))
			# pygame.draw.rect(screen, (255, 0, 0), eric.rect)

			pygame.display.flip()
	while game_over:



		# pygame.init()
		screen.fill((255, 255, 255))
		game_over_background_image =  pygame.image.load("../Pages/gameOverPage.jpg")
		game_over_background_image = pygame.transform.scale(game_over_background_image, (1000,500))
		screen.blit(game_over_background_image, (0, 0))
		
		highscore_board_array = check_highscore()
		highscore_font = pygame.font.SysFont("comicsansms", 20)
		index = 0
		for player_score in highscore_board_array:
			# Check for new highscore
			if player_name_input == player_score[0] and eric.ranch_collected == player_score[1]:
				new_high_score_image = pygame.image.load("../Pages/newHighScore.png")
				new_high_score_image = pygame.transform.scale(new_high_score_image, (450, 450))
				screen.blit(new_high_score_image, (240, 90))

				player_score_highlight_box = pygame.rect.Rect((800, 208 + (index * 24)), (200, 17))
				pygame.draw.rect(screen, (0, 0, 255), player_score_highlight_box)


			player_board_score = highscore_font.render(str(player_score[1]), True, (0, 255, 0))
			screen.blit(player_board_score, (850, 200 + (index  * 24)))

			player_board_name = highscore_font.render(str(player_score[0]), True, (255, 0, 0))
			screen.blit(player_board_name, (950, 200 + (index * 24)))

			index += 1

		pygame.display.flip()

		for event in pygame.event.get():
				if not hasattr(event, 'key'): continue
		key = pygame.key.get_pressed()
		if key[pygame.K_ESCAPE]:
				end_program()
				sys.exit()
		if key[pygame.K_RETURN]:
			start_page = False
			game_over = False
			game_play = False
			playing_game = False
			enter_initals_page = True
			player_name_input = ""
