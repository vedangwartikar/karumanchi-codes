def towersOfHanoi(noOfDisks, start = 1, end = 3):
	
	if noOfDisks:
		towersOfHanoi(noOfDisks-1, start, 6-start-end)
		print("Move disk %d from peg %d to peg %d"%(noOfDisks, start, end))
		towersOfHanoi(noOfDisks-1, 6-start-end, end)
towersOfHanoi(noOfDisks = 3)
