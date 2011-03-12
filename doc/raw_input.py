#python raw_input
nIds = raw_input("Input your id car:")
if len(nIds) != 15:
    print "error your input id car"
else:
    print "your input value is: %s" %(nIds)

#test int(str, base), float, 
nAge = int(nIds)
print nAge

    
