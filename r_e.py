import re
file = input("File name: ")
fhandle = open(file)

for line in fhandle:
    line = line.rstrip()
    donor = re.findall('\s?(ENCDO[0-9]{3}[A-Z]{3})\s?', line)
    print(donor)