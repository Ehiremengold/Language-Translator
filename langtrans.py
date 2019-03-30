def translator(phrase):
 translation = ""
 for letter in phrase:
        if letter in "AEIOU":
            translation += "J"
        elif letter in "aeiou":
            translation += "j"
        else:
            translation += letter
 return translation
print(translator(input("Enter word:")))
