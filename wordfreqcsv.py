import csv

# Taking filename as input as lab wants to try with variety of files
file_name = input()

# Creating a dictionary to count words into
freq = {}

# Opening the file based on the filename entered above
with open(file_name, 'r') as csvfile:
    word_reader = csv.reader(csvfile)
        
# iterating through word_reader list     
    for row in word_reader:
       for word in row:
# Checking to see if the word is already in the frequency dictionary and if not adding it. 
# I went through several variations on this program, and found only this method to work. It is subtly
# different than the lab from 6.18 which threw me, but I think this method will work.
           if word not in freq.keys():
               freq[word] = 1
           else: 
               freq[word] += 1
                           
# Print out each word from the dictionary as they come, rather than all out in a list.
    for key, value in freq.items():
        print('{} {}'.format(key, value))
