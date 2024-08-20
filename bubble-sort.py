import random

@profile
def bubble_sort(a):
	n = len(a)
	for i in range(n):
		for j in range(n - i - 1):
			if a[j] > a[j + 1]:
					a[j], a[j + 1] = a[j + 1], a[j]
	return a


bubble_sort([random.randint(0, 100) for _ in range(1000000)])
