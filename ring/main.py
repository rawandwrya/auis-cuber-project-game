import time

colours = {"red": "\033[91m", "end": "\033[0m"}


def type_writer_effect(text):
    for char in text:
          print(char, end='', flush=True)
          time.sleep(0.017)  # Adjust the sleep time for the desired speed
    print()  # Move to the next line after the text is fully typed


def boring_day(count):
    print("")
    if (count > 1):
          type_writer_effect(
                    "Please, change your coffee for next day, and be more adventurous ;)")
          print("")
    type_writer_effect(
                  "You come back from work, your are exhusted. You watched a movie and you slept."
    )
    type_writer_effect(
                  "You woke up a little bit late this time, and you rashed to prepared yourself to go to work and buy a coffe again"
    )
    type_writer_effect("Your favorite coffee is Latte Macchiato. What type of coffee do you choose today?")
    type_writer_effect("Latte Macchiato or Caramel Macchiato?")
    type_writer_effect(
                  "Note: You can choose 1 as \"Latte Macchiato\", and 2 as\"Caramel Macchiato\""
    )
    coffee = input().lower()
    return coffee

def ring():
    type_writer_effect("What do you want to be the name of your character?")
    name = input().lower()
    string = "The name of your charechter is ", name
    type_writer_effect(string)
    count = 5
    print("")
    while (count > 0):
        print(count, "... ", end='', flush=True)
        count -= 1
        time.sleep(0.5)
    print("")
    print("")
    type_writer_effect("You are a middle aged person working in a bank")
    type_writer_effect(
            "Everyday you work from 9 am until 5 pm, and you hate your job and your boss is a total dickhead"
    )
    type_writer_effect(
            "you wake up everyday at the same time and get ready for work and grab a coffee shop near your work place"
    )
    type_writer_effect("What type of coffe do you choose today")
    type_writer_effect("Latte Macchiato or Caramel Macchiato?")
    type_writer_effect(
            "Note: You can choose 1 as \"Latte Macchiato\", and 2 as\"Caramel Macchiato\""
    )
    coffee = input().lower()
    print("")
    while (coffee[0] == "l" or coffee == "1"):
        count += 1
        coffee = boring_day(count)

    type_writer_effect(
            "For the first time ever you picked a new type of coffee, but strangely, you barely tell the difference!!"
    )
    type_writer_effect(
            "You arrived to your workplace straight to your desk and all of the sudden you hear this."
    )
    string = "\"Everybody on the ground, don’t move, don't touch shit. You are not the hero today and if you try to be I will put a bullet in your skull.\" "
    type_writer_effect(string)
    type_writer_effect("The bank you are working at is getting robbed.")
    type_writer_effect(
            "While you are on the ground, you see Maya(The Boss's secretary who you have a crush on) being captured by the criminals."
    )
    type_writer_effect("Do you choose to do something or not?")
    type_writer_effect("yes,or no?")
    acter_choise = input().lower()

    if acter_choise[0] == "y":
        type_writer_effect(
                    "You choose to do something about it, and by that you suddenly sneak to the backroom of the building."
        )
        type_writer_effect(
                    "Unfortunately, One choice of the robbers that’s looking out in the main lobby sees you. "
        )
        surrenderOrRun = input().lower()
        if surrenderOrRun[0] == "r":
            type_writer_effect(
                        "You rushed and ran as fast as you could to the backroom of the building!!"
            )
            type_writer_effect(
                        "Sadly enough you won't get far because one of the robbers caught you!!"
            )
            type_writer_effect(
                        "As they catch you the police arrived, at outside of the bank!!")
            type_writer_effect("The robbers are about to take Maya as a hostage!!")
            type_writer_effect("What are you going to do?")
            type_writer_effect(
                        "Convince the robbers to take you instead of Maya, or let the robbers take Maya?"
            )
        
        elif surrenderOrRun[0] == "a" :
            type_writer_effect(
                    "They shoot you right where you are. You are taking your last breaths and thinking about every detail of Maya's face: her eyes, the way she talks, the way she looks, the way she smiles, the way she laughs, and the way she walks. Last breath, the last image of Maya's face, the last image of her smile, the last image of her eyes. The final drop of tears, breath, and heartbeat."
            )
            youOrMaya = input().lower()
            if youOrMaya[0] == "m":
                    type_writer_effect(
                        "You let them take Maya, but sadly because of that she get killed by the criminals after threatening the police by using her as a shield."
                    )
                    type_writer_effect(
                        "After the accident, you feel demolished inside, and you feel that you made the worst decision of your life."
                    )
                    type_writer_effect(
                        "Now years past and everyday you think about the day that you really had the choice of saving the one who you loved most in yourlife, but you didn't"
                    )
            else:
                    type_writer_effect(
                        "You conivinced the criminals on taking you as a hostage by showing them the secret way they could escape from the police."
                    )
                    type_writer_effect(
                        "As expected the robbers agreed to your deal and you were on your way to go outside of the bank from the secret way!!"
                    )
                    type_writer_effect(
                        "After getting out of the bank and running a few blocks away, the police sees you and started shooting bullets at you since officially you are a criminal too after helping them get out of the bank."
                    )
                    type_writer_effect(
                        "You and the robbers ran to different directions, but one of the robbers surprisingly got killed by the cops!!"
                    )
                    type_writer_effect(
                        "The dead robber held a full bag of money with him, so you decided to take it with you."
                    )
                    type_writer_effect(
                        "After some desperate time trying to survive the cops you finally survived with a full bag of money!!"
                    )
                    type_writer_effect(
                        "But since you have no way back to go to your hometown again you have to leave the country and start a new life."
                    )
                    type_writer_effect(
                        "You cross the border of the USA to Mexico. You no longer have to work a day in your life and can spend your time the way you like."
                    )
        else:
            type_writer_effect("You surrendered to the criminals")
            type_writer_effect("Fortunately, after surrending the police arrived, outside of the bank!!")
            type_writer_effect("The robbers are about to take Maya as a hostage!!")
            type_writer_effect("What are you going to do?")
            type_writer_effect("Convince the robbers to take you instead of Maya,or let the robbers take Maya?")
            youOrMaya = input().lower()
            if youOrMaya[0] == "m":

                    # This means that you decided to let them take Maya
                    type_writer_effect(
                        "You let them take Maya, but sadly because of that she get killed by the criminals after threatening the police by using her as a shield."
                    )
                    type_writer_effect(
                        "After the accident, you feel demolished inside, and you feel that you made the worst decision of yourlife."
                    )
                    type_writer_effect(
                        "Now years past and everyday you think about the day that you really had the choice of saving the one who you loved most in yourlife, but you didn't"
                    )
            else:
                    type_writer_effect(
                        "You conivinced the criminals on taking you as a hostage by showing them the secret way they could escape from the police."
                    )
                    type_writer_effect(
                        "As expected the robbers agreed to your deal and you were on your way to go outside of the bank from the secret way!!"
                    )
                    type_writer_effect(
                        "After getting out of the bank and running a few blocks away, the police sees you and started shooting bullets at you since officially you are a criminal too after helping them get out of the bank."
                    )
                    type_writer_effect(
                        "You and the robbers ran to different directions, but one of the robbers surprisingly got killed by the cops!!"
                    )
                    type_writer_effect(
                        "The dead robber held a full bag of money with him, so you decided to take it with you."
                    )
                    type_writer_effect(
                        "After some desperate time trying to survive the cops you finally survived with a full bag of money!!"
                    )
                    type_writer_effect(
                        "But since you have no way back to go to your hometown again you have to leave the country and start a new life."
                    )
                    type_writer_effect(
                        "You cross the border of the USA to Mexico. You no longer have to work a day in your life and can spend your time the way you like."
                    )
    else:
        # You decided on not doing anything and save yourself
        type_writer_effect(
                    "Unfortunately, because you didn't do anything the criminals caught your crush and the bank got robbed."
        )
        type_writer_effect(
                    "After that horrible day that ocurred to you, you ended up by living the rest of your life regreting because of not doing anything that day."
        )

        type_writer_effect(
                    "You are now living your life in a state of depression and you feel that you made the worst decision of your life."
        )

    print(colours["red"] + "Did you notice that we have not used", name,
                    "in this story?" + colours["end"])

if __name__ == '__main__':
    ring()