# insertionSort.py

def insertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while (j >= 0 and arr[j] > key):
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key

def main():

	size = int(input("Please enter the size of the array: "))
	global arr
	arr = []
	for i in range(size):
		arr.append(int(input("Enter element no (%d): "% (i+1))))

	print("Given array is: ")

	for i in range(size):
		print(arr[i])

	insertionSort(arr)

	print ("Sorted array is: ")
	for i in range(size):
		print(arr[i])


if (__name__ == "__main__"):
	main()