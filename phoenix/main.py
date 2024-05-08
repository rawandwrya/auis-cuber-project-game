import time

def type_writer_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.003)  
    print()  
  
def phoenix():
    print('Please insert your name')
    x = input()
    print('Hello, ' + x)
    type_writer_effect("You can choose between two worlds")
    type_writer_effect("a. Old Medieval world")
    type_writer_effect("b. Futuristic Cyber punk city")
    response = input()
    if response == "a": 
        type_writer_effect("It's Medieval time ")
        type_writer_effect("you're playing as an apathetic man who is riding a horse he's in a green plain")
        type_writer_effect("Every where he looks has a heavenly view")
        type_writer_effect("Waterfalls has changed to water climbs in this fantasy world, rivers and streams reverse back")
        type_writer_effect("However he's a man marked by no emotional response to anything he sees thus make him look like a man who wander around aimlessly.")
        type_writer_effect("After a long ride he rides toward the direction of the villages until he comes across a village that is burnt down by rebels,")
        type_writer_effect("He sees some kids that asks for his help.")
        type_writer_effect("Will you help the kids")
        type_writer_effect("a. Yes")
        type_writer_effect("b. No")
        response = input()
        if response == "b":
            type_writer_effect("The kids are getting vaporized by the black magic.")
            type_writer_effect("you didn't help the kids you lost the game.")
            type_writer_effect("Game Over, You never become a better man.")
        elif response =="a": 
            type_writer_effect("The kids are bounded by black magic.")
            type_writer_effect("You need to solve a riddle to save the kids.")
            type_writer_effect("the riddle is ")
            type_writer_effect("(“I have a sharp nose I can fly with a broom, and I have a sorting hat, what am I ?.”) ")
            response = input()
            if response == "witch":
                type_writer_effect("Good job you solved the riddle the kids are now saved")
                type_writer_effect("The kids will grow up to repay him by eliminating rebels that constitute to the crisis")
                type_writer_effect("He witnesses so many crises that teaches him to become sympathetic,")
                type_writer_effect("He has seen so much of happiness in this heavenly world that he has become desensitized to happiness")
                type_writer_effect("Thus making him need some agony to counterbalance that.")
                type_writer_effect("He learns to appreciate the heaven he has which makes him continue the good deeds to maintain peace in this world.")
                type_writer_effect("From all this he achieves sympathy. ")
                type_writer_effect("Congrats you won.")
            else:
                type_writer_effect("You failed to solve the riddle ")
                type_writer_effect("The kids died you monster why you didn't save them")
    elif response == "b":
        type_writer_effect("It's a Cyber Punk city")
        type_writer_effect("It's a heavenly world,you're playingas an apathetic man who is living in the future and everything looks beautiful, the ultimate utopian city u can imagine.")
        type_writer_effect("The city is futuristic and completely technological, robots are living along with humans here and the mayor here is a robot that is conscious and aware. ")
        type_writer_effect("A giant corporation named ''East India Company'' has manipulated the mayor by hacking him,")
        type_writer_effect("and aims to spread corruption and ruin the utopian image by making him give destructive order.")
        type_writer_effect("Although you're playing as an apathetic man but his instinct is inclined toward freedom,")
        type_writer_effect("He can't let this corporation ruin the beautiful city that needed decades of innovation and invention to become what it is today.")
        type_writer_effect("To retrieve the mayor and not letting this corporation have their way you have to hack the mayor again")
        type_writer_effect("to do this you have to crack password and to do this you need solve a riddle.")
        type_writer_effect("The riddle is")
        type_writer_effect("(8 14 22 , 13 1 15 25  , 22 14 19 4 18 , 1 19 5  , 9 15 ,  20 8  5 ,  1 12 16 8 1 3 5 20) ")#how many words are in the alphabet 
        type_writer_effect("Hint:")
        type_writer_effect("1 = a")
        type_writer_effect("3 = b")
        type_writer_effect("4 = c")
        type_writer_effect("8 = d")
        type_writer_effect("16 = e")
        type_writer_effect("...")
        response = input()
        if response == "none"or"zero"or"0":
            type_writer_effect("You solved riddle the mayor is now free again the city will be saved.")
            type_writer_effect("The people are celebrating and marking him as a hero for saving the city.")
            type_writer_effect("After this incident he gains feelings ")
            type_writer_effect("congrats you won")
        else:
            type_writer_effect("You failed to solve the riddle the company will carry on their plan. ")
            type_writer_effect("The city is destroyed everything is ruined. ")
            type_writer_effect("You failed to save the mayor.")
            type_writer_effect("Game Over")

if __name__=='__main__':
    phoenix()