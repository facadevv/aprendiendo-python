#Given two strings ransomNote and magazine, return:
#true if ransomNote can be constructed by using the letters from magazine 
#false otherwise.

#Each letter in magazine can only be used once in ransomNote.

#Example 1:                         Input: ransomNote = "a", magazine = "b"
#                                   Output: false
#Example 2:                         Input: ransomNote = "aa", magazine = "aab"
#                                   Output: true

                                                                                                                                                                                                                                                            #

ransom_note=dict()
magazine=dict()

def ransom_check():
    ransomNote=input("Please, enter RansomNote: ")
    magazine=input("Please, enter Magazine: ")
    print("Verification in precess...")
    for char in ransomNote:
        if char in magazine:
            verification="True"
        else:
            verification="False"
    print(verification)

ransom_check()