import sys

LOGFILE = "logfile.txt" #file for results

# function read local types one by one and print name and description
def test_local_types(ordinal):
    (type, fields) = GetLocalTinfo(ordinal)
    if not type:
        return -1

    # get and print name of type
    name = GetLocalTypeName(ordinal)

    # get and print full description of type
    description = GetLocalType(ordinal,PRTYPE_MULTI)

    # if local type is struct  then saved it
    if "struct" in description:
        TypeInfo = name + " " + description + "\n"
        return TypeInfo
    else:
        return ""

#start 
print ("script start...")

NumberOfLocalTypes = GetMaxLocalType() #Get number of local types
logfile = open (LOGFILE, "w")

for a in range (1, NumberOfLocalTypes): #inspect each local type 
    logfile.write(test_local_types(a))
logfile.close()

print (str(a) + " types was saved in logfile.txt")
print ("script finish...")

       



