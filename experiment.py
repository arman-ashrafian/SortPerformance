# Arman Ashrafian
# CS 1D Extra Credit Assignment

import random
import time
from sort import *

SIZE_1 = 5000
SIZE_2 = 10000
SIZE_3 = 50000

def output_already_ordered():
	# create ordered lists
	already_ordered_1 = [x for x in range(0,SIZE_1)]
	already_ordered_2 = [x for x in range(0,SIZE_2)]
	already_ordered_3 = [x for x in range(0,SIZE_3)]

	print("Already Ordered")
	print("%-20s %-20s %-20s %-20s" % ("SIZE(N)", "FIRST PIVOT", "RANDOM PIVOT", "MIDDLE PIVOT"))

	a_f = quick_sort(list(already_ordered_1), 0, SIZE_1 - 1, partition1)
	a_m = quick_sort(list(already_ordered_1), 0, SIZE_1 - 1, partition2)
	a_r = quick_sort(list(already_ordered_1), 0, SIZE_1 - 1, partition3)

	b_f = quick_sort(already_ordered_2, 0, SIZE_2 - 1, partition1)
	b_m = quick_sort(already_ordered_2, 0, SIZE_2 - 1, partition2)
	b_r = quick_sort(already_ordered_2, 0, SIZE_2 - 1, partition3)

	c_f = quick_sort(already_ordered_3, 0, SIZE_3 - 1, partition1)
	c_m = quick_sort(already_ordered_3, 0, SIZE_3 - 1, partition2)
	c_r = quick_sort(already_ordered_3, 0, SIZE_3 - 1, partition3)

	print("%-20d %-20d %-20s %-20s" % (SIZE_1, a_f, a_r, a_m))
	print("%-20d %-20d %-20s %-20s" % (SIZE_2, b_f, b_r, b_m))
	print("%-20d %-20d %-20s %-20s" % (SIZE_3, c_f, c_r, c_m))

	print(already_ordered_1[0:5])

def output_reverse_ordered():
	# create reverse ordered lists
	reverse_ordered_1 = [x for x in range(SIZE_1 - 1, -1, -1)]
	reverse_ordered_2 = [x for x in range(SIZE_2 - 1, -1, -1)]
	reverse_ordered_3 = [x for x in range(SIZE_3 - 1, -1, -1)]

	print("Reverse Ordered")
	print("%-20s %-20s %-20s %-20s" % ("SIZE(N)", "FIRST PIVOT", "RANDOM PIVOT", "MIDDLE PIVOT"))

	a_f = quick_sort(list(reverse_ordered_1), 0, SIZE_1 - 1, partition1)
	a_m = quick_sort(list(reverse_ordered_1), 0, SIZE_1 - 1, partition2)
	a_r = quick_sort(list(reverse_ordered_1), 0, SIZE_1 - 1, partition3)

	b_f = quick_sort(list(reverse_ordered_2), 0, SIZE_2 - 1, partition1)
	b_m = quick_sort(list(reverse_ordered_2), 0, SIZE_2 - 1, partition2)
	b_r = quick_sort(list(reverse_ordered_2), 0, SIZE_2 - 1, partition3)

	c_f = quick_sort(list(reverse_ordered_3), 0, SIZE_3 - 1, partition1)
	c_m = quick_sort(list(reverse_ordered_3), 0, SIZE_3 - 1, partition2)
	c_r = quick_sort(list(reverse_ordered_3), 0, SIZE_3 - 1, partition3)

	print("%-20d %-20d %-20s %-20s" % (SIZE_1, a_f, a_r, a_m))
	print("%-20d %-20d %-20s %-20s" % (SIZE_2, b_f, b_r, b_m))
	print("%-20d %-20d %-20s %-20s" % (SIZE_3, c_f, c_r, c_m))

	print(reverse_ordered_1[0:5])

def output_random_ordered():
	random.seed(time.time())
	already_ordered = [x for x in range(0,SIZE_3)]

	# create random ordered list
	random_ordered_1 = random.sample(already_ordered, SIZE_1)
	random_ordered_2 = random.sample(already_ordered, SIZE_2)
	random_ordered_3 = random.sample(already_ordered, SIZE_3)

	print("Random Ordered")
	print("%-20s %-20s %-20s %-20s" % ("SIZE(N)", "FIRST PIVOT", "RANDOM PIVOT", "MIDDLE PIVOT"))

	a_f = quick_sort(list(random_ordered_1), 0, SIZE_1 - 1, partition1)
	a_m = quick_sort(list(random_ordered_1), 0, SIZE_1 - 1, partition2)
	a_r = quick_sort(random_ordered_1, 0, SIZE_1 - 1, partition3)

	b_f = quick_sort(list(random_ordered_2), 0, SIZE_2 - 1, partition1)
	b_m = quick_sort(list(random_ordered_2), 0, SIZE_2 - 1, partition2)
	b_r = quick_sort(list(random_ordered_2), 0, SIZE_2 - 1, partition3)

	c_f = quick_sort(random_ordered_3, 0, SIZE_3 - 1, partition1)
	c_m = quick_sort(random_ordered_3, 0, SIZE_3 - 1, partition2)
	c_r = quick_sort(random_ordered_3, 0, SIZE_3 - 1, partition3)

	print("%-20d %-20d %-20s %-20s" % (SIZE_1, a_f, a_r, a_m))
	print("%-20d %-20d %-20s %-20s" % (SIZE_2, b_f, b_r, b_m))
	print("%-20d %-20d %-20s %-20s" % (SIZE_3, c_f, c_r, c_m))

	print(random_ordered_1[0:5])


def main():
	output_already_ordered()
	print()
	print()
	output_reverse_ordered()
	print()
	print()
	output_random_ordered()

main()