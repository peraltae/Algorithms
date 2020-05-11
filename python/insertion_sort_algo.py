def insertion-sort(nums: List[int]):

	for i in range(1,len(nums)):
		#set key to current interation elm 
		key = A[i]

		#Insert A[i] into sorted sequence A[1...i-1]
		j = i - 1 #j becomes the index one less than current i which is the sorted sublist 
		while j > 0 and A[j] > key:
			#Swich elm at position i with j then keep going until sub-array is sorted
			A[j+1] = A[j]
			j -= 1
			
		A[j + 1] = key


