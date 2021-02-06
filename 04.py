# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 10:16:43 2021

@author: Ailin
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()


x,y,z=mc.player.getTilePos()

width=10
height=6
lengh=5

mc.setblocks(x,y,z,x+width,y+height,z+lengh,20)
mc.setBlocks(x+1,y+1,z+1,x+width-1,y+height-1,z+lengh-1,0)

while True:
    x,y,z=mc.player.getTilePos()
    
    a=mc.getBlock(x+1,y-1,z)
    b=mc.getBlock(x-1,y-1,z)
    c=mc.getBlock(x,y-1,z+1)
    d=mc.getBlock(x,y-1,z-1)
    
    if a == 8 or a == 9 or b == 8 or b ==9 or c == 8 or c == 9 or d ==8 or d == 9:
        mc.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,20)
x,y,z=mc.player.getTilepos()
a=0
while a<8:
    mc.setBlocks(x+30,y-1,z,x-30,y-10,z,19)
    z=z+5
    a=a+1