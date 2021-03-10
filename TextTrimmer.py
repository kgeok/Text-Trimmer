#Written by Kevin George
#Version 0.1
import os
import sys

print (sys.argv[1])
inputlines = []
buffer = []
Beginning = 0
End = 0
bvalue = sys.argv[2]
evalue = sys.argv[3]
inputfile = open(sys.argv[1], "r")
outputnamebuffer = str(sys.argv[1])
outputfile = open(outputnamebuffer.replace('.txt', '_EDITED.txt'), "w+")

for x in inputfile:
    inputlines.append(x)

for i in range(len(inputlines)):
    if inputlines[i] == bvalue:
        #print("Found Beginning")
        Beginning = i
        #print(i)
        
for i in range(len(inputlines)):
    if inputlines[i] == evalue:
        #print("Found End")
        End = i
        #print(i)

buffer = list(inputlines[Beginning:End])
#print(buffer)

for i in range(len(buffer)):
    outputfile.write(buffer[i])

inputfile.close()
outputfile.close()

print ("Done with: " + outputnamebuffer)
