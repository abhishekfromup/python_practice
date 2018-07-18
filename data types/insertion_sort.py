# insertion_sort.py

def insertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		
		while (j >= 0 and arr[j] > key):
			arr[j+1] = arr[j]
			j = j-1
		arr[j+1] = key


def main():
	size = int(input("Please enter the size of the array: "))
	global arr
	arr = []
	for i in range(size):
		arr.append(int(input("Please enter the element: ")))
		
	print ("Given elements are: ")
	for i in range(len(arr)):
		print ("%d"% arr[i])
	insertionSort(arr)
	print ("Sorted array: ")
	
	for i in range(len(arr)):
		print ("%d"% arr[i])

if (__name__ == "__main__"):
	main()
