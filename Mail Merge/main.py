#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# TODO Create a list of all invited names
with open("./Input/Names/invited_names.txt", mode="r") as invited_names_file:
    invited_list = invited_names_file.readlines()
    print(invited_list)

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_contents = letter_file.read()
    # print(letter_contents)
    for name in invited_list:
        stripped_name = name.strip()
        new_letter = letter_contents.replace("[name]", stripped_name)
        # print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as edited_letter:
            edited_letter.write(new_letter)