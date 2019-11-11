################################################################################
#
################################################################################
def getDelimiterAndColumns(fileName):
	myDelimiter = ','
	nCol = getNumberOfColumns(fileName, myDelimiter)
	# print("number of columns: ", nCol)
	if (nCol == 1):
		myDelimiter = ' '
		iscsv = False
	else:
		myDelimiter = ','
		iscsv = True
	#
	# print("my delimiter: ", myDelimiter)

	# get actual number of columns
	nCol = getNumberOfColumns(fileName, myDelimiter)
	# print("my delimiter: ", myDelimiter, nCol)
	return myDelimiter, nCol
#

################################################################################
#
################################################################################
def getNumberOfColumns(fileName, myDelimiter):
	with open(fileName) as f:
	  line = f.readline()
	  # print(line)
	#
	return len(line.split(myDelimiter))
#

################################################################################
# https://stackoverflow.com/questions/15670760/built-in-function-in-python-to-check-header-in-a-text-file
################################################################################
def check_header(fileName):
	with open(fileName) as f:
		first = f.read(1)
	return first not in '.-0123456789'


################################################################################
#
################################################################################
# importing the required module
import matplotlib.pyplot as plt 

# to accept external arguments
import sys
# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)
# print( 'Number of arguments:', len(sys.argv), 'arguments.')
# print( 'Argument List:', str(sys.argv))

import os
fileName = sys.argv[1]
if ( not os.path.exists(fileName) ):
	print("file not found.")
	sys.exit()


X, Y1, Y2 = [], [], []

myDelimiter, nCol = getDelimiterAndColumns(fileName)
# print("nCol=", nCol)
# sys.exit()

import csv

if ( not check_header(fileName) ):
	# you can use `row = l.split()` if you weren't going to use a csv file
	with open(fileName, 'r') as csv_file: # 'r': just for reading
		reader = csv.reader(csv_file, delimiter=myDelimiter)
		# for line in reader:
		# 	print(line)

		#https://www.programiz.com/python-programming/reading-csv-files # skipinitialspace=True
		if (nCol == 3):
			for line in reader:
				X.append(float(line[0]))
				Y1.append(float(line[1]))
				Y2.append(float(line[2]))
			#
		if (nCol == 2):
			for line in reader:
				X.append(float(line[0]))
				Y1.append(float(line[1]))
			#
		# if (nCol > 3):
		# 	print("hey")
	#
	csv_file.close()
	#
	#
	if (nCol == 3):
		fig, ax1 = plt.subplots()

		# color = 'tab:red'
		color = 'r'
		ax1.set_xlabel('X - steps')
		ax1.set_ylabel('Y1 - Emax_of_step', color=color)
		ax1.plot(X, Y1, color=color)
		# ax1.scatter(X, Y1, color=color, marker=".")
		ax1.tick_params(axis='y', labelcolor=color)

		ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

		#color = 'tab:blue'
		color = 'b'
		ax2.set_ylabel('Y2 - T_estimate', color=color)  # we already handled the x-label with ax1
		ax2.plot(X, Y2, color=color)
		# ax2.scatter(X, Y2, color=color, marker=".")
		ax2.tick_params(axis='y', labelcolor=color)

		fig.set_tight_layout(True) ## << this works!
		# fig.tight_layout()  # otherwise the right y-label is slightly clipped
		plt.show()
		#
	elif (nCol == 2):
		# plotting the points  
		plt.plot(X, Y1) 

		# naming the x axis 
		plt.xlabel('X - axis') 
		# naming the y axis 
		plt.ylabel('Y - axis') 
		  
		# giving a title to my graph 
		# plt.title('My first graph!') 
		  
		# show a legend on the plot 
		# plt.legend() 

		# function to show the plot 
		plt.show() 
	##

else:
	# print("nCol > 3")
	# if (check_header(fileName)):
	# 	print("the file has header")

	# https://matplotlib.org/3.1.0/gallery/misc/plotfile_demo.html#sphx-glr-gallery-misc-plotfile-demo-py
	import matplotlib.pyplot as plt
	import matplotlib.cbook as cbook

	import os
	currentPath = os.getcwd()
	absFileName = currentPath + "/" + fileName
	fname = cbook.get_sample_data(absFileName, asfileobj=False)
	# print(sys.argv[1], sys.argv[2], sys.argv[3])
	

	columnsToDisplay = len(sys.argv)
	
	# columns = []
	labels = () # it's a tuple
	# for i in range(columnsToDisplay):
	# 	columns.append( sys.argv[i] )
	#
	# colX = sys.argv[2]
	if ( sys.argv[2].isnumeric() ):
		# begin in 2 to avoid the names of plot.py and the file data.
		for i in range(2, columnsToDisplay):
			labels = labels + (int( sys.argv[i] ), )
	else:
		for i in range(2,columnsToDisplay):
			labels = labels + (sys.argv[i].lower(), )

	#
	# print(labels)
	# print(labels[0])
	# sys.exit()


	# colX = sys.argv[2]
	# colY = sys.argv[3]
	# if ( colX.isnumeric() ):
	# 	colX = int(colX)
	# 	colY = int(colY)
	# else:
	# 	colX = colX.lower()
	# 	colY = colY.lower()

	#
	# plt.plotfile( fname, (int(sys.argv[2]),1), delimiter=',' )
	# plt.plotfile( fname, (0,1), delimiter=',' )
	# plt.plotfile( fname, (colX, colY), delimiter=myDelimiter )
	plt.plotfile( fname, labels, delimiter=myDelimiter, subplots=False)
	plt.show()
#


############
#
# x axis values 
# x = [1,2,3] 
# corresponding y axis values 
# y = [2,4,1] 








