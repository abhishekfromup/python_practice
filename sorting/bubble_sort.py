# bubble_sort.py

def bubbleSort(arr):
	n = len(arr)
	for i in range (n-1):
		for j in range (n-i-1):
			if (arr[j+1] < arr[j]):
				arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
	size = int(input("Please enter the size of the array: "))
	print("Enter %d integers... "% size)
	global arr
	arr = []
	for i in range(size):
		arr.append(int(input("Enter element no (%d): "%(i+1))))

	print("Given array is: ")
	for i in range(len(arr)):
		print(arr[i])

	bubbleSort(arr)
	print("Sorted array is: ")
	for i in range(len(arr)):
		print(arr[i])

if (__name__ == "__main__"):
	main()