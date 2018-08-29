#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  practica1.py
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

def forma(lado, largo): #Definimos esta variable para que al llamarla dibuje un cuadrado
	for lados in range (lado):
		forward(largo)
		left(360/lado)

def loop(veces,lados, largo): #Creamos un loop para definir cuantas veces se repetira la secuencia
	for sec in range (veces): 
		forma(lados,largo)
		forward(largo)

lds=1
while(lds>0):
	lds = int(raw_input("Ingrese el numero de lados: "))
	lrg = int(raw_input("Ingrese un numero para el largo: "))
	vcs = int(raw_input("Ingrese cuantas veces se repetira: "))
	loop(vcs, lds, lrg)


exitonclick()
