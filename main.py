from os import name, system
from time import sleep
from sys import exit
import pathlib
# Get the first million digits of pi
pi = float(pathlib.Path('pi.txt').read_text())
# Get title banner
banner = pathlib.Path('banner.txt').read_text()
# Clear the screen
def clear():
	if name == 'nt':
		system('cls')
	else:
		system('clear')
# Check if the number ends in .0
def check_dot_zero(num):
	return str(num).endswith('.0')

# Perimeter
def p():
	try:
		clear()
		print('To calculate the perimeter of a square, choose 1')
		print('To calculate the perimeter of a rectangle, choose 2')
		print('To calculate the perimeter of a triangle, choose 3')
		print('To calculate the circumference of a circle, choose 4')
		print('\nTo return to main menu, choose 9')
		sleep(1.5)
		choice = input('Enter your choice: ')
		if choice == '1':
			p_square()
		elif choice == '2':
			p_rec()
		elif choice == '3':
			p_tri()
		elif choice == '4':
			p_circ()
		elif choice == '9':
			menu()
		else:
			sleep(1)
			print('Invalid choice!')
			sleep(1.5)
			return p()
	except KeyboardInterrupt:
		exit(0)

# Perimeter of a square
def p_square():
	try:
		clear()
		side = float(input('Enter the side length: '))
		result = side * 4
		if check_dot_zero(result) == True:
			print(f'The perimeter of the square is: {int(result)}')
		else:
			print(f'The perimeter of the square is: {round(result, 3)}')
	
	except ValueError:
		sleep(1)
		print('Invalid choice!')
		sleep(1.5)
		return p_square()

	except KeyboardInterrupt:
		exit(0)

# Perimeter of a rectangle
def p_rec():
	try:
		clear()
		length = float(input('Enter the length: '))
		width = float(input('Enter the width: '))
		result = 2 * (length + width)
		if check_dot_zero(result) == True:
			print(f'The perimeter of the rectangle is: {int(result)}')
		else:
			print(f'The perimeter of the rectangle is: {round(result, 3)}')
	
	except ValueError:
		sleep(1)
		print('Invalid choice!')
		sleep(1.5)
		return p_rec()

	except KeyboardInterrupt:
		exit(0)

# Perimeter of a triangle
def p_tri():
	try:
		clear()
		equal = input('Are all of the sides equal? Enter your choice (y/n): ')
		if equal == 'y':
			side_len = float(input('Enter the side length: '))
			result = side_len * 3
			clear()
			if check_dot_zero(result) == True:
				print(f'The perimeter of the triangle is: {int(result)}')
			else:
				print(f'The perimeter of the triangle is: {round(result, 3)}')

		if equal == 'n':
			clear()
			a = float(input('Enter the length of a: '))
			b = float(input('Enter the length of b: '))
			c = float(input('Enter the length of c: '))
			result = a + b + c
			clear()
			if check_dot_zero(result) == True:
				print(f'The perimeter of the triangle is: {int(result)}')
			else:
				print(f'The perimeter of the triangle is: {round(result, 3)}')
	
	except ValueError:
		sleep(1)
		print('Invalid choice!')
		sleep(1.5)
		return p_tri()

	except KeyboardInterrupt:
		exit(0)

# Circumference of a circle
def p_circ():
	try:
		clear()
		r = float(input('Enter the radius: '))
		result = 2 * pi * r
		if check_dot_zero(result) == True:
			print(f'The circumference of the circle is: {int(result)}')
		else:
			print(f'The circumference of the circle is: {round(result, 3)}')

	except ValueError:
		sleep(1)
		print('Invalid choice!')
		sleep(1.5)
		return p_circ()
	
	except KeyboardInterrupt:
		exit(0)

# Area
def a():
	try:
		clear()
		print('To calculate the area of a square, choose 1')
		print('To calculate the area of a rectangle, choose 2')
		print('To calculate the area of a triangle, choose 3')
		print('To calculate the area of a parallelogram, choose 4')
		print('To calculate the area of a trapezoid, choose 5')
		print('To calculate the area of a circle, choose 6')
		print('\nTo return to main menu, choose 9')
		sleep(1.5)
		choice = input('Enter your choice: ')
		if choice == '1':
			a_square()
		elif choice == '2':
			a_rec()
		elif choice == '3':
			a_tri()
		elif choice == '4':
			a_parallel()
		elif choice == '5':
			a_trap()
		elif choice == '6':
			a_circ()
		elif choice == '9':
			menu()
		else:
			sleep(1)
			print('Invalid choice!')
			sleep(1.5)
			return a()
	except KeyboardInterrupt:
		exit(0)

# Area of a square
def a_square():
	try:
		clear()
		side = float(input('Enter the side length: '))
		result = side ** 2
		if check_dot_zero(result) == True:
			print(f'The area of the square is: {int(result)}')
		else:
			print(f'The area of the square is: {round(result), 3}')

	except ValueError:
		sleep(1)
		print('Invalid choice!')
		sleep(1.5)
		return a_square()

	except KeyboardInterrupt:
		exit(0)

# Area of a rectangle
def a_rec():
	try:
		clear()
		length = float(input('Enter the length: '))
		width = float(input('Enter the width: '))
		result = length * width
		if check_dot_zero(result) == True:
			print(f'The area of the rectangle is: {int(result)}')
		else:
			print(f'The area of the rectangle is: {round(result, 3)}')
	
	except ValueError:
		sleep(1)
		print('Invalid choice!')
		sleep(1.5)
		return a_rec()

	except KeyboardInterrupt:
		exit(0)

# Area of a triangle
def a_tri():
	try:
		clear()
		base = float(input('Enter the base: '))
		height = float(input('Enter the height: '))
		result = (base * height) / 2
		if check_dot_zero(result) == True:
			print(f'The area of the triangle is: {int(result)}')
		else:
			print(f'The area of the triangle is: {round(result, 3)}')
	
	except ValueError:
		sleep(1)
		print('Invalid choice!')
		sleep(1.5)
		return a_tri()
	
	except KeyboardInterrupt:
		exit(0)

# Area of a parallelogram
def a_parallel():
	try:
		clear()
		base = float(input('Enter the base: '))
		height = float(input('Enter the height: '))
		result = base * height
		if check_dot_zero(result) == True:
			print(f'The area of the parallelogram is: {int(result)}')
		else:
			print(f'The area of the parallelogram is: {round(result, 3)}')
	
	except ValueError:
		sleep(1)
		print('Invalid choice!')
		sleep(1.5)
		return a_parallel()
	
	except KeyboardInterrupt:
		exit(0)

# Area of a trapezoid
def a_trap():
	try:
		clear()
		top = float(input('Enter the length of a: '))
		bottom = float(input('Enter the length of b: '))
		height = float(input('Enter the height: '))
		result = ((top + bottom) / 2) * height
		if check_dot_zero(result) == True:
			print(f'The area of the trapezoid is: {int(result)}')
		else:
			print(f'The area of the trapezoid is: {round(result, 3)}')
	
	except ValueError:
		sleep(1)
		print('Invalid choice!')
		sleep(1.5)
		return a_trap()
	
	except KeyboardInterrupt:
		exit(0)

# Area of a circle
def a_circ():
	try:
		r = float(input('Enter the radius: '))
		result = pi * r ** 2
		if check_dot_zero(result) == True:
			print(f'The area of the circle is: {int(result)}')
		else:
			print(f'The area of the circle is: {round(result, 3)}')
	
	except ValueError:
		sleep(1)
		print('Invalid choice!')
		sleep(1.5)
		return a_trap()
	
	except KeyboardInterrupt:
		exit(0)

# Volume
def v():
	try:
		clear()
		print('To calculate the volume of a cube, choose 1')
		print('To calculate the volume of a prism, choose 2')
		print('To calculate the volume of a square pyramid, choose 3')
		print('To calculate the volume of a cone, choose 4')
		print('To calculate the volume of a cylinder, choose 5')
		print('To calculate the volume of a sphere, choose 6')
		print('\nTo return to main menu, choose 9')
		sleep(1.5)
		choice = input('Enter your choice: ')
		if choice == '1':
			v_cube()
		elif choice == '2':
			v_prism()
		elif choice == '3':
			v_pyramid()
		elif choice == '4':
			v_cone()
		elif choice == '5':
			v_cylinder()
		elif choice == '6':
			v_sphere()
		elif choice == '9':
			menu()
		else:
			sleep(1)
			print('Invalid choice!')
			sleep(1.5)
			return v()
	except KeyboardInterrupt:
		exit(0)

# Volume of a cube
def v_cube():
	try:
		clear()
		side = float(input('Enter the length of one of the sides: '))
		result = side ** 3
		if check_dot_zero(result) == True:
			print(f'The volume of the cube is: {int(result)}')
		else:
			print(f'The volume of the cube is: {round(result, 3)}')
	
	except ValueError:
		sleep(1)
		print('Invalid choice!')
		sleep(1.5)
		return v_cube()
	
	except KeyboardInterrupt:
		exit(0)

# Volume of a prism
def v_prism():
	try:
		clear()
		print('To calculate the volume of a rectangular prism, choose 1')
		print('To calculate the volume of a triangular prism, choose 2')
		print('\nTo return to volume menu, choose 9')
		sleep(1.5)
		choice = input('Enter your choice: ')
		if choice == '1':
			try:
				clear()
				length = float(input('Enter the length: '))
				width = float(input('Enter the width: '))
				height = float(input('Enter the height: '))
				result = length * width * height
				if check_dot_zero(result) == True:
					print(f'The volume of the rectangular prism is: {int(result)}')
				else:
					print(f'The volume of the rectangular prism is: {round(result, 3)}')
			
			except KeyboardInterrupt:
				exit(0)

			except ValueError:
				sleep(1)
				print('Invalid choice!')
				sleep(1.5)
				return v_prism()
		elif choice == '2':
			try:
				clear()
				base = float(input('Enter the length of the base: '))
				height = float(input('Enter the height: '))
				length = float(input('Enter the length: '))
				result = (base * height * length) / 2
				if check_dot_zero(result) == True:
					print(f'The volume of the triangular prism is: {int(result)}')
				else:
					print(f'The volume of the triangular prism is: {round(result, 3)}')
			
			except KeyboardInterrupt:
				exit(0)
			
			except ValueError:
				sleep(1)
				print('Invalid choice!')
				sleep(1.5)
				return v_prism()
		elif choice == '9':
			v()
		else:
			sleep(1)
			print('Invalid choice!')
			sleep(1.5)
			return v_prism()
	except KeyboardInterrupt:
		exit(0)

# Volume of a pyramid
def v_pyramid():
	try:
		length = float(input('Enter the length: '))
		width = float(input('Enter the width: '))
		height = float(input('Enter the height: '))
		result = (length * width * height) / 3
		if check_dot_zero(result) == True:
			print(f'The volume of the pyramid is: {int(result)}')
		else:
			print(f'The volume of the pyramid is: {round(result, 3)}')
	
	except ValueError:
		sleep(1)
		print('Invalid choice!')
		sleep(1.5)
		return v_pyramid()
	
	except KeyboardInterrupt:
		exit(0)

# Volume of a cone
def v_cone():
	try:
		clear()
		radius = float(input('Enter the radius: '))
		height = float(input('Enter the height: '))
		result = (pi * radius ** 2) * (height / 3)
		if check_dot_zero(result) == True:
			print(f'The volume of the cone is: {int(result)}')
		else:
			print(f'The volume of the cone is: {round(result, 3)}')
	
	except ValueError:
		sleep(1)
		print('Invalid choice!')
		sleep(1.5)
		return v_cone()
	
	except KeyboardInterrupt:
		exit(0)

# Volume of a cylinder
def v_cylinder():
	try:
		clear()
		radius = float(input('Enter the radius: '))
		height = float(input('Enter the height: '))
		result = pi * radius ** 2 * height
		if check_dot_zero(result) == True:
			print(f'The volume of the cylinder is: {int(result)}')
		else:
			print(f'The volume of the cylinder is: {round(result, 3)}')
	
	except ValueError:
		sleep(1)
		print('Invalid choice!')
		sleep(1.5)
		return v_cylinder()
	
	except KeyboardInterrupt:
		exit(0)

# Volume of a sphere
def v_sphere():
	try:
		clear()
		radius = float(input('Enter the radius: '))
		result = (4 / 3) * pi * radius ** 3
		if check_dot_zero(result) == True:
			print(f'The volume of the sphere is: {int(result)}')
		else:
			print(f'The volume of the sphere is: {round(result, 3)}')
	
	except ValueError:
		sleep(1)
		print('Invalid choice!')
		sleep(1.5)
		return v_sphere()
	
	except KeyboardInterrupt:
		exit(0)

# Menu
def menu():
	try:
		clear()
		print(banner + '\n')
		sleep(1)
		print('To calculate the perimeter of something, choose 1')
		print('To calculate the area of something, choose 2')
		print('To calulate the volume of something, choose 3')
		print('\nTo exit, choose 9')
		sleep(1.5)
		choice = input('Enter your choice and press "Enter": ')
		if choice == '1':
			p()
		elif choice == '2':
			a()
		elif choice == '3':
			v()
		elif choice == '9':
			clear()
			print('Goodbye!')
			sleep(2)
			exit(0)
		else:
			sleep(1)
			print('Invalid choice!')
			sleep(1.5)
			return menu()
	except KeyboardInterrupt:
		exit(0)

# Run again
def run_again():
	answer = input('\nWould you like to run the program again?\nEnter your choice (y/n): ').lower()
	if answer == 'y':
		menu()
	elif answer == 'n':
		clear()
		print('Goodbye!')
		sleep(2)
		exit(0)
	else:
		sleep(1)
		print('Invalid choice!')
		sleep(1.5)
		return run_again()

# Run the program
menu()
run_again()
