print("Fill in the blank spaces in the following order.")

madlibs2 = "The ____ dancer gracefully ____ across the ____, captivating the mesmerized ____ with ____ fluid movements and expressive ____ of the ____."
print(madlibs2)

adjective = input("Adjective: ")
verb = input("Verb: ")
noun = input("Noun: ")
noun2 = input("Noun: ")
pronoun = input("Pronoun: ")
noun3 = input("Noun: ")
noun4 = input("Noun: ")

madlibs = (f"The {adjective} dancer gracefully {verb} across the {noun}," 
           f"captivating the mesmerized {noun2} with {pronoun} fluid movements and "
           f"expressive {noun3} of the {noun4}.")

print(madlibs)