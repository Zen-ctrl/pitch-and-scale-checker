# define a dictionary that maps notes to pitch classes
note_to_pitch_class = {
    "C": 0,
    "D": 2,
    "E": 4,
    "F": 5,
    "G": 7,
    "A": 9,
    "B": 11
}

# define a dictionary that maps notes to equivalent notes
note_to_equivalent = {
    "C": ["C"],
    "D": ["D"],
    "E": ["E"],
    "F": ["F"],
    "G": ["G"],
    "A": ["A"],
    "B": ["B"],
    "C#": ["Db"],
    "D#": ["Eb"],
    "F#": ["Gb"],
    "G#": ["Ab"],
    "A#": ["Bb"]
}

def get_pitch_class(note):
    # get the pitch class of the note
    pitch_class = note_to_pitch_class.get(note, None)
    if pitch_class is not None:
        print(f"The pitch class of {note} is {pitch_class}.")
    else:
        print(f"{note} is not a valid musical note.")

def get_equivalent_notes(note):
    # get the equivalent notes for the note
    equivalent_notes = note_to_equivalent.get(note, [])
    if equivalent_notes:
        print(f"Other notes equivalent to {note} in pitch are: {', '.join(equivalent_notes)}.")
    else:
        print(f"{note} is not a valid musical note.")

def are_within_perfect_fifth(note1, note2):
    # get the pitch classes of the two notes
    pitch_class1 = note_to_pitch_class.get(note1, None)
    pitch_class2 = note_to_pitch_class.get(note2, None)

    # check if the pitch classes are within one perfect fifth of each other
    if pitch_class1 is not None and pitch_class2 is not None:
        if (pitch_class1 - pitch_class2) % 12 in (7, -5):
            print("The two notes are within a perfect fifth of each other.")
        else:
            print("The two notes are not within a perfect fifth of each other.")
    else:
        print("One or both of the notes are not valid musical notes.")

while True:
    # ask the user which function they want to use
    user_input = input('''
    
    Enter the number of the function you want to use | 
    Find the pitch class of a note (1) | Check if two notes are within a perfect fifth (2) | Exit the program (3): 
    ''')

    # check the user input and call the appropriate function
    if user_input == "1":
        note_input = input("Enter a musical note: ")
        get_pitch_class(note_input)
        get_equivalent_notes(note_input)
    elif user_input == "2":
        note1 = input("Enter the first musical note: ")
        note2 = input("Enter the second musical note: ")
        are_within_perfect_fifth(note1, note2)
    elif user_input == "3":
        # exit the program
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please enter '1', '2', or '3'.")
