s = str(input("Enter your sentence: "))
upper = s.upper()
print("Sentence in uppercase: ",upper)
lower = s.lower()
print("Sentence in lowercase: ",lower)
length = len(s.split())
print("No. of words in sentence: ",length)
l1 = len(s)
print("No. of characters in the sentence: ",l1)
w = str(input("Enter the word you want to search in the sentence: "))
if w in s:
    print(w,"is in the sentence")
else:
    print(w,"is not in the sentence")
