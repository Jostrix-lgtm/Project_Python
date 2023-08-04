filename=input("Enter the news file name:")

import shutil               #import shutil to use the copy function from one file to another
original = filename         #the file you want to copy
target = r'filedata.txt'    #the file that you want to copy to
shutil.copyfile(original, target)

with open("filedata.txt",'r',encoding="utf8") as filedata:
    word_list=filedata.read().split()               #split the words in the text file

#create list for vowel
a=[]
e=[]
i=[]
o=[]
u=[]

for word in word_list:                  #words that start with vowel add into the list
    if word[0].lower()=="a":
        a.append(word)
    elif word[0].lower()=="e":
        e.append(word)
    elif word[0].lower()=="i":
        i.append(word)
    elif word[0].lower()=="o":
        o.append(word)
    elif word[0].lower()=="u":
        u.append(word)

print("List of words that begins with vowel 'a':",a)
print("List of words that begins with vowel 'e':",e)
print("List of words that begins with vowel 'i':",i)
print("List of words that begins with vowel 'o':",o)
print("List of words that begins with vowel 'u':",u)

length_4_word_list=[]                               #create a list for 4 words

vowellist=a+e+i+o+u                                 #join the vowel list together

for x in vowellist:                                 #from the vowel list
    if len(x)==4 and x.isalpha():                   #if the word is length 4/ 4 letter then add into the 4 letter word list
            length_4_word_list.append(x.upper())
length_4_word_list=list(set(length_4_word_list))    #use set for unique word then change back to list
print("Word with length 4 in list: ",length_4_word_list)

def vowel_both_ends(word):                          #function to check if the word start and end with vowels
    vowels = ["a","e","i","o","u"]
    if word[0].lower() in vowels and word[-1].lower() in vowels:
        return True
    else:
        return False

import random
for files in ["file1", "file2", "file3", "file4", "file5"]:
    the_word = random.choice(length_4_word_list)        #randomly choose among the 4-letter words
    with open(f"{files}.txt", "w") as file:             #open the 5 files as text file and write
        file.write(the_word)                            #write the chosen word in the file
        if vowel_both_ends(the_word)==True:             #use the function above
            print(f"In {files}, the word '{the_word}' starts and ends with a vowel.")
        else:
            print(f"In {files}, the word '{the_word}' does not start and end with a vowel.")

longest_string=max(word_list, key=len)                  #find longest string inside the text file
print("The longest string in the news is:",longest_string)

def one_vowel(ov):                                      #function to find words that has one vowel in it
    vowels = "aeiou"
    count = 0
    for char in ov:
        if char.lower() in vowels:
            count+=1
    return count==1

consonant_end_one_vowel_list=[]                         #create a list for word ending with consonant and have one vowel in it
for word in word_list:
    if word[-1].lower() not in "aeiou" and word.isalpha():          #if word end with consonant
        if one_vowel(word)==True:                                   #and has one vowel in it
            consonant_end_one_vowel_list.append(word)               #add into the list above
print("List of words that ends with consonant and has only one vowel in it:\n", consonant_end_one_vowel_list)
