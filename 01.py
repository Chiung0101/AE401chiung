# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
print(mc.player.getTilePos())
x=-58
y=78
z=168
mc.player.setTilePos(x,y,z)
