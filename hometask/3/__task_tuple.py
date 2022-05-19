# Write a Python program calculate the product, multiplying all the numbers of a given tuple.
# Original Tuple:

nums = (4, 3, 2, 2, -1, 18)

count = 1
for i in nums:
    count *= i

result = count

#Product - multiplying all the numbers of the said tuple: -864
assert result == -864

# Write a Python program to convert a tuple of string values to a tuple of integer values.
# Original tuple values:
nums = (('333', '33'), ('1416', '55'))

result = tuple((int(x[0]), int(x[1])) for x in nums)


assert result == ((333, 33), (1416, 55))

# Write a Python program to convert a given tuple of positive integers into an integer.
# Original tuple:
original = (1, 2, 3)


original_new = original[0] * 100 + original[1] * 10 + original[2]


result = original_new

assert result == 123

original = (10, 20, 40, 5, 70)

num = int(''.join(map(str, original)))


result = num
assert result == 102040570