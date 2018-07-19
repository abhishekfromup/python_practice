# bubbleSort.py

def bubbleSort(arr):
	for i in range(len(arr)-1):
		for j in range(len(arr)-i-1):
			if (arr[j+1] < arr[j]):
				arr[j+1], arr[j] = arr[j], arr[j+1]

def main():
	size = int(input("Please enter the size of the array: "))
	global arr
	arr = []
	for i in range(size):
		arr.append(int(input("Enter element no (%d):"% (i+1))))

	print ("Given array is: ")
	for i in range(size):
		print(arr[i])
	bubbleSort(arr)

	print ("Sorted array: ")
	for i in range(size):
		print(arr[i])

if (__name__ == "__main__"):
	main()