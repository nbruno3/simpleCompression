# A simple compression algorithm based on reducing/eliminating repetitive data in file
# Nick Bruno - 05/10/2019

import math
import time

# Define compression method, takes filename and True or False as input
def compress_text_file(filename, isCaseSensitive):
	
	# Initialize our temp storage and compression arrays
	comp_file = []
	storage = []
	
	# See how long compression method takes
	start_time = time.time()
	
	# Open file for reading and place into storage list
	with open(filename, 'r') as file:
		for line in file:
			for char in line:
				storage.append(char)
	
	# Compress data by eliminating repetitions in adjacent data bits
	storage.append('0')
	cnt = 1
	for i in range(len(storage)-1):
		
		# Only execute if compression method is NOT case sensitive
		if not isCaseSensitive:
			if storage[i].isalpha():
				storage[i] = storage[i].upper()
			if storage[i+1].isalpha():
				storage[i+1] = storage[i+1].upper()
		
		# Add to counter until continuous charactres end, then write to file
		# Write to file after 9 instances to avoid double digit counter
		if storage[i] == storage[i+1]:
			cnt += 1
			if cnt == 10:
				comp_file.append(cnt-1)
				comp_file.append(storage[i])
				cnt = 1
		else:
			comp_file.append(cnt)
			comp_file.append(storage[i])
			cnt = 1
				
	# Write the new compressed data to file
	with open('test_file_comp.txt', 'w') as comp:
		for i in comp_file:
			comp.write("%s"%i)
			
	# Calculate how much time compression method takes
	end_time = time.time()
	duration = end_time - start_time
	print("Compression time: {} milliseconds".format(duration*1000))
	
# Define method to retrieve original data from compressed file,
# takes filename of compresed file
def uncompress_text_file(filename):
	
	# Initialize our temp storage and final uncompressed arrays
	uncomp_file = []
	storage = []
	
	# Read in file to uncompress
	with open(filename, 'r') as compressed:
		for line in compressed:
			for char in line:
				storage.append(char)
			
	# Uncompress data 
	cnt = 0
	for i in range(len(storage)-1):
		# Uncompress until cnt passes length of storage buffer, then pass until end of i
		try:
			num = int(storage[cnt])
			val = storage[cnt+1]
			uncomp_file.append(val*num)
			cnt += 2
		except:
			pass
			
	# Write the uncompressed data to file
	with open('test_file_uncomp.txt', 'w') as new_file:
		for i in uncomp_file:
			new_file.write("%s"%i)
	
	
if __name__ == '__main__':
	# test_file.txt is default file included with program
	# Feel free to change this value to your own file, or alter text within test_file.txt
	compress_text_file('test_file.txt', True)
	
	uncompress_text_file('test_file_comp.txt')
	
	
