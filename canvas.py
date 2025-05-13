import pygame
import palette

class Canvas:
	
	hex="0123456789ABCDEF"
	
	def __init__(self,filename):
		fh=open(filename,"r")
		a=fh.readline().split(",")
		self.w=int(a[0])
		self.h=int(a[1])
		self.f=int(a[2])
		self.t=int(a[3])
		self.p=[]
		while(c:=fh.read(1)):
			v=self.hex.find(c)
			if v!=-1:
				self.p.append(v)
		fh.close()

	def draw(self,screen,x,y,f,s):
		for j in range(self.h):
			for i in range(self.w):
				c=self.p[f*self.w*self.h+j*self.w+i]
				if c != self.t:
					nx=i*s+x
					ny=j*s+y
					pygame.draw.rect(screen,palette.palette[c],pygame.Rect(nx,ny,s,s))

