def translator(phrase):
 translation = ""
 for letter in phrase:
  #In the program, I made the letter "j" "J" a substitute for a vowel in any word inputed 
        if letter in "AEIOU":
            translation += "J"
        elif letter in "aeiou":
            translation += "j"
        else:
            translation += letter
 return translation
print(translator(input("Enter word:")))
