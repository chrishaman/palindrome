print("""
 _______________________________________
|                                       |
|*Let's see which words are Polindrome!*|
|_______________________________________|

""")

def palindrome_test():
    while True:
        word = input("Enter a word: [q] for exit!\n->")
        word = " ".join(word.replace(" ", ""))
        word = word.lower()
        if word == "q":
            break

        elif word == word[::-1]:
            print('Palindrome!\n')

        else:
            print("Not a Palindrome!\n")
    
    print("\nEnd of program!")

palindrome_test()
