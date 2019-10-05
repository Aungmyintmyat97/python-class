#	with open('testCOPY.txt', 'w') as wf:
#		with open('testCOPY.txt', 'w') as wf:

#		for line in rf:
#			wf.write(line)	

with open('photo.jpg', 'rb') as rf:
	with open('photo_copy.png', 'wb') as wf:




		for line in rf:
			wf.write(line)


with open('photo.jpg', 'rb') as rf:
	with open('photo_copy.png', 'wb') as wf:
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)

		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)


with open('crop.jpg', 'rb') as rf:
	with open('crop_copy.png', 'wb') as wf:

		for line in rf:
			wf.write(line)

with open('download.jpg', 'rb') as rf:
	with open('download_copy.png', 'wb') as wf:

		for line in rf:
			wf.write(line)

with open('rose.png', 'rb') as rf:
	with open('rose_copy.jpg', 'wb') as wf:
		chunk_size = 4000
		rf_chunk = rf.read(chunk_size)

		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)
