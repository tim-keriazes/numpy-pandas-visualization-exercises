import numpy as np
a = np.array([4,10,12,23,-2,-1,0,0,0,-6,3,-7])



# Exercises
# a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?
#utilize boolean masking

a< 0
a_mask = a < 0 #storing that boolean as a_mask

a[a_mask]

len(a[a <0])
#4


# How many positive numbers are there?
len(a[a>0])
#5

# How many even positive numbers are there?

# If you were to add 3 to each data point, how many positive numbers would there be?

# If you squared each number, what would the new mean and standard deviation be?

# A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.

# Calculate the z-score for each data point. Recall that the z-score is given by:

# Z
# =
# x
# −
# μ
# σ
# Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.

# Awesome Bonus For much more practice with numpy, Go to https://github.com/rougier/numpy-100 and clone the repo down to your laptop. To clone a repository: - Copy the SSH address of the repository - cd ~/codeup-data-science - Then type git clone git@github.com:rougier/numpy-100.git - Now do cd numpy-100 on your terminal. - Type git remote remove origin, so you won't accidentally try to push your work to Rougier's repo.

# Congratulations! You have cloned Rougier's 100 numpy exercises to your computer. Now you need to make a new, blank, repository on GitHub.

# Go to https://github.com/new to make a new repo. Name it numpy-100.
# DO NOT check any check boxes. We need a blank, empty repo.
# Finally, follow the directions to "push an existing repository from the command line" so that you can push up your changes to your own account.
# Now do work, add it, commit it, and push it!
