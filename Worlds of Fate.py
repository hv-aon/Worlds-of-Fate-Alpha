import random
import secrets
import time
import sys
import shelve

# hi. if you're reading this you're either me, a friend of mine, or some random guy who's decided to dig through the files.
# well i'm gonna explain some bits for ya so better pay attention
# also i have a few complaints about python, why is there no goto command??? or even an easy to understand inventory thing???
# so i just got a goto module
# anyways without further ado lets get into it

# little note: this is all pretty much spaghetti code because ai sucks and i refuse to use it. all the results on google are for "HoW tO mAkE yOuR oWn AdVeNtUrE gAmE wItH AI"
# (Artificial Incompetence), but this style of code is so much more charming

name = None
placement = [0, 1] # creates a list to save the player's place
inventory = set() # inventory code

shelfFile = shelve.open('SaveFile.txt', writeback=True)
shelfFile['nameVariable'] = name
shelfFile['placementVariable'] = placement
shelfFile['inventoryVariable'] = inventory
# above is code to implement the upcoming save feature

spawn = secrets.choice((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) # randomly or pseudo-randomly generates number to spawn you in one of five places

print("VER a 0.1")
time.sleep(3)
print("__THIS GAME IS CURRENTLY UNFINISHED AND IN AN EARLY STATE OF DEVELOPMENT, AND THEREFORE SAVING IS NONEXISTENT. I AM WORKING ON IMPLEMENTING IT, SO FOR NOW I RECCOMEND WRITING YOUR CHOICES SOMEWHERE TO 'SAVE' OR JUST KEEP THE APP OPEN.__")
time.sleep(2) # causes the game to wait before the next line of text
print("__Hey! Join the Discord server in the description of this itch.io page or subscribe to Woilef's YouTube channel (far more infrequent) to recieve notifications when this game is updated!__")
print(" ")
time.sleep(3)
print("HV AON PRESENTS...")
time.sleep(2)
print("Worlds of Fate")
print(" ")
time.sleep(3)
print("Greetings, stranger.")
while True: # begins a loop
    time.sleep(2)
    print("What is your name?")
    name = input() # makes the player's text an answer to the question
    time.sleep(1)
    print(f"Ah... {name}. Yes...") # {name} is the player's answer to "What is your name?"
    time.sleep(1)
    print(f"{name} is your name?")
    answer = input().lower() # this will occur many times, signifies that variable answer is an input that will always be processed as lowercase
    if answer == "no":
        continue # if it's not your name, restarts the loop
    elif answer == "yes":
        print(f"Greetings, {name}.")
        break # if it is your name, breaks the loop
time.sleep(2)
print("You will now enter this world.")
time.sleep(2)
print(f"Goodbye, {name}...")
placement.append(2) # adds 2 to variable placement's list
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(2)
if (spawn == 1, 8, 3): # uses randomly generated code to spawn you here. happens four times
    print("*A beam of light hits your eyes. It seems to be coming from your window, by the direction of it. You roll over and groan.")
    time.sleep(3)
    print("*After a few seconds you finally get up. You take a shower, brush your teeth, put on some clothes, and step out of your room. You walk downstairs and enter the kitchen, because you're starving.*")
    time.sleep(3)
    print("*You can make three meals: eggs, a bagel, or a bowl of cereal.*")
    answer = input().lower()
    if answer == "eggs":
        time.sleep(2)
        print("*You crack the eggs over a bowl and whisk them. Then, you turn on the stove and place butter on it. You melt the butter and move the pan to spread it evenly.*")
        time.sleep(3)
        print("*Then you pour the whisked eggs into the pan and scrape them with a spatulaas to harvest their scrambled form. Once no liquid egg is left, you grab a plate, turn off the stove, and pour the eggs onto the plate.*")
        time.sleep(3)
        print("*You put the bowl, whisk, pan, and spatula into the sink, and add a little salt to the scrambled eggs and eat them.*")
    elif answer == "bagel":
        time.sleep(2)
        print("*You put the bagel into the toaster, and wait until they're properly toasted. You grab a plate and put the bagel on it.*")
        print("*Add cream cheese?*")
        answer = input().lower()
        if answer == "no":
            time.sleep(1)
            print("*You eat a bland, but crunchy, bagel.") # nobody wants to eat a bland bagel
        elif answer == "yes":
            time.sleep(1)
            print("*The flavor of the cream cheese explodes in your mouth. It's delicious.*") # now thats better
    elif answer == "bowl of cereal":
        time.sleep(2)
        print("*You grab a bowl, a box of your favorite cereal (LEGALLY DISTINCT HONEY FLAVORED CRUNCHY CIRCULAR SHAPED CONFECTIONARY Os), and a carton of milk.*")
        print("*Do you add the milk before or after pouring the cereal?*")
        answer = input().lower()
        if answer == "after":
            time.sleep(2)
            print("*You pour the milk after pouring the cereal and enjoy your LEGALLY DISTINCT HONEY FLAVORED CRUNCHY CIRCULAR SHAPED CONFECTIONARY Os.*")
        elif answer == "before":
            time.sleep(2)
            print("*You monster. You disgrace of a human being. Enjoy your last five seconds of this run of the game.*") # this person is a fool for putting the milk in before
            time.sleep(5)
            placement = 0 # resets placement
            name = None # removes name
            shelfFile.close # saves the above... probably...
            print("*I hope you have learned your lesson. There is only one option: type the word kill.*") # stops the game, provides choice
            print("ENDING 0: You Are A Monster")
            exitgame = input().lower()
            if exitgame == "kill":
                sys.exit()
            else:
                sys.exit()
    time.sleep(2)
    print("*You finish eating, when from the door, you hear the thud of mail. You get up and place your dishes into the sink. You think to yourself, 'What could it possibly be...'*")
    time.sleep(3)
    print("*You grab the mail. It's addressed to you. You open it immediately and a piece of paper falls out.*")
    time.sleep(3)
    print(f"*Your eyes glide over the paper. 'Dear {name}...' You reach the end of the paper. 'Your application to Wyrd University has been accepted, and we are awaiting your arrival.*")
    time.sleep(3)
    print("*You beam with gladness and pride. You run upstairs to your room and begin packing.*")
    time.sleep(2)
    print("__TWO DAYS LATER__")
    time.sleep(2)
    print("*You have finished packing up. Your parents have agreed to keep the things too large for a dormitory, like your bed. So all you have are your clothes, devices, a few plants, and some knicknacks.*")
    time.sleep(3)
    print("*Your parents have offered you a frying pan, perhaps as a joke. You took it anyways-can't say no to a frying pan!*")
    inventory.add('Pan') # adds pan to inventory = set()
    panattribute = 1 # variable to add pan to inventory
    time.sleep(3)
    print("*You load your car, say goodbye to your family, and leave. Your next destination: Wyrd University.*")
elif (spawn == 2, 5, 6):
    print("*A beam of light hits your eyes. You wake up, and feel the hard wood and metal of the bench press against your back. You sit up.*")
    time.sleep(3)
    print("*You had decided to rest there, as you had just finished a bike race with some friends. You check the time-you've been asleep for an hour.*")
    time.sleep(3)
    print("*You get up and walk towards your apartment building. Along the way, you spot a key. It seems to have been sitting there for years.*")
    time.sleep(3)
    print("*Pick it up?*")
    answer = input().lower() # checking the inventory didnt work, so i had to split each path. hoping that doesnt happen again.
    if answer == "yes":
        time.sleep(1)
        print("*You pick up the key, and continue walking.*")
        inventory.add('Rusted_Key') # adds key to inventory = set()
        keyattribute = 1 # variable to add key to inventory
        time.sleep(2)
        print("*You enter the building. The doors open automatically, and you approach the person at the front desk. Do you ask the front desk person about your rusted key?*")
        answer = input().lower()
        if answer == "yes":
            time.sleep(1)
            print("*They lean over the desk and inspect your key.*")
            time.sleep(2)
            print("Front Desk Person: Huh, it's not one of ours.")
            time.sleep(2)
            print("*You thank them, pocket the key, and continue walking.*")
        elif answer == "no":
            time.sleep(1)
            print("*You say hello to them and continue walking.*")
    if answer == "no":
        time.sleep(1)
        print("*You don't pick up the key, and continue walking.*")
        time.sleep(2)
        print("*You enter the building. The doors open automatically. You say hello to the person at the front desk and continue walking.*")
    time.sleep(2)
    print("*You pass by many doors on your way to your apartment. Finally, you get there-floor 1, room 28-and in front of it lies an envelope.*")
    time.sleep(3)
    print("*You grab the mail. It's addressed to you. You open it immediately and a piece of paper falls out.*")
    time.sleep(3)
    print(f"*Your eyes glide over the paper. 'Dear {name}...' You reach the end of the paper. 'Your application to Wyrd University has been accepted, and we are awaiting your arrival.*")
    time.sleep(3)
    print("*You beam with gladness and pride. You unlock your door and begin packing.*")
    time.sleep(2)
    print("__ONE DAY LATER__")
    time.sleep(2)
    print("*You've packed all your clothes and knicknacks and other items. You're ready to leave. You carry everything in a few boxes to your car, turn in your apartment key, and stop by your room one last time.*")
    time.sleep(3)
    print("*You look at it with a sense of nostalgia, before closing the door and entering your car.*")
    time.sleep(3)
    print("*Your next destination: Wyrd University.*")
elif (spawn == 4, 7, 9):
    print("*A beam of light hits your eyes. You're laying on a hammock, dangling between two trees. You're outside of your friend's house (you pay rent to live there currently).*")
    time.sleep(3)
    print("*You climb down from the hammock and untie it, shoving it into your pack that you just so happen to have. You then walk into your friend's house-he had left to go buy some groceries.*")
    time.sleep(3)
    print("*At the front door is a game console. You've never seen it before. There's a sticky note on it saying, 'In case you get bored.' Play it?*")
    answer = input().lower()
    if answer == "yes":
        print("*You pick up the game and turn it on...*")
        time.sleep(2)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(2)
        print("You are now trapped within a game MWAHAHHAA. If you could not tell, I am the villain of this game.")
        print("So anyways go play this short and fun game with four endings")
        time.sleep(5)
        print("*You awake, laying on the floor of an old-timey tavern. Above you, a concerned JOHN FREAKING ADAMS is trying to wake you up.*")
        time.sleep(2)
        print("John Adams: Hey, are you awake?")
        time.sleep(1)
        print("*You lift your head up off the ground.*")
        time.sleep(2)
        print("John Adams: By god, you are awake! Thank the Lord you are alive. That random guy with a frying pan knocked you out pretty hard..")
        time.sleep(3)
        print("You have two options: 'Frying pan...? What are you talking about?' and 'Who hit me with a frying pan???'. Answer with one or two")
        answer = input().lower()
        if (answer == 'one'):
            print("John Adams: Oh yeah i guess you weren't conscious to see him hit you")
        elif (answer == 'two'):
            print("John Adams: I couldn't catch his name, sorry man.")
        time.sleep(2)
        print("John Adams: Oh yeah, I never got your name... what is it?")
        name_ingame = input()
        time.sleep(2)
        print(f"John Adams: Ok hello {name_ingame}, anyways lets go find this guy who hit you with a frying pan")
        time.sleep(2)
        print("*John Adams has joined your party.*")
        time.sleep(1)
        print("*You and John Adams are now searching through the tavern for the man who hit you on the head with a frying pan.*")
        time.sleep(2)
        print("John Adams: Oh hey Edgar!")
        time.sleep(1)
        print("*You look around for this Edgar person.*")
        time.sleep(1)
        print("Edgar: Oh hey John!")
        time.sleep(1)
        print("*You turn to the sound of this voice. It's... Edgar Allen Poe?!*")
        time.sleep(2)
        print("*You ask John Adams something. (One: 'Who is this?'; Two: 'How do you know Edgar Allen Poe?!'*")
        answer = input().lower()
        if (answer == 'one'):
            print(f"John Adams: This is Edgar Allen Poe, my poet friend. Edgar, this is {name_ingame}.")
        elif (answer == 'two'):
            print(f"John Adams: Yeah I've known him basically all my life! Oh, and Edgar, this is {name_ingame}.")
        time.sleep(2)
        print("Im getting bored so this is version alpha 1 haha bye see you next update")
        time.sleep(2)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(2)
        print("*You throw your head back with a frustrated sigh-you were actually beginning to like the game-and pocket the device.*")
        inventory.add('Gaming_Device') # adds game to inventory = set()
        gameattribute = 1 # variable to add game to inventory
    elif answer == "no":
        print("*You ignore the device and move on.*")
    time.sleep(2)
    print("*As you walk into the kitchen, you notice an envelope addressed to you. You rip it open.*")
    time.sleep(2)
    print(f"*Your eyes glide over the paper. 'Dear {name}...' You reach the end of the paper. 'Your application to Wyrd University has been accepted, and we are awaiting your arrival.*")
    time.sleep(3)
    print("*You beam with gladness and pride. You're already packed, so you just throw a 50 on the counter with a note: 'Off to university. See ya soon!' and hop in your car.*")
    time.sleep(3)
    print("*Your next destination: Wyrd University.*")
elif (spawn == 10, 12):
    print("*A beam of light hits your eyes. You wake up, and feel the hard wood and metal of the bench press against your back. You sit up.*")
    time.sleep(3)
    print("*You stand up. You don't have anywhere to be right now, so you just walk around, admiring all the items within the stores around you.*")
    time.sleep(3)
    print("*After a few minutes of walking, you stumble upon a rusted key. Take it?*")
    answer = input().lower()
    if answer == "yes":
        time.sleep(1)
        print("*You pick up the key, and continue walking.*")
        inventory.add('Rusted_Key_Secret') # adds SECRET key to inventory = set()
        keysecretattribute = 1 # variable to add SECRET key to inventory
    elif answer == "no":
        print("*You understand that this is someone else's property and carry on with your life.*")
        time.sleep(2)
        print("ENDING 2: Carrying On")
        sys.exit
    time.sleep(1)
    print("*Something compels you to take it to the post office, so you do. When there, you find the box with the same number as the key has on it... a 101.*")
    time.sleep(3)
    print("*It's rusted. Inside is a piece of mail addressed to... you? You open it and begin reading the contents.*")
    print(f"*Your eyes glide over the paper. 'Dear {name}...' You reach the end of the paper. 'Your application to Wyrd University has been accepted, and we are awaiting your arrival.*")
    time.sleep(3)
    print("*You're confused. You never made an application to this university... you're still glad you found it, though, and walk back to the square. You grab your bike, and begin biking to your next destination: Wyrd University.*")
elif (spawn == 13):
    print("idiot")
    time.sleep(30)
    print("ENDING 1: Idiot")
placement.append(3)
time.sleep(3)
print("Update a 0.2, coming soon.")
shelfFile.close # maybe saves?


