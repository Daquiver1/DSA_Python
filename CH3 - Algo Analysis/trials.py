
# A data structure is a systematic way or organizing and accessing data.
# An algorithmis a step-by-step procedure to perform a task in finite time.
from time import time
start_time = time()
# do something
end_time = time()
elapsed = end_time - start_time

# You can use the magic method(notebookss) to run a code 1000s of time and
# measure the average run time.

# Asymptotic notations are the mathematical notations
# used to describe the runing
# time of an algorithm

# Floor function is the largest integer less than or equal to x
# Ceiling function is the smallest integer greater than or equal to x

# Big oh - worst case, longest time,growth rate is less than value
# big omega - best case, shortest time, growth rate is greater than value
# big theta - average case, growth rate is equal to value

# In python when using len on list, it doesn't iterate to count the values
# rather, len is already stored so it just calls the function.

# Built in sort has a worst case of O(nlogn)

# Justification is when you want to show that your algorithm is extremely fast
# or accurate. You justify it by proving with mathematical language.
# Contradiction (de morgan)
# Contrapositive (negative mirror, use opposite to show it's true,
# bit of de morgan)
# Counterexample (show one is false for generalization)
# Induction
