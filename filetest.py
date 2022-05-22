#fileprocessingprogram
#Desc - Program that creates, reads and writes files
#CIS245
#Erin Weithers

import os.path
filepath = input("What is the location of the directory you want to save your file in?")
filename = input("What do you want to name your file?")
completepath= filepath+filename


if os.path.exists(filepath):
	print("Directory exists.")
else: f = open(filename, "x")

import csv

with open ('userinfo.csv', 'w', newline='') as file:
	csv_writer = csv.writer(file)
	csv_writer.writerow(["Name","Address","Phone Number"])
	name = input("Please enter your name: ")
	address = input("Please enter your address: ")
	phonenumber = input("Please enter your phone number: ")
	csv_writer.writerow([name,address,phonenumber])

with open ('userinfo.csv', 'r') as file:
	csv_reader = csv.reader(file)

	for line in csv_reader:
		print(line)