import time

from . import Questionhandler


def type_writer_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)  # Adjust the sleep time for the desired speed
    print()  # Print a new line after the text is typed out

def tradition():
    type_writer_effect("You are a young Kurdish girl, Nawroz festivities has just finished and you are in a crowded place.\n")
    type_writer_effect("You are standing at the opening of the Bazaar, it is late afternoon and the sun is starting to cast shadows on the hanging persian rugs.\n")
    type_writer_effect("People are everywhere you turn, and you are starting to feel frantic.\n")
    type_writer_effect("It is nearly impossible to find the little store you bought the damned fire-lamp from.\n")
    type_writer_effect("You are starting to feel dizzy, your grandmother's voice starts to echoing in angry tone:\n")
    type_writer_effect("'How many times do I have to tell you to stop buying old people’s trinkets?'\n")
    type_writer_effect("'This lamp has the emblem of the jinn. Did you light its fire?'\n")
    type_writer_effect("A shiver runs down your spine, you push through the crowd frantically. You just wanted to help her. The owner said it will help her heal if you pray over it.\n")
    type_writer_effect("You run around frantically. It cannot be true, you did not worship the jinn, you just.\n") 
    type_writer_effect("You just...\n") 
    type_writer_effect("'I cannot believe you lit it!' your grandmother yelled at you, 'I thought you were my witty girl, how could you wake the jinn!'\n")
    type_writer_effect("Her disappointment and anger still squeezes at your heart, you shake yourself into action. What do you do?\n")
    type_writer_effect("1. Break the lamp in hopes that it will put the jinn back into slumber\n")
    type_writer_effect("2. Find the store in hopes of rectifying what you did.\n")

    response = Questionhandler.question_response("Enter your numerical answer:", "1", "2")

    if response == "1":
        type_writer_effect("You break the lamp and wait in suspense.\n") 
        type_writer_effect("Nothing.") 
        type_writer_effect("You wait for hours, days. Nothing.\n")
        type_writer_effect("Odd things start to happen around town, store owners lose business, tourists stop visiting.\n")
        type_writer_effect("Monuments close down, factories clog up.\n")
        type_writer_effect("You chalk it up to bad economy, plus you are too busy taking care of your sick grandmother.\n")
        type_writer_effect("Until one night you hear her muffled screams, you rush to her room.\n")
        type_writer_effect("Horrified at the sight you let out a weakened squeak as you watch your grandmother cradled in the arms of a phantomenous figure.\n")
        type_writer_effect("White mist is being pulled out of her open mouth as she heaves out her last breaths.\n")
        type_writer_effect("The figure is rumbling, you realize it is laughing at you.\n")
        type_writer_effect("'You are too late,' it says, 'should have prayed and surrendered her soul long ago.'\n")
        type_writer_effect("'I am sorry,' you say, 'I am sorry for what I did. I thought if I break your lamp...'\n")
        type_writer_effect("The figure turns to you, 'You are no jinn! you cannot undo what has been done, you do not have access to that realm!'\n") 
        type_writer_effect("'Humans can only rectify what they have done, but it is too late! You forced me to take her soul to the land of the damned, look what your foolishness has done.\n'")
        type_writer_effect("'Now you must pay too.\n'")
        type_writer_effect("The figure lunges at you, darkness engulfs and chokes you.\n")
        type_writer_effect("Game Over.")
    elif response == "2":
        type_writer_effect("You chose to rectify what you did, and rectify yourself from damning your grandmother's soul.\n")     
        type_writer_effect("Good choice.")
        type_writer_effect("You finally find the store and you rush to open the door.\n")
        type_writer_effect("But it's locked, damn it! There's a numbered keypad that was not there before, you look up and see the owner snickering at you\n")
        type_writer_effect("'Three riddles answered, that's the key, to bring your fire back to me'\n")
        type_writer_effect("'Damn you! You are forcing me to play your foul game!'\n")
        type_writer_effect("'I am not afraid of you, or your foul games'\n")
        type_writer_effect("'Give me your best shot!'\n")
        type_writer_effect("'I wear a spotted coat, each mark unique, I am used in games, where snakes reside over ladders. I am in the name of a Turkish game. I tempt you with chance, a playful dare, How many faces do I wear?'\n")

        response = Questionhandler.question_response("Enter your numerical answer:", "6", "6")

        if response == "6":
            type_writer_effect("'Not so fast, there are two more riddles to go'\n")
            type_writer_effect("'Shapes come in all sorts of sizes, From squares of four to circles of none, edged with angles, sharper than your wit. A triangle stands with sturdy might, How many corners guide its wit?'\n")
        else:
            type_writer_effect("'You are not worthy of meeting the jinn, you cannot save your grandmother, go home and let her live the rest of her days in peace. Goodbye'\n")
            type_writer_effect("Game Over.")

        response = Questionhandler.question_response("Enter your numerical answer:", "3", "3")

        if response == "3":
            type_writer_effect("'One more to go!'\n")
            type_writer_effect("'Think of religious significance as a hint'\n")
            type_writer_effect("I hold the crescent moon, I sit on a worldly throne that spans the life itself, I wield souls from soil and singularly weave the story of your death, how many of me are there?\n")
        else:
            type_writer_effect("'You are not worthy of meeting the jinn, you cannot save your grandmother, go home and let her live the rest of her days in peace. Goodbye'\n")
            type_writer_effect("Game Over.")

        response = Questionhandler.question_response("Enter your numerical answer:", "1", "1")

        if response == "1":
            type_writer_effect("'You have answered all the riddles correctly, you may now enter the store'\n")
            type_writer_effect("You quickly unlock the door, and right when you want to pit the lamp down, the owner cackles. 'Not so fast!'\n")
            type_writer_effect("'What is it?', you say, exasperated.\n")
            type_writer_effect("You cannot return the lamp, once it has lit, you must find the rightful owner!\n")
            type_writer_effect("You ask,'who is the rightful owner?'")
            type_writer_effect("You wait for a second and then angrily say, 'but you never told me the conditions when you sold it to me!\n'")
            type_writer_effect("He replies, mirthlessly: 'Had I told you what it was, would you have bought it from me? You were drawn to it when you saw it, who am I to come in the way of fate? Alas! \n'")
            type_writer_effect("'This is the way of life, you can never know what is in store for you. But I have a map to help. \n'")
            type_writer_effect("'What map!?', you ask. \n'")
            type_writer_effect("'The map to the Jinn's \n")
            type_writer_effect("The Div, a malevolent jinn's tavern. \n")
            type_writer_effect("The Jinn is said to reside in the abandoned tavern on the city outskirts, he has always been a hushed nightmare. \n") 
            type_writer_effect("You still have a choice foolish girl, what do you want to do?\n")
            type_writer_effect("\n1. Go to the tavern and appeal to the jinn for mercy\n")
            type_writer_effect("\n2. Go back to your grandmother's home and forget the deaths to come\n")

            response = Questionhandler.question_response("Enter your numerical answer:", "1", "2")

            if response == "1": 
                type_writer_effect("You ask the owner to give you the map to head on your adventure. \n")
                type_writer_effect("You decide you are going to not tell anyone where you are going. \n")
                type_writer_effect("You take a three day journey to get to the tavern. \n")
                type_writer_effect("You arrive at the tavern, and the owner greets you. \n")
                type_writer_effect("'What could a young girl like you want to do here?'\n")
                type_writer_effect("You respond, somberly, 'I want to talk to the Jinn.'\n")
                type_writer_effect("The owner looks you up and down, then he says, 'if you want to talk to the jinn, you must answer my riddles.'\n")
                type_writer_effect("'What is the first riddle?'\n")
                type_writer_effect("'I whisper secrets in the wind, yet leave no voice behind.'\n")
                type_writer_effect("'I can appear in human form, but vanish in a passing storm.'\n")
                type_writer_effect("'What am I?'\n")
                type_writer_effect("'1. Elves'\n")
                type_writer_effect("'2. Witches'\n")
                type_writer_effect("'3. The Jinn'\n")

                response = Questionhandler.question_response("Enter your numerical answer:", "1", "3")

                if response == "1": 
                    type_writer_effect("'You are incorrect, elves are ethereal beings that do not appear in other forms but their own perfect form. \n'")
                    type_writer_effect("'You are not ready to face the jinn, go home. \n'")
                    type_writer_effect("'Game Over. \n'")
                elif response == "2": 
                    type_writer_effect("'You are incorrect, witches cannot stand the human form. \n'")
                    type_writer_effect("'You are not ready to face the jinn, go home. \n'")
                    type_writer_effect("'Game Over.'")
                elif response == "3":
                    type_writer_effect("'Ah, so you are not just some foolish girl after all!\n'")
                    type_writer_effect("'You are not what I thought you are,'says the jinn, amused.\n'")
                    type_writer_effect("'Neither are you,'you say audaciously\n'")
                    type_writer_effect("Fiery anger flickers in his eyes, his amusement turns into anger, 'so, grandma's little witty girl thinks she understands what the world is about!'\n'")
                    type_writer_effect("angered and a little embarrassed, you say:'what do you want from me?'\n'")
                    type_writer_effect("The jinn's eyes narrow, 'Who said I want anything from you wiseass? I do not like people like you. \n'")
                    type_writer_effect("You stare at him, tears welling up at your throat. \n") 
                    type_writer_effect("'I tell you what,' if you can prove to me that you have become wise, I will let go of your grandmother's soul. \n'")
                    type_writer_effect("You nod, 'I will do it.'\n'")
                    type_writer_effect("'I have no voice, yet I can speak volumes.\n")
                    type_writer_effect("I have no body, yet I can travel the world.\n")
                    type_writer_effect("I have no eyes, yet I can witness all.\n")
                    type_writer_effect("I have no life, yet I can destroy empires.\n")
                    type_writer_effect("What am I?'\n")
                    response = Questionhandler.question_response("Enter your numerical answer:", "rumor", "rumor")
                    if response == "rumor":
                        type_writer_effect("The jinn's eyes narrow, 'You have proven yourself to be worthy of the jinn's favor, \n")
                        type_writer_effect("'I will let you go, and you both will be free from the damned realm. \n'")
                        type_writer_effect("'have a good day.'")
                    else:
                        type_writer_effect("'You are not wise enough to have access to my realm, I am sorry you cannot save your grandmother.'")
                        type_writer_effect("'Game Over.'")
                else: 
                    type_writer_effect("You are wrong, and you are not witty enough to win over the jinn.\n")
                    type_writer_effect("You are forced to leave the tavern, and you are forced to go home. \n")
                    type_writer_effect("Game Over.")
            else:
                type_writer_effect("You are not ready for the jinn, you must go back to your grandmother, & wait for her life to end.\n")
    else:
        type_writer_effect("Invalid input, Game Over.")

if __name__ == '__main__':
    tradition()
