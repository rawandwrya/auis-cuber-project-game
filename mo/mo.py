import time

def printE(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()

        
def ask_question(question, option1, option2):
    for char in question:
        print(char, end='', flush=True)
        time.sleep(0.003)
    print()
    response = input().lower()
    if response == option1 or response == option2:
        return response
    while response != option1 or response != option2:
        for char in "Invalid input, try again":
            print(char, end='', flush=True)
            time.sleep(0.003)
        print()
        response = input().lower()
        if response == option1 or response == option2:
            break
    return response      

def unknown():
  printE("Hello Mr.user, welcome to the game.")
  printE("Your name is Aegis the Iron Heart, are you brave enough to deserve the title?")
  response = ask_question("Yes or no", "yes", "no")

  if response == "no":
      printE("You are not brave enough to fight")
      printE("Game Over")

  if response == "yes":
      printE("Good, you are ready to begin your journey.")
      printE("You live in a secluded mountain village with your beloved wife.")
      printE("The days are filled with the rhythmic clang of your hammer on glowing metal,")
      printE("the sound of your sword clashing with the rocks of the mountain.")
      printE("The nights are peaceful, spent in the warm embrace of your wife, sharing stories")
      printE("by the crackling fire about long-lost dragons and the sacred mountain rituals.")
      printE("Little did you know that fires, when started, cannot always be muffled.")
      printE("On the fateful night that you walked home, horror gripped your heart as you")
      printE("see the raging snarls of the flames eat away at your house.")
      printE("You feel paralyzed as you stare at the gaping fire, then you remember your father's words:" )
      printE("'you have were never worthy of this bloodline. You are not worthy of the title of Iron Heart.'")
      response = ask_question("""You have two options, you can either:
      1. Run away and never return
      2. Stay and fight for your life""", "1", "2")
      if response == "1":
          printE("You run away from the fire and never return.")
          printE("Your wife's gasping cries haunt you to eternity")
          printE("You have failed to deserve the title of Iron Heart.")
          printE("You will never see the light of sanity again.")
          printE("Game Over.")
      elif response == "2": 
          printE("You decide to stay and fight for your life.")
          printE("You gather your strength and prepare for the fight of your life.")
          printE("You stand before the fire, ready to face whatever lies ahead.")
          printE("However, it took you too long to decide, your wife doesn't survive the fire.")
          printE("Grief and rage surge within you, are you the type of man that seeks vengeance?")
          response = ask_question("""You have two options, you can either:
      1. Let grief and rage consume you
      2. Vow vengeance against the culprit""", "1", "2")
          if response == "1":
            printE("You die of heartbreak and shame.")
            printE("You have failed to deserve the title of Iron Heart.")
            printE("You will never see the light of day again.")
            printE("Game Over.")
          elif response=="2": 
            printE("You vow to avenge your wife's death and defeat the culprit.")
            printE("you run to your villagers, and you gather enough water to turn the fire down.")
            printE("as you walk through the ruins of the life you used to have, you notice a shining emblem.")
            printE("you walk across the house, with memories cracking beneath your feet.")
            printE("your heart beats beyond the grief, blood is rushing through your veins.")
            printE("could it be?")
            printE("you haven't seen emerald so rich since you were a child.")
            printE("you quickly dust away the remnants of your house, and pick up the emblem.")
            printE("you swallow the dust of your thoughts, and realize, with horror, that it is the emblem of the dragon.")
            printE("you have two options, you can either:))")
            printE("1. brush it off as dragons have long gone extinct")
            printE("2. take matters into your own hands")
            response = ask_question("What is your decision? ", "1", "2")
            if response == "1":
              printE("coincidences do not exist my friend.")
              printE("things do not materialize out of the blue.")
              printE("the emblem was the dragon's emblem, who was in hibernation for the past century.")
              printE("you have failed to follow your calling, the village will be burnt down soon.")
              printE("Game Over. Goodbye.")
            elif response =="2": 
              printE("you take the emblem and run back to your village.")
              printE("you gather all the weapons you have yielded and gather the brave men of your village.")
              printE("you realize that you do not know where the lair lays.")
              printE("A Wise old man, Erdur, you know resides in a small hut.")
              printE("You take your fellowship and strode towards the hut.")
              printE("You hand over your embelm. Using his imense knowledge, the wise man examines its peculiar rune")
              printE("there is a riddle written by dwarves on this emblem, I will translate it for you.")
              printE("His voice resoundedly says: I am a long, flowing stream, A single word, yet not a dream. What am I?")
            answer = ask_question("What is the answer?", "river", "river")
            if answer == "river":
              printE("You look at Old Man Warner, and he smiles.")
              printE("He says: did you understand Aegis?")
              printE("You hesitantly respond: is it ironriver?")
              printE("He says: legend says your ancesters fought the dragons there, and your name comes from that war.")
              printE("are you worthy of it?")
              printE("the men around you nod, and you nod in somber recognition. 'We must go to the cursed blue mountain', you say.") 
              printE("you and your party head to the blue mountain, tread carefully, the wind is howling.")
              printE("it howls so strong that a boulder falls in front of your path.")
              printE("do you a. go back or b. do you push it off the cliff?")
              response = ask_question("What do you choose?", "a", "b")
              if response == "a": 
                printE("it wasnt the wind that blew the rock in your way it was the dragon, it will eat all the men in your party.")
                printE("you have failed to deserve the title of Iron Heart.")
                printE("Goodbye. Game Over.")
              elif response == "b":
                printE( "you push the boulder off the cliff and it falls into the river.")
                printE("the splasing noise grabs the attenstion of the dragon")
                printE("his massive flapping wing starts to shadow your party, he is the dragon king.")
                printE("you and your men stare up in awe as he turns daylight into night, towering above you.")
                printE("you and your men charge into battle, you are the only one who can defeat him.")
                printE("but the dragon is unfazed by the arrows being shot at him, he gives an awful rumbling laugh.")
                printE("you and your men charge at him, but he is too fast, he grabs you and flies away with you.")
                printE("you stare down at your men yelling in despair and feel fear grip your heart, is this the end?")
                printE("the dragon, as if sensing your fear, speaks to you.")
                printE("he says, in a rumbling burnt tenure, 'you fool, I am not going to kill you. Quit squirming like a mouse.'")
                printE("surprised, try to look at him but you cannot see anything until you reach his lair.")
                printE("you try to attack him there but the dragon simply blows his nose at you and you fall back stumbling.")
                printE("you look up at him and he is staring at you almost disappointed")
                printE("He says, 'His bravery was as foolish as it was insulting to intelligence. Did you ask yourself, you foolish man, where your wife's corpse is?''")
                printE("you stare at him, confused.")
                printE("he says, 'would a criminal leave the weapon at the scene of the crime?'")
                printE("you feel a delirious, your heartbeats feel faint as you try to remember what happened.")
                printE("'your father was as hotblooded as you were, that is why those witches killed him!'")
                printE("'did you never ask yourself why her womb bore you no children?'")
                printE("'witches are barren when not married to their own kind'")
                printE("'you have been fooled, it is time to wake up.'")
                printE("You have two options here player, do you believe him, or not?")
                printE("1. Believe him")
                printE("2. Do not believe him")
              response = ask_question("What do you choose?", "1", "2")
              if response == "1":
                printE("you decide to believe him, and when your men finally arrive you tell them the full story.")
                printE("some men, like you, have been fooled.")
                printE("the village was slowly dying and that was the witches plan all along.")
                printE("they were the ones who killed your father.")
                printE("you swear vengeance on them, but that's a story for another day, thank you for playing wisely visitor.")
                printE("Have a nice day. Goodbye.")
              elif response == "2":
                printE("you decide to not believe him, and you try to fight the dragon.")
                printE("the dragon realizes you are in denial")
                printE("he blows soot filled air in your face, and you fall back asleep.")
                printE("the next day you wake up with your family alive, but you remember the truth.")
                printE("you have no proof of this truth, you waste away in insane denial.")
                printE("to have an iron heart means to face unpleasant realities.")
                printE("Do better next time. Goodbye.")
            else: 
              printE("you are incorrect, the answer was river, you run on a wilde goose chase, and the dragon burns the village down.") 
              printE("you have failed to follow your calling, the village will be burnt down soon.")
              printE("Game Over. Goodbye.")  

if __name__=='__main__':
   unknown()