#Ask user to enter the names and addresses of five friends
buddy1 = raw_input("Type the name and address of your first friend.")
buddy2 = raw_input("Type the name and address of your second friend.")
buddy3 = raw_input("Type the name and address of your third friend.")
buddy4 = raw_input("Type the name and address of your fourth friend.")
buddy5 = raw_input("Type the name and address of your fifth friend.")

#Split each string into First Name, Last Name, and Address
fname1, lname1, address1 = buddy1.split(" ",2)
fname2, lname2, address2 = buddy2.split(" ",2)
fname3, lname3, address3 = buddy3.split(" ",2)
fname4, lname4, address4 = buddy4.split(" ",2)
fname5, lname5, address5 = buddy5.split(" ",2)

#Output just the zip codes
print address1[-5:]
print address2[-5:]
print address3[-5:]
print address4[-5:]
print address5[-5:]

#Output formatted list of zip codes
print "I have friends with zip codes of {0}, {1}, {2}, {3}, and {4}.".format(address1[-5:], address2[-5:], address3[-5:], address4[-5:], address5[-5:])

#Output a list that connects names with zip codes
print "{0} {1} has the zip code {2}".format(fname1, lname1, address1[-5:])
print "{0} {1} has the zip code {2}".format(fname2, lname2, address2[-5:])
print "{0} {1} has the zip code {2}".format(fname3, lname3, address3[-5:])
print "{0} {1} has the zip code {2}".format(fname4, lname4, address4[-5:])
print "{0} {1} has the zip code {2}".format(fname5, lname5, address5[-5:])