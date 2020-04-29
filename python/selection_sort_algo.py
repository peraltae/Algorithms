#Selection sort algorithm
#Input: unsorted array 
#output: none 
def selection_sort(nums: List[int]):

	#Traverse all elements in remaining in unsorted array
	for i in range(len(nums)):
		min = i

		#find the next lowest 
		for j in range(i+1, len(nums)):
			if nums[min] > nums[j]:
				min = j

		#swap the current element at index i with the new found min			
		A[i], A[min] = A[min], A[i]



def alt_selection_sort(nums: List[int]):
		#Iterate over array
	for i in range(len(nums)):

	#Compare current element in position i with all others in array 
	#If another item in place j is smaller than element in position i, move it index i
		for j in range(len(nums)): 
			if nums[j] < nums[i]:
				nums[j], nums[i] = nums[i], nums[j]
