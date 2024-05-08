import time

def type_writer_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)  # Adjust the sleep time for the desired speed
    print()  # Move to the next line after the text is fully typed

def introduction():
    type_writer_effect("Broken Sword")
    type_writer_effect("In the year 3024, on the neon-lit streets of Neo-Tokyo, there lived a cybernetic samurai named Kenzo...")
    time.sleep(2)
    decision_1()

def decision_1():
    type_writer_effect("\nKenzo finds a code left for him: {brx fdq qhyhu oryh djlq}")
    type_writer_effect("can you brake the code? (enter the code/no)")
    choice = input("Enter your choice: ").lower()
    if choice == "you will never love again":
        kenzo_understands_code()
    elif choice == "no":
        kenzo_does_not_understand_code()
    else:
        type_writer_effect("Invalid choice. Please try again.")
        decision_1()

def kenzo_understands_code():
    type_writer_effect("\nThe code meant 'you will never love again'.")
    type_writer_effect("Kenzo didn't understand what it means and looked at a symbol belonging to the Black Lotus, a notorious crime syndicate.")
    type_writer_effect("He spent years tracking them down, preparing for revenge.")
    time.sleep(2)
    encounter_with_hana()

def kenzo_does_not_understand_code():
    type_writer_effect("\nKenzo couldn't decipher the code's meaning.")
    type_writer_effect("His only other clue was a mysterious symbol left at the scene of the crime, belonging to the Black Lotus.")
    type_writer_effect("He spent years tracking them down, preparing for revenge.")
    time.sleep(2)
    encounter_with_hana()

def encounter_with_hana():
    type_writer_effect("\nDuring his journey, Kenzo finds a woman named Hana.")
    type_writer_effect("Hana needs help because she is the target of the Black Lotus, she is a very smart scientist.")
    type_writer_effect("Do you want to help her? (yes/no)")
    choice = input("Enter your choice: ").lower()
    if choice == "yes":
        kenzo_helps_hana()
    elif choice == "no":
        kenzo_does_not_help_hana()
    else:
        type_writer_effect("Invalid choice. Please try again.")
        encounter_with_hana()

def kenzo_helps_hana():
    type_writer_effect("\nKenzo helped Hana and soon fell in love with her.")
    type_writer_effect("Hana was a brilliant scientist, and she helped Kenzo upgrade his cybernetic enhancements.")
    type_writer_effect("They became inseparable lovers, finding solace in each other's company amidst the chaos of their lives.")
    time.sleep(2)
    decision_to_use_new_sword()

def kenzo_does_not_help_hana():
    type_writer_effect("\nKenzo always finds Hana in trouble and he has to help her each time so he keeps her with him since she can help him a lot.")
    type_writer_effect("After some time he falls in love with her.")
    time.sleep(2)
    decision_to_use_new_sword()

def decision_to_use_new_sword():
    type_writer_effect("\nHana gives you a new sword. Do you want to use it? (yes/no)")
    choice = input("Enter your choice: ").lower()
    if choice == "yes":
        type_writer_effect("\nYou took the new sword and you started using it.")
    elif choice == "no":
        type_writer_effect("\nYou refused to use the sword because it was not meant for a samurai to use.")
        type_writer_effect("Hana convinced him to use it anyway, and something seemed to be off.")
    else:
        type_writer_effect("Invalid choice. Please try again.")
        decision_to_use_new_sword()
    time.sleep(2)
    suspicion_about_hana()

def suspicion_about_hana():
    type_writer_effect("\nKenzo looks at the sword and he sees a very familiar code: {brx fdq qhyhu oryh djlq}.")
    type_writer_effect("He looks at it again since he doesn't remember the meaning of it.")
    type_writer_effect("It meant 'you will never love again'. He didn’t tell Hana about this and he became suspicious of her.")
    time.sleep(2)
    type_writer_effect("One night, Kenzo sees her going out from her room.")
    type_writer_effect("Do you want to follow Hana? (yes/no)")
    choice = input("Enter your choice: ").lower()
    if choice == "yes":
        type_writer_effect("\nKenzo gets up and follows her to see her talking to someone.")
    elif choice == "no":
        type_writer_effect("\nKenzo can’t sleep and follows her anyway. There he sees her talking to someone.")
    else:
        type_writer_effect("Invalid choice. Please try again.")
        suspicion_about_hana()
    time.sleep(2)
    revelation_about_hana()

def revelation_about_hana():
    type_writer_effect("\nKenzo discovers Hana's betrayal.")
    type_writer_effect("Hana revealed that she had orchestrated the murder of Kenzo's family to lure him to her.")
    type_writer_effect("She had fallen in love with him and knew that he would stop at nothing to avenge his family.")
    type_writer_effect("In her twisted logic, this was the only way they could be together.")
    time.sleep(2)
    type_writer_effect("Do you want to challenge Hana? (yes/no)")
    choice = input("Enter your choice: ").lower()
    if choice == "yes":
        type_writer_effect("\nFaced with this betrayal, Kenzo was filled with rage and sorrow.")
        type_writer_effect("But he was a samurai, bound by the code of Bushido.")
        type_writer_effect("He challenged Hana to a duel, a battle to the death.")
        time.sleep(2)
        type_writer_effect("\nThe battle was fierce, but in the end, Kenzo's determination prevailed.")
        type_writer_effect("With a heavy heart, he struck the final blow, avenging his family and fulfilling his vow.")
        type_writer_effect("Kenzo went to his family’s grave, pierced his sword into the ground and slowly died from his wounds.")
        type_writer_effect("The memories of Hana and his family were running around his head.")
        type_writer_effect("He wanted to smile but couldn’t hold his tears.")
    elif choice == "no":
        type_writer_effect("\nKenzo tells Hana he doesn't want to fight but he has no choice but revenge.")
        time.sleep(2)
        type_writer_effect("\nFaced with this betrayal, Kenzo was filled with rage and sorrow.")
        type_writer_effect("But he was a samurai, bound by the code of Bushido.")
        type_writer_effect("He challenged Hana to a duel, a battle to the death.")
        time.sleep(2)
        type_writer_effect("\nThe battle was fierce, but in the end, Kenzo's determination prevailed.")
        type_writer_effect("With a heavy heart, he struck the final blow, avenging his family and fulfilling his vow.")
        type_writer_effect("Kenzo went to his family’s grave, pierced his sword into the ground and slowly died from his wounds.")
        type_writer_effect("The memories of Hana and his family were running around his head.")
        type_writer_effect("He wanted to smile but couldn’t hold his tears.")
    else:
        type_writer_effect("Invalid choice. Please try again.")
        revelation_about_hana()

# Start the story
if __name__=="__main__":
    introduction()
