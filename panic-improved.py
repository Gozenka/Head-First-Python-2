phrase = str(input("Introduce your phrase: "))
word = str(input("Introduce the word you want to construct: "))

temporal_letters = []
working_letter = []
show = True

for letter in phrase:
    if letter in word:
        temporal_letters.append(letter.lower())

for letter in word:
    if letter in temporal_letters:
        working_letter.append(temporal_letters.pop(temporal_letters.index(letter)))
    else:
        print("You can't construct the given word with your phrase")
        show = False
        break

if show:
    print(''.join(working_letter))

    
        
