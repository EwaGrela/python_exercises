"""
simple program to count areas and perimeters of shapes
"""
from time import sleep
from math import pi


perimeter_msg = "Perimeter it is"
area_msg = "Area it is"
loading_msg = "Counting..."
error_msg = "Something went wrong, try again"
choice_msg = "Would you like to count area or perimeter?"
shapes = {"T":"You chose triangle", 
"C": "You chose circle", 
"R": "You chose rectangle", 
"N": "You chose regular rectangle",
 "Y": "You chose square"}

def calculate_triangle_area(b,h):
  area =  0.5 * h * b
  print "The area of the triangle is %.2f: " % area

def calculate_triangle_perimeter(a,b,c):
  perimeter = a + b + c
  print "The perimeter of the triangle is %.2f: " % perimeter

def calculate_circle_area(r):
  area = (pi * r) ** 2
  print "The area of the circle is %.2f: " % area

def calculate_circle_perimeter(r):
  perimeter = 2 * pi * r
  print "The perimeter of the circle is %.2f: " % perimeter

def calculate_rectangle_area(a,b):
  area = a * b
  print "The area of the rectangle is %.2f: " % area

def calculate_rectangle_perimeter(a,b):
  perimeter = 2 * (a + b)
  print "The perimeter of the rectangle is %.2f: " % perimeter

def calculate_square_area(a):
  area = a ** 2
  print "The area of the square is %.2f: " % area

def choose_shape():
  shape = raw_input("Please choose shape you want to calculate: T for 'triangle', 'C' for circle and 'R' for rectangle: ").upper()
  if shape =="T":
    print shapes[shape]
    print choice_msg
    choice = raw_input(" Put 'A' for 'area' and 'P' for perimeter: ").upper()
    if choice == "A":
      print area_msg
      height = int(raw_input("Choose height: "))
      base = int(raw_input("Choose base: "))
      print loading_msg
      sleep(2)
      calculate_triangle_area(base, height)
    elif choice == "P":
      print perimeter_msg
      side1 = int(raw_input("Put in side length: "))
      side2 = int(raw_input("Put in side length: "))
      side3 = int(raw_input("Put in side length: "))
      print loading_msg
      sleep(2)
      calculate_triangle_perimeter(side1, side2, side3)
    else:
      print error_msg
  elif shape =="C":
    print shapes[shape]
    print choice_msg
    choice = raw_input(" Put 'A' for 'area' and 'P' for perimeter: ").upper()
    radius = int(raw_input("Put in radius: "))
    if choice == "A":
      print area_msg
      print loading_msg
      sleep(2)
      calculate_circle_area(radius)
    elif choice == "P":
      print perimeter_msg
      print loading_msg
      sleep(2)
      calculate_circle_perimeter(radius)
    else: 
      print error_msg
  elif shape == "R":
    print shapes[shape]
    choice1 = raw_input("Is it a square? Y/N: ").upper()
    if choice1 == "Y":
      print shapes[choice1]
      choice2 = raw_input(" Put 'A' for 'area' and 'P' for perimeter: ").upper()
      side = int(raw_input(" How long is its side?: "))
      if choice2 =="A":
      	print area_msg
        print loading_msg
        sleep(2)
        calculate_square_area(side)
      elif choice2 =="P":
      	print perimeter_msg
        print loading_msg
        sleep(2)
        calculate_square_perimeter(side)
      else:
        print error_msg
    elif choice1 =="N":
      print shapes[choice1]
      choice2 = raw_input(" Put 'A' for 'area' and 'P' for perimeter: ").upper()
      height = int(raw_input("What is its height?: "))
      width = int(raw_input("What is its width?: "))
      if choice2 =="A":
      	print area_msg
        print loading_msg
        sleep(2)
        calculate_rectangle_area(height, width)
      elif choice2 =="P":
      	print perimeter_msg
        print loading_msg
        sleep(2)
        calculate_rectangle_perimeter(height, width)
      else:
        print error_msg
    else:
      print error_msg 
  else:
    print error_msg
choose_shape()
