import os
import time
import pygame
from tkinter import *
import random
import tkinter.messagebox as tmsg
os.system('cls')
##Import Success
#Defining The main and game
def main():
	print("There Are 6 Snake,Food,Background Colors And They Are:\n\
	red        blue\n\
	green      yellow\n\
	white      black\n")
	time.sleep(1.5)
	print("The Default \n\nSnake Color Is black\n\nFood Color Is red\n\nBackGround Color Is white")
	time.sleep(1.5)
	print("")
	print("If you Don't Know How To Use Open Readme.txt File")
	time.sleep(1.5)
	root = Tk()
	root.title("ASGC")
	root.geometry("300x363")
	root.minsize(400,620)
	root.maxsize(400,620)
	Label(text = "Automatic Snake Game Creator..",bg = "green",font = 15,pady = 20).pack(anchor = "w")
	#Inf
	l4 = Label(text = "If You Will Press 'c' Key From Your Keyboard\n\nThen That Will Increase Your Snake Size And Your Score\n\nJust Think That Its Your Cheat Code\n       ",pady = 5,bg = "green",font = 10)

	l4.pack(anchor = "w")
	#Snake Color
	color = StringVar()
	color.set("black")
	colorbox = Entry(textvariable = color,bg = "black",fg = "white",width = 60,font = 11)
	l1 = Label(text = "                     Snake Color..       ",font = 10,pady = 5,bg = "green")

	l1.pack(anchor = "w")
	colorbox.pack(anchor = "w")

	#Food Color
	fcolor = StringVar()
	fcolor.set("red")
	fcolorbox = Entry(textvariable = fcolor,bg = "black",fg = "white",width = 60,font = 11)
	l2 = Label(text = "                     Food Color..       ",pady = 5,bg = "green",font = 10)

	l2.pack(anchor = "w")
	fcolorbox.pack(anchor = "w")

	#Background Color
	bcolor = StringVar()
	bcolor.set("green")
	bcolorbox = Entry(textvariable = bcolor,bg = "black",fg = "white",width = 60,font = 11)
	l3 = Label(text = "                     Background Color Of Your Game.       ",pady = 5,bg = "green",font = 10)

	l3.pack(anchor = "w")
	bcolorbox.pack(anchor = "w")

	#Title
	title = StringVar()
	title.set("Snake Game")
	titlebox = Entry(textvariable = title,bg = "black",fg = "white",width = 60,font = 11)
	l3 = Label(text = "                     Title Of Your Game       ",pady = 5,bg = "green",font = 10)

	l3.pack(anchor = "w")
	titlebox.pack(anchor = "w")

	press = StringVar()
	press.set("You Have Exitted The Game")
	pressbox = Entry(textvariable = press,bg = "black",fg = "white",width = 60,font = 11)
	l5 = Label(text = "                     What To Say If THE Game Is EXIT ?       ",pady = 5,bg = "green",font = 10)

	l5.pack(anchor = "w")
	pressbox.pack(anchor = "w")

	width = IntVar()
	width.set(700)
	widthbox = Entry(textvariable = width,bg = "black",fg = "white",width = 60,font = 11)
	l6 = Label(text = "                     Game Screen Width        ",pady = 5,bg = "green",font = 10)

	l6.pack(anchor = "w")
	widthbox.pack(anchor = "w")

	height = IntVar()
	height.set(500)
	heightbox = Entry(textvariable = height,bg = "black",fg = "white",width = 60,font = 11)
	l7 = Label(text = "                     Game Screen Height        ",pady = 5,bg = "green",font = 10)

	l7.pack(anchor = "w")
	heightbox.pack(anchor = "w")

	Label(text = "",pady = 5,bg = "green").pack(anchor = "w")
	def game():
		os.system('cls')

		pygame.init()

		screen_width = (width.get())
		screen_height = (height.get())
		screen_caption = f"{(title.get())}"

		screen = pygame.display.set_mode((screen_width,screen_height))
		pygame.display.set_caption((screen_caption))

		game_over = False
		game_end = False
		snake_x = 45
		snkae_y = 55
		snake_size = 14
		vel_x = 0
		vel_y = 0

		food_x = random.randint(20,screen_width/2)
		food_y = random.randint(20,screen_height/2)

		food_size = 12
		fps = 25

		score = 0

		red = [255,0,0]
		white = [255,255,255]
		black = [0,0,0]

		green = [0,204,0]
		yellow = [255,255,0]
		blue = [0,0,204]

		clock = pygame.time.Clock()
		def sblack(screen,black,snake_x,snkae_y,snake_size):
			pygame.draw.rect(screen,black,[snake_x,snkae_y,snake_size,snake_size])
		def swhite(screen,white,snake_x,snkae_y,snake_size):
			pygame.draw.rect(screen,white,[snake_x,snkae_y,snake_size,snake_size])
		def sblue(screen,blue,snake_x,snkae_y,snake_size):
			pygame.draw.rect(screen,blue,[snake_x,snkae_y,snake_size,snake_size])
		def syellow(screen,yellow,snake_x,snkae_y,snake_size):
			pygame.draw.rect(screen,yellow,[snake_x,snkae_y,snake_size,snake_size])
		def sgreen(screen,green,snake_x,snkae_y,snake_size):
			pygame.draw.rect(screen,green,[snake_x,snkae_y,snake_size,snake_size])
		def sred(screen,red,snake_x,snkae_y,snake_size):
			pygame.draw.rect(screen,red,[snake_x,snkae_y,snake_size,snake_size])
		#Food
		def fblack(screen,black,food_x,food_y,food_size):
			pygame.draw.rect(screen,black,[food_x,food_y,food_size,food_size])
		def fwhite(screen,white,food_x,food_y,food_size):
			pygame.draw.rect(screen,white,[food_x,food_y,food_size,food_size])
		def fblue(screen,blue,food_x,food_y,food_size):
			pygame.draw.rect(screen,blue,[food_x,food_y,food_size,food_size])
		def fyellow(screen,yellow,food_x,food_y,food_size):
			pygame.draw.rect(screen,yellow,[food_x,food_y,food_size,food_size])
		def fgreen(screen,green,food_x,food_y,food_size):
			pygame.draw.rect(screen,green,[food_x,food_y,food_size,food_size])
		def fred(screen,red,food_x,food_y,food_size):
			pygame.draw.rect(screen,red,[food_x,food_y,food_size,food_size])
		#Background
		while not game_end:
			if game_over == True:
				os.system('cls')
				screen.fill(white)
				pygame.display.update()
				pygame.display.set_caption(("Game Over....."))
				time.sleep(1)
				pygame.display.update()
				pygame.display.set_caption(("Loading 50%.."))
				time.sleep(.9)
				pygame.display.update()
				pygame.display.set_caption(("Loading 100%..."))
				os.system('cls')
				time.sleep(.9)
				os.system('cls')
				game()
			else:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						os.system('cls')
						pygame.display.set_caption((f"{(press.get())}"))
						os.system('cls')
						time.sleep(1.5)
						game_end = True
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_DOWN:
							vel_y = 10
							vel_x = 0
						if event.key == pygame.K_UP:
							vel_y = -10
							vel_x = 0
						if event.key == pygame.K_LEFT:
							vel_y = 0
							vel_x = -10
						if event.key == pygame.K_RIGHT:
							vel_y = 0
							vel_x = 10
						if event.key == pygame.K_c:
							score = score +200
							os.system('cls')
							snake_size = snake_size+1
							print(f"Score: {score}")
				if abs(snake_x-food_x)<10 and abs(snkae_y-food_y)<10:
					os.system('cls')
					score = score+1
					print(f"Score: {score}")
					food_x = random.randint(20,screen_width/2)
					food_y = random.randint(20,screen_height/2)
					snake_size = snake_size+1
					food_size = food_size+1
					pygame.display.set_caption((f"Score: {score}"))
				if snake_x>screen_width or snkae_y>screen_height or snake_x<0 or snkae_y<0:
					game_over = True
				snake_x = snake_x+vel_x
				snkae_y = snkae_y + vel_y
				if((bcolor.get()) == "white"):
					screen.fill(white)
				elif((bcolor.get()) == "red"):
					screen.fill(red)
				elif((bcolor.get()) == "black"):
					screen.fill(black)
				elif((bcolor.get()) == "blue"):
					screen.fill(blue)
				elif((bcolor.get()) == "yellow"):
					screen.fill(yellow)
				elif((bcolor.get()) == "green"):
					screen.fill(green)
				else:
					tmsg.showinfo('Error','Error...Something Is Empty\nOR\nWrong Input Given')
					pygame.quit()
					quit()
				#Snake If
				if((color.get()) == "black"):
					sblack(screen,black,snake_x,snkae_y,snake_size)
				elif((color.get()) == "white"):
					swhite(screen,white,snake_x,snkae_y,snake_size)
				elif((color.get()) == "yellow"):
					syellow(screen,yellow,snake_x,snkae_y,snake_size)
				elif((color.get()) == "red"):
					sred(screen,red,snake_x,snkae_y,snake_size)
				elif((color.get()) == "green"):
					sgreen(screen,green,snake_x,snkae_y,snake_size)
				elif((color.get()) == "blue"):
					sblue(screen,blue,snake_x,snkae_y,snake_size)
				else:
					tmsg.showinfo('Error','Error...Something Is Empty\nOR\nWrong Input Given')
					pygame.quit()
					quit()

				#Food If
				if((fcolor.get()) == "black"):
					fblack(screen,black,food_x,food_y,food_size)
				elif((fcolor.get()) == "white"):
					fwhite(screen,white,food_x,food_y,food_size)
				elif((fcolor.get()) == "yellow"):
					fyellow(screen,yellow,food_x,food_y,food_size)
				elif((fcolor.get()) == "red"):
					fred(screen,red,food_x,food_y,food_size)
				elif((fcolor.get()) == "green"):
					fgreen(screen,green,food_x,food_y,food_size)
				elif((fcolor.get()) == "blue"):
					fblue(screen,blue,food_x,food_y,snake_size)
				else:
					tmsg.showinfo('Error','Error...Something Is Empty\nOR\nWrong Input Given')
					pygame.quit()
					quit()
			pygame.display.update()
			clock.tick(fps)
		pygame.quit()
	Button(text ="Click Here To Make The Game As Your Wish",command = game,bg = "red").pack(anchor="w")
	root.config(bg = "green")
	root.mainloop()
main()
#Def SUccess