# # assignment
# question 1
text = (input("Enter a word: "))
text=text[0]+text[1:].lower() #retain 1st letter and lowercase for 2nd letter onwards so can read dictionary
text_blank = {'a': ' ', 'e': ' ', 'i': '', 'o': ' ', 'u': ' ', 'h': ' ', 'y': ' ', 'w': ' ', }
text_1 = {'b': '1', 'f': '1', 'p': '1', 'v': '1', }
text_2 = {'c': '2', 'g': '2', 'j': '2', 'k': '2', 'q': '2', 's': '2', 'x': '2', 'z': '2'}
text_3 = {'d':'3','t':'3'}
text_4 = {'l': '4'}
text_5 = {'m': '5', 'n': '5'}
text_6 = {'r': '6'}
text_replace={**text_blank,**text_1,**text_2,**text_3,**text_4,**text_5,**text_6} #group up the dictionary for word replace

#replacing words
retain=text[0]                                              #to keep 1st letter
for word in text[1:]:                                       #start from 2nd letter onwards
    for wrd, rpl in text_replace.items():                   #replace letter from dictionary
        word = word.replace(wrd, rpl)                       #replace letter from word from dictionary
    retain+= word                                           #1st letter plus replaced word

#for adjacent word retain 1st one
adjacent=retain[0]
for i in range(1,len(retain)):
    if retain[i] == retain[i-1]:                            #check for every chr of i if the current chr of i is same as previous chr of i
        continue                                            #if not same then add to adjacent, if same then skip current chr
    else:
        adjacent += retain[i]                               #no then continue with the chr you have


blank=adjacent[0]
for i in range(1,len(adjacent)):                            #check if there is blank space that is replaced from the dictionary
    if adjacent[i]==" ":
        continue
    else:
        blank += adjacent[i]

#limit to 4 chr or add 0 if less than 4 chr until have 4 chr
length=blank
if len(length) >=4:                                         #limit the word to 4
    print(length[:4])                                       #print word till length 4
else:
    print(length.ljust(4,"0"))                              #if less than 4 then add 0 behind with ljust
                                                            #ljust use for inserting chr until reached the length

