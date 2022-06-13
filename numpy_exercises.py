import numpy as np
a = np.array([4,10,12,23,-2,-1,0,0,0,-6,3,-7])



# Exercises
# a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?
#utilize boolean masking

a< 0
a_mask = a < 0 #storing that boolean as a_mask

a[a_mask]

len(a[a < 0])
#4


# How many positive numbers are there?

len(a[a > 0])
#5

# How many even positive numbers are there?

pos_even = a[(a>0) & (a%2==0)] #assigne pos even to variable, check length
len(pos_even)
#3


# If you were to add 3 to each data point, how many positive numbers would there be?
#(a+3)>0 finds boolean of array, function np.sum counts the true
np.sum((a+3)>0)
#10

# If you squared each number, what would the new mean and standard deviation be?
#np.mean and np.std of the **2 operator
np.mean(a**2)
np.std(a**2)

# A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.
center_value=np.mean(a)
a-center_value
#array([  1.,   7.,   9.,  20.,  -5.,  -4.,  -3.,  -3.,  -3.,  -9.,   0., -10.])

# Calculate the z-score for each data point. Recall that the z-score is given by:
#zscore= (a-np.mean(a))/np.std(a)

(a-np.mean(a))/np.std(a)

#array([ 0.12403473,  0.86824314,  1.11631261,  2.48069469, -0.62017367,
 #      -0.49613894, -0.3721042 , -0.3721042 , -0.3721042 , -1.11631261,
  #      0.        , -1.24034735])

import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
#Assigning the proper value to each variable using the base python library
sum_of_a = sum(a)
print('Sum of a: {}'.format(sum_of_a))

#Sum of a: 55

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a)
print('Min of a: {}'.format(min_of_a))
#Min of a: 1


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print('Max of a: {}'.format(max_of_a))
#Max of a: 10


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum_of_a / len(a)
print('Mean of a: {}'.format(mean_of_a))
#Mean of a: 5.5


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1
for num in a:
    product_of_a *= num

print('Product of a: {}'.format(product_of_a))

#Product of a: 3628800

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [num ** 2 for num in a]
print('Squares of a: {}'.format(squares_of_a))
#Squares of a: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [num for num in a if num % 2 == 1]
print('Odds in a: {}'.format(odds_in_a))
#Odds in a: [1, 3, 5, 7, 9]


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = [num for num in a if num % 2 == 0]
print('Evens in a: {}'.format(evens_in_a))

#Evens in a: [2, 4, 6, 8, 10]
 
## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = np.sum(b)
print('Sum of b: {}.'.format(sum_of_b))
#Sum of b: 33.



# Exercise 2 - refactor the following to use numpy. 
min_of_b = np.min(b)
print('Min of b: {}.'.format(min_of_b)
#Min of b: 3.


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = np.max(b)
print('Max of b: {}.'.format(max_of_b))
#Max of b: 8.


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = np.mean(b)
print('Mean of b: {}.'.format(mean_of_b))
#Mean of b: 5.5.

      
# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = np.product(b)
print('Product of b: {}.'.format(product_of_b))
#Product of b: 20160.

      
# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = np.square(b)
print('Squares of b:\n{}.'.format(squares_of_b))
# Squares of b:[[ 9 16 25] [36 49 64]].



# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = b[b % 2 == 1]
print('Odds in b: {}.'.format(odds_in_b))
#Odds in b: [3 5 7].



# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = b[b % 2 == 0]
print('Evens in b: {}.'.format(evens_in_b))
#Evens in b: [4 6 8].
   

# Exercise 9 - print out the shape of the array b.
print('Shape of b: {}.'.format(b.shape))
#Shape of b: (2, 3).

      
# Exercise 10 - transpose the array b.
print('b transposed:\n{}.'.format(b.transpose()))
# b transposed:
# [[3 6]
#  [4 7]
#  [5 8]].

      
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
print('b reshaped to (1, 6): {}.'.format(b.reshape((1, 6))))
# b reshaped to (1, 6): [[3 4 5 6 7 8]].

      
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
print('b reshaped to (6, 1):\n{}.'.format(b.reshape((6, 1))))
# b reshaped to (6, 1):
# [[3]
#  [4]
#  [5]
#  [6]
#  [7]
#  [8]].         
      
## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
##Determing the min, max, sum, and product of c
c.min()
#1
c.max()
#9
c.sum()
#45
c.prod()
#362880



# Exercise 2 - Determine the standard deviation of c.
print('Standard deviation of c: {}.'.format(c.std()))
# Standard deviation of c: 2.581988897471611.
      
# Exercise 3 - Determine the variance of c.
print('Variance of c: {}.'.format(c.var()))


# Variance of c: 6.666666666666667.
      
# Exercise 4 - Print out the shape of the array c
print('Shape of c: {}.'.format(c.shape))
# Shape of c: (3, 3).

      
# Exercise 5 - Transpose c and print out transposed result.
print('c transposed:\n{}.'.format(c.transpose()))
# c transposed:
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]].

      
# Exercise 6 - Get the dot product of the array c with c. 
print('Dot product of c with c:\n{}.'.format(np.dot(c, c)))
# Dot product of c with c:
# [[ 30  36  42]
#  [ 66  81  96]
#  [102 126 150]].

      
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
print('Sum of c times c transposed: {}.'.format(np.sum(c * c.transpose())))
#Sum of c times c transposed: 261.
      
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

print('Product of c times c transposed: {}.'.format(np.product(c * c.transpose())))
#Product of c times c transposed: 131681894400.
      
## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d
print('Sin values of d:\n{}.\n\n'.format(np.sin(d)))

# Sin values of d:
# [[ 0.89399666 -0.98803162  0.85090352  0.          0.58061118 -0.80115264]
#  [ 0.85090352 -0.89399666  0.98803162 -0.17604595  0.89399666  0.        ]
#  [-0.30481062  0.85090352 -0.85090352  0.89399666 -0.85090352 -0.80115264]].
      
# Exercise 2 - Find the cosine of all the numbers in d
print('Cos values of d:\n{}.\n\n'.format(np.cos(d)))

# Cos values of d:
# [[-0.44807362  0.15425145  0.52532199  1.          0.81418097 -0.59846007]
#  [ 0.52532199 -0.44807362  0.15425145  0.98438195 -0.44807362  1.        ]
#  [-0.95241298  0.52532199  0.52532199 -0.44807362  0.52532199 -0.59846007]].
      
# Exercise 3 - Find the tangent of all the numbers in d
print('Tan values of d:\n{}.\n\n'.format(np.tan(d)))

# Tan values of d:
# [[-1.99520041 -6.4053312   1.61977519  0.          0.71312301  1.33869021]
#  [ 1.61977519  1.99520041  6.4053312  -0.17883906 -1.99520041  0.        ]
#  [ 0.32004039  1.61977519 -1.61977519 -1.99520041 -1.61977519  1.33869021]].
      
# Exercise 4 - Find all the negative numbers in d
print('Negative numbers in d: {}.\n'.format(d[d < 0]))

# Negative numbers in d: [-90 -30 -45 -45].
      
# Exercise 5 - Find all the positive numbers in d
print('Positive numbers in d: {}.\n'.format(d[d > 0]))
# Positive numbers in d: [ 90  30  45 120 180  45 270  90  60  45  90 180].

      
# Exercise 6 - Return an array of only the unique numbers in d.
print('Unique numbers in d: {}.\n'.format(np.unique(d)))
# Unique numbers in d: [-90 -45 -30   0  30  45  60  90 120 180 270].

      
# Exercise 7 - Determine how many unique numbers there are in d.
print('Shape of d: {}.\n'.format(np.shape(d)))
# Shape of d: (3, 6)

# Exercise 8 - Print out the shape of d.
print('d transposed:\n{}.\n'.format(np.transpose(d)))
# Shape of d: (3, 6).

      
# Exercise 9 - Transpose and then print out the shape of d.
print('d transposed:\n{}.\n'.format(np.transpose(d)))
 # d transposed:
# [[ 90  45  60]
#  [ 30 -90  45]
#  [ 45 -30 -45]
#  [  0 270  90]
#  [120  90 -45]
#  [180   0 180]].

      
# Exercise 10 - Reshape d into an array of 9 x 2
      
print('d reshaped to (9, 2):\n{}.'.format(np.reshape(d, (9, 2))))
 d reshaped to (9, 2):
# [[ 90  30]
#  [ 45   0]
#  [120 180]
#  [ 45 -90]
#  [-30 270]
#  [ 90   0]
#  [ 60  45]
#  [-45  90]
#  [-45 180]].     
      
# Awesome Bonus For much more practice with numpy, Go to https://github.com/rougier/numpy-100 and clone the repo down to your laptop. To clone a repository: - Copy the SSH address of the repository - cd ~/codeup-data-science - Then type git clone git@github.com:rougier/numpy-100.git - Now do cd numpy-100 on your terminal. - Type git remote remove origin, so you won't accidentally try to push your work to Rougier's repo.

# Congratulations! You have cloned Rougier's 100 numpy exercises to your computer. Now you need to make a new, blank, repository on GitHub.

# Go to https://github.com/new to make a new repo. Name it numpy-100.
# DO NOT check any check boxes. We need a blank, empty repo.
# Finally, follow the directions to "push an existing repository from the command line" so that you can push up your changes to your own account.
# Now do work, add it, commit it, and push it!
