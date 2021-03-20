# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 10:12:27 2021

@author: Ailin
"""

from mcpi.minecraft import Minecraft 
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

for i in range(1000):
    mc.setBlock(x,y-1,z+i,1)
 
from mcpi.minecraft import Minecraft 
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

for i in range(1000):
    mc.setBlock(x+i,y-1,z+i,x+i,y-1,z+i+3,1)
    
      