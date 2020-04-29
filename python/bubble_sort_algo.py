
def bubble_sort(nums):
	#Set the number for sweeps to that of the length of the array
	for round in range(len(nums)):

		#Scanning the array and comaring numbers and their adjacent.
		#Go up to the one less than the last item to not go out of range 
		for i in range(len(nums) - 1):
			if nums[i] > num[i + 1]:
				nums[i], nums[i+1] = nums[i+1], nums[i]

