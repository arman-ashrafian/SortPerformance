# Arman Ashrafian
# CS 1D Extra Credit Assignment

# This file runs the experiments and displays the results

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
	print(already_ordered_1[0:5])
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

	
	print('\n')

def output_reverse_ordered():
	# create reverse ordered lists
	reverse_ordered_1 = [x for x in range(SIZE_1 - 1, -1, -1)]
	reverse_ordered_2 = [x for x in range(SIZE_2 - 1, -1, -1)]
	reverse_ordered_3 = [x for x in range(SIZE_3 - 1, -1, -1)]

	print("Reverse Ordered")
	print(reverse_ordered_1[0:5])
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
	
	print('\n')

def output_random_ordered():
	random.seed(time.time())
	already_ordered = [x for x in range(0,SIZE_3)]

	# create random ordered list
	random_ordered_1 = random.sample(already_ordered, SIZE_1)
	random_ordered_2 = random.sample(already_ordered, SIZE_2)
	random_ordered_3 = random.sample(already_ordered, SIZE_3)

	print("Random Ordered")
	print(random_ordered_1[0:5])
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

	print('\n')

def output_ordered_mergeheap():
	already_ordered_1 = [x for x in range(0,50000)]
	already_ordered_2 = [x for x in range(0,75000)]

	print("Already Ordered")
	print(already_ordered_1[0:5])
	print("%-20s %-20s %-20s" % ("ALGORITHM", "50,000", "75,000"))

	m1 = merge_sort(list(already_ordered_1))
	m2 = merge_sort(list(already_ordered_2))

	print("%-20s %-20d %-20d" % ("Merge Sort", m1, m2))

	h1 = heap_sort(list(already_ordered_1))
	h2 = heap_sort(list(already_ordered_2))

	print("%-20s %-20d %-20d" % ("Heap Sort", h1, h2))
	print("\n")


def output_reversed_mergeheap():
	reverse_ordered_1 = [x for x in range(49999,-1, -1)]
	reverse_ordered_2 = [x for x in range(74999,-1, -1)]

	print("Reverse Ordered")
	print(reverse_ordered_1[0:5])
	print("%-20s %-20s %-20s" % ("ALGORITHM", "50,000", "75,000"))

	m1 = merge_sort(list(reverse_ordered_1))
	m2 = merge_sort(list(reverse_ordered_1))

	print("%-20s %-20d %-20d" % ("Merge Sort", m1, m2))

	h1 = heap_sort(list(reverse_ordered_1))
	h2 = heap_sort(list(reverse_ordered_1))

	print("%-20s %-20d %-20d" % ("Heap Sort", h1, h2))
	print("\n")

def output_random_mergeheap():
	random.seed(time.time())
	already_ordered = [x for x in range(0,75000)]

	# create random ordered list
	random_ordered_1 = random.sample(already_ordered, 50000)
	random_ordered_2 = random.sample(already_ordered, 75000)

	print("Random Ordered")
	print(random_ordered_1[0:5])
	print("%-20s %-20s %-20s" % ("ALGORITHM", "50,000", "75,000"))

	m1 = merge_sort(list(random_ordered_1))
	m2 = merge_sort(list(random_ordered_2))

	print("%-20s %-20d %-20d" % ("Merge Sort", m1, m2))

	h1 = heap_sort(list(random_ordered_1))
	h2 = heap_sort(list(random_ordered_2))

	print("%-20s %-20d %-20d" % ("Heap Sort", h1, h2))
	print("\n")

def output_radix_sort():
	arr = ['acdes', 'asdsd', 'ksjtr', 'kerpt', 'absqa',
	 'zabaa', 'rkdsb', 'qqqqq', 'kdfaa', 'zedsd']

	sorted_array = radix_sort_string(arr, 0)

	print("Sorted Array")
	for s in sorted_array:
		print(s)


def main():
	# output_already_ordered()
	# output_reverse_ordered()
	# output_random_ordered()
	# output_ordered_mergeheap()
	# output_reversed_mergeheap()
	# output_random_mergeheap()
	output_radix_sort()

main()