fname = input("Enter file name: ")
fhandle = open(fname)

for line in fhandle:
    line = line.rstrip()
    