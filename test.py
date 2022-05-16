from os import name, system
from time import sleep
# import pathlib
# import mpmath, math
# Get the first million digits of pi
# pi = pathlib.Path('pi.txt').read_text()
# Get title banner
# banner = pathlib.Path('banner.txt').read_text()
# Clear the screen
def clear():
	if name == 'nt':
		system('cls')
	else:
		system('clear')
# Check if the number ends in .0
# def check_dot_zero(num):
	# return len(str(num)) == 2 or str(num)[0].endswith('.0')

# Perimeter
# def p():
	# clear()
	# print('To calculate the perimeter of a square, choose 1')
	# print('To calculate the perimeter of a rectangle, choose 2')
	# print('To calculate the perimeter of a triangle, choose 3')
	# print('To calculate the perimeter of a right triangle, choose 4')
	# print('To calculate the circumference of a circle, choose 5')

# Area
# def a():
	# clear()
	# print('To calculate the area of a square, choose 1')
	# print('To calculate the area of a rectangle, choose 2')
	# print('To calculate the area of a triangle, choose 3')
	# print('To calculate the area of a parallelogram, choose 4')
	# print('To calculate the area of a trapezoid, choose 5')
	# print('To calculate the area of a circle, choose 6')

# Volume
# def v():
	# clear()
	# print('To calculate the volume of a cube, choose 1')
	# print('To calculate the volume of a right rectangular prism, choose 2')
	# print('To calculate the volume of a regular prism, choose 3')
	# print('To calculate the volume of a pyramid, choose 4')
	# print('To calculate the volume of a cone, choose 5')
	# print('To calculate the volume of a cylinder, choose 6')
	# print('To calculate the volume of a sphere, choose 7')
	# sleep(1.5)

# Menu
def menu():
	clear()
	print('To calculate the perimeter of something, choose 1')
	print('To calculate the area of something, choose 2')
	print('To calulate the volume of something, choose 3')
	sleep(1.5)
	choice = input('Enter your choice and press "Enter": ').lower()
	# if choice == '1':
		# p()
	# elif choice == '2':
		# a()
	# elif choice == '3':
		# v()
	# else:
		# return menu()
# Code
menu()