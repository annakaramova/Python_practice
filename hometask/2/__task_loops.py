# 1. Fill the missing pieces
# Fill the ____ parts in the code below.

words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']
upper_case_words = []

for i in words:
    if i.isupper():
        upper_case_words.append(i)
assert upper_case_words == ['PYTHON', 'JOHN', 'DOE']

# 2. Calculate the sum of dict values
# Calculate the sum of the values in magic_dict by taking only into account numeric values (hint: see isinstance).

magic_dict = dict(val1=44, val2='secret value', val3=55.0, val4=1)
# Your implementation:
sum_of_values = 0

for i in magic_dict.values():
    if not isinstance(i, str):
        sum_of_values += i
assert sum_of_values == 100

# 3. Create a list of strings based on a list of numbers
# The rules:

# If the number is a multiple of five and odd, the string should be 'five odd'
# If the number is a multiple of five and even, the string should be 'five even'
# If the number is odd, the string is 'odd'
# If the number is even, the string is 'even'

numbers = [1, 3, 4, 6, 81, 80, 100, 95]
# Your implementation:

my_list = []

for nums in numbers:
    if nums % 5 == 0 and nums % 2 != 0:
        my_list.append('five odd')
    elif nums % 5 == 0 and nums % 2 == 0:
        my_list.append('five even')
    elif nums % 2 != 0:
        my_list.append('odd')
    elif nums % 2 == 0:
        my_list.append('even')
assert my_list == ['odd', 'odd', 'even', 'even', 'odd', 'five even', 'five even', 'five odd']