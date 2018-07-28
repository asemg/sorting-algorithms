def bubble_sort(arr):
	is_sorted = False
	while not is_sorted:
		is_sorted = True
		for k in range(len(arr)):
			if k < len(arr) - 1:
				if arr[k] > arr[k+1]:
					is_sorted = False
					arr[k], arr[k+1] = arr[k+1], arr[k]
	return arr
