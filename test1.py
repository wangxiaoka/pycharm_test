# -*- coding: utf-8 -*-
import pygame

class Bullet:  #定义一个bullet类，封装子弹的相关数据和方法
	def __init__(self):  #初始化成员变量，x y image
		self.x=0
		self.y=-1
		self.image=pygame.image.load('bullet.png').convert_alpha()
	def move(self):  #处理子弹的运动
		if self.y<0:
			mouseX, mouseY = pygame.mouse.get_pos()
			self.x=mouseX - self.image.get_width()/2
			self.y=mouseY - self.image.get_height()/2
		else:
			self.y-=5

pygame.init()
screen=pygame.display.set_mode((450,800),0,32)
bu = Bullet()
bu.move()