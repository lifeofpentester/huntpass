#!/usr/bin/python

import sys  #Taking Arguments in Terminal
import os   #Clearscreen
import time

if len(sys.argv) < 4:  #First Argument is always the program name
        sys.exit('Usage: python HuntPass.py <InputFile> <OutputFile> <SearchString>')    #Exit if New User doesn't give all the Arguments

os.system('clear')

time_on_your_system = time.asctime(time.localtime(time.time()))

print "_____________", time_on_your_system, "_____________"
print "\n_____A Small Script to find Passwords in Dumps_____"

print "\n####################################################"

print "\n_________________Written by Pranshu__________________"

print "______________________________________________________"



filename = sys.argv[1]  #Input File

newfile = sys.argv[2]   #Output File

f1 = open (filename, "r") #Read Mode

f2 = open (newfile, "a+") #Append Mode

search_string = sys.argv[3] #Text to Search

print "\n[+]Looking in", filename + "\n[+]Storing Result in", newfile + "\n[+]Searching for", search_string

flag = raw_input("\n\nProceed? (y/n): ")

if flag == 'y':
	lines_seen = set()  #A Data Structure to store lines seen, to prevent duplicate passwords while saving

	total_pass = 0

	for line in f1:
		if line not in lines_seen:	
			if search_string in line:
				f2.write(line)
				lines_seen.add(line)
				total_pass = total_pass + 1
	print "\n[+]Total Passwords found are: ", total_pass
	print "\n[+]Saved in ", newfile
f1.close()
f2.close()
print "\n________________________QUITTING!____________________\n\n"
