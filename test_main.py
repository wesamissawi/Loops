import main


# Task #1
def test_get_range():
	assert main.get_reange(1, 10) == '1 2 3 4 5 6 7 8 9 10'
	assert main.get_reange(-3, 14) == '-3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14'
	assert main.get_reange(0 , 0) == '0'
	assert main.get_range(5, 8) == '5 6 7 8'
	assert main.get_reange(3, 9) == '3 4 5 6 7 8 9'


# Task #2
def test_get_range_by_3()
	assert main.get_range_by_3(1, 10) == '1 4 7 10'
	assert main.get_range_by_3(-3, 14) == '-3 0 3 6 9 12'
	assert main.get_range_by_3(0, 0) == '0'
	assert main.get_range_by_3(5, 8) == '5 8'
	assert main.get_range_by_3(3, 9) == '3 6 9'



# Task #3
def test_get_sequence():
	assert main.get_sequence(8, 5) == '8 7 6 5'
	assert main.get_sequence(1, 10) == '1 2 3 4 5 6 7 8 9 10'
	assert main.get_sequence(179, 179) == '179'
	assert main.get_sequence(14, 7) == '-14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7'
	assert main.get_sequence(12, -5) == '12 11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5'




# Task #4

def test_cubed_series():
	assert main.cubed_series(20) == 44100
	assert main.cubed_series(10) == 3025
	assert main.cubed_series(9) == 2025
	assert main.cubed_series(8) == 1296
	assert main.cubed_series(7) == 784
	assert main.cubed_series(6) == 441
	assert main.cubed_series(5) == 225
	assert main.cubed_series(4) == 100
	assert main.cubed_series(3) == 36
	assert main.cubed_series(2) == 9
	assert main.cubed_series(1) == 1


# Task #5

def test_factorial():
	assert main.factorial(4) == 24
	assert main.factorial(1) == 1
	assert main.factorial(2) == 2
	assert main.factorial(3) == 6
	assert main.factorial(6) == 720
	assert main.factorial(10) == 3628800


# Task #6

def test_factorial_series():
	assert main.factorial_series(4) == 33
	assert main.factorial_series(5) == 153
	assert main.factorial_series(10) == 4037913 
	assert main.factorial_series(1) == 1
	assert main.factorial_series(2) == 3
	assert main.factorial_series(3) == 9



# Task #7

def test_add_underscore():
	assert main.add_underscore("Wesam Issawi") == "W_e_s_a_m_ _I_s_s_a_w_i_"
	assert main.add_underscore("Monkey") == 'M_o_n_k_e_y_'
	assert main.add_underscore("Hyphen") == 'Hyphen_'


# Task #8

def test_number_growth():
	assert main.number_growth(3) == '1 12 123'
	assert main.number_growth(4) == '1 12 123 1234'
	assert main.number_growth(7) == '1 12 123 1234 12345 123456 1234567'
	assert main.number_growth(7) == '1 12 123 1234 12345 123456 1234567 12345678 123456789'
	assert main.number_growth(1) == '1'

# Task #9

def test_star_growth():
	asset main.star_growth(3) == '* ** ***'
	asset main.star_growth(4) == '* ** *** ****'
	asset main.star_growth(1) == '*'
	asset main.star_growth(7) == '* ** *** **** ***** ****** *******'
	asset main.star_growth(9) == '* ** *** **** ***** ****** ******* ******** *********'



# Task #10

def test_number_increase_step():
	assert main.number_increase_step(5) == "1 23 45"
	assert main.number_increase_step(9) == "1 23 456 789"
	assert main.number_increase_step(3) == "1 23"
	assert main.number_increase_step(4) == "1 23 4"
	assert main.number_increase_step(7) == "1 23 456 7"


# Task #11

def test_spell_pyramid():
	assert main.spell_pyramid("Wesam") == 'W We Wes Wesa Wesam'
	assert main.spell_pyramid("Issawi") == 'I Is Iss Issa Issaw Issawi'
	assert main.spell_pyramid("Monkey") == 'M Mo Mon Monk Monke Monkey'
	assert main.spell_pyramid("Backwards") == 'B Ba Bac Back Backw Backwa Backwar Backward Backwards'



# Task #12

def test_reverse_spell_pyramid():
	assert main.reverse_spell_pyramid("Wesam") == 'm ma mas mase maseW'
	assert main.reverse_spell_pyramid("Issawi") == "i iw iwa iwas iwass iwassI'
	assert main.reverse_spell_pyramid('Monkey') == 'y ye yek yekn yekno yeknoM'
	assert main.reverse_spell_pyramid('Backwards') == 's sd sdr sdra sdraw sdrawk sdrawkc sdrawkca sdrawkcaB'



# Task #13

def test_star_match_growth():
	assert main.star_match_growth('Wesam Issawi', 's') == 'Wes*am Is**s***awi'
	assert main.star_match_growth('Indicative', 'i') == 'I*ndi**cati***ve'
	assert main.star_match_growth("Lollipop", 'L') == 'L*ol**l***ipop'
	assert main.star_match_growth("gGgGgG", "g") == 'g*G**g***G****g*****G******'
	assert main.star_match_growth("*", "*") == "**"
	assert main.star_match_growth("**", "*") == "*****"
	assert main.star_match_growth("***", "*") == "*********"
	assert main.star_match_growth("Hello There", "i") == 'Hello There'
