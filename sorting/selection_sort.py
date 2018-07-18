# selection.py

def selectionSort(arr):
	n = len(arr)

	for i in range(n-1):
		min_index = i
		for j in range (i+1,n):
			if (arr[j] < arr[min_index]):
				min_index = j
		arr[min_index], arr[i] = arr[i], arr[min_index]


def main():
	size = int(input("Please enter the size of the array: "))
	global arr
	arr = []
	print("Please enter %d elements... \n" %size)
	for i in range(size):
		arr.append(int(input("Enter element no %d: "% (i+1))))
	print("Given array is: ")
	for i in range(size):
		print(arr[i])

	selectionSort(arr)

	print("Sorted array is: ")
	for i in range(size):
		print(arr[i])

if(__name__ == "__main__"):
	main()