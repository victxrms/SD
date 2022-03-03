# Exercise 4 Template
import os

# Do not modify the file name or function header

# Return the size of the file and words ending in 's'
def get_file_info(filename):
	# Your code here
	size = 0
	wordlist = []
	size = os.path.getsize(filename)
	
	with open (filename, "r") as fichero:
		for line in fichero:
			for word in line.split():
				if word.endswith("s"):
					wordlist.append(word)



	# ...

	return (size, wordlist)