import time
from colorama import Fore
from . import QuestionHandler


def type_writer_effect(text):
  for char in text:
    print(char, end='', flush=True)
    time.sleep(0.0003)  # Adjust the sleep time for the desired speed
  print()  # Move to the next line after the text is fully typed

def hope():
  good = 0
  evil = 0
  type_writer_effect("Hello user, welcome to the game \"Hope\".\n")
  type_writer_effect(
      "Your name is Lloyd and you are a traveler who travels throgth contrys \nand you have the power of lightning itself and in your journey you found yourself in a village.\n"
  )
  input(Fore.GREEN + "press enter to continue.... \n " + Fore.RESET)

  type_writer_effect(
      "You have been traveling for a while and you have decided to take a rest in the Village's bar,\nwhen you go to the bartender you order a drink, the bartendr gives you a drink and looks at you in a strage way and say \n\"well well!, its not everyday you see a strage face in the village,... \ntell me boy! who are you and where are you from? \" said the bartendr.\n"
  )

  input(Fore.GREEN + "press enter to continue.... \n " + Fore.RESET)

  type_writer_effect(
      "Lloyd stayed quiet and started drinking. The bartender told him\n\"this place is not the right place for you kid, you should leave here, you will get into trouble if you stayed for too long.\"\nLloyd finished his drink and stood up, \nhe gave the bartender some extra coins and asked him for directions but the bartender gave him a wrong direction that lead him to thiefs.\n"
  )

  input(Fore.GREEN + "press enter to continue.... \n " + Fore.RESET)

  type_writer_effect(
      "Lloyd started his journey again through the woods and when it became night he got ambushed by nearly 17 thiefs.\nThe bandits leader said \"our prize is big as the information that we got said, catch him alive boys!.\"\n "
  )

  input(Fore.GREEN + "press enter to continue.... \n " + Fore.RESET)

  type_writer_effect(
      "Lloyd didn't understand what he meant, but what the bandits don't know is \nLloyd is a very good swordsman and he have the power of lighting, they started fighting, \nLloyd killed almost all of them then he got to the bandits leader and say \n\"tell me based on which information you said that i'm a big prize? \" \nThe bandits leader said \"haaaah information what do you mean?! I don't know what you're talking about, let me go you brat!!!\"\n"
  )

  # response = input(Fore.RED +"Hit the bandit"+ Fore.RESET +" or "+ Fore.BLUE +"Stay calm "+Fore.RESET+"? ").lower()
  response = QuestionHandler.question_response(
      Fore.RED + "1- Hit the bandit" + Fore.RESET + " or " + Fore.BLUE +
      "2- Stay calm " + Fore.RESET + "?   please choose by number ", "1", "2")
  if response == "1":
    type_writer_effect(
        "Lloyd hit the bandit leader and threten to kill him and scared of his life the bandit leader said \n\"OK! OK! i will tell you everything \" then the bandit leader tells the truth \n\" the bartender said there are a prince that got in to the town and if you catch him and sell him back to his father (the king) \nhe will offer you a big amount of money\" \nLloyd got confused, \"I'm not a prince\" he said, but the bandits leader insist that the bartender confirmed 100% that you are the prince, \n\"this doesn't make any sense how can he confuse me with a prince and be so sure about it?! \" \nsaid Lloyd. He gets back to the village angrily and goes straight to that bartender.\n"
    )

  else:
    type_writer_effect(
        "Lloyd stayed calm and tells the bandits leader that he will set him free if he tells him the truth, \nand the bandits leader sayd \"fine! i will tell you everything\" then the bandits leadre tells the truth \n\"the bartender said there is a prince that got in to the town and if you catch him and sell him back to his father (the king) he will offer you a big amount of money\n\" after that Lloyd get confused, \"I'm not a prince\" he said, \nbut the bandits leader insist that the bartender confirmed 100% that you are the prince, \"this doesn't make any sense how can he confuse me with a prince and how can he be so sure?! \n\" said Lloyd, he gets back to the village calmly to that bartender.\n"
    )

  input(Fore.GREEN + "press enter to continue.... \n " + Fore.RESET)

  if response == "1":
    type_writer_effect(
        "Lloyd got back to the village and asked the bartender angrily \n\"who are you and why you told the bandits to catch me \"Lloyd said grabing the bartender by the collar, and the bartender replays \n\"keep your voice down Mr.prince this place is not the place you want to get a fight into. \n\" Lloyd turn around and look at the bar he see all the people are about to pull their swords. "
    )

  else:
    type_writer_effect(
        "Lloyd goot back to the village and asked the bartender \n\"who are you and why you told the bandits to catch me \" said Lloyd while he is tring to pull his sowrd out, and the bartender smiles and replied \n\"hello again Mr.prince this place is not the place you want to get a into fight at. \" \nLloyd turn around and look at the bar, he saw all the people are about to pull their swords."
    )

  response_2 = QuestionHandler.question_response(
      Fore.RED + "1- Start a FIght!" + Fore.RESET + " or " + Fore.BLUE +
      "2- Don't do anything! " + Fore.RESET + "?    please choose by number ",
      "1", "2").lower()
  if response_2 == "1":
    evil += 1
    type_writer_effect(
        "Lloyd gets angry and pull his sowrd, and he kills everyone in the bar exept the bartender, \nhe went to the bartender and asked him \"why did you mistook me for a prince, TELL ME EVERYTHING YOU KNOW !!.\" said Lloyd angrily,\n\"OK!OK! calm down.\" Said the bartender and he showed him a picture of the royal family and Lloyd got confused because\n he see that the son of the king is exactly looking like him \n\"you must have lost your way am I right?!\" Said the bartender"
    )

  else:
    good += 1
    type_writer_effect(
        "Lloyd stayed calm and put the sowrd down.\"\nyou want to start talking by telling me what are you doing here at this time of the year mr prince ?\" said the bartender. \n \"I'm not a prince you must mistook me for someone else.\" Said Lloyd.\n\" ohhhh did I ? \" Said the bartender showing him a picture of the royal family. Lloyd got confused because he saw that the son of the king is exactly looking like him \n\"hahaha,, you must have lost your way am i right?!\" Said the bartender.\n"
    )

  input(Fore.GREEN + "press enter to continue.... \n " + Fore.RESET)

  type_writer_effect(
      "After that you ask the bartender and he tells you everything about the royal family and their names, \nLloyd gets confused and asks the bartender \"have they lost any part of their family in the past 16 years?\" \nthe bartender thinks a lot and say\" yes!... I heard that they had another son that he got lost, and he is now considered dead\" \nand Lloyd  said \" where did they lose him ? \" The bartender replays \" in the dark forest (BloodMoon Grove) in the far north of the (Caernel), \nthey say he got attacked by wolves when he was only 4 years old!!! And died\", \nat that moment Lloyd gets a flashback like a nightmare, he saw when he was chased by wolves and manage to get away by difficulty, \n\"so it's not just a dream, it's not a coincidence, \nit's the same place that Aldar (the first person who adopt Lloyd when he was just a kid) said he found me when I was a kid, \nhe said when he found me I was in a terrible shape and I didn't eat for a few days and i was wounded and some of the woods looked like a wolf bite."
  )
  input(Fore.GREEN + "press enter to continue.... \n " + Fore.RESET)

  type_writer_effect(
      "Then Lloyd started thinking about his life and realized that he has a family, he has something to live for,\n this is not for Money and fame, this is about having some place to call home.\n He start his journey looking for his family and along the way he will encounter much more difficulty."
  )

  input(Fore.CYAN + ">>> to be continue \n " + Fore.RESET)

  print("good: ", good, "evil: ", evil)

if __name__ == '__main__':
  hope()
