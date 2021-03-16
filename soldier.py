import os
def soldier(path , file , format):
	os.chdir(path)
	i=0
	files = os.listdir(path)
	with open(file) as f:
		filelist = f.read().split("\n")
	for file in files:
		if file not in filelist:
			os.rename(file,file.capitalize())
		if os.path.splitext(file)[1] == format :
			os.rename(file,f'{i}{format}')
			i=i+1
soldier(r'D:\testing',r'D:\images\gcc\ext.txt','.png')

