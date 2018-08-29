#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  practica2.py
#  
#  Copyright 2018 Live System User <liveuser@localhost>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from turtle import *

for techo in range(3): #Creamos el techo con la forma de un triangulo
	forward(50)		   #Definimos el largo de cada linea
	left(360/3)		   #Dividimos 360° en 3 para obtener la forma de un triangulo

for cuadrado in range(4): 
	forward(50)
	right(360/4)
	
exitonclick()
