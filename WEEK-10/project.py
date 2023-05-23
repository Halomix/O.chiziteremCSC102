#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Oranges:
    def __init__(self):
        self.stock = 50

    def buy_oranges(self):
        input1 = int(input("HOW MANY ORANGES WOULD YOU LIKE TO BUY: "))
        if input1 > self.stock:
            print("Select a quantity less than or equal to", self.stock)
        else:
            self.calculate_cost(input1)

    def calculate_cost(self, quantity):
        one_piece_cost = 50
        total_cost = one_piece_cost * quantity
        print("Total cost:", total_cost)
        print("Thanks for your pratronage")

oranges = Oranges()
oranges.buy_oranges()

        


# In[9]:


class Calculations:
    def __init__(self):
        pass

    def trapezium(self):
        Height = float(input("Enter Height: "))
        base1 = float(input("Enter Base1: "))
        base2 = float(input("Enter Base2: "))
        Area = Height / 2 * (base1 + base2)
        print("AREA =", Area)

    def rhombus(self):
        Diagonal1 = float(input("Enter Diagonal1: "))
        Diagonal2 = float(input("Enter Diagonal2: "))
        Area = 0.5 * Diagonal1 * Diagonal2
        print("AREA =", Area)

    def parallelogram(self):
        Base = float(input("Enter Base: "))
        Altitude = float(input("Enter Altitude: "))
        Area = Base * Altitude
        print("AREA =", Area)

    def cube(self):
        Length_of_the_side = float(input("Enter length of side: "))
        Area = 6 * Length_of_the_side ** 2
        print("AREA =", Area)

    def cylinder(self):
        Radius = float(input("Enter Radius: "))
        Height = float(input("Enter Height: "))
        Area = 3.14 * Radius * 2 * Height
        print("AREA =", Area)

    def use_formula(self):
        Input1 = input("What would you like to calculate?\nA. area of a trapezium\nB. area of a rhombus\nC. area of a parallelogram\nD. area of cylinder\nE. area of cube\n")

        if Input1 == 'A':
            self.trapezium()
        elif Input1 == 'B':
            self.rhombus()
        elif Input1 == 'C':
            self.parallelogram()
        elif Input1 == 'D':
            self.cylinder()
        elif Input1 == 'E':
            self.cube()
        else:
            print("Invalid entry")


calculate = Calculations()
calculate.use_formula()

     
    


# In[ ]:


import pandas as pd
class Nigerian_Brewries_Plc():
    def __init__(self):
        pass
    def ledger():
        print("Welcome to Nigerian Brewries Plc  \n")

goalkeepers = {'Madiba : ' : 'Çhubby Obiora-Okafo' ,
          'Blue-Jays:': 'Oladimeji Abaniwondea /Jeffery Awagu',
          'Cirok :'    : 'Timileyin Pearse / Izuako Jeremy',
          'TSG Walkers:': 'Ayomide Ojituku'}

captain = {'Madiba:': 'Chubby Obiora-Okafo', 'Blue-Jays:' : 'Christopher Uweh',
            'Cirok:': 'Alexander', 'TSG Walkers:' : 'Ikechukwu'}

        

