import random


def selection_sort(arr): 
	swaps = 0
	comparisons = 0
	
	for indx1 in range(len(arr) - 1): 
		key = indx1
		for indx2 in range(indx1 + 1, len(arr)):
			comparisons += 1 
			if arr[indx2] < arr[key]: 
				key = indx2
		if not key == indx1: 
			arr[indx1], arr[key] = arr[key], arr[indx1]
			swaps += 1

	return arr, swaps, comparisons


def print_array(arr_type, func):
	arr, swaps, comparisons = func
	print(f"{arr_type} Array, selection sort")
	print(f"number of comparisons: {comparisons}")
	print(f"number of swaps:       {swaps}")
	for indx in range(len(arr)): 
		if (indx + 1) % 10 == 0: 
			print(arr[indx])
		else: 
			print(arr[indx], end=' ')
	print()


array = list(range(100, 200))

print_array("Sorted", selection_sort(array))

random.shuffle(array)
print_array("Unsorted", selection_sort(array))

array = sorted(array, reverse=True)
print_array("Reverse Sorted", selection_sort(array))


'''
Example of Output: 

	Sorted Array, selection sort
	number of comparisons: 4950
	number of swaps:       0
	100 101 102 103 104 105 106 107 108 109
	110 111 112 113 114 115 116 117 118 119
	120 121 122 123 124 125 126 127 128 129
	130 131 132 133 134 135 136 137 138 139
	140 141 142 143 144 145 146 147 148 149
	150 151 152 153 154 155 156 157 158 159
	160 161 162 163 164 165 166 167 168 169
	170 171 172 173 174 175 176 177 178 179
	180 181 182 183 184 185 186 187 188 189
	190 191 192 193 194 195 196 197 198 199

	Unsorted Array, selection sort
	number of comparisons: 4950
	number of swaps:       97
	100 101 102 103 104 105 106 107 108 109
	110 111 112 113 114 115 116 117 118 119
	120 121 122 123 124 125 126 127 128 129
	130 131 132 133 134 135 136 137 138 139
	140 141 142 143 144 145 146 147 148 149
	150 151 152 153 154 155 156 157 158 159
	160 161 162 163 164 165 166 167 168 169
	170 171 172 173 174 175 176 177 178 179
	180 181 182 183 184 185 186 187 188 189
	190 191 192 193 194 195 196 197 198 199

	Reverse Sorted Array, selection sort
	number of comparisons: 4950
	number of swaps:       50
	100 101 102 103 104 105 106 107 108 109
	110 111 112 113 114 115 116 117 118 119
	120 121 122 123 124 125 126 127 128 129
	130 131 132 133 134 135 136 137 138 139
	140 141 142 143 144 145 146 147 148 149
	150 151 152 153 154 155 156 157 158 159
	160 161 162 163 164 165 166 167 168 169
	170 171 172 173 174 175 176 177 178 179
	180 181 182 183 184 185 186 187 188 189
	190 191 192 193 194 195 196 197 198 199
'''