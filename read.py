'''Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, 
and print out the results to the screen. I have a .txt file for you, if you want to use it!

Extra:

Instead of using the .txt file from above (or instead of, if you want the challenge), take http://www.practicepython.org/assets/Training_01.txt, 
and count how many of each “category” of each image there are. This text file is 
actually a list of files corresponding to the SUN database scene recognition database, and 
lists the file directory hierarchy for the images. Once you take a look at the first line or two 
of the file, it will be clear which part represents the scene category. 
To do this, you’re going to have to remember a bit about string parsing in Python 3. 
I talked a little bit about it in this post.'''

import re

filename = input("Enter file name: ")
fhandle = open(filename)

#In this case, I tried for the challenge. The only change for nameslist.txt is to remove the parser line.
categories = {}
for line in fhandle:
    line = line.rstrip()
    category = line[3:-25]
    categories[category] = categories.get(category, 0) + 1

print(categories)  