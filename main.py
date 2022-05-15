from os import name, system
from time import sleep
import mpmath
import math
# Get the first million digits of pi from pi.txt file
with open(r'pi.txt') as f:
	pi = float(f.read())
# Clear the screen
def clear():
	if name == 'nt':
		system('cls')
	else:
		system('clear')
# Check if the number ends in .0 or not
def check_dot_zero(num):
	return len(str(num)) == 2 or str(num)[0].endswith('.0')
# Code
clear()
print('To calculate the perimeter of something, enter "p".')
print('To calculate the area of something, enter "a".')
print('To calculate the volume of something, enter "v".')
sleep(1.5)
choice = input('Enter your choice and press "Enter": ').lower()

if choice == 'p':
	clear()
	print('To calculate the perimeter of a square, enter "p square".')
	print('To calculate the perimeter of a rectangle, enter "p rectangle".')
	print('To calculate the perimeter of a triangle, enter "p triangle".')
	print('To calculate the perimeter of a right triangle, enter "p right tri".')
	print('To calculate the circumference of a circle, enter "c circle".')
	sleep(1.5)
	choice1 = input('Enter your choice and press "Enter": ').lower()
	if choice1 == 'p square':
		clear()
		p_square_side = float(input('Enter the length of a side: '))
		clear()
		p_square_result = p_square_side**4
		if check_dot_zero(p_square_result) == True:
			print(f'The perimeter of the square is: {int(p_square_result)}')
		else:
			print(f'The perimeter of the square is: {p_square_result}')

	elif choice1 == 'p rectangle':
		clear()
		p_rectangle_side = float(input('Enter the length of a side: '))
		clear()
		p_rectangle_side1 = float(input('Enter the length of the other side: '))
		clear()
		p_rectangle_result = (p_rectangle_side*2)+(p_rectangle_side1*2)
		if check_dot_zero(p_rectangle_result) == True:
			print(f'The perimeter of the rectangle is: {int(p_rectangle_result)}')
		else:
			print(f'The perimeter of the rectangle is: {p_rectangle_result}')

	elif choice1 == 'p triangle':
		clear()
		p_triangle_side = float(input('Enter the length of a side: '))
		clear()
		p_triangle_side1 = float(input('Enter the length of another side: '))
		clear()
		p_triangle_side2 = float(input('Enter the length of the remaining side: '))
		clear()
		p_triangle_result = p_triangle_side+p_triangle_side1+p_triangle_side2
		if check_dot_zero(p_triangle_result) == True:
			print(f'The perimeter of the triangle is: {int(p_triangle_result)}')
		else:
			print(f'The perimeter of the triangle is: {p_triangle_result}')

	elif choice1 == 'p right tri':
		clear()
		p_right_side = float(input('Enter the length of one of the legs: '))
		clear()
		p_right_side1 = float(input('Enter the length of the other leg: '))
		clear()
		p_right_result = (p_right_side+p_right_side1)+(math.sqrt((p_right_side**2)+(p_right_side1**2)))
		if check_dot_zero(p_right_result) == True:
			print(f'The perimeter of the right triangle is: {int(p_right_result)}')
		else:
			print(f'The perimeter of the right triangle is: {p_right_result}')

	elif choice1 == 'c circle':
		clear()
		p_circle_r = float(input('Enter the radius of the circle: '))
		clear()
		p_circle_result = (pi*p_circle_r)*2
		if p_circle_result == True:
			print(f'The circumference of the circle is: {int(p_circle_result)}')
		else:
			print(f'The circumference of the circle is: {p_circle_result}')

	else:
		while choice1 != 'p square' and choice1 != 'p rectangle' and choice1 != 'p triangle' and choice1 != 'p right tri' and choice1 != 'c circle':
			clear()
			print("You didn't enter any of the options!")
			sleep(2)
			clear()
			print('To calculate the perimeter of a square, enter "p square".')
			print('To calculate the perimeter of a rectangle, enter "p rectangle".')
			print('To calculate the perimeter of a triangle, enter "p triangle".')
			print('To calculate the perimeter of a right triangle, enter "p right tri".')
			print('To calculate the circumference of a circle, enter "c circle".')
			sleep(1.5)
			choice1 = input('Enter your choice and press "Enter": ').lower()
			if choice1 == 'p square':
				clear()
				p_square_side = float(input('Enter the length of a side: '))
				clear()
				p_square_result = p_square_side**4
				if check_dot_zero(p_square_result) == True:
					print(f'The perimeter of the square is: {int(p_square_result)}')
				else:
					print(f'The perimeter of the square is: {p_square_result}')
				break

			elif choice1 == 'p rectangle':
				clear()
				p_rectangle_side = float(input('Enter the length of a side: '))
				clear()
				p_rectangle_side1 = float(input('Enter the length of the other side: '))
				clear()
				p_rectangle_result = (p_rectangle_side*2)+(p_rectangle_side1*2)
				if check_dot_zero(p_rectangle_result) == True:
					print(f'The perimeter of the rectangle is: {int(p_rectangle_result)}')
				else:
					print(f'The perimeter of the rectangle is: {p_rectangle_result}')
				break

			elif choice1 == 'p triangle':
				clear()
				p_triangle_side = float(input('Enter the length of a side: '))
				clear()
				p_triangle_side1 = float(input('Enter the length of another side: '))
				clear()
				p_triangle_side2 = float(input('Enter the length of the remaining side: '))
				clear()
				p_triangle_result = p_triangle_side+p_triangle_side1+p_triangle_side2
				if check_dot_zero(p_triangle_result) == True:
					print(f'The perimeter of the triangle is: {int(p_triangle_result)}')
				else:
					print(f'The perimeter of the triangle is: {p_triangle_result}')
				break

			elif choice1 == 'p right tri':
				clear()
				p_right_side = float(input('Enter the length of one of the legs: '))
				clear()
				p_right_side1 = float(input('Enter the length of the other leg: '))
				clear()
				p_right_result = (p_right_side+p_right_side1)+(math.sqrt((p_right_side**2)+(p_right_side1**2)))
				if check_dot_zero(p_right_result) == True:
					print(f'The perimeter of the right triangle is: {int(p_right_result)}')
				else:
					print(f'The perimeter of the right triangle is: {p_right_result}')
				break

			elif choice1 == 'c circle':
				clear()
				p_circle_r = float(input('Enter the radius of the circle: '))
				clear()
				p_circle_result = (pi*p_circle_r)*2
				if p_circle_result == True:
					print(f'The circumference of the circle is: {int(p_circle_result)}')
				else:
					print(f'The circumference of the circle is: {p_circle_result}')
				break

elif choice == 'a':
	clear()
	print('To calculate the area of a square, enter "a square".')
	print('To calculate the area of a rectangle, enter "a rectangle".')
	print('To calculate the area of a triangle, enter "a triangle".')
	print('To calculate the area of a parallelogram, enter "a parallel".')
	print('To calculate the area of a trapezoid, enter "a trapezoid".')
	print('To calculate the area of a circle, enter "a circle".')
	sleep(1.5)
	choice2 = input('Enter your choice and press "Enter": ').lower()
	if choice2 == 'a square':
		clear()
		a_square_side = float(input('Enter the length of a side: '))
		clear()
		a_square_result = a_square_side**2
		if check_dot_zero(a_square_result) == True:
			print(f'The area of the square is: {int(a_square_result)}')
		else:
			print(f'The area of the square is: {a_square_result}')

	elif choice2 == 'a rectangle':
		clear()
		a_rectangle_side = float(input('Enter the length of a side: '))
		clear()
		a_rectangle_side1 = float(input('Enter the length of the other side: '))
		clear()
		a_rectangle_result = a_rectangle_side*a_rectangle_side1
		if check_dot_zero(a_rectangle_result) == True:
			print(f'The area of the rectangle is: {int(a_rectangle_result)}')
		else:
			print(f'The area of the rectangle is: {a_rectangle_result}')

	elif choice2 == 'a triangle':
		clear()
		a_triangle_base = float(input('Enter the length of the base: '))
		clear()
		a_triangle_height = float(input('Enter the length of the height: '))
		clear()
		a_triangle_result = (1/2*(a_triangle_base*a_triangle_height))
		if check_dot_zero(a_triangle_result) == True:
			print(f'The area of the triangle is: {int(a_triangle_result)}')
		else:
			print(f'The area of the triangle is: {a_triangle_result}')

	elif choice2 == 'a parallel':
		clear()
		a_parallel_base = float(input('Enter the length of the base: '))
		clear()
		a_parallel_height = float(input('Enter the length of the height: '))
		clear()
		a_parallel_result = a_parallel_base*a_parallel_height
		if check_dot_zero(a_parallel_result) == True:
			print(f'The area of the parallelogram is: {int(a_parallel_result)}')
		else:
			print(f'The area of the parallelogram is: {a_parallel_result}')

	elif choice2 == 'a trapezoid':
		clear()
		a_trapezoid_b1 = float(input('Enter the length of a base: '))
		clear()
		a_trapezoid_b2 = float(input('Enter the length of the other base: '))
		clear()
		a_trapezoid_h = float(input('Enter the length of the height: '))
		clear()
		a_trapezoid_result = (((a_trapezoid_b1+a_trapezoid_b2)/2)*a_trapezoid_h)
		if check_dot_zero(a_trapezoid_result) == True:
			print(f'The area of the trapezoid is: {int(a_trapezoid_result)}')
		else:
			print(f'The area of the trapezoid is: {a_trapezoid_result}')

	elif choice2 == 'a circle':
		clear()
		a_circle_r = float(input('Enter the radius: '))
		clear()
		a_circle_result = (pi*(a_circle_r**2))
		if check_dot_zero(a_circle_result) == True:
			print(f'The area of the circle is: {int(a_circle_result)}')
		else:
			print(f'The area of the circle is: {a_circle_result}')

	else:
		while choice2 != 'a square' and choice2 != 'a rectangle' and choice2 != 'a triangle' and choice2 != 'a parallel' and choice2 != 'a trapezoid' and choice2 != 'a circle':
			clear()
			print("You didn't enter any of the options!")
			sleep(2)
			clear()
			print('To calculate the area of a square, enter "a square".')
			print('To calculate the area of a rectangle, enter "a rectangle".')
			print('To calculate the area of a triangle, enter "a triangle".')
			print('To calculate the area of a parallelogram, enter "a parallel".')
			print('To calculate the area of a trapezoid, enter "a trapezoid".')
			print('To calculate the area of a circle, enter "a circle".')
			sleep(1.5)
			choice2 = input('Enter your choice and press "Enter": ').lower()
			if choice2 == 'a square':
				clear()
				a_square_side = float(input('Enter the length of a side: '))
				clear()
				a_square_result = a_square_side**2
				if check_dot_zero(a_square_result) == True:
					print(f'The area of the square is: {int(a_square_result)}')
				else:
					print(f'The area of the square is: {a_square_result}')
				break

			elif choice2 == 'a rectangle':
				clear()
				a_rectangle_side = float(input('Enter the length of a side: '))
				clear()
				a_rectangle_side1 = float(input('Enter the length of the other side: '))
				clear()
				a_rectangle_result = a_rectangle_side*a_rectangle_side1
				if check_dot_zero(a_rectangle_result) == True:
					print(f'The area of the rectangle is: {int(a_rectangle_result)}')
				else:
					print(f'The area of the rectangle is: {a_rectangle_result}')
				break

			elif choice2 == 'a triangle':
				clear()
				a_triangle_base = float(input('Enter the length of the base: '))
				clear()
				a_triangle_height = float(input('Enter the length of the height: '))
				clear()
				a_triangle_result = (1/2*(a_triangle_base*a_triangle_height))
				if check_dot_zero(a_triangle_result) == True:
					print(f'The area of the triangle is: {int(a_triangle_result)}')
				else:
					print(f'The area of the triangle is: {a_triangle_result}')
				break

			elif choice2 == 'a parallel':
				clear()
				a_parallel_base = float(input('Enter the length of the base: '))
				clear()
				a_parallel_height = float(input('Enter the length of the height: '))
				clear()
				a_parallel_result = a_parallel_base*a_parallel_height
				if check_dot_zero(a_parallel_result) == True:
					print(f'The area of the parallelogram is: {int(a_parallel_result)}')
				else:
					print(f'The area of the parallelogram is: {a_parallel_result}')
				break

			elif choice2 == 'a trapezoid':
				clear()
				a_trapezoid_b1 = float(input('Enter the length of a base: '))
				clear()
				a_trapezoid_b2 = float(input('Enter the length of the other base: '))
				clear()
				a_trapezoid_h = float(input('Enter the length of the height: '))
				clear()
				a_trapezoid_result = (((a_trapezoid_b1+a_trapezoid_b2)/2)*a_trapezoid_h)
				if check_dot_zero(a_trapezoid_result) == True:
					print(f'The area of the trapezoid is: {int(a_trapezoid_result)}')
				else:
					print(f'The area of the trapezoid is: {a_trapezoid_result}')
				break

			elif choice2 == 'a circle':
				clear()
				a_circle_r = float(input('Enter the radius: '))
				clear()
				a_circle_result = (pi*(a_circle_r**2))
				if check_dot_zero(a_circle_result) == True:
					print(f'The area of the circle is: {int(a_circle_result)}')
				else:
					print(f'The area of the circle is: {a_circle_result}')
				break

elif choice == 'v':
	clear()
	print('To calculate the volume of a cube, enter "v cube".')
	print('To calculate the volume of a right rectangular prism, enter "v right r prism".')
	print('To calculate the volume of a regular prism, enter "v prism".')
	print('To calculate the volume of a pyramid, enter "v pyramid".')
	print('To calculate the volume of a cone, enter "v cone".')
	print('To calculate the volume of a cylinder, enter "v cylinder".')
	print('To calculate the volume of a sphere, enter "v sphere".')
	sleep(1.5)
	choice3 = input('Enter your choice and press "Enter": ')
	if choice3 == 'v cube':
		clear()
		v_cube_side = float(input('Enter the length of the side: '))
		clear()
		v_cube_result = v_cube_side**3
		if check_dot_zero(v_cube_result) == True:
			print(f'The volume of the cube is: {int(v_cube_result)}')
		else:
			print(f'The volume of the cube is: {v_cube_result}')

	elif choice3 == 'v right r prism':
		clear()
		v_right_r_prism_l = float(input('Enter the length: '))
		clear()
		v_right_r_prism_w = float(input('Enter the width: '))
		clear()
		v_right_r_prism_h = float(input('Enter the height: '))
		clear()
		v_right_r_prism_result = v_right_r_prism_l*v_right_r_prism_w*v_right_r_prism_h
		if check_dot_zero(v_right_r_prism_result) == True:
			print(f'The volume of the right rectangular prism is: {int(v_right_r_prism_result)}')
		else:
			print(f'The volume of the right rectangular prism is: {v_right_r_prism_result}')

	elif choice3 == 'v prism':
		clear()
		print('If the prism is a square prism, enter "s prism".')
		print('If the prism is a rectangular prism, enter "r prism".')
		print('If the prism is a triangular prism, enter "t prism".')
		print('If the prism is a pentagonal prism (5 sides), enter "p prism".')
		print('If the prism is a hexagonal prism (6 sides), enter "h prism".')
		print('If the prism is a heptagonal prism (7 sides), enter "hept prism".')
		print('If the prism is an octagonal prism (8 sides), enter "o prism".')
		print('If the prism is a trapezoidal prism, enter "trap prism".')
		sleep(1.5)
		choice4 = input('Enter your choice and press "Enter": ')
		if choice4 == 's prism':
			clear()
			v_s_prism_s = float(input('Enter the length of a side of the base: '))
			clear()
			v_s_prism_h = float(input('Enter the height of the prism: '))
			clear()
			v_s_prism_result = (v_s_prism_s**2)*v_s_prism_h
			if check_dot_zero(v_s_prism_result) == True:
				print(f'The volume of the square prism is: {int(v_s_prism_result)}')
			else:
				print(f'The volume of the square prism is: {v_s_prism_result}')

		elif choice4 == 'r prism':
			clear()
			v_r_prism_l = float(input('Enter the length: '))
			clear()
			v_r_prism_w = float(input('Enter the width: '))
			clear()
			v_r_prism_h = float(input('Enter the height: '))
			clear()
			v_r_prism_result = v_r_prism_l*v_r_prism_w*v_r_prism_h
			if check_dot_zero(v_r_prism_result) == True:
				print(f'The volume of the rectangular prism is: {int(v_r_prism_result)}')
			else:
				print(f'The volume of the rectangular prism is: {v_r_prism_result}')

		elif choice4 == 't prism':
			clear()
			v_t_prism_a = float(input('Enter one of the sides of the base: '))
			clear()
			v_t_prism_b = float(input('Enter one of the other sides of the base: '))
			clear()
			v_t_prism_c = float(input('Enter the remaining side of the base: '))
			clear()
			v_t_prism_h = float(input('Enter the height of the prism: '))
			clear()
			v_t_prism_result = ((1/4)*v_t_prism_h)*math.sqrt(-v_t_prism_a**4+(2*((v_t_prism_a*v_t_prism_b)**2)+2*((v_t_prism_a*v_t_prism_c)**2)-v_t_prism_b**4+2*((v_t_prism_b*v_t_prism_c)**2)-v_t_prism_c**4))
			if check_dot_zero(v_t_prism_result) == True:
				print(f'The volume of the triangular prism is: {int(v_t_prism_result)}')
			else:
				print(f'The volume of the triangular prism is: {v_t_prism_result}')

		elif choice4 == 'p prism':
			clear()
			v_p_prism_a = float(input('Enter the length of one of the sides of the base: '))
			clear()
			v_p_prism_h = float(input('Enter the height of the prism: '))
			clear()
			v_p_prism_result = ((1/4)*math.sqrt((5*(5+(2*(math.sqrt(5)))))))*((v_p_prism_a**2)*v_p_prism_h)
			if check_dot_zero(v_p_prism_result) == True:
				print(f'The volume of the pentagonal prism is: {int(v_p_prism_result)}')
			else:
				print(f'The volume of the pentagonal prism is: {v_p_prism_result}')

		elif choice4 == 'h prism':
			clear()
			v_h_prism_a = float(input('Enter the length of one of the sides of the base: '))
			clear()
			v_h_prism_h = float(input('Enter the height of the prism: '))
			clear()
			v_h_prism_result = (((3*math.sqrt(3))/2)*(v_h_prism_a**2))*v_h_prism_h
			if check_dot_zero(v_h_prism_result) == True:
				print(f'The volume of the hexagonal prism is: {int(v_h_prism_result)}')
			else:
				print(f'The volume of the hexagonal prism is: {v_h_prism_result}')

		elif choice4 == 'hept prism':
			clear()
			v_hept_prism_a = float(input('Enter the length of one of the sides of the base: '))
			clear()
			v_hept_prism_h = float(input('Enter the height of the prism: '))
			clear()
			v_hept_prism_result = ((7/4)*v_hept_prism_a**2)*mpmath.cot((math.radians(180)/7))*v_hept_prism_h
			if check_dot_zero(v_hept_prism_result) == True:
				print(f'The volume of the heptagonal prism is: {int(v_hept_prism_result)}')
			else:
				print(f'The volume of the heptagonal prism is: {v_hept_prism_result}')

		elif choice4 == 'o prism':
			clear()
			v_o_prism_a = float(input('Enter the length of one of the sides of the base: '))
			clear()
			v_o_prism_h = float(input('Enter the height of the prism: '))
			clear()
			v_o_prism_result = ((2*(1+math.sqrt(2)))*(v_o_prism_a**2))*v_o_prism_h
			if check_dot_zero(v_o_prism_result) == True:
				print(f'The volume of the octagonal prism is: {int(v_o_prism_result)}')
			else:
				print(f'The volume of the octagonal prism is: {v_o_prism_result}')

		elif choice4 == 'trap prism':
			clear()
			print('If the height is known, enter "trap h prism".')
			print('If the height isn\'t known, but the slant height is known, enter "trap s prism".')
			sleep(1.5)
			choice6 = input('Enter your choice and press "Enter": ')
			if choice6 == 'trap h prism':
				clear()
				v_trap_prism_l = float(input('Enter the height of the prism: '))
				clear()
				v_trap_prism_h = float(input('Enter the height of the base: '))
				clear()
				v_trap_prism_b1 = float(input('Enter the top width of the base: '))
				clear()
				v_trap_prism_b2 = float(input('Enter the bottom width of the base: '))
				clear()
				v_trap_prism_result = v_trap_prism_l*v_trap_prism_h*((v_trap_prism_b1+v_trap_prism_b2)/2)
				if check_dot_zero(v_trap_prism_result) == True:
					print(f'The volume of the trapezoidal prism is: {int(v_trap_prism_result)}')
				else:
					print(f'The volume of the trapezoidal prism is: {v_trap_prism_result}')

			elif choice6 == 'trap s prism':
				clear()
				v_trap_prism_s_l = float(input('Enter the height of the prism: '))
				clear()
				v_trap_prism_s_h = float(input('Enter the slant height: '))
				clear()
				v_trap_prism_s_b1 = float(input('Enter the top width of the base: '))
				clear()
				v_trap_prism_s_b2 = float(input('Enter the bottom width of the base: '))
				clear()
				v_trap_prism_s_result = v_trap_prism_s_l*(v_trap_prism_s_b1+v_trap_prism_s_b2)*math.sqrt((4*(v_trap_prism_s_h**2))+(2*(v_trap_prism_s_b1*v_trap_prism_s_b2))-math.sqrt(v_trap_prism_s_b1)-math.sqrt(v_trap_prism_s_b2))/4
				if check_dot_zero(v_trap_prism_s_result) == True:
					print(f'The volume of the trapezoidal prism is: {int(v_trap_prism_s_result)}')
				else:
					print(f'The volume of the trapezoidal prism is: {v_trap_prism_s_result}')

			else:
				while choice6 != 'trap h prism' and choice6 != 'trap s prism':
					clear()
					print("You didn't enter any of the options!")
					sleep(2)
					clear()
					print('If the height is known, enter "trap h prism".')
					print('If the height isn\'t known, but the slant height is known, enter "trap s prism".')
					sleep(1.5)
					choice6 = input('Enter your choice and press "Enter": ')
					if choice6 == 'trap h prism':
						clear()
						v_trap_prism_l = float(input('Enter the height of the prism: '))
						clear()
						v_trap_prism_h = float(input('Enter the height of the base: '))
						clear()
						v_trap_prism_b1 = float(input('Enter the top width of the base: '))
						clear()
						v_trap_prism_b2 = float(input('Enter the bottom width of the base: '))
						clear()
						v_trap_prism_result = v_trap_prism_l*v_trap_prism_h*((v_trap_prism_b1+v_trap_prism_b2)/2)
						if check_dot_zero(v_trap_prism_result) == True:
							print(f'The volume of the trapezoidal prism is: {int(v_trap_prism_result)}')
						else:
							print(f'The volume of the trapezoidal prism is: {v_trap_prism_result}')

					elif choice6 == 'trap s prism':
						clear()
						v_trap_prism_s_l = float(input('Enter the height of the prism: '))
						clear()
						v_trap_prism_s_h = float(input('Enter the slant height: '))
						clear()
						v_trap_prism_s_b1 = float(input('Enter the top width of the base: '))
						clear()
						v_trap_prism_s_b2 = float(input('Enter the bottom width of the base: '))
						clear()
						v_trap_prism_s_result = v_trap_prism_s_l*(v_trap_prism_s_b1+v_trap_prism_s_b2)*math.sqrt((4*(v_trap_prism_s_h**2))+(2*(v_trap_prism_s_b1*v_trap_prism_s_b2))-math.sqrt(v_trap_prism_s_b1)-math.sqrt(v_trap_prism_s_b2))/4
						if check_dot_zero(v_trap_prism_s_result) == True:
							print(f'The volume of the trapezoidal prism is: {int(v_trap_prism_s_result)}')
						else:
							print(f'The volume of the trapezoidal prism is: {v_trap_prism_s_result}')

		else:
			while choice4 != 's prism' and choice4 != 'r prism' and choice4 != 't prism' and choice4 != 'p prism' and choice4 != 'h prism' and choice4 != 'hept prism' and choice4 != 'o prism' and choice4 != 'trap prism':
				clear()
				print("You didn't enter any of the options!")
				sleep(2)
				clear()
				print('If the prism is a square prism, enter "s prism".')
				print('If the prism is a rectangular prism, enter "r prism".')
				print('If the prism is a triangular prism, enter "t prism".')
				print('If the prism is a pentagonal prism (5 sides), enter "p prism".')
				print('If the prism is a hexagonal prism (6 sides), enter "h prism".')
				print('If the prism is a heptagonal prism (7 sides), enter "hept prism".')
				print('If the prism is an octagonal prism (8 sides), enter "o prism".')
				print('If the prism is a trapezoidal prism, enter "trap prism".')
				sleep(1.5)
				choice4 = input('Enter your choice and press "Enter": ')
				if choice4 == 's prism':
					clear()
					v_s_prism_s = float(input('Enter the length of a side of the base: '))
					clear()
					v_s_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_s_prism_result = (v_s_prism_s**2)*v_s_prism_h
					if check_dot_zero(v_s_prism_result) == True:
						print(f'The volume of the square prism is: {int(v_s_prism_result)}')
					else:
						print(f'The volume of the square prism is: {v_s_prism_result}')
					break

				elif choice4 == 'r prism':
					clear()
					v_r_prism_l = float(input('Enter the length: '))
					clear()
					v_r_prism_w = float(input('Enter the width: '))
					clear()
					v_r_prism_h = float(input('Enter the height: '))
					clear()
					v_r_prism_result = v_r_prism_l*v_r_prism_w*v_r_prism_h
					if check_dot_zero(v_r_prism_result) == True:
						print(f'The volume of the rectangular prism is: {int(v_r_prism_result)}')
					else:
						print(f'The volume of the rectangular prism is: {v_r_prism_result}')
					break

				elif choice4 == 't prism':
					clear()
					v_t_prism_a = float(input('Enter one of the sides of the base: '))
					clear()
					v_t_prism_b = float(input('Enter one of the other sides of the base: '))
					clear()
					v_t_prism_c = float(input('Enter the remaining side of the base: '))
					clear()
					v_t_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_t_prism_result = ((1/4)*v_t_prism_h)*math.sqrt(-v_t_prism_a**4+(2*((v_t_prism_a*v_t_prism_b)**2)+2*((v_t_prism_a*v_t_prism_c)**2)-v_t_prism_b**4+2*((v_t_prism_b*v_t_prism_c)**2)-v_t_prism_c**4))
					if check_dot_zero(v_t_prism_result) == True:
						print(f'The volume of the triangular prism is: {int(v_t_prism_result)}')
					else:
						print(f'The volume of the triangular prism is: {v_t_prism_result}')
					break

				elif choice4 == 'p prism':
					clear()
					v_p_prism_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_p_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_p_prism_result = ((1/4)*math.sqrt((5*(5+(2*(math.sqrt(5)))))))*((v_p_prism_a**2)*v_p_prism_h)
					if check_dot_zero(v_p_prism_result) == True:
						print(f'The volume of the pentagonal prism is: {int(v_p_prism_result)}')
					else:
						print(f'The volume of the pentagonal prism is: {v_p_prism_result}')
					break

				elif choice4 == 'h prism':
					clear()
					v_h_prism_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_h_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_h_prism_result = (((3*math.sqrt(3))/2)*(v_h_prism_a**2))*v_h_prism_h
					if check_dot_zero(v_h_prism_result) == True:
						print(f'The volume of the hexagonal prism is: {int(v_h_prism_result)}')
					else:
						print(f'The volume of the hexagonal prism is: {v_h_prism_result}')
					break

				elif choice4 == 'hept prism':
					clear()
					v_hept_prism_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_hept_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_hept_prism_result = ((7/4)*v_hept_prism_a**2)*mpmath.cot((math.radians(180)/7))*v_hept_prism_h
					if check_dot_zero(v_hept_prism_result) == True:
						print(f'The volume of the heptagonal prism is: {int(v_hept_prism_result)}')
					else:
						print(f'The volume of the heptagonal prism is: {v_hept_prism_result}')
					break

				elif choice4 == 'o prism':
					clear()
					v_o_prism_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_o_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_o_prism_result = ((2*(1+math.sqrt(2)))*(v_o_prism_a**2))*v_o_prism_h
					if check_dot_zero(v_o_prism_result) == True:
						print(f'The volume of the octagonal prism is: {int(v_o_prism_result)}')
					else:
						print(f'The volume of the octagonal prism is: {v_o_prism_result}')
					break

				elif choice4 == 'trap prism':
					clear()
					print('If the height is known, enter "trap h prism".')
					print('If the height isn\'t known, but the slant height is known, enter "trap s prism".')
					sleep(1.5)
					choice6 = input('Enter your choice and press "Enter": ')
					if choice6 == 'trap h prism':
						clear()
						v_trap_prism_l = float(input('Enter the height of the prism: '))
						clear()
						v_trap_prism_h = float(input('Enter the height of the base: '))
						clear()
						v_trap_prism_b1 = float(input('Enter the top width of the base: '))
						clear()
						v_trap_prism_b2 = float(input('Enter the bottom width of the base: '))
						clear()
						v_trap_prism_result = v_trap_prism_l*v_trap_prism_h*((v_trap_prism_b1+v_trap_prism_b2)/2)
						if check_dot_zero(v_trap_prism_result) == True:
							print(f'The volume of the trapezoidal prism is: {int(v_trap_prism_result)}')
						else:
							print(f'The volume of the trapezoidal prism is: {v_trap_prism_result}')

					elif choice6 == 'trap s prism':
						clear()
						v_trap_prism_s_l = float(input('Enter the height of the prism: '))
						clear()
						v_trap_prism_s_h = float(input('Enter the slant height: '))
						clear()
						v_trap_prism_s_b1 = float(input('Enter the top width of the base: '))
						clear()
						v_trap_prism_s_b2 = float(input('Enter the bottom width of the base: '))
						clear()
						v_trap_prism_s_result = v_trap_prism_s_l*(v_trap_prism_s_b1+v_trap_prism_s_b2)*math.sqrt((4*(v_trap_prism_s_h**2))+(2*(v_trap_prism_s_b1*v_trap_prism_s_b2))-math.sqrt(v_trap_prism_s_b1)-math.sqrt(v_trap_prism_s_b2))/4
						if check_dot_zero(v_trap_prism_s_result) == True:
							print(f'The volume of the trapezoidal prism is: {int(v_trap_prism_s_result)}')
						else:
							print(f'The volume of the trapezoidal prism is: {v_trap_prism_s_result}')

					else:
						while choice6 != 'trap h prism' and choice6 != 'trap s prism':
							clear()
							print("You didn't enter any of the options!")
							sleep(2)
							clear()
							print('If the height is known, enter "trap h prism".')
							print('If the height isn\'t known, but the slant height is known, enter "trap s prism".')
							sleep(1.5)
							choice6 = input('Enter your choice and press "Enter": ')
							if choice6 == 'trap h prism':
								clear()
								v_trap_prism_l = float(input('Enter the height of the prism: '))
								clear()
								v_trap_prism_h = float(input('Enter the height of the base: '))
								clear()
								v_trap_prism_b1 = float(input('Enter the top width of the base: '))
								clear()
								v_trap_prism_b2 = float(input('Enter the bottom width of the base: '))
								clear()
								v_trap_prism_result = v_trap_prism_l*v_trap_prism_h*((v_trap_prism_b1+v_trap_prism_b2)/2)
								if check_dot_zero(v_trap_prism_result) == True:
									print(f'The volume of the trapezoidal prism is: {int(v_trap_prism_result)}')
								else:
									print(f'The volume of the trapezoidal prism is: {v_trap_prism_result}')

							elif choice6 == 'trap s prism':
								clear()
								v_trap_prism_s_l = float(input('Enter the height of the prism: '))
								clear()
								v_trap_prism_s_h = float(input('Enter the slant height: '))
								clear()
								v_trap_prism_s_b1 = float(input('Enter the top width of the base: '))
								clear()
								v_trap_prism_s_b2 = float(input('Enter the bottom width of the base: '))
								clear()
								v_trap_prism_s_result = v_trap_prism_s_l*(v_trap_prism_s_b1+v_trap_prism_s_b2)*math.sqrt((4*(v_trap_prism_s_h**2))+(2*(v_trap_prism_s_b1*v_trap_prism_s_b2))-math.sqrt(v_trap_prism_s_b1)-math.sqrt(v_trap_prism_s_b2))/4
								if check_dot_zero(v_trap_prism_s_result) == True:
									print(f'The volume of the trapezoidal prism is: {int(v_trap_prism_s_result)}')
								else:
									print(f'The volume of the trapezoidal prism is: {v_trap_prism_s_result}')
					break

	elif choice3 == 'v pyramid':
		clear()
		print('If the pyramid is a tetrahedron (3 sides), enter "v tetra".')
		print('If the pyramid is a square pyramid (4 sides), enter "v square".')
		print('If the pyramid is a pentagonal pyramid (5 sides), enter "v penta".')
		print('If the pyramid is a hexagonal pyramid (6 sides), enter "v hexa".')
		print('If the pyramid is a heptagonal pyramid (7 sides), enter "v hepta".')
		print('If the pyramid is a octagonal pyramid (8 sides), enter "v octa".')
		sleep(1.5)
		choice5 = input('Enter your choice and press "Enter": ')
		if choice5 == 'v tetra':
			clear()
			v_tri_a = float(input('Enter the length of one of the edges of one of the sides: '))
			clear()
			v_tri_result = (v_tri_a**3)/(6*math.sqrt(2))
			if check_dot_zero(v_tri_result) == True:
				print(f'The volume of the triangular pyramid is: {int(v_tri_result)}')
			else:
				print(f'The volume of the triangular pyramid is: {v_tri_result}')

		elif choice5 == 'v square':
			clear()
			v_square_l = float(input('Enter the length: '))
			clear()
			v_square_w = float(input('Enter the width: '))
			clear()
			v_square_h = float(input('Enter the height: '))
			clear()
			v_square_result = (v_square_l*v_square_w*v_square_h)
			if check_dot_zero(v_square_result) == True:
				print(f'The volume of the pyramid is: {int(v_square_result)}')
			else:
				print(f'The volume of the pyramid is: {v_square_result}')

		elif choice5 == 'v penta':
			clear()
			v_penta_a = float(input('Enter the length of one of the sides of the base: '))
			clear()
			v_penta_h = float(input('Enter the height of the pyramid: '))
			clear()
			global v_penta_result
			v_penta_result = ((5/12)*(math.tan(math.radians(54))))*(v_penta_h*(v_penta_a**2))
			if check_dot_zero(v_penta_result) == True:
				print(f'The volume of the pentagonal pyramid is: {int(v_penta_result)}')
			else:
				print(f'The volume of the pentagonal pyramid is: {v_penta_result}')

		elif choice5 == 'v hexa':
			clear()
			v_hexa_a = float(input('Enter the length of one of the sides of the base: '))
			clear()
			v_hexa_h = float(input('Enter the height of the pyramid: '))
			clear()
			v_hexa_result = (((math.sqrt(3))/2)*(v_hexa_a**2))*v_hexa_h
			if check_dot_zero(v_penta_result) == True:
				print(f'The volume of the hexagonal pyramid is: {int(v_penta_result)}')
			else:
				print(f'The volume of the hexagonal pyramid is: {v_penta_result}')

		elif choice5 == 'v hepta':
			clear()
			v_hepta_a = float(input('Enter the length of one of the sides of the base: '))
			clear()
			v_hepta_h = float(input('Enter the height of the pyramid: '))
			clear()
			v_hepta_result = (7/12)*v_hepta_h*(v_hepta_a**2)*(mpmath.cot(pi/7))
			if check_dot_zero(v_hepta_result) == True:
				print(f'The volume of the heptagonal pyramid is: {int(v_hepta_result)}')
			else:
				print(f'The volume of the heptagonal pyramid is: {v_hepta_result}')

		elif choice5 == 'v octa':
			clear()
			v_octa_a = float(input('Enter the length of one of the sides of the base: '))
			clear()
			v_octa_h = float(input('Enter the height of the pyramid: '))
			clear()
			v_octa_result = ((8/12)*v_octa_h*(v_octa_a**2))*mpmath.cot(pi/8)
			if check_dot_zero(v_octa_result) == True:
				print(f'The volume of the octagonal pyramid is: {int(v_octa_result)}')
			else:
				print(f'The volume of the octagonal pyramid is: {v_octa_result}')

		else:
			while choice5 != 'v tetra' and choice5 != 'v square' and choice5 != 'v penta' and choice5 != 'v hexa' and choice5 != 'v hepta' and choice5 != 'v octa':
				clear()
				print("You didn't enter any of the options!")
				sleep(2)
				clear()
				print('If the pyramid is a tetrahedron (3 sides), enter "v tetra".')
				print('If the pyramid is a square pyramid (4 sides), enter "v square".')
				print('If the pyramid is a pentagonal pyramid (5 sides), enter "v penta".')
				print('If the pyramid is a hexagonal pyramid (6 sides), enter "v hexa".')
				print('If the pyramid is a heptagonal pyramid (7 sides), enter "v hepta".')
				print('If the pyramid is a octagonal pyramid (8 sides), enter "v octa".')
				sleep(1.5)
				choice5 = input('Enter your choice and press "Enter": ')
				if choice5 == 'v tetra':
					clear()
					v_tri_a = float(input('Enter the length of one of the edges of one of the sides: '))
					clear()
					v_tri_result = (v_tri_a**3)/(6*math.sqrt(2))
					if check_dot_zero(v_tri_result) == True:
						print(f'The volume of the triangular pyramid is: {int(v_tri_result)}')
					else:
						print(f'The volume of the triangular pyramid is: {v_tri_result}')
					break

				elif choice5 == 'v square':
					clear()
					v_square_l = float(input('Enter the length: '))
					clear()
					v_square_w = float(input('Enter the width: '))
					clear()
					v_square_h = float(input('Enter the height: '))
					clear()
					v_square_result = (v_square_l*v_square_w*v_square_h)
					if check_dot_zero(v_square_result) == True:
						print(f'The volume of the pyramid is: {int(v_square_result)}')
					else:
						print(f'The volume of the pyramid is: {v_square_result}')
					break

				elif choice5 == 'v penta':
					clear()
					v_penta_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_penta_h = float(input('Enter the height of the pyramid: '))
					clear()
					v_penta_result = ((5/12)*(math.tan(math.radians(54))))*(v_penta_h*(v_penta_a**2))
					if check_dot_zero(v_penta_result) == True:
						print(f'The volume of the pentagonal pyramid is: {int(v_penta_result)}')
					else:
						print(f'The volume of the pentagonal pyramid is: {v_penta_result}')
					break

				elif choice5 == 'v hexa':
					clear()
					v_hexa_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_hexa_h = float(input('Enter the height of the pyramid: '))
					clear()
					v_hexa_result = (((math.sqrt(3))/2)*(v_hexa_a**2))*v_hexa_h
					if check_dot_zero(v_penta_result) == True:
						print(f'The volume of the hexagonal pyramid is: {int(v_penta_result)}')
					else:
						print(f'The volume of the hexagonal pyramid is: {v_penta_result}')
					break

				elif choice5 == 'v hepta':
					clear()
					v_hepta_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_hepta_h = float(input('Enter the height of the pyramid: '))
					clear()
					v_hepta_result = (7/12)*v_hepta_h*(v_hepta_a**2)*(mpmath.cot(pi/7))
					if check_dot_zero(v_hepta_result) == True:
						print(f'The volume of the heptagonal pyramid is: {int(v_hepta_result)}')
					else:
						print(f'The volume of the heptagonal pyramid is: {v_hepta_result}')
					break

				elif choice5 == 'v octa':
					clear()
					v_octa_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_octa_h = float(input('Enter the height of the pyramid: '))
					clear()
					v_octa_result = ((8/12)*v_octa_h*(v_octa_a**2))*mpmath.cot(pi/8)
					if check_dot_zero(v_octa_result) == True:
						print(f'The volume of the octagonal pyramid is: {int(v_octa_result)}')
					else:
						print(f'The volume of the octagonal pyramid is: {v_octa_result}')
					break

	elif choice3 == 'v cone':
		clear()
		v_cone_r = float(input('Enter the radius of the base: '))
		clear()
		v_cone_h = float(input('Enter the height of the cone: '))
		clear()
		v_cone_result = (pi*(v_cone_r**2))*(v_cone_h/3)
		if check_dot_zero(v_cone_result) == True:
			print(f'The volume of the cone is: {int(v_cone_result)}')
		else:
			print(f'The volume of the cone is: {v_cone_result}')

	elif choice3 == 'v cylinder':
		clear()
		v_cylinder_r = float(input('Enter the radius of the base: '))
		clear()
		v_cylinder_h = float(input('Enter the height of the cylinder: '))
		clear()
		v_cylinder_result = (pi*(v_cylinder_r**2))*v_cylinder_h
		if check_dot_zero(v_cylinder_result) == True:
			print(f'The volume of the cylinder is: {int(v_cylinder_result)}')
		else:
			print(f'The volume of the cylinder is: {v_cylinder_result}')

	elif choice3 == 'v sphere':
		clear()
		v_sphere_r = float(input('Enter the radius: '))
		clear()
		v_sphere_result = (4/3)*(pi*(v_sphere_r**3))
		if check_dot_zero(v_sphere_result) == True:
			print(f'The volume of the sphere is: {int(v_sphere_result)}')
		else:
			print(f'The volume of the sphere is: {v_sphere_result}')

	else:
		while choice3 != 'v cube' and choice3 != 'v right r prism' and choice3 != 'v prism' and choice3 != 'v pyramid' and choice3 != 'v cone' and choice3 != 'v cylinder' and choice3 != 'v sphere':
			clear()
			print("You didn't enter any of the options!")
			sleep(2)
			clear()
			print('To calculate the volume of a cube, enter "v cube".')
			print('To calculate the volume of a right rectangular prism, enter "v right r prism".')
			print('To calculate the volume of a regular prism, enter "v prism".')
			print('To calculate the volume of a pyramid, enter "v pyramid".')
			print('To calculate the volume of a cone, enter "v cone".')
			print('To calculate the volume of a cylinder, enter "v cylinder".')
			print('To calculate the volume of a sphere, enter "v sphere".')
			sleep(1.5)
			choice3 = input('Enter your choice and press "Enter": ')
			if choice3 == 'v cube':
				clear()
				v_cube_side = float(input('Enter the length of the side: '))
				clear()
				v_cube_result = v_cube_side**3
				if check_dot_zero(v_cube_result) == True:
					print(f'The volume of the cube is: {int(v_cube_result)}')
				else:
					print(f'The volume of the cube is: {v_cube_result}')
				break

			elif choice3 == 'v right r prism':
				clear()
				v_right_r_prism_l = float(input('Enter the length: '))
				clear()
				v_right_r_prism_w = float(input('Enter the width: '))
				clear()
				v_right_r_prism_h = float(input('Enter the height: '))
				clear()
				v_right_r_prism_result = v_right_r_prism_l*v_right_r_prism_w*v_right_r_prism_h
				if check_dot_zero(v_right_r_prism_result) == True:
					print(f'The volume of the right rectangular prism is: {int(v_right_r_prism_result)}')
				else:
					print(f'The volume of the right rectangular prism is: {v_right_r_prism_result}')
				break

			elif choice3 == 'v prism':
				clear()
				print('If the prism is a square prism, enter "s prism".')
				print('If the prism is a rectangular prism, enter "r prism".')
				print('If the prism is a triangular prism, enter "t prism".')
				print('If the prism is a pentagonal prism (5 sides), enter "p prism".')
				print('If the prism is a hexagonal prism (6 sides), enter "h prism".')
				print('If the prism is a heptagonal prism (7 sides), enter "hept prism".')
				print('If the prism is an octagonal prism (8 sides), enter "o prism".')
				sleep(1.5)
				choice4 = input('Enter your choice and press "Enter": ')
				if choice4 == 's prism':
					clear()
					v_s_prism_s = float(input('Enter the length of a side of the base: '))
					clear()
					v_s_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_s_prism_result = (v_s_prism_s**2)*v_s_prism_h
					if check_dot_zero(v_s_prism_result) == True:
						print(f'The volume of the square prism is: {int(v_s_prism_result)}')
					else:
						print(f'The volume of the square prism is: {v_s_prism_result}')

				elif choice4 == 'r prism':
					clear()
					v_r_prism_l = float(input('Enter the length: '))
					clear()
					v_r_prism_w = float(input('Enter the width: '))
					clear()
					v_r_prism_h = float(input('Enter the height: '))
					clear()
					v_r_prism_result = v_r_prism_l*v_r_prism_w*v_r_prism_h
					if check_dot_zero(v_r_prism_result) == True:
						print(f'The volume of the rectangular prism is: {int(v_r_prism_result)}')
					else:
						print(f'The volume of the rectangular prism is: {v_r_prism_result}')

				elif choice4 == 't prism':
					clear()
					v_t_prism_a = float(input('Enter one of the sides of the base: '))
					clear()
					v_t_prism_b = float(input('Enter one of the other sides of the base: '))
					clear()
					v_t_prism_c = float(input('Enter the remaining side of the base: '))
					clear()
					v_t_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_t_prism_result = ((1/4)*v_t_prism_h)*math.sqrt(-v_t_prism_a**4+(2*((v_t_prism_a*v_t_prism_b)**2)+2*((v_t_prism_a*v_t_prism_c)**2)-v_t_prism_b**4+2*((v_t_prism_b*v_t_prism_c)**2)-v_t_prism_c**4))
					if check_dot_zero(v_t_prism_result) == True:
						print(f'The volume of the triangular prism is: {int(v_t_prism_result)}')
					else:
						print(f'The volume of the triangular prism is: {v_t_prism_result}')

				elif choice4 == 'p prism':
					clear()
					v_p_prism_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_p_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_p_prism_result = ((1/4)*math.sqrt((5*(5+(2*(math.sqrt(5)))))))*((v_p_prism_a**2)*v_p_prism_h)
					if check_dot_zero(v_p_prism_result) == True:
						print(f'The volume of the pentagonal prism is: {int(v_p_prism_result)}')
					else:
						print(f'The volume of the pentagonal prism is: {v_p_prism_result}')

				elif choice4 == 'h prism':
					clear()
					v_h_prism_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_h_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_h_prism_result = (((3*math.sqrt(3))/2)*(v_h_prism_a**2))*v_h_prism_h
					if check_dot_zero(v_h_prism_result) == True:
						print(f'The volume of the hexagonal prism is: {int(v_h_prism_result)}')
					else:
						print(f'The volume of the hexagonal prism is: {v_h_prism_result}')

				elif choice4 == 'hept prism':
					clear()
					v_hept_prism_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_hept_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_hept_prism_result = ((7/4)*v_hept_prism_a**2)*mpmath.cot((math.radians(180)/7))*v_hept_prism_h
					if check_dot_zero(v_hept_prism_result) == True:
						print(f'The volume of the heptagonal prism is: {int(v_hept_prism_result)}')
					else:
						print(f'The volume of the heptagonal prism is: {v_hept_prism_result}')

				elif choice4 == 'o prism':
					clear()
					v_o_prism_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_o_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_o_prism_result = ((2*(1+math.sqrt(2)))*(v_o_prism_a**2))*v_o_prism_h
					if check_dot_zero(v_o_prism_result) == True:
						print(f'The volume of the octagonal prism is: {int(v_o_prism_result)}')
					else:
						print(f'The volume of the octagonal prism is: {v_o_prism_result}')

				else:
					while choice4 != 's prism' and choice4 != 'r prism' and choice4 != 't prism' and choice4 != 'p prism' and choice4 != 'h prism' and choice4 != 'hept prism' and choice4 != 'o prism':
						clear()
						print("You didn't enter any of the options!")
						sleep(2)
						clear()
						print('If the prism is a square prism, enter "s prism".')
						print('If the prism is a rectangular prism, enter "r prism".')
						print('If the prism is a triangular prism, enter "t prism".')
						print('If the prism is a pentagonal prism (5 sides), enter "p prism".')
						print('If the prism is a hexagonal prism (6 sides), enter "h prism".')
						print('If the prism is a heptagonal prism (7 sides), enter "hept prism".')
						print('If the prism is an octagonal prism (8 sides), enter "o prism".')
						sleep(1.5)
						choice4 = input('Enter your choice and press "Enter": ')
						if choice4 == 's prism':
							clear()
							v_s_prism_s = float(input('Enter the length of a side of the base: '))
							clear()
							v_s_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_s_prism_result = (v_s_prism_s**2)*v_s_prism_h
							if check_dot_zero(v_s_prism_result) == True:
								print(f'The volume of the square prism is: {int(v_s_prism_result)}')
							else:
								print(f'The volume of the square prism is: {v_s_prism_result}')
							break

						elif choice4 == 'r prism':
							clear()
							v_r_prism_l = float(input('Enter the length: '))
							clear()
							v_r_prism_w = float(input('Enter the width: '))
							clear()
							v_r_prism_h = float(input('Enter the height: '))
							clear()
							v_r_prism_result = v_r_prism_l*v_r_prism_w*v_r_prism_h
							if check_dot_zero(v_r_prism_result) == True:
								print(f'The volume of the rectangular prism is: {int(v_r_prism_result)}')
							else:
								print(f'The volume of the rectangular prism is: {v_r_prism_result}')
							break

						elif choice4 == 't prism':
							clear()
							v_t_prism_a = float(input('Enter one of the sides of the base: '))
							clear()
							v_t_prism_b = float(input('Enter one of the other sides of the base: '))
							clear()
							v_t_prism_c = float(input('Enter the remaining side of the base: '))
							clear()
							v_t_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_t_prism_result = ((1/4)*v_t_prism_h)*math.sqrt(-v_t_prism_a**4+(2*((v_t_prism_a*v_t_prism_b)**2)+2*((v_t_prism_a*v_t_prism_c)**2)-v_t_prism_b**4+2*((v_t_prism_b*v_t_prism_c)**2)-v_t_prism_c**4))
							if check_dot_zero(v_t_prism_result) == True:
								print(f'The volume of the triangular prism is: {int(v_t_prism_result)}')
							else:
								print(f'The volume of the triangular prism is: {v_t_prism_result}')
							break

						elif choice4 == 'p prism':
							clear()
							v_p_prism_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_p_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_p_prism_result = ((1/4)*math.sqrt((5*(5+(2*(math.sqrt(5)))))))*((v_p_prism_a**2)*v_p_prism_h)
							if check_dot_zero(v_p_prism_result) == True:
								print(f'The volume of the pentagonal prism is: {int(v_p_prism_result)}')
							else:
								print(f'The volume of the pentagonal prism is: {v_p_prism_result}')
							break

						elif choice4 == 'h prism':
							clear()
							v_h_prism_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_h_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_h_prism_result = (((3*math.sqrt(3))/2)*(v_h_prism_a**2))*v_h_prism_h
							if check_dot_zero(v_h_prism_result) == True:
								print(f'The volume of the hexagonal prism is: {int(v_h_prism_result)}')
							else:
								print(f'The volume of the hexagonal prism is: {v_h_prism_result}')
							break

						elif choice4 == 'hept prism':
							clear()
							v_hept_prism_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_hept_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_hept_prism_result = ((7/4)*v_hept_prism_a**2)*mpmath.cot((math.radians(180)/7))*v_hept_prism_h
							if check_dot_zero(v_hept_prism_result) == True:
								print(f'The volume of the heptagonal prism is: {int(v_hept_prism_result)}')
							else:
								print(f'The volume of the heptagonal prism is: {v_hept_prism_result}')
							break

						elif choice4 == 'o prism':
							clear()
							v_o_prism_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_o_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_o_prism_result = ((2*(1+math.sqrt(2)))*(v_o_prism_a**2))*v_o_prism_h
							if check_dot_zero(v_o_prism_result) == True:
								print(f'The volume of the octagonal prism is: {int(v_o_prism_result)}')
							else:
								print(f'The volume of the octagonal prism is: {v_o_prism_result}')
							break
				break

			elif choice3 == 'v pyramid':
				clear()
				print('If the pyramid is a tetrahedron (3 sides), enter "v tetra".')
				print('If the pyramid is a square pyramid (4 sides), enter "v square".')
				print('If the pyramid is a pentagonal pyramid (5 sides), enter "v penta".')
				print('If the pyramid is a hexagonal pyramid (6 sides), enter "v hexa".')
				print('If the pyramid is a heptagonal pyramid (7 sides), enter "v hepta".')
				print('If the pyramid is a octagonal pyramid (8 sides), enter "v octa".')
				sleep(1.5)
				choice5 = input('Enter your choice and press "Enter": ')
				if choice5 == 'v tetra':
					clear()
					v_tri_a = float(input('Enter the length of one of the edges of one of the sides: '))
					clear()
					v_tri_result = (v_tri_a**3)/(6*math.sqrt(2))
					if check_dot_zero(v_tri_result) == True:
						print(f'The volume of the triangular pyramid is: {int(v_tri_result)}')
					else:
						print(f'The volume of the triangular pyramid is: {v_tri_result}')

				elif choice5 == 'v square':
					clear()
					v_square_l = float(input('Enter the length: '))
					clear()
					v_square_w = float(input('Enter the width: '))
					clear()
					v_square_h = float(input('Enter the height: '))
					clear()
					v_square_result = (v_square_l*v_square_w*v_square_h)
					if check_dot_zero(v_square_result) == True:
						print(f'The volume of the pyramid is: {int(v_square_result)}')
					else:
						print(f'The volume of the pyramid is: {v_square_result}')

				elif choice5 == 'v penta':
					clear()
					v_penta_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_penta_h = float(input('Enter the height of the pyramid: '))
					clear()
					v_penta_result = ((5/12)*(math.tan(math.radians(54))))*(v_penta_h*(v_penta_a**2))
					if check_dot_zero(v_penta_result) == True:
						print(f'The volume of the pentagonal pyramid is: {int(v_penta_result)}')
					else:
						print(f'The volume of the pentagonal pyramid is: {v_penta_result}')

				elif choice5 == 'v hexa':
					clear()
					v_hexa_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_hexa_h = float(input('Enter the height of the pyramid: '))
					clear()
					v_hexa_result = (((math.sqrt(3))/2)*(v_hexa_a**2))*v_hexa_h
					if check_dot_zero(v_penta_result) == True:
						print(f'The volume of the hexagonal pyramid is: {int(v_penta_result)}')
					else:
						print(f'The volume of the hexagonal pyramid is: {v_penta_result}')

				elif choice5 == 'v hepta':
					clear()
					v_hepta_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_hepta_h = float(input('Enter the height of the pyramid: '))
					clear()
					v_hepta_result = (7/12)*v_hepta_h*(v_hepta_a**2)*(mpmath.cot(pi/7))
					if check_dot_zero(v_hepta_result) == True:
						print(f'The volume of the heptagonal pyramid is: {int(v_hepta_result)}')
					else:
						print(f'The volume of the heptagonal pyramid is: {v_hepta_result}')

				elif choice5 == 'v octa':
					clear()
					v_octa_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_octa_h = float(input('Enter the height of the pyramid: '))
					clear()
					v_octa_result = ((8/12)*v_octa_h*(v_octa_a**2))*mpmath.cot(pi/8)
					if check_dot_zero(v_octa_result) == True:
						print(f'The volume of the octagonal pyramid is: {int(v_octa_result)}')
					else:
						print(f'The volume of the octagonal pyramid is: {v_octa_result}')

				else:
					while choice5 != 'v tetra' and choice5 != 'v square' and choice5 != 'v penta' and choice5 != 'v hexa' and choice5 != 'v hepta' and choice5 != 'v octa':
						clear()
						print("You didn't enter any of the options!")
						sleep(2)
						clear()
						print('If the pyramid is a tetrahedron (3 sides), enter "v tetra".')
						print('If the pyramid is a square pyramid (4 sides), enter "v square".')
						print('If the pyramid is a pentagonal pyramid (5 sides), enter "v penta".')
						print('If the pyramid is a hexagonal pyramid (6 sides), enter "v hexa".')
						print('If the pyramid is a heptagonal pyramid (7 sides), enter "v hepta".')
						print('If the pyramid is a octagonal pyramid (8 sides), enter "v octa".')
						sleep(1.5)
						choice5 = input('Enter your choice and press "Enter": ')
						if choice5 == 'v tetra':
							clear()
							v_tri_a = float(input('Enter the length of one of the edges of one of the sides: '))
							clear()
							v_tri_result = (v_tri_a**3)/(6*math.sqrt(2))
							if check_dot_zero(v_tri_result) == True:
								print(f'The volume of the triangular pyramid is: {int(v_tri_result)}')
							else:
								print(f'The volume of the triangular pyramid is: {v_tri_result}')
							break

						elif choice5 == 'v square':
							clear()
							v_square_l = float(input('Enter the length: '))
							clear()
							v_square_w = float(input('Enter the width: '))
							clear()
							v_square_h = float(input('Enter the height: '))
							clear()
							v_square_result = (v_square_l*v_square_w*v_square_h)
							if check_dot_zero(v_square_result) == True:
								print(f'The volume of the pyramid is: {int(v_square_result)}')
							else:
								print(f'The volume of the pyramid is: {v_square_result}')
							break

						elif choice5 == 'v penta':
							clear()
							v_penta_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_penta_h = float(input('Enter the height of the pyramid: '))
							clear()
							v_penta_result = ((5/12)*(math.tan(math.radians(54))))*(v_penta_h*(v_penta_a**2))
							if check_dot_zero(v_penta_result) == True:
								print(f'The volume of the pentagonal pyramid is: {int(v_penta_result)}')
							else:
								print(f'The volume of the pentagonal pyramid is: {v_penta_result}')
							break

						elif choice5 == 'v hexa':
							clear()
							v_hexa_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_hexa_h = float(input('Enter the height of the pyramid: '))
							clear()
							v_hexa_result = (((math.sqrt(3))/2)*(v_hexa_a**2))*v_hexa_h
							if check_dot_zero(v_penta_result) == True:
								print(f'The volume of the hexagonal pyramid is: {int(v_penta_result)}')
							else:
								print(f'The volume of the hexagonal pyramid is: {v_penta_result}')
							break

						elif choice5 == 'v hepta':
							clear()
							v_hepta_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_hepta_h = float(input('Enter the height of the pyramid: '))
							clear()
							v_hepta_result = (7/12)*v_hepta_h*(v_hepta_a**2)*(mpmath.cot(pi/7))
							if check_dot_zero(v_hepta_result) == True:
								print(f'The volume of the heptagonal pyramid is: {int(v_hepta_result)}')
							else:
								print(f'The volume of the heptagonal pyramid is: {v_hepta_result}')
							break

						elif choice5 == 'v octa':
							clear()
							v_octa_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_octa_h = float(input('Enter the height of the pyramid: '))
							clear()
							v_octa_result = ((8/12)*v_octa_h*(v_octa_a**2))*mpmath.cot(pi/8)
							if check_dot_zero(v_octa_result) == True:
								print(f'The volume of the octagonal pyramid is: {int(v_octa_result)}')
							else:
								print(f'The volume of the octagonal pyramid is: {v_octa_result}')
							break
				break                 

			elif choice3 == 'v cone':
				clear()
				v_cone_r = float(input('Enter the radius of the base: '))
				clear()
				v_cone_h = float(input('Enter the height of the cone: '))
				clear()
				v_cone_result = (pi*(v_cone_r**2))*(v_cone_h/3)
				if check_dot_zero(v_cone_result) == True:
					print(f'The volume of the cone is: {int(v_cone_result)}')
				else:
					print(f'The volume of the cone is: {v_cone_result}')
				break

			elif choice3 == 'v cylinder':
				clear()
				v_cylinder_r = float(input('Enter the radius of the base: '))
				clear()
				v_cylinder_h = float(input('Enter the height of the cylinder: '))
				clear()
				v_cylinder_result = (pi*(v_cylinder_r**2))*v_cylinder_h
				if check_dot_zero(v_cylinder_result) == True:
					print(f'The volume of the cylinder is: {int(v_cylinder_result)}')
				else:
					print(f'The volume of the cylinder is: {v_cylinder_result}')
				break

			elif choice3 == 'v sphere':
				clear()
				v_sphere_r = float(input('Enter the radius: '))
				clear()
				v_sphere_result = (4/3)*(pi*(v_sphere_r**3))
				if check_dot_zero(v_sphere_result) == True:
					print(f'The volume of the sphere is: {int(v_sphere_result)}')
				else:
					print(f'The volume of the sphere is: {v_sphere_result}')
				break

else:
	while choice != 'p' and choice != 'a' and choice != 'v':
		clear()
		print("You didn't enter any of the options!")
		sleep(2)
		clear()
		print('To calculate the perimeter of something, enter "p".')
		print('To calculate the area of something, enter "a".')
		print('To calculate the volume of something, enter "v".')
		sleep(1.5)
		choice = input('Enter your choice and press "Enter": ').lower()
		if choice == 'p':
			clear()
			print('To calculate the perimeter of a square, enter "p square".')
			print('To calculate the perimeter of a rectangle, enter "p rectangle".')
			print('To calculate the perimeter of a triangle, enter "p triangle".')
			print('To calculate the perimeter of a right triangle, enter "p right tri".')
			print('To calculate the circumference of a circle, enter "c circle".')
			sleep(1.5)
			choice1 = input('Enter your choice and press "Enter": ').lower()
			if choice1 == 'p square':
				clear()
				p_square_side = float(input('Enter the length of a side: '))
				clear()
				p_square_result = p_square_side**4
				if check_dot_zero(p_square_result) == True:
					print(f'The perimeter of the square is: {int(p_square_result)}')
				else:
					print(f'The perimeter of the square is: {p_square_result}')

			elif choice1 == 'p rectangle':
				clear()
				p_rectangle_side = float(input('Enter the length of a side: '))
				clear()
				p_rectangle_side1 = float(input('Enter the length of the other side: '))
				clear()
				p_rectangle_result = (p_rectangle_side*2)+(p_rectangle_side1*2)
				if check_dot_zero(p_rectangle_result) == True:
					print(f'The perimeter of the rectangle is: {int(p_rectangle_result)}')
				else:
					print(f'The perimeter of the rectangle is: {p_rectangle_result}')

			elif choice1 == 'p triangle':
				clear()
				p_triangle_side = float(input('Enter the length of a side: '))
				clear()
				p_triangle_side1 = float(input('Enter the length of another side: '))
				clear()
				p_triangle_side2 = float(input('Enter the length of the remaining side: '))
				clear()
				p_triangle_result = p_triangle_side+p_triangle_side1+p_triangle_side2
				if check_dot_zero(p_triangle_result) == True:
					print(f'The perimeter of the triangle is: {int(p_triangle_result)}')
				else:
					print(f'The perimeter of the triangle is: {p_triangle_result}')

			elif choice1 == 'p right tri':
				clear()
				p_right_side = float(input('Enter the length of one of the legs: '))
				clear()
				p_right_side1 = float(input('Enter the length of the other leg: '))
				clear()
				p_right_result = (p_right_side+p_right_side1)+(math.sqrt((p_right_side**2)+(p_right_side1**2)))
				if check_dot_zero(p_right_result) == True:
					print(f'The perimeter of the right triangle is: {int(p_right_result)}')
				else:
					print(f'The perimeter of the right triangle is: {p_right_result}')

			elif choice1 == 'c circle':
				clear()
				p_circle_r = float(input('Enter the radius of the circle: '))
				clear()
				p_circle_result = (pi*p_circle_r)*2
				if p_circle_result == True:
					print(f'The circumference of the circle is: {int(p_circle_result)}')
				else:
					print(f'The circumference of the circle is: {p_circle_result}')

			else:
				while choice1 != 'p square' and choice1 != 'p rectangle' and choice1 != 'p triangle' and choice1 != 'p right tri' and choice1 != 'c circle':
					clear()
					print("You didn't enter any of the options!")
					sleep(2)
					clear()
					print('To calculate the perimeter of a square, enter "p square".')
					print('To calculate the perimeter of a rectangle, enter "p rectangle".')
					print('To calculate the perimeter of a triangle, enter "p triangle".')
					print('To calculate the perimeter of a right triangle, enter "p right tri".')
					print('To calculate the circumference of a circle, enter "c circle".')
					sleep(1.5)
					choice1 = input('Enter your choice and press "Enter": ').lower()
					if choice1 == 'p square':
						clear()
						p_square_side = float(input('Enter the length of a side: '))
						clear()
						p_square_result = p_square_side**4
						if check_dot_zero(p_square_result) == True:
							print(f'The perimeter of the square is: {int(p_square_result)}')
						else:
							print(f'The perimeter of the square is: {p_square_result}')
						break

					elif choice1 == 'p rectangle':
						clear()
						p_rectangle_side = float(input('Enter the length of a side: '))
						clear()
						p_rectangle_side1 = float(input('Enter the length of the other side: '))
						clear()
						p_rectangle_result = (p_rectangle_side*2)+(p_rectangle_side1*2)
						if check_dot_zero(p_rectangle_result) == True:
							print(f'The perimeter of the rectangle is: {int(p_rectangle_result)}')
						else:
							print(f'The perimeter of the rectangle is: {p_rectangle_result}')
						break

					elif choice1 == 'p triangle':
						clear()
						p_triangle_side = float(input('Enter the length of a side: '))
						clear()
						p_triangle_side1 = float(input('Enter the length of another side: '))
						clear()
						p_triangle_side2 = float(input('Enter the length of the remaining side: '))
						clear()
						p_triangle_result = p_triangle_side+p_triangle_side1+p_triangle_side2
						if check_dot_zero(p_triangle_result) == True:
							print(f'The perimeter of the triangle is: {int(p_triangle_result)}')
						else:
							print(f'The perimeter of the triangle is: {p_triangle_result}')
						break

					elif choice1 == 'p right tri':
						clear()
						p_right_side = float(input('Enter the length of one of the legs: '))
						clear()
						p_right_side1 = float(input('Enter the length of the other leg: '))
						clear()
						p_right_result = (p_right_side+p_right_side1)+(math.sqrt((p_right_side**2)+(p_right_side1**2)))
						if check_dot_zero(p_right_result) == True:
							print(f'The perimeter of the right triangle is: {int(p_right_result)}')
						else:
							print(f'The perimeter of the right triangle is: {p_right_result}')
						break

					elif choice1 == 'c circle':
						clear()
						p_circle_r = float(input('Enter the radius of the circle: '))
						clear()
						p_circle_result = (pi*p_circle_r)*2
						if p_circle_result == True:
							print(f'The circumference of the circle is: {int(p_circle_result)}')
						else:
							print(f'The circumference of the circle is: {p_circle_result}')
						break
			break

		elif choice == 'a':
			clear()
			print('To calculate the area of a square, enter "a square".')
			print('To calculate the area of a rectangle, enter "a rectangle".')
			print('To calculate the area of a triangle, enter "a triangle".')
			print('To calculate the area of a parallelogram, enter "a parallel".')
			print('To calculate the area of a trapezoid, enter "a trapezoid".')
			print('To calculate the area of a circle, enter "a circle".')
			sleep(1.5)
			choice2 = input('Enter your choice and press "Enter": ').lower()
			if choice2 == 'a square':
				clear()
				a_square_side = float(input('Enter the length of a side: '))
				clear()
				a_square_result = a_square_side**2
				if check_dot_zero(a_square_result) == True:
					print(f'The area of the square is: {int(a_square_result)}')
				else:
					print(f'The area of the square is: {a_square_result}')

			elif choice2 == 'a rectangle':
				clear()
				a_rectangle_side = float(input('Enter the length of a side: '))
				clear()
				a_rectangle_side1 = float(input('Enter the length of the other side: '))
				clear()
				a_rectangle_result = a_rectangle_side*a_rectangle_side1
				if check_dot_zero(a_rectangle_result) == True:
					print(f'The area of the rectangle is: {int(a_rectangle_result)}')
				else:
					print(f'The area of the rectangle is: {a_rectangle_result}')

			elif choice2 == 'a triangle':
				clear()
				a_triangle_base = float(input('Enter the length of the base: '))
				clear()
				a_triangle_height = float(input('Enter the length of the height: '))
				clear()
				a_triangle_result = (1/2*(a_triangle_base*a_triangle_height))
				if check_dot_zero(a_triangle_result) == True:
					print(f'The area of the triangle is: {int(a_triangle_result)}')
				else:
					print(f'The area of the triangle is: {a_triangle_result}')

			elif choice2 == 'a parallel':
				clear()
				a_parallel_base = float(input('Enter the length of the base: '))
				clear()
				a_parallel_height = float(input('Enter the length of the height: '))
				clear()
				a_parallel_result = a_parallel_base*a_parallel_height
				if check_dot_zero(a_parallel_result) == True:
					print(f'The area of the parallelogram is: {int(a_parallel_result)}')
				else:
					print(f'The area of the parallelogram is: {a_parallel_result}')

			elif choice2 == 'a trapezoid':
				clear()
				a_trapezoid_b1 = float(input('Enter the length of a base: '))
				clear()
				a_trapezoid_b2 = float(input('Enter the length of the other base: '))
				clear()
				a_trapezoid_h = float(input('Enter the length of the height: '))
				clear()
				a_trapezoid_result = (((a_trapezoid_b1+a_trapezoid_b2)/2)*a_trapezoid_h)
				if check_dot_zero(a_trapezoid_result) == True:
					print(f'The area of the trapezoid is: {int(a_trapezoid_result)}')
				else:
					print(f'The area of the trapezoid is: {a_trapezoid_result}')

			elif choice2 == 'a circle':
				clear()
				a_circle_r = float(input('Enter the radius: '))
				clear()
				a_circle_result = (pi*(a_circle_r**2))
				if check_dot_zero(a_circle_result) == True:
					print(f'The area of the circle is: {int(a_circle_result)}')
				else:
					print(f'The area of the circle is: {a_circle_result}')

			else:
				while choice2 != 'a square' and choice2 != 'a rectangle' and choice2 != 'a triangle' and choice2 != 'a parallel' and choice2 != 'a trapezoid' and choice2 != 'a circle':
					clear()
					print("You didn't enter any of the options!")
					sleep(2)
					clear()
					print('To calculate the area of a square, enter "a square".')
					print('To calculate the area of a rectangle, enter "a rectangle".')
					print('To calculate the area of a triangle, enter "a triangle".')
					print('To calculate the area of a parallelogram, enter "a parallel".')
					print('To calculate the area of a trapezoid, enter "a trapezoid".')
					print('To calculate the area of a circle, enter "a circle".')
					sleep(1.5)
					choice2 = input('Enter your choice and press "Enter": ').lower()
					if choice2 == 'a square':
						clear()
						a_square_side = float(input('Enter the length of a side: '))
						clear()
						a_square_result = a_square_side**2
						if check_dot_zero(a_square_result) == True:
							print(f'The area of the square is: {int(a_square_result)}')
						else:
							print(f'The area of the square is: {a_square_result}')
						break

					elif choice2 == 'a rectangle':
						clear()
						a_rectangle_side = float(input('Enter the length of a side: '))
						clear()
						a_rectangle_side1 = float(input('Enter the length of the other side: '))
						clear()
						a_rectangle_result = a_rectangle_side*a_rectangle_side1
						if check_dot_zero(a_rectangle_result) == True:
							print(f'The area of the rectangle is: {int(a_rectangle_result)}')
						else:
							print(f'The area of the rectangle is: {a_rectangle_result}')
						break

					elif choice2 == 'a triangle':
						clear()
						a_triangle_base = float(input('Enter the length of the base: '))
						clear()
						a_triangle_height = float(input('Enter the length of the height: '))
						clear()
						a_triangle_result = (1/2*(a_triangle_base*a_triangle_height))
						if check_dot_zero(a_triangle_result) == True:
							print(f'The area of the triangle is: {int(a_triangle_result)}')
						else:
							print(f'The area of the triangle is: {a_triangle_result}')
						break

					elif choice2 == 'a parallel':
						clear()
						a_parallel_base = float(input('Enter the length of the base: '))
						clear()
						a_parallel_height = float(input('Enter the length of the height: '))
						clear()
						a_parallel_result = a_parallel_base*a_parallel_height
						if check_dot_zero(a_parallel_result) == True:
							print(f'The area of the parallelogram is: {int(a_parallel_result)}')
						else:
							print(f'The area of the parallelogram is: {a_parallel_result}')
						break

					elif choice2 == 'a trapezoid':
						clear()
						a_trapezoid_b1 = float(input('Enter the length of a base: '))
						clear()
						a_trapezoid_b2 = float(input('Enter the length of the other base: '))
						clear()
						a_trapezoid_h = float(input('Enter the length of the height: '))
						clear()
						a_trapezoid_result = (((a_trapezoid_b1+a_trapezoid_b2)/2)*a_trapezoid_h)
						if check_dot_zero(a_trapezoid_result) == True:
							print(f'The area of the trapezoid is: {int(a_trapezoid_result)}')
						else:
							print(f'The area of the trapezoid is: {a_trapezoid_result}')
						break

					elif choice2 == 'a circle':
						clear()
						a_circle_r = float(input('Enter the radius: '))
						clear()
						a_circle_result = (pi*(a_circle_r**2))
						if check_dot_zero(a_circle_result) == True:
							print(f'The area of the circle is: {int(a_circle_result)}')
						else:
							print(f'The area of the circle is: {a_circle_result}')
						break
			break

		elif choice == 'v':
			clear()
			print('To calculate the volume of a cube, enter "v cube".')
			print('To calculate the volume of a right rectangular prism, enter "v right r prism".')
			print('To calculate the volume of a regular prism, enter "v prism".')
			print('To calculate the volume of a pyramid, enter "v pyramid".')
			print('To calculate the volume of a cone, enter "v cone".')
			print('To calculate the volume of a cylinder, enter "v cylinder".')
			print('To calculate the volume of a sphere, enter "v sphere".')
			choice3 = input('Enter your choice and press "Enter": ')
			if choice3 == 'v cube':
				clear()
				v_cube_side = float(input('Enter the length of the side: '))
				clear()
				v_cube_result = v_cube_side**3
				if check_dot_zero(v_cube_result) == True:
					print(f'The volume of the cube is: {int(v_cube_result)}')
				else:
					print(f'The volume of the cube is: {v_cube_result}')

			elif choice3 == 'v right r prism':
				clear()
				v_right_r_prism_l = float(input('Enter the length: '))
				clear()
				v_right_r_prism_w = float(input('Enter the width: '))
				clear()
				v_right_r_prism_h = float(input('Enter the height: '))
				clear()
				v_right_r_prism_result = v_right_r_prism_l*v_right_r_prism_w*v_right_r_prism_h
				if check_dot_zero(v_right_r_prism_result) == True:
					print(f'The volume of the right rectangular prism is: {int(v_right_r_prism_result)}')
				else:
					print(f'The volume of the right rectangular prism is: {v_right_r_prism_result}')

			elif choice3 == 'v prism':
				clear()
				print('If the prism is a square prism, enter "s prism".')
				print('If the prism is a rectangular prism, enter "r prism".')
				print('If the prism is a triangular prism, enter "t prism".')
				print('If the prism is a pentagonal prism (5 sides), enter "p prism".')
				print('If the prism is a hexagonal prism (6 sides), enter "h prism".')
				print('If the prism is a heptagonal prism (7 sides), enter "hept prism".')
				print('If the prism is an octagonal prism (8 sides), enter "o prism".')
				sleep(1.5)
				choice4 = input('Enter your choice and press "Enter": ')
				if choice4 == 's prism':
					clear()
					v_s_prism_s = float(input('Enter the length of a side of the base: '))
					clear()
					v_s_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_s_prism_result = (v_s_prism_s**2)*v_s_prism_h
					if check_dot_zero(v_s_prism_result) == True:
						print(f'The volume of the square prism is: {int(v_s_prism_result)}')
					else:
						print(f'The volume of the square prism is: {v_s_prism_result}')

				elif choice4 == 'r prism':
					clear()
					v_r_prism_l = float(input('Enter the length: '))
					clear()
					v_r_prism_w = float(input('Enter the width: '))
					clear()
					v_r_prism_h = float(input('Enter the height: '))
					clear()
					v_r_prism_result = v_r_prism_l*v_r_prism_w*v_r_prism_h
					if check_dot_zero(v_r_prism_result) == True:
						print(f'The volume of the rectangular prism is: {int(v_r_prism_result)}')
					else:
						print(f'The volume of the rectangular prism is: {v_r_prism_result}')

				elif choice4 == 't prism':
					clear()
					v_t_prism_a = float(input('Enter one of the sides of the base: '))
					clear()
					v_t_prism_b = float(input('Enter one of the other sides of the base: '))
					clear()
					v_t_prism_c = float(input('Enter the remaining side of the base: '))
					clear()
					v_t_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_t_prism_result = ((1/4)*v_t_prism_h)*math.sqrt(-v_t_prism_a**4+(2*((v_t_prism_a*v_t_prism_b)**2)+2*((v_t_prism_a*v_t_prism_c)**2)-v_t_prism_b**4+2*((v_t_prism_b*v_t_prism_c)**2)-v_t_prism_c**4))
					if check_dot_zero(v_t_prism_result) == True:
						print(f'The volume of the triangular prism is: {int(v_t_prism_result)}')
					else:
						print(f'The volume of the triangular prism is: {v_t_prism_result}')

				elif choice4 == 'p prism':
					clear()
					v_p_prism_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_p_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_p_prism_result = ((1/4)*math.sqrt((5*(5+(2*(math.sqrt(5)))))))*((v_p_prism_a**2)*v_p_prism_h)
					if check_dot_zero(v_p_prism_result) == True:
						print(f'The volume of the pentagonal prism is: {int(v_p_prism_result)}')
					else:
						print(f'The volume of the pentagonal prism is: {v_p_prism_result}')

				elif choice4 == 'h prism':
					clear()
					v_h_prism_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_h_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_h_prism_result = (((3*math.sqrt(3))/2)*(v_h_prism_a**2))*v_h_prism_h
					if check_dot_zero(v_h_prism_result) == True:
						print(f'The volume of the hexagonal prism is: {int(v_h_prism_result)}')
					else:
						print(f'The volume of the hexagonal prism is: {v_h_prism_result}')

				elif choice4 == 'hept prism':
					clear()
					v_hept_prism_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_hept_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_hept_prism_result = ((7/4)*v_hept_prism_a**2)*mpmath.cot((math.radians(180)/7))*v_hept_prism_h
					if check_dot_zero(v_hept_prism_result) == True:
						print(f'The volume of the heptagonal prism is: {int(v_hept_prism_result)}')
					else:
						print(f'The volume of the heptagonal prism is: {v_hept_prism_result}')

				elif choice4 == 'o prism':
					clear()
					v_o_prism_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_o_prism_h = float(input('Enter the height of the prism: '))
					clear()
					v_o_prism_result = ((2*(1+math.sqrt(2)))*(v_o_prism_a**2))*v_o_prism_h
					if check_dot_zero(v_o_prism_result) == True:
						print(f'The volume of the octagonal prism is: {int(v_o_prism_result)}')
					else:
						print(f'The volume of the octagonal prism is: {v_o_prism_result}')

				else:
					while choice4 != 's prism' and choice4 != 'r prism' and choice4 != 't prism' and choice4 != 'p prism' and choice4 != 'h prism' and choice4 != 'hept prism' and choice4 != 'o prism':
						clear()
						print("You didn't enter any of the options!")
						sleep(2)
						clear()
						print('If the prism is a square prism, enter "s prism".')
						print('If the prism is a rectangular prism, enter "r prism".')
						print('If the prism is a triangular prism, enter "t prism".')
						print('If the prism is a pentagonal prism (5 sides), enter "p prism".')
						print('If the prism is a hexagonal prism (6 sides), enter "h prism".')
						print('If the prism is a heptagonal prism (7 sides), enter "hept prism".')
						print('If the prism is an octagonal prism (8 sides), enter "o prism".')
						sleep(1.5)
						choice4 = input('Enter your choice and press "Enter": ')
						if choice4 == 's prism':
							clear()
							v_s_prism_s = float(input('Enter the length of a side of the base: '))
							clear()
							v_s_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_s_prism_result = (v_s_prism_s**2)*v_s_prism_h
							if check_dot_zero(v_s_prism_result) == True:
								print(f'The volume of the square prism is: {int(v_s_prism_result)}')
							else:
								print(f'The volume of the square prism is: {v_s_prism_result}')
							break

						elif choice4 == 'r prism':
							clear()
							v_r_prism_l = float(input('Enter the length: '))
							clear()
							v_r_prism_w = float(input('Enter the width: '))
							clear()
							v_r_prism_h = float(input('Enter the height: '))
							clear()
							v_r_prism_result = v_r_prism_l*v_r_prism_w*v_r_prism_h
							if check_dot_zero(v_r_prism_result) == True:
								print(f'The volume of the rectangular prism is: {int(v_r_prism_result)}')
							else:
								print(f'The volume of the rectangular prism is: {v_r_prism_result}')
							break

						elif choice4 == 't prism':
							clear()
							v_t_prism_a = float(input('Enter one of the sides of the base: '))
							clear()
							v_t_prism_b = float(input('Enter one of the other sides of the base: '))
							clear()
							v_t_prism_c = float(input('Enter the remaining side of the base: '))
							clear()
							v_t_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_t_prism_result = ((1/4)*v_t_prism_h)*math.sqrt(-v_t_prism_a**4+(2*((v_t_prism_a*v_t_prism_b)**2)+2*((v_t_prism_a*v_t_prism_c)**2)-v_t_prism_b**4+2*((v_t_prism_b*v_t_prism_c)**2)-v_t_prism_c**4))
							if check_dot_zero(v_t_prism_result) == True:
								print(f'The volume of the triangular prism is: {int(v_t_prism_result)}')
							else:
								print(f'The volume of the triangular prism is: {v_t_prism_result}')
							break

						elif choice4 == 'p prism':
							clear()
							v_p_prism_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_p_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_p_prism_result = ((1/4)*math.sqrt((5*(5+(2*(math.sqrt(5)))))))*((v_p_prism_a**2)*v_p_prism_h)
							if check_dot_zero(v_p_prism_result) == True:
								print(f'The volume of the pentagonal prism is: {int(v_p_prism_result)}')
							else:
								print(f'The volume of the pentagonal prism is: {v_p_prism_result}')
							break

						elif choice4 == 'h prism':
							clear()
							v_h_prism_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_h_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_h_prism_result = (((3*math.sqrt(3))/2)*(v_h_prism_a**2))*v_h_prism_h
							if check_dot_zero(v_h_prism_result) == True:
								print(f'The volume of the hexagonal prism is: {int(v_h_prism_result)}')
							else:
								print(f'The volume of the hexagonal prism is: {v_h_prism_result}')
							break

						elif choice4 == 'hept prism':
							clear()
							v_hept_prism_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_hept_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_hept_prism_result = ((7/4)*v_hept_prism_a**2)*mpmath.cot((math.radians(180)/7))*v_hept_prism_h
							if check_dot_zero(v_hept_prism_result) == True:
								print(f'The volume of the heptagonal prism is: {int(v_hept_prism_result)}')
							else:
								print(f'The volume of the heptagonal prism is: {v_hept_prism_result}')
							break

						elif choice4 == 'o prism':
							clear()
							v_o_prism_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_o_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_o_prism_result = ((2*(1+math.sqrt(2)))*(v_o_prism_a**2))*v_o_prism_h
							if check_dot_zero(v_o_prism_result) == True:
								print(f'The volume of the octagonal prism is: {int(v_o_prism_result)}')
							else:
								print(f'The volume of the octagonal prism is: {v_o_prism_result}')
							break

			elif choice3 == 'v pyramid':
				clear()
				print('If the pyramid is a tetrahedron (3 sides), enter "v tetra".')
				print('If the pyramid is a square pyramid (4 sides), enter "v square".')
				print('If the pyramid is a pentagonal pyramid (5 sides), enter "v penta".')
				print('If the pyramid is a hexagonal pyramid (6 sides), enter "v hexa".')
				print('If the pyramid is a heptagonal pyramid (7 sides), enter "v hepta".')
				print('If the pyramid is a octagonal pyramid (8 sides), enter "v octa".')
				sleep(1.5)
				choice5 = input('Enter your choice and press "Enter": ')
				if choice5 == 'v tetra':
					clear()
					v_tri_a = float(input('Enter the length of one of the edges of one of the sides: '))
					clear()
					v_tri_result = (v_tri_a**3)/(6*math.sqrt(2))
					if check_dot_zero(v_tri_result) == True:
						print(f'The volume of the triangular pyramid is: {int(v_tri_result)}')
					else:
						print(f'The volume of the triangular pyramid is: {v_tri_result}')

				elif choice5 == 'v square':
					clear()
					v_square_l = float(input('Enter the length: '))
					clear()
					v_square_w = float(input('Enter the width: '))
					clear()
					v_square_h = float(input('Enter the height: '))
					clear()
					v_square_result = (v_square_l*v_square_w*v_square_h)
					if check_dot_zero(v_square_result) == True:
						print(f'The volume of the pyramid is: {int(v_square_result)}')
					else:
						print(f'The volume of the pyramid is: {v_square_result}')

				elif choice5 == 'v penta':
					clear()
					v_penta_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_penta_h = float(input('Enter the height of the pyramid: '))
					clear()
					v_penta_result = ((5/12)*(math.tan(math.radians(54))))*(v_penta_h*(v_penta_a**2))
					if check_dot_zero(v_penta_result) == True:
						print(f'The volume of the pentagonal pyramid is: {int(v_penta_result)}')
					else:
						print(f'The volume of the pentagonal pyramid is: {v_penta_result}')

				elif choice5 == 'v hexa':
					clear()
					v_hexa_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_hexa_h = float(input('Enter the height of the pyramid: '))
					clear()
					v_hexa_result = (((math.sqrt(3))/2)*(v_hexa_a**2))*v_hexa_h
					if check_dot_zero(v_penta_result) == True:
						print(f'The volume of the hexagonal pyramid is: {int(v_penta_result)}')
					else:
						print(f'The volume of the hexagonal pyramid is: {v_penta_result}')

				elif choice5 == 'v hepta':
					clear()
					v_hepta_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_hepta_h = float(input('Enter the height of the pyramid: '))
					clear()
					v_hepta_result = (7/12)*v_hepta_h*(v_hepta_a**2)*(mpmath.cot(pi/7))
					if check_dot_zero(v_hepta_result) == True:
						print(f'The volume of the heptagonal pyramid is: {int(v_hepta_result)}')
					else:
						print(f'The volume of the heptagonal pyramid is: {v_hepta_result}')

				elif choice5 == 'v octa':
					clear()
					v_octa_a = float(input('Enter the length of one of the sides of the base: '))
					clear()
					v_octa_h = float(input('Enter the height of the pyramid: '))
					clear()
					v_octa_result = ((8/12)*v_octa_h*(v_octa_a**2))*mpmath.cot(pi/8)
					if check_dot_zero(v_octa_result) == True:
						print(f'The volume of the octagonal pyramid is: {int(v_octa_result)}')
					else:
						print(f'The volume of the octagonal pyramid is: {v_octa_result}')

				else:
					while choice5 != 'v tetra' and choice5 != 'v square' and choice5 != 'v penta' and choice5 != 'v hexa' and choice5 != 'v hepta' and choice5 != 'v octa':
						clear()
						print("You didn't enter any of the options!")
						sleep(2)
						clear()
						print('If the pyramid is a tetrahedron (3 sides), enter "v tetra".')
						print('If the pyramid is a square pyramid (4 sides), enter "v square".')
						print('If the pyramid is a pentagonal pyramid (5 sides), enter "v penta".')
						print('If the pyramid is a hexagonal pyramid (6 sides), enter "v hexa".')
						print('If the pyramid is a heptagonal pyramid (7 sides), enter "v hepta".')
						print('If the pyramid is a octagonal pyramid (8 sides), enter "v octa".')
						sleep(1.5)
						choice5 = input('Enter your choice and press "Enter": ')
						if choice5 == 'v tetra':
							clear()
							v_tri_a = float(input('Enter the length of one of the edges of one of the sides: '))
							clear()
							v_tri_result = (v_tri_a**3)/(6*math.sqrt(2))
							if check_dot_zero(v_tri_result) == True:
								print(f'The volume of the triangular pyramid is: {int(v_tri_result)}')
							else:
								print(f'The volume of the triangular pyramid is: {v_tri_result}')
							break

						elif choice5 == 'v square':
							clear()
							v_square_l = float(input('Enter the length: '))
							clear()
							v_square_w = float(input('Enter the width: '))
							clear()
							v_square_h = float(input('Enter the height: '))
							clear()
							v_square_result = (v_square_l*v_square_w*v_square_h)
							if check_dot_zero(v_square_result) == True:
								print(f'The volume of the pyramid is: {int(v_square_result)}')
							else:
								print(f'The volume of the pyramid is: {v_square_result}')
							break

						elif choice5 == 'v penta':
							clear()
							v_penta_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_penta_h = float(input('Enter the height of the pyramid: '))
							clear()
							v_penta_result = ((5/12)*(math.tan(math.radians(54))))*(v_penta_h*(v_penta_a**2))
							if check_dot_zero(v_penta_result) == True:
								print(f'The volume of the pentagonal pyramid is: {int(v_penta_result)}')
							else:
								print(f'The volume of the pentagonal pyramid is: {v_penta_result}')
							break

						elif choice5 == 'v hexa':
							clear()
							v_hexa_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_hexa_h = float(input('Enter the height of the pyramid: '))
							clear()
							v_hexa_result = (((math.sqrt(3))/2)*(v_hexa_a**2))*v_hexa_h
							if check_dot_zero(v_penta_result) == True:
								print(f'The volume of the hexagonal pyramid is: {int(v_penta_result)}')
							else:
								print(f'The volume of the hexagonal pyramid is: {v_penta_result}')
							break

						elif choice5 == 'v hepta':
							clear()
							v_hepta_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_hepta_h = float(input('Enter the height of the pyramid: '))
							clear()
							v_hepta_result = (7/12)*v_hepta_h*(v_hepta_a**2)*(mpmath.cot(pi/7))
							if check_dot_zero(v_hepta_result) == True:
								print(f'The volume of the heptagonal pyramid is: {int(v_hepta_result)}')
							else:
								print(f'The volume of the heptagonal pyramid is: {v_hepta_result}')
							break

						elif choice5 == 'v octa':
							clear()
							v_octa_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_octa_h = float(input('Enter the height of the pyramid: '))
							clear()
							v_octa_result = ((8/12)*v_octa_h*(v_octa_a**2))*mpmath.cot(pi/8)
							if check_dot_zero(v_octa_result) == True:
								print(f'The volume of the octagonal pyramid is: {int(v_octa_result)}')
							else:
								print(f'The volume of the octagonal pyramid is: {v_octa_result}')
							break

			elif choice3 == 'v cone':
				clear()
				v_cone_r = float(input('Enter the radius of the base: '))
				clear()
				v_cone_h = float(input('Enter the height of the cone: '))
				clear()
				v_cone_result = (pi*(v_cone_r**2))*(v_cone_h/3)
				if check_dot_zero(v_cone_result) == True:
					print(f'The volume of the cone is: {int(v_cone_result)}')
				else:
					print(f'The volume of the cone is: {v_cone_result}')

			elif choice3 == 'v cylinder':
				clear()
				v_cylinder_r = float(input('Enter the radius of the base: '))
				clear()
				v_cylinder_h = float(input('Enter the height of the cylinder: '))
				clear()
				v_cylinder_result = (pi*(v_cylinder_r**2))*v_cylinder_h
				if check_dot_zero(v_cylinder_result) == True:
					print(f'The volume of the cylinder is: {int(v_cylinder_result)}')
				else:
					print(f'The volume of the cylinder is: {v_cylinder_result}')

			elif choice3 == 'v sphere':
				clear()
				v_sphere_r = float(input('Enter the radius: '))
				clear()
				v_sphere_result = (4/3)*(pi*(v_sphere_r**3))
				if check_dot_zero(v_sphere_result) == True:
					print(f'The volume of the sphere is: {int(v_sphere_result)}')
				else:
					print(f'The volume of the sphere is: {v_sphere_result}')

			else:
				while choice3 != 'v cube' and choice3 != 'v right r prism' and choice3 != 'v prism' and choice3 != 'v pyramid' and choice3 != 'v cone' and choice3 != 'v cylinder' and choice3 != 'v sphere':
					clear()
					print("You didn't enter any of the options!")
					sleep(2)
					print('To calculate the volume of a cube, enter "v cube".')
					print('To calculate the volume of a right rectangular prism, enter "v right r prism".')
					print('To calculate the volume of a regular prism, enter "v prism".')
					print('To calculate the volume of a pyramid, enter "v pyramid".')
					print('To calculate the volume of a cone, enter "v cone".')
					print('To calculate the volume of a cylinder, enter "v cylinder".')
					print('To calculate the volume of a sphere, enter "v sphere".')
					sleep(1.5)
					choice3 = input('Enter your choice and press "Enter": ')
					if choice3 == 'v cube':
						clear()
						v_cube_side = float(input('Enter the length of the side: '))
						clear()
						v_cube_result = v_cube_side**3
						if check_dot_zero(v_cube_result) == True:
							print(f'The volume of the cube is: {int(v_cube_result)}')
						else:
							print(f'The volume of the cube is: {v_cube_result}')
						break

					elif choice3 == 'v right r prism':
						clear()
						v_right_r_prism_l = float(input('Enter the length: '))
						clear()
						v_right_r_prism_w = float(input('Enter the width: '))
						clear()
						v_right_r_prism_h = float(input('Enter the height: '))
						clear()
						v_right_r_prism_result = v_right_r_prism_l*v_right_r_prism_w*v_right_r_prism_h
						if check_dot_zero(v_right_r_prism_result) == True:
							print(f'The volume of the right rectangular prism is: {int(v_right_r_prism_result)}')
						else:
							print(f'The volume of the right rectangular prism is: {v_right_r_prism_result}')
						break
					
					elif choice3 == 'v prism':
						clear()
						print('If the prism is a square prism, enter "s prism".')
						print('If the prism is a rectangular prism, enter "r prism".')
						print('If the prism is a triangular prism, enter "t prism".')
						print('If the prism is a pentagonal prism (5 sides), enter "p prism".')
						print('If the prism is a hexagonal prism (6 sides), enter "h prism".')
						print('If the prism is a heptagonal prism (7 sides), enter "hept prism".')
						print('If the prism is an octagonal prism (8 sides), enter "o prism".')
						print('If the prism is a trapezoidal prism, enter "trap prism".')
						sleep(1.5)
						choice4 = input('Enter your choice and press "Enter": ')
						if choice4 == 's prism':
							clear()
							v_s_prism_s = float(input('Enter the length of a side of the base: '))
							clear()
							v_s_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_s_prism_result = (v_s_prism_s**2)*v_s_prism_h
							if check_dot_zero(v_s_prism_result) == True:
								print(f'The volume of the square prism is: {int(v_s_prism_result)}')
							else:
								print(f'The volume of the square prism is: {v_s_prism_result}')

						elif choice4 == 'r prism':
							clear()
							v_r_prism_l = float(input('Enter the length: '))
							clear()
							v_r_prism_w = float(input('Enter the width: '))
							clear()
							v_r_prism_h = float(input('Enter the height: '))
							clear()
							v_r_prism_result = v_r_prism_l*v_r_prism_w*v_r_prism_h
							if check_dot_zero(v_r_prism_result) == True:
								print(f'The volume of the rectangular prism is: {int(v_r_prism_result)}')
							else:
								print(f'The volume of the rectangular prism is: {v_r_prism_result}')

						elif choice4 == 't prism':
							clear()
							v_t_prism_a = float(input('Enter one of the sides of the base: '))
							clear()
							v_t_prism_b = float(input('Enter one of the other sides of the base: '))
							clear()
							v_t_prism_c = float(input('Enter the remaining side of the base: '))
							clear()
							v_t_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_t_prism_result = ((1/4)*v_t_prism_h)*math.sqrt(-v_t_prism_a**4+(2*((v_t_prism_a*v_t_prism_b)**2)+2*((v_t_prism_a*v_t_prism_c)**2)-v_t_prism_b**4+2*((v_t_prism_b*v_t_prism_c)**2)-v_t_prism_c**4))
							if check_dot_zero(v_t_prism_result) == True:
								print(f'The volume of the triangular prism is: {int(v_t_prism_result)}')
							else:
								print(f'The volume of the triangular prism is: {v_t_prism_result}')

						elif choice4 == 'p prism':
							clear()
							v_p_prism_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_p_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_p_prism_result = ((1/4)*math.sqrt((5*(5+(2*(math.sqrt(5)))))))*((v_p_prism_a**2)*v_p_prism_h)
							if check_dot_zero(v_p_prism_result) == True:
								print(f'The volume of the pentagonal prism is: {int(v_p_prism_result)}')
							else:
								print(f'The volume of the pentagonal prism is: {v_p_prism_result}')

						elif choice4 == 'h prism':
							clear()
							v_h_prism_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_h_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_h_prism_result = (((3*math.sqrt(3))/2)*(v_h_prism_a**2))*v_h_prism_h
							if check_dot_zero(v_h_prism_result) == True:
								print(f'The volume of the hexagonal prism is: {int(v_h_prism_result)}')
							else:
								print(f'The volume of the hexagonal prism is: {v_h_prism_result}')

						elif choice4 == 'hept prism':
							clear()
							v_hept_prism_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_hept_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_hept_prism_result = ((7/4)*v_hept_prism_a**2)*mpmath.cot((math.radians(180)/7))*v_hept_prism_h
							if check_dot_zero(v_hept_prism_result) == True:
								print(f'The volume of the heptagonal prism is: {int(v_hept_prism_result)}')
							else:
								print(f'The volume of the heptagonal prism is: {v_hept_prism_result}')

						elif choice4 == 'o prism':
							clear()
							v_o_prism_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_o_prism_h = float(input('Enter the height of the prism: '))
							clear()
							v_o_prism_result = ((2*(1+math.sqrt(2)))*(v_o_prism_a**2))*v_o_prism_h
							if check_dot_zero(v_o_prism_result) == True:
								print(f'The volume of the octagonal prism is: {int(v_o_prism_result)}')
							else:
								print(f'The volume of the octagonal prism is: {v_o_prism_result}')
								
						elif choice4 == 'trap prism':
							clear()
							print('If the height is known, enter "trap h prism".')
							print('If the height isn\'t known, but the slant height is known, enter "trap s prism".')
							sleep(1.5)
							choice6 = input('Enter your choice and press "Enter": ')
							if choice6 == 'trap h prism':
								clear()
								v_trap_prism_l = float(input('Enter the height of the prism: '))
								clear()
								v_trap_prism_h = float(input('Enter the height of the base: '))
								clear()
								v_trap_prism_b1 = float(input('Enter the top width of the base: '))
								clear()
								v_trap_prism_b2 = float(input('Enter the bottom width of the base: '))
								clear()
								v_trap_prism_result = v_trap_prism_l*v_trap_prism_h*((v_trap_prism_b1+v_trap_prism_b2)/2)
								if check_dot_zero(v_trap_prism_result) == True:
									print(f'The volume of the trapezoidal prism is: {int(v_trap_prism_result)}')
								else:
									print(f'The volume of the trapezoidal prism is: {v_trap_prism_result}')

							elif choice6 == 'trap s prism':
								clear()
								v_trap_prism_s_l = float(input('Enter the height of the prism: '))
								clear()
								v_trap_prism_s_h = float(input('Enter the slant height: '))
								clear()
								v_trap_prism_s_b1 = float(input('Enter the top width of the base: '))
								clear()
								v_trap_prism_s_b2 = float(input('Enter the bottom width of the base: '))
								clear()
								v_trap_prism_s_result = v_trap_prism_s_l*(v_trap_prism_s_b1+v_trap_prism_s_b2)*math.sqrt((4*(v_trap_prism_s_h**2))+(2*(v_trap_prism_s_b1*v_trap_prism_s_b2))-math.sqrt(v_trap_prism_s_b1)-math.sqrt(v_trap_prism_s_b2))/4
								if check_dot_zero(v_trap_prism_s_result) == True:
									print(f'The volume of the trapezoidal prism is: {int(v_trap_prism_s_result)}')
								else:
									print(f'The volume of the trapezoidal prism is: {v_trap_prism_s_result}')

							else:
								while choice6 != 'trap h prism' and choice6 != 'trap s prism':
									clear()
									print("You didn't enter any of the options!")
									sleep(2)
									clear()
									print('If the height is known, enter "trap h prism".')
									print('If the height isn\'t known, but the slant height is known, enter "trap s prism".')
									sleep(1.5)
									choice6 = input('Enter your choice and press "Enter": ')
									if choice6 == 'trap h prism':
										clear()
										v_trap_prism_l = float(input('Enter the height of the prism: '))
										clear()
										v_trap_prism_h = float(input('Enter the height of the base: '))
										clear()
										v_trap_prism_b1 = float(input('Enter the top width of the base: '))
										clear()
										v_trap_prism_b2 = float(input('Enter the bottom width of the base: '))
										clear()
										v_trap_prism_result = v_trap_prism_l*v_trap_prism_h*((v_trap_prism_b1+v_trap_prism_b2)/2)
										if check_dot_zero(v_trap_prism_result) == True:
											print(f'The volume of the trapezoidal prism is: {int(v_trap_prism_result)}')
										else:
											print(f'The volume of the trapezoidal prism is: {v_trap_prism_result}')

									elif choice6 == 'trap s prism':
										clear()
										v_trap_prism_s_l = float(input('Enter the height of the prism: '))
										clear()
										v_trap_prism_s_h = float(input('Enter the slant height: '))
										clear()
										v_trap_prism_s_b1 = float(input('Enter the top width of the base: '))
										clear()
										v_trap_prism_s_b2 = float(input('Enter the bottom width of the base: '))
										clear()
										v_trap_prism_s_result = v_trap_prism_s_l*(v_trap_prism_s_b1+v_trap_prism_s_b2)*math.sqrt((4*(v_trap_prism_s_h**2))+(2*(v_trap_prism_s_b1*v_trap_prism_s_b2))-math.sqrt(v_trap_prism_s_b1)-math.sqrt(v_trap_prism_s_b2))/4
										if check_dot_zero(v_trap_prism_s_result) == True:
											print(f'The volume of the trapezoidal prism is: {int(v_trap_prism_s_result)}')
										else:
											print(f'The volume of the trapezoidal prism is: {v_trap_prism_s_result}')

						else:
							while choice4 != 's prism' and choice4 != 'r prism' and choice4 != 't prism' and choice4 != 'p prism' and choice4 != 'h prism' and choice4 != 'hept prism' and choice4 != 'o prism' and choice4 != 'trap prism':
								clear()
								print("You didn't enter any of the options!")
								sleep(2)
								clear()
								print('If the prism is a square prism, enter "s prism".')
								print('If the prism is a rectangular prism, enter "r prism".')
								print('If the prism is a triangular prism, enter "t prism".')
								print('If the prism is a pentagonal prism (5 sides), enter "p prism".')
								print('If the prism is a hexagonal prism (6 sides), enter "h prism".')
								print('If the prism is a heptagonal prism (7 sides), enter "hept prism".')
								print('If the prism is an octagonal prism (8 sides), enter "o prism".')
								sleep(1.5)
								choice4 = input('Enter your choice and press "Enter": ')
								if choice4 == 's prism':
									clear()
									v_s_prism_s = float(input('Enter the length of a side of the base: '))
									clear()
									v_s_prism_h = float(input('Enter the height of the prism: '))
									clear()
									v_s_prism_result = (v_s_prism_s**2)*v_s_prism_h
									if check_dot_zero(v_s_prism_result) == True:
										print(f'The volume of the square prism is: {int(v_s_prism_result)}')
									else:
										print(f'The volume of the square prism is: {v_s_prism_result}')
									break

								elif choice4 == 'r prism':
									clear()
									v_r_prism_l = float(input('Enter the length: '))
									clear()
									v_r_prism_w = float(input('Enter the width: '))
									clear()
									v_r_prism_h = float(input('Enter the height: '))
									clear()
									v_r_prism_result = v_r_prism_l*v_r_prism_w*v_r_prism_h
									if check_dot_zero(v_r_prism_result) == True:
										print(f'The volume of the rectangular prism is: {int(v_r_prism_result)}')
									else:
										print(f'The volume of the rectangular prism is: {v_r_prism_result}')
									break

								elif choice4 == 't prism':
									clear()
									v_t_prism_a = float(input('Enter one of the sides of the base: '))
									clear()
									v_t_prism_b = float(input('Enter one of the other sides of the base: '))
									clear()
									v_t_prism_c = float(input('Enter the remaining side of the base: '))
									clear()
									v_t_prism_h = float(input('Enter the height of the prism: '))
									clear()
									v_t_prism_result = ((1/4)*v_t_prism_h)*math.sqrt(-v_t_prism_a**4+(2*((v_t_prism_a*v_t_prism_b)**2)+2*((v_t_prism_a*v_t_prism_c)**2)-v_t_prism_b**4+2*((v_t_prism_b*v_t_prism_c)**2)-v_t_prism_c**4))
									if check_dot_zero(v_t_prism_result) == True:
										print(f'The volume of the triangular prism is: {int(v_t_prism_result)}')
									else:
										print(f'The volume of the triangular prism is: {v_t_prism_result}')
									break

								elif choice4 == 'p prism':
									clear()
									v_p_prism_a = float(input('Enter the length of one of the sides of the base: '))
									clear()
									v_p_prism_h = float(input('Enter the height of the prism: '))
									clear()
									v_p_prism_result = ((1/4)*math.sqrt((5*(5+(2*(math.sqrt(5)))))))*((v_p_prism_a**2)*v_p_prism_h)
									if check_dot_zero(v_p_prism_result) == True:
										print(f'The volume of the pentagonal prism is: {int(v_p_prism_result)}')
									else:
										print(f'The volume of the pentagonal prism is: {v_p_prism_result}')
									break

								elif choice4 == 'h prism':
									clear()
									v_h_prism_a = float(input('Enter the length of one of the sides of the base: '))
									clear()
									v_h_prism_h = float(input('Enter the height of the prism: '))
									clear()
									v_h_prism_result = (((3*math.sqrt(3))/2)*(v_h_prism_a**2))*v_h_prism_h
									if check_dot_zero(v_h_prism_result) == True:
										print(f'The volume of the hexagonal prism is: {int(v_h_prism_result)}')
									else:
										print(f'The volume of the hexagonal prism is: {v_h_prism_result}')
									break

								elif choice4 == 'hept prism':
									clear()
									v_hept_prism_a = float(input('Enter the length of one of the sides of the base: '))
									clear()
									v_hept_prism_h = float(input('Enter the height of the prism: '))
									clear()
									v_hept_prism_result = ((7/4)*v_hept_prism_a**2)*mpmath.cot((math.radians(180)/7))*v_hept_prism_h
									if check_dot_zero(v_hept_prism_result) == True:
										print(f'The volume of the heptagonal prism is: {int(v_hept_prism_result)}')
									else:
										print(f'The volume of the heptagonal prism is: {v_hept_prism_result}')
									break

								elif choice4 == 'o prism':
									clear()
									v_o_prism_a = float(input('Enter the length of one of the sides of the base: '))
									clear()
									v_o_prism_h = float(input('Enter the height of the prism: '))
									clear()
									v_o_prism_result = ((2*(1+math.sqrt(2)))*(v_o_prism_a**2))*v_o_prism_h
									if check_dot_zero(v_o_prism_result) == True:
										print(f'The volume of the octagonal prism is: {int(v_o_prism_result)}')
									else:
										print(f'The volume of the octagonal prism is: {v_o_prism_result}')
									break

								clear()
								print('If the height is known, enter "trap h prism".')
								print('If the height isn\'t known, but the slant height is known, enter "trap s prism".')
								sleep(1.5)
								choice6 = input('Enter your choice and press "Enter": ')
								if choice6 == 'trap h prism':
									clear()
									v_trap_prism_l = float(input('Enter the height of the prism: '))
									clear()
									v_trap_prism_h = float(input('Enter the height of the base: '))
									clear()
									v_trap_prism_b1 = float(input('Enter the top width of the base: '))
									clear()
									v_trap_prism_b2 = float(input('Enter the bottom width of the base: '))
									clear()
									v_trap_prism_result = v_trap_prism_l*v_trap_prism_h*((v_trap_prism_b1+v_trap_prism_b2)/2)
									if check_dot_zero(v_trap_prism_result) == True:
										print(f'The volume of the trapezoidal prism is: {int(v_trap_prism_result)}')
									else:
										print(f'The volume of the trapezoidal prism is: {v_trap_prism_result}')

								elif choice6 == 'trap s prism':
									clear()
									v_trap_prism_s_l = float(input('Enter the height of the prism: '))
									clear()
									v_trap_prism_s_h = float(input('Enter the slant height: '))
									clear()
									v_trap_prism_s_b1 = float(input('Enter the top width of the base: '))
									clear()
									v_trap_prism_s_b2 = float(input('Enter the bottom width of the base: '))
									clear()
									v_trap_prism_s_result = v_trap_prism_s_l*(v_trap_prism_s_b1+v_trap_prism_s_b2)*math.sqrt((4*(v_trap_prism_s_h**2))+(2*(v_trap_prism_s_b1*v_trap_prism_s_b2))-math.sqrt(v_trap_prism_s_b1)-math.sqrt(v_trap_prism_s_b2))/4
									if check_dot_zero(v_trap_prism_s_result) == True:
										print(f'The volume of the trapezoidal prism is: {int(v_trap_prism_s_result)}')
									else:
										print(f'The volume of the trapezoidal prism is: {v_trap_prism_s_result}')

								else:
									while choice6 != 'trap h prism' and choice6 != 'trap s prism':
										clear()
										print("You didn't enter any of the options!")
										sleep(2)
										clear()
										print('If the height is known, enter "trap h prism".')
										print('If the height isn\'t known, but the slant height is known, enter "trap s prism".')
										sleep(1.5)
										choice6 = input('Enter your choice and press "Enter": ')
										if choice6 == 'trap h prism':
											clear()
											v_trap_prism_l = float(input('Enter the height of the prism: '))
											clear()
											v_trap_prism_h = float(input('Enter the height of the base: '))
											clear()
											v_trap_prism_b1 = float(input('Enter the top width of the base: '))
											clear()
											v_trap_prism_b2 = float(input('Enter the bottom width of the base: '))
											clear()
											v_trap_prism_result = v_trap_prism_l*v_trap_prism_h*((v_trap_prism_b1+v_trap_prism_b2)/2)
											if check_dot_zero(v_trap_prism_result) == True:
												print(f'The volume of the trapezoidal prism is: {int(v_trap_prism_result)}')
											else:
												print(f'The volume of the trapezoidal prism is: {v_trap_prism_result}')
										elif choice6 == 'trap s prism':
											clear()
											v_trap_prism_s_l = float(input('Enter the height of the prism: '))
											clear()
											v_trap_prism_s_h = float(input('Enter the slant height: '))
											clear()
											v_trap_prism_s_b1 = float(input('Enter the top width of the base: '))
											clear()
											v_trap_prism_s_b2 = float(input('Enter the bottom width of the base: '))
											clear()
											v_trap_prism_s_result = v_trap_prism_s_l*(v_trap_prism_s_b1+v_trap_prism_s_b2)*math.sqrt((4*(v_trap_prism_s_h**2))+(2*(v_trap_prism_s_b1*v_trap_prism_s_b2))-math.sqrt(v_trap_prism_s_b1)-math.sqrt(v_trap_prism_s_b2))/4
											if check_dot_zero(v_trap_prism_s_result) == True:
												print(f'The volume of the trapezoidal prism is: {int(v_trap_prism_s_result)}')
											else:
												print(f'The volume of the trapezoidal prism is: {v_trap_prism_s_result}')
								break
						break

					elif choice3 == 'v pyramid':
						clear()
						print('If the pyramid is a tetrahedron (3 sides), enter "v tetra".')
						print('If the pyramid is a square pyramid (4 sides), enter "v square".')
						print('If the pyramid is a pentagonal pyramid (5 sides), enter "v penta".')
						print('If the pyramid is a hexagonal pyramid (6 sides), enter "v hexa".')
						print('If the pyramid is a heptagonal pyramid (7 sides), enter "v hepta".')
						print('If the pyramid is a octagonal pyramid (8 sides), enter "v octa".')
						sleep(1.5)
						choice5 = input('Enter your choice and press "Enter": ')
						if choice5 == 'v tetra':
							clear()
							v_tri_a = float(input('Enter the length of one of the edges of one of the sides: '))
							clear()
							v_tri_result = (v_tri_a**3)/(6*math.sqrt(2))
							if check_dot_zero(v_tri_result) == True:
								print(f'The volume of the triangular pyramid is: {int(v_tri_result)}')
							else:
								print(f'The volume of the triangular pyramid is: {v_tri_result}')

						elif choice5 == 'v square':
							clear()
							v_square_l = float(input('Enter the length: '))
							clear()
							v_square_w = float(input('Enter the width: '))
							clear()
							v_square_h = float(input('Enter the height: '))
							clear()
							v_square_result = (v_square_l*v_square_w*v_square_h)
							if check_dot_zero(v_square_result) == True:
								print(f'The volume of the pyramid is: {int(v_square_result)}')
							else:
								print(f'The volume of the pyramid is: {v_square_result}')

						elif choice5 == 'v penta':
							clear()
							v_penta_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_penta_h = float(input('Enter the height of the pyramid: '))
							clear()
							v_penta_result = ((5/12)*(math.tan(math.radians(54))))*(v_penta_h*(v_penta_a**2))
							if check_dot_zero(v_penta_result) == True:
								print(f'The volume of the pentagonal pyramid is: {int(v_penta_result)}')
							else:
								print(f'The volume of the pentagonal pyramid is: {v_penta_result}')

						elif choice5 == 'v hexa':
							clear()
							v_hexa_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_hexa_h = float(input('Enter the height of the pyramid: '))
							clear()
							v_hexa_result = (((math.sqrt(3))/2)*(v_hexa_a**2))*v_hexa_h
							if check_dot_zero(v_penta_result) == True:
								print(f'The volume of the hexagonal pyramid is: {int(v_penta_result)}')
							else:
								print(f'The volume of the hexagonal pyramid is: {v_penta_result}')

						elif choice5 == 'v hepta':
							clear()
							v_hepta_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_hepta_h = float(input('Enter the height of the pyramid: '))
							clear()
							v_hepta_result = (7/12)*v_hepta_h*(v_hepta_a**2)*(mpmath.cot(pi/7))
							if check_dot_zero(v_hepta_result) == True:
								print(f'The volume of the heptagonal pyramid is: {int(v_hepta_result)}')
							else:
								print(f'The volume of the heptagonal pyramid is: {v_hepta_result}')

						elif choice5 == 'v octa':
							clear()
							v_octa_a = float(input('Enter the length of one of the sides of the base: '))
							clear()
							v_octa_h = float(input('Enter the height of the pyramid: '))
							clear()
							v_octa_result = ((8/12)*v_octa_h*(v_octa_a**2))*mpmath.cot(pi/8)
							if check_dot_zero(v_octa_result) == True:
								print(f'The volume of the octagonal pyramid is: {int(v_octa_result)}')
							else:
								print(f'The volume of the octagonal pyramid is: {v_octa_result}')

						else:
							while choice5 != 'v tetra' and choice5 != 'v square' and choice5 != 'v penta' and choice5 != 'v hexa' and choice5 != 'v hepta' and choice5 != 'v octa':
								clear()
								print("You didn't enter any of the options!")
								sleep(2)
								clear()
								print('If the pyramid is a tetrahedron (3 sides), enter "v tetra".')
								print('If the pyramid is a square pyramid (4 sides), enter "v square".')
								print('If the pyramid is a pentagonal pyramid (5 sides), enter "v penta".')
								print('If the pyramid is a hexagonal pyramid (6 sides), enter "v hexa".')
								print('If the pyramid is a heptagonal pyramid (7 sides), enter "v hepta".')
								print('If the pyramid is a octagonal pyramid (8 sides), enter "v octa".')
								sleep(1.5)
								choice5 = input('Enter your choice and press "Enter": ')
								if choice5 == 'v tetra':
									clear()
									v_tri_a = float(input('Enter the length of one of the edges of one of the sides: '))
									clear()
									v_tri_result = (v_tri_a**3)/(6*math.sqrt(2))
									if check_dot_zero(v_tri_result) == True:
										print(f'The volume of the triangular pyramid is: {int(v_tri_result)}')
									else:
										print(f'The volume of the triangular pyramid is: {v_tri_result}')
									break

								elif choice5 == 'v square':
									clear()
									v_square_l = float(input('Enter the length: '))
									clear()
									v_square_w = float(input('Enter the width: '))
									clear()
									v_square_h = float(input('Enter the height: '))
									clear()
									v_square_result = (v_square_l*v_square_w*v_square_h)
									if check_dot_zero(v_square_result) == True:
										print(f'The volume of the pyramid is: {int(v_square_result)}')
									else:
										print(f'The volume of the pyramid is: {v_square_result}')
									break

								elif choice5 == 'v penta':
									clear()
									v_penta_a = float(input('Enter the length of one of the sides of the base: '))
									clear()
									v_penta_h = float(input('Enter the height of the pyramid: '))
									clear()
									v_penta_result = ((5/12)*(math.tan(math.radians(54))))*(v_penta_h*(v_penta_a**2))
									if check_dot_zero(v_penta_result) == True:
										print(f'The volume of the pentagonal pyramid is: {int(v_penta_result)}')
									else:
										print(f'The volume of the pentagonal pyramid is: {v_penta_result}')
									break

								elif choice5 == 'v hexa':
									clear()
									v_hexa_a = float(input('Enter the length of one of the sides of the base: '))
									clear()
									v_hexa_h = float(input('Enter the height of the pyramid: '))
									clear()
									v_hexa_result = (((math.sqrt(3))/2)*(v_hexa_a**2))*v_hexa_h
									if check_dot_zero(v_penta_result) == True:
										print(f'The volume of the hexagonal pyramid is: {int(v_penta_result)}')
									else:
										print(f'The volume of the hexagonal pyramid is: {v_penta_result}')
									break

								elif choice5 == 'v hepta':
									clear()
									v_hepta_a = float(input('Enter the length of one of the sides of the base: '))
									clear()
									v_hepta_h = float(input('Enter the height of the pyramid: '))
									clear()
									v_hepta_result = (7/12)*v_hepta_h*(v_hepta_a**2)*(mpmath.cot(pi/7))
									if check_dot_zero(v_hepta_result) == True:
										print(f'The volume of the heptagonal pyramid is: {int(v_hepta_result)}')
									else:
										print(f'The volume of the heptagonal pyramid is: {v_hepta_result}')
									break

								elif choice5 == 'v octa':
									clear()
									v_octa_a = float(input('Enter the length of one of the sides of the base: '))
									clear()
									v_octa_h = float(input('Enter the height of the pyramid: '))
									clear()
									v_octa_result = ((8/12)*v_octa_h*(v_octa_a**2))*mpmath.cot(pi/8)
									if check_dot_zero(v_octa_result) == True:
										print(f'The volume of the octagonal pyramid is: {int(v_octa_result)}')
									else:
										print(f'The volume of the octagonal pyramid is: {v_octa_result}')
									break
						break             

					elif choice3 == 'v cone':
						clear()
						v_cone_r = float(input('Enter the radius of the base: '))
						clear()
						v_cone_h = float(input('Enter the height of the cone: '))
						clear()
						v_cone_result = (pi*(v_cone_r**2))*(v_cone_h/3)
						if check_dot_zero(v_cone_result) == True:
							print(f'The volume of the cone is: {int(v_cone_result)}')
						else:
							print(f'The volume of the cone is: {v_cone_result}')
						break

					elif choice3 == 'v cylinder':
						clear()
						v_cylinder_r = float(input('Enter the radius of the base: '))
						clear()
						v_cylinder_h = float(input('Enter the height of the cylinder: '))
						clear()
						v_cylinder_result = (pi*(v_cylinder_r**2))*v_cylinder_h
						if check_dot_zero(v_cylinder_result) == True:
							print(f'The volume of the cylinder is: {int(v_cylinder_result)}')
						else:
							print(f'The volume of the cylinder is: {v_cylinder_result}')
						break
					
					elif choice3 == 'v sphere':
						clear()
						v_sphere_r = float(input('Enter the radius: '))
						clear()
						v_sphere_result = (4/3)*(pi*(v_sphere_r**3))
						if check_dot_zero(v_sphere_result) == True:
							print(f'The volume of the sphere is: {int(v_sphere_result)}')
						else:
							print(f'The volume of the sphere is: {v_sphere_result}')
			break