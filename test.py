from sort import *
import random

def main():
	rand_list = [random.randint(0,5000) for x in range(5000)]

	stats = quick_sort(rand_list, 0, 4999, partition3)

	for x in rand_list: print(x)

	print(stats)

if __name__ == '__main__':
	main()