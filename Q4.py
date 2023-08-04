# 4.

#Input
Sentence=input("Enter a sentence:")

# Split sentence into words
word_list = Sentence.split()

# To check in a line whether 'python' or ',python' exists
def word_check(line, word, invalid_word):
    for i in range(len(line)):
        if line[i:i+len(word)] == word:
            return True
        elif line[i:i+len(invalid_word)] == invalid_word:
            return False


word="python"
invalid_word=",python"
x=0
y=0

# Loop the 'check line' for every word in the list
for element in word_list:
    if word_check(element, word, invalid_word) is True:
        x+=1
    elif word_check(element, word, invalid_word) is False:
        y+=1

# Output sequence
if y>0:
    print(False)
elif x>0:
    print(True)
else:
    print(False)

# another way
# sample=str(input("Input your line:"))
# if ",python" in sample:
#         print(False)
# elif "python" in sample:
#         print(True)
# else:
#     print("Your line dont have python: ")



