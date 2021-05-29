'''
Title: Seed-Disposition-Golden-Angle
Author: SammygoodTunes
Version: 1.0
'''

import pygame, math, random, os

pygame.init()


class Window:
	
	def __init__(self, w=420, h=360):
		self.w, self.h = w, h
		self.screen = pygame.display.set_mode([self.w, self.h])
		self.clock = pygame.time.Clock()
		self.screenshot = pygame.Rect(0, 0, self.w, self.h)

	def take_screenshot(self):
		sub = self.screen.subsurface(self.screenshot)
		saved = False
		i = 0
		if not os.path.exists("screenshots"):
			os.mkdir("screenshots")
			print("made folder")
		while not saved:
			if os.path.isfile("screenshots/screenshot_" + str(i) + ".png"):
				i += 1
			else:
				saved = True
				name = "screenshot_" + str(i) + ".png"
				pygame.image.save(sub, "screenshots/" + name)
				print("Saved screenshot to /screenshots/" + name)		


	def get_width(self):
		return self.w


	def get_height(self):
		return self.h


class Colours:

	def __init__(self):
		self.black = (0, 0, 0)
		self.white = (255, 255, 255)


	def get_black(self):
		return self.black


	def get_white(self):
		return self.white


class Simulation:
	
	def __init__(self):
		self.end = False
		self.x, self.y = 0, 0
		self.angle = 0
		self.radius = 0
		self.width, self.height = 3, 3
		self.seed = (self.x, self.y, self.width, self.height)
		self.angle_constant = (3 - math.sqrt(5)) * 180


	def end_simulation(self):
		self.end = True


	def get_angle(self, x, y, angle):
		dx = int(x * math.cos(angle) - y * math.sin(angle))
		dy = int(x * math.sin(angle) + y * math.cos(angle))
		return dx, dy


	def change_angle(self, win, sim):
		self.x = (win.get_width() / 2) + sim.get_angle(self.radius, self.radius, math.radians(self.angle))[0]
		self.y = (win.get_height() / 2) + sim.get_angle(self.radius, self.radius, math.radians(self.angle))[1]
		self.radius += 1 - (360 - self.angle_constant) / 360



	def update_seed(self):
		self.seed = (self.x, self.y, self.width, self.height)


	def draw_seed(self, win, col, sim):
		pygame.draw.ellipse(win.screen, col.get_white(), sim.get_seed_rect())


	#remove the comments from the code below to enable randomised mode
	def decrease_angle(self):
		#if random.randint(0, 5) == 0:
			#self.angle_constant = -self.angle_constant
		self.angle -= self.angle_constant
		#self.angle_constant+=0.05

	def get_pos(self):
		return self.x, self.y


	def get_seed_rect(self):
		return self.seed



pygame.display.set_caption("Seed positioning by the Golden Angle")

def main():
	win = Window()
	sim = Simulation()
	col = Colours()

	while not sim.end:

		sim.decrease_angle()
		sim.change_angle(win, sim)
		sim.update_seed()
		sim.draw_seed(win, col, sim)

		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				sim.end_simulation()

			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_UP:
					pass

				if e.key == pygame.K_DOWN:
					pass

				if e.key == pygame.K_SPACE:
					pass

				if e.key == pygame.K_ESCAPE:
					win.take_screenshot()

		pygame.display.flip()
		win.clock.tick(60)

	pygame.quit()


if __name__ == '__main__':
	main()
