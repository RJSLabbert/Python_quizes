print("Test palindrome")
word = input("enter the word to test: ")
is_palindrome = True
for i in range(len(word)):
    if word[i] != word[len(word)-1-i]:
        is_palindrome = False
        break
    
print(is_palindrome)        
