

# Task # 1

Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.


#### Example function call
```python
>>> get_range(1, 10)
'1 2 3 4 5 6 7 8 9 10'
```




****
****
****
****
****
****
# Task #2

Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively skip by 3

#### Example function call
```python
>>> get_range_by3(1, 10)
'1 4 7 10'
>>> get_range_by3(6, 7)
6
```





****
****
****
****
****
****
# Task #3


Given two integers A and B. Print all numbers from A to B inclusively, in increasing order, if A < B, or in decreasing order, if A ≥ B.

#### Example function call
```python
get_sequence(8, 5)
'8 7 6 5'
get_sequence(5,8)
'5 6 7 8'
```




****
****
****
****
****
****
# Task # 4

For the given integer N calculate the following sum:

1³ + 2³ + ... + N³


#### Example function call
``` python
>>> cubed_series(5)    	# 1³ + 2³ + 3³ + 4³+ 5³
225
>>> cubed_series(4)			# 1³ + 2³ + 3³ + 4³
100
>>> cubed_series(3)			# 1³ + 2³ + 3³
36
>>> cubed_series(2)			# 1³ + 2³
9
>>> cubed_series(1)			# 1³ 
1		
```






****
****
****
****
****
****
# Task # 5



In mathematics, the factorial of an integer n, denoted by n! is the following product:

n! = 1 × 2 × … × n

For the given integer n calculate the value n!. Don't use math module in this exercise.

```python
>>> factorial(4)
24
>>> factorial(1)
1
>>> factorial(5)
120
>>> factorial(2)
2

```



****
****
****
****
****
****
# Task # 6 



In mathematics, the factorial of an integer n, denoted by n! is the following product:

n! = 1 × 2 × … × n

For the given integer n calculate the value 

1! + 2! + 3! + ... + n!

Try to discover the solution that uses only one for-loop. And don't use math module in this exercise.

Try using the factorial function from a previous exercise.

#### Example function call
```python
>>> factorial_series(2) 		# 1! + 2!      <-(1)  + (2 * 1)
3
>>> factorial_series(2) 		# 1! + 2! +3!  <-(1)  + (2 * 1) + (3 * 2 * 1)
9
>>> factorial_series(4)     # 1! + 2! + 3! + 4!
33
>>> factorial_series(5)     # 1! + 2! + 3! + 4! + 5!
153


```




****
****
****
****
****
****
# Task # 7

Given a string, s, return the same string with underscores between each letter

#### Example function call:

```python
>>> add_underscore("Wesam Issawi") 
"W_e_s_a_m_ _I_s_s_a_w_i_"
>>>add_underscore("Monkey")
'M_o_n_k_e_y_'
```








****
****
****
****
****
****
# Task # 8

For given integer n ≤ 9 return a string conisting of  numbers sequences increasing by one.

A few example sample function calls will illustrate better.

#### Example function calls
```python
>>> number_growth(3) 
'1 12 123'
>>> number_growth(5)
'1 12 123 1234 12345'
```





****
****
****
****
****
****
# Task # 9


For given integer n ≤ 9 print a ladder of n steps. The k-th step consists of the k asterisks  without spaces between them.

A few example sample function calls will illustrate better.

#### Example function calls
```python
>>> star_growth(3)
'* ** ***'
>>> star_growth(5)
'* ** *** **** *****'

```





****
****
****
****
****
****
# Task # 10


For given integer n ≤ 9 return a "ladder" of n steps. Each character in the steps represent an increasing number.


A few example sample function calls will illustrate better.

#### Example function calls
```python
>>> number_increase_step(5) 
'1 23 45'
>>> number_increase_step(3)
"1 23"
>>> number_increase_step(9)
"1 23 456 789"
>>> number_increase_step(4)
'1 23 4'
>>> number_increase_step(7)
"1 23 456 7"
```







****
****
****
****
****
****
# Task # 11


For a given string, s, create a program that will return the first letter the frist and second, then first to thrid, etc. until it reaches the end of the word. Seperate each substring with a space.


#### Sample Fuction Call:
```python
>>> spell_pyramid("Wesam")
'W We Wes Wesa Wesam'
>>> spell_pyramid("Issawi") 
'I Is Iss Issa Issaw Issawi'
```





****
****
****
****
****
****
# Task # 12

For a given string, s, create a program that will return a string consisting of last character of s then the last and second last characters, etc. until it reaches the begining of the word. Seperate Each substrings with a space.

This is better illustrate in an example

Sample Funciton Call:
```python
>>> reverse_spell_pyramid("Wesam")
'm ma mas mase maseW'
>>> reverse_spell_pyramid("Issawi")
'i iw iwa iwas iwass iwassI'
```





****
****
****
****
****
****
# Task # 13

For a given string, s and a character as input, create a function that will print each character of s, but When the character input appears in the string add an asterisk beside the matching character. Each time the letter appears add an extra asterisk



This is better illustrate in an example

#### Sample Function Call
```python
>>> star_match_growth("Wesam Issawi", 's')
'Wes*am Is**s***awi'

# Explanation: The first time 's' occurs only one asterist
#							The second time, two asterisks
# etc

>>> star_match_growth("Indicative", 'i')
'I*ndi**cati***ve'


# Note how 'i' mathces capital 'I' and small 'i'
```
