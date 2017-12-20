# testing sort functions

from sort import *
import random

def main():

	done_bucket = radix_sort_string(arr, 0)

	print("\n")
	for x in done_bucket: print(x)

if __name__ == '__main__':
	main()