#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  practica3.py
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

speed(0)

def casa():				   #Creamos la variable para formar una casa
	for techo in range(3): #Creamos el techo con la forma de un triangulo
		forward(50)		   #Definimos el largo de cada linea
		left(360/3)		   #Dividimos 360° en 3 para obtener la forma de un triangulo

	for cuadrado in range(4): #Creamos la base de la casa con la forma de un cuadrado
		forward(50)			  #Definimos el largo de cada linea
		right(360/4)	      #Dividimos 360° en 4 para obtener la forma de un cuadrado

def loop(veces): 					   #Creamos un loop para definir cuantas veces se repetira la secuencia
	for repeticiones in range (veces): #Hacemos un loop para obtener 'x' cantidad de casas
		casa() 						   #Llamamos la variable 'Casa'
		forward(50)					   #La tortuga avanza 50pxl para crear una casa aparte

def lineas(linea, veces):              
	for distancia in range(linea):
		loop(veces)
		left(180)
		forward(50 * veces)
		right(90)
		penup()
		forward(100)
		right(90)
		pendown()
		

lds=1
while(lds>0):
	vcs = int(raw_input("Ingrese la cantidad de casas en una misma linea: "))
	lns = int(raw_input("Ingrese la cantidad de lineas: "))
	lineas(lns, vcs)

