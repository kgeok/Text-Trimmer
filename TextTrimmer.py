import os
import sys

version = "0.2"

if (sys.argv[1] == "-h"):
    print ("")
    print ("-------------Text Trimmer " + version + "-------------")
    print ("-------------Written by Kevin George-------------")
    print ("-h for usage and help")
    print ("-t to trim text file")
    print ("Usage: ./TextTrimmer -t [FileName.txt] [Beginning Text] [End Text]")
    print ("")

elif (sys.argv[1] == "-t"):
    print (sys.argv[2])
    inputlines = []
    buffer = []
    Beginning = 0
    End = 0
    bvalue = sys.argv[3]
    evalue = sys.argv[4]
    inputfile = open(sys.argv[2], "r")
    outputnamebuffer = str(sys.argv[2])
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

else:
    print ("Invalid argument, please type -h for a list of all arguments")
