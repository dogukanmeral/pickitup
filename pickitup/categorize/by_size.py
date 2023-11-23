import os

megabyte = 1000000 #byte
gigabyte = megabyte*1000

size_intervals = {0:"Less than 1 MB",
				  1*megabyte:"1-10 MB",
				  10*megabyte:"10-100 MB",
				  100*megabyte:"100 MB - 1 GB",
				  1*gigabyte:"More than 1 GB"}

def file_size_bytes(file_path):
	return os.stat(file_path).st_size

def by_size(files, directory_path):
	global size_intervals

	files_by_sizes = {}
	for file in files:
		full_path = os.path.join(directory_path, file)

		file_size = file_size_bytes(full_path)
		
		for size in reversed(size_intervals):
			if file_size > size:
				files_by_sizes[file] = size_intervals[size]
				break

	return files_by_sizes