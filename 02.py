# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x=-79
y=70
z=226




mc.player.setTilePos(x,y,z )
time.sleep(0.5)
y=y+1
mc.player.setTilePos(x,y,z )
time.sleep(0.5)
y=y+1
mc.player.setTilePos(x,y,z )

t=0
while True:

    t=t+1
    mc.postToChat(str(t)+'times')
while True:
    x,y.z=player.getTilePos()
    mc.postToChat
    
    mc.postToChat(str(x,y,z)+'times')