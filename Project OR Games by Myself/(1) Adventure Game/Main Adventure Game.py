import pygame
from time import sleep

# ==================================================SETTINGS===========================================================#
NumberOfTimePlayBackgroundMUSIC = 2000000000


# ==================================================SETTINGS===========================================================#

# Functions
def play_bac_sound(secs):
    pygame.init()
    pygame.mixer.music.load('ratsasan.mp3')
    pygame.mixer.music.play(secs)


def wait(sec):
    sleep(sec)


def call_ghostSOUND():
    pygame.init()
    pygame.mixer.music.load('scary.mp3')
    pygame.mixer.music.play()


def print_space():
    print("")


play_bac_sound(NumberOfTimePlayBackgroundMUSIC)

print_space()

PlayerName = input("Before we Begin the Game, please tell us your Name here: ")

print_space()
print("Saving Your Data...")
wait(3)
print_space()
print(
    "======================================================HOW TO PLAY======================================================")
print_space()
print("1st. Answer all the questions wisely with correct thought in correct situation!")
print_space()
wait(3)
print(
    "2nd. Your main goal is to escape the house and you are a police officer. You character will collect proof every second. You dont have to look after it!")
wait(3)
print_space()
print(
    "HINT: This game is particularly very big but there are only some of the main situations in which you can escape! In Total there are 500+ situations coming Up!")
print_space()
wait(3)
print(
    "CHEATING: Not allowed to see back code!! Not allowed to escape the house in starting of game. Will not count as VICTORY! Option of leaving in starting is for person who dont have time to play and by mistake launch th game!")
print_space()
print(
    "======================================================HOW TO PLAY======================================================")
print_space()
print("Loading the Game...")
wait(2.9)
print_space()

print("==============================================WELCOME TO GAME==============================================")

print_space()
print(f"1. Welcome to the Haunted Mansion, {PlayerName}!")
wait(3)

print(
    "2. You are a police officer, and your head IG has ordered you to explore its secret and prove that this house has ghosts."
    "\nMany people here said this house has a ghost, and some of them don't come out alive!")
wait(5)

print("3. As the OFFICER, you agreed and will visit this house!")
wait(2.5)

print("4. The house is dated, creaky, and falling apart. As you entered, there were 3 gates in front of YOU!")
wait(2.5)

print("On the top of the Gates, there was written where the Gates Go.")
wait(2.4)

print_space()
print("========================================GAME STARTED========================================")
print_space()

print(f"Which Gate {PlayerName} do you want to Go in? \n 1. Gate(1) Living Room \n 2. Gate(2) Dining Room "
      f"\n 3. Gate(3) Main Hall \n 4. Leave the House")

roomChoice = input("> ")

if roomChoice == "4":
    print("You Choose to leave the house!")
    wait(0.9)
    print("You then decided that you would come to this house later and explore its secrets!")
    wait(1)
    print("Your IG will give you half your salary for this month because of not exploring this house!")
    wait(1.8)

elif roomChoice == "3":
    print("You choose to enter the MAIN HALL!")
    wait(1.5)
    print("When you entered, there were many rooms, and in total, there were 100 rooms.")
    wait(2.5)
    print(
        "Out of which 98 were locked! 2 Gates were only open, and it says that 1 gate goes to the correct path and other goes to DEATH!")
    wait(3.2)
    print("Which Gate do you want to enter?? \n 1. GATE 1 \n 2. GATE 2")

    whichGATE1GATE2 = input("> ")

    if whichGATE1GATE2 == "1":
        print("BAD LUCK! You entered Gate 1, and that gate goes to death!")
        wait(1.9)
        print("You were eaten by a monster that was behind the DOOR!")
        call_ghostSOUND()
        wait(4.8)
        print(f"THANK YOU FOR PLAYING, {PlayerName.upper()}!")

    elif whichGATE1GATE2 == "2":
        print("GOOD LUCK! You choose to enter gate 2, and it was a safe one!!!")
        wait(1.9)
        print("After you entered the Gate, Gate 2 goes to a bathroom!")
        wait(1.8)
        print("There was a tub, and a pistol was there with 45 bullets!")
        wait(1.8)
        print("Do you want to pick up the Pistol??")

        pickUpPistol = input("> ").lower()

        if pickUpPistol == "yes":
            print("You picked up the pistol and bullets; now it is in your inventory!!")
            wait(1.8)
            print("[Inventory - 'Pistol', '45 Bullets']")
            wait(1)
            print("You now sat in a tub and found a way that goes to a new place!!")
            wait(1.1)
            print("Do you want to enter the place??")

            enter_place = input("> ")

            if enter_place == "yes":
                print("You entered the place!")
                wait(1.8)
                print("You are safe from the monster")
                wait(1.8)
                print("As you entered your clothes automatically disappear!")
                wait(2)
                print("DO you want to find yourself clothes??")

                find_clothes2nd = input("> ")

                if find_clothes2nd == "no":
                    print("You roam around without clothes and fell cold! You sat in a hot water and slept there")
                    wait(2.1)
                    print("Because you were unclothe you fell very cold and died of HYpOthErmIa!!")

                elif find_clothes2nd == "yes":
                    print(
                        "Okay, You go to find clothes and you came across a room and there was a AK47 out there. You pick up the armor and gun!")
                    wait(1)
                    print("[Inventory - \"Armor\", \"AK47\", \"100 Ammo\", \"Pistol\", \"45 Ammo\"]")
                    wait(1)
                    print("DO you want to Equip the Armor??")

                    equipArmor = input("> ")

                    if equipArmor == "no":
                        print("You choose to not equip armor!")
                        wait(1)
                        print("You Have Gun. Waana fight Demon??")
                        call_ghostSOUND()
                        wait(5)

                        fight_demon = input("> ")

                        if fight_demon == "no":
                            print(
                                "You took good decision but your have armor but dont wore it and died because of HYPOTHERMIA!")
                            call_ghostSOUND()
                            wait(5)
                            print(f"Bye-Bye {PlayerName}")

                        elif fight_demon == "yes":
                            call_ghostSOUND()
                            wait(5)
                            print("You dont have armor and fight it! MONSTER killed you!")
                            call_ghostSOUND()
                            wait(5)
                            print("Bye-Bye!")


                    elif equipArmor == "yes":
                        print("Good Decision! You wore the armor and then was Ready enough!")
                        wait(1)
                        print("Do you want to fight the Demon??")

                        fightDemon = input("> ")

                        if fightDemon == "yes":
                            print("You wore armor and ready!")
                            wait(2)
                            print("You shoot the monster!!")
                            wait(2)
                            print("Game loading...")
                            wait(6)
                            print("He attacked you you safe! Armor broke properly!")
                            wait(1.1)
                            print("One more bullet and he ran away far!")
                            wait(2)
                            print("You now dont have clothes again!")
                            wait(1)
                            print("Waana find clothes??")

                            find_clothes3rd = input("> ")

                            if find_clothes3rd == "no":
                                print("Demon again come and tried to kill you. You checked your inventory!")
                                wait(1)
                                print("[Inventory - \"AK47\", \"50 bullets\", \"Pistol\", \"45 Ammo\"]")
                                wait(1.7)
                                print("Waana use AK47 and Pistol Both?")

                                use_Gun = input("> ")

                                if use_Gun == "no":
                                    print("Demon Killed You ONE SHOT!!")
                                    call_ghostSOUND()
                                    wait(5)
                                    print("Bye-bYe!")

                                elif use_Gun == "yes":
                                    print("You used all your ammo but monster was ready this time!!")
                                    wait(1)
                                    print("You used Gun but monster killed you!")
                                    call_ghostSOUND()
                                    wait(5)
                                    print('HAHAHAHAHAH')

                                else:
                                    print("Invalid Input")

                            elif find_clothes3rd == "yes":
                                print("You tried to find clothes but again found an armor. Now waana wear armor??")

                                wearArmor2nd = input("> ")

                                if wearArmor2nd == "no":
                                    print(
                                        "You don't wore armor and now this time you are killed by the freaking monster!!")
                                    call_ghostSOUND()
                                    wait(5)
                                    print("LOL!")

                                elif wearArmor2nd == "yes":
                                    print("You wore the armor but now you dont have weapons!")
                                    wait(2)
                                    print("You were back to the place where game stared! Waana leave the house??")

                                    leave_house = input("> ")

                                    if leave_house == "no":
                                        print("Monster CAme and Killed you 💀☠")
                                        call_ghostSOUND()
                                        wait(5)
                                        print(f"Lost Boy {PlayerName}!")

                                    elif leave_house == "yes":
                                        print(f"Okay Bye {PlayerName}")
                                        wait(3)
                                        print("Thanks for playinGG...")
                                        wait(2)
                                        print("")
                                        print(
                                            "======================================FEEDBACK======================================")
                                        print("")
                                        feedback = input("HOW WAS OUR GAME RATE(1⭐ to 5⭐⭐⭐⭐⭐): ")
                                        if feedback == "1":
                                            print("SORRY!!WE TRY TO IMPROVE")
                                            print("THANKS FOR PLAYING...😊☺")

                                        elif feedback == "2":
                                            print("SORRY!!WE TRY TO IMPROVE MUCH")
                                            print("THANKS FOR PLAYING...😊☺")

                                        elif feedback == "3":
                                            print("Average huh! We try to IMPROVE!")
                                            print("THANKS FOR PLAYING...😊☺")

                                        elif feedback == "4":
                                            print("THANKS !!WE STILL TRY TO IMPROVE MORE")
                                            print("THANKS FOR PLAYING...😊☺")

                                        elif feedback == "5":
                                            print("THANKSSSSSS😻🤗 !!WE STILL TRY TO IMPROVE MORE!")
                                            print("THANKS FOR PLAYING...😊☺")

                                        else:
                                            print("Invalid Input")

                                    else:
                                        print("Invalid Input")

                                else:
                                    print("Invalid Input!")

                            else:
                                print("Invalid Input!")

                        elif fightDemon == "no":
                            print(
                                "Smart Decision Huh??. You roam here and there and trying to escape the house now but cant find way")
                            wait(2)
                            print(
                                "When you roamed for about 1 hr then you came the the place back where the game was started!!")
                            wait(2)
                            print(
                                "Now last question! WAANA ESCAPE HOUSE? Monster might come and kill you now and then!. There is other way of escaping also! WAANA ESCAPE FROM MAIN GATE??")

                            final_escape = input("> ")

                            if final_escape == "yes":
                                print("JUST JOKING. You are Safe and escaped!")
                                wait(2)
                                print("THANKS FOR PLAYING!")
                                wait(1)
                                print("")
                                print(
                                    "======================================FEEDBACK======================================")
                                print("")
                                feedback = input("HOW WAS OUR GAME RATE(1⭐ to 5⭐⭐⭐⭐⭐): ")
                                if feedback == "1":
                                    print("SORRY!!WE TRY TO IMPROVE")
                                    print("THANKS FOR PLAYING...😊☺")

                                elif feedback == "2":
                                    print("SORRY!!WE TRY TO IMPROVE MUCH")
                                    print("THANKS FOR PLAYING...😊☺")

                                elif feedback == "3":
                                    print("Average huh! We try to IMPROVE!")
                                    print("THANKS FOR PLAYING...😊☺")

                                elif feedback == "4":
                                    print("THANKS !!WE STILL TRY TO IMPROVE MORE")
                                    print("THANKS FOR PLAYING...😊☺")

                                elif feedback == "5":
                                    print("THANKSSSSSS😻🤗 !!WE STILL TRY TO IMPROVE MORE!")
                                    print("THANKS FOR PLAYING...😊☺")

                                else:
                                    print("Invalid Input!")

                            elif final_escape == "no":
                                print("Good Decision! That gate may be a dangerous to escape from")
                                wait(2)
                                print("")

                            else:
                                print("Invalid Input!")

                        else:
                            print("Invalid Input")



                    else:
                        print("Invalid Input!")


            elif enter_place == "no":
                print("You didn't enter the place and then sat there for 45 min, and then a monster came!")
                print("Do you want to use the pistol to save your life??")

                use_pistol = input("> ")

                if use_pistol == "no":
                    print("You didn't use the pistol, and now you are dead by the monster")
                    call_ghostSOUND()
                    wait(5)
                    print("THE END!")

                elif use_pistol == "yes":
                    print(
                        "You used your 45 ammo and the monster is not killed yet! He ran away! He might come again to kill you!!!")
                    wait(2.2)
                    print("Now you want to enter the place??")

                    enter_place2 = input("> ")

                    if enter_place2 == "no":
                        print("This time your luck won't work! You don't have any ammo now!!")
                        print("Monster came again and now killed you!!!")
                        call_ghostSOUND()
                        wait(5)
                        print("THE END!")

                    elif enter_place2 == "yes":
                        print("You chose to enter the place!!")
                        wait(1.6)
                        print(
                            "As you entered, suddenly all your clothes were automatically removed, and your underwear was also removed!")
                        wait(2)
                        print("Do you want to find clothes??")
                        wait(0.8)

                        find_clothes = input("> ")

                        if find_clothes == "no":
                            print("You unfortunately died because of cold! Hypothermia led to your death!")

                        elif find_clothes == "yes":
                            print("You tried to find clothes but can't find it!")
                            wait(1.4)
                            print("You are Dead! Hypothermia led to your ☠eath!!!")

                        else:
                            print("Invalid Input!")

        elif pickUpPistol == "no":
            print("You didn't pick up the pistol and continued your journey!")
            wait(1)
            print("You found a way down. Do you want to enter that place??")

            enter_place_pistolNo = input("> ").lower()

            if enter_place_pistolNo == "no":
                print("You sat there and a monster came and...")
                wait(2)
                print("[Inventory = \"Stun Gun\"]")
                wait(0.99)
                print("Wait I already have Stun Gun")
                wait(1)
                print("Waana kill Monster with stun gun??")

                stunKill = input("> ")

                if stunKill == "no":
                    print("You took a wrong decision but monster dont know why ran away!")
                    print("Want to escape from the bathroom??")

                    escapeBathroom = input("> ")

                    if escapeBathroom == "no":
                        print(
                            "You sat in the bathroom for too long but this time monster came back again with great preparations.")
                        wait(2)
                        print("Monster came a kill-d you!")
                        call_ghostSOUND()
                        wait(5)
                        print("gud!")

                    elif escapeBathroom == "yes":
                        print("You escape from bathroom.")
                        wait(1)
                        print("You find yourself armor and weapons to fight demon!")
                        wait(2)
                        print("Luckily! You found a Monster Proof and MiniGun with 3000 Ammo in it!!")
                        wait(2)
                        print("You Pick them up and store it in your inventory! You already Have stun Gun")
                        print(0.9)
                        print("Take your time seeing inventory and take you decision!")
                        wait(2)
                        print("[Inventory - \"Minigun\", \"3000 Ammo\" \"Stun Gun\"] {Monster Proof Armor on Body}")
                        wait(5)
                        print("Waana fight monster!")

                        fight_DemonXFearnot = input("> ")

                        if fight_DemonXFearnot == "no":
                            print("You choose not to fight and find the way of escape!")
                            wait(2)
                            print("Waana Escape!")

                            escapeHouse = input("> ")

                            if escapeHouse == "no":
                                print("Monster Came with Armor and fight with you!")
                                wait(2)
                                print("Waana use minigun??")

                                useMinigun = input("> ")

                                if useMinigun == "no":
                                    print("Monster Kill-d you!")
                                    call_ghostSOUND()
                                    wait(5)
                                    print(f"Bye {PlayerName}")

                                elif useMinigun == "yes":
                                    print("You Finally Killed the Monster and find way of Escape!")
                                    wait(2)
                                    print("You Finally Escape!")
                                    wait(2)
                                    print("THANKS FOR PLAYING!!!")
                                    wait(1)

                                    print("")
                                    print(
                                        "======================================FEEDBACK======================================")
                                    print("")
                                    feedback = input("HOW WAS OUR GAME RATE(1⭐ to 5⭐⭐⭐⭐⭐): ")
                                    if feedback == "1":
                                        print("SORRY!!WE TRY TO IMPROVE")
                                        print("THANKS FOR PLAYING...😊☺")

                                    elif feedback == "2":
                                        print("SORRY!!WE TRY TO IMPROVE MUCH")
                                        print("THANKS FOR PLAYING...😊☺")

                                    elif feedback == "3":
                                        print("Average huh! We try to IMPROVE!")
                                        print("THANKS FOR PLAYING...😊☺")

                                    elif feedback == "4":
                                        print("THANKS !!WE STILL TRY TO IMPROVE MORE")
                                        print("THANKS FOR PLAYING...😊☺")

                                    elif feedback == "5":
                                        print("THANKSSSSSS😻🤗 !!WE STILL TRY TO IMPROVE MORE!")
                                        print("THANKS FOR PLAYING...😊☺")

                                    else:
                                        print("Invalid Input!")


                                else:
                                    print("Invalid Input")

                            elif escapeHouse == "yes":
                                print("You Escaped the House!")
                                wait(2)
                                print("THANKS FOR PLAYING!")
                                wait(1)

                                print("")
                                print(
                                    "======================================FEEDBACK======================================")
                                print("")
                                feedback = input("HOW WAS OUR GAME RATE(1⭐ to 5⭐⭐⭐⭐⭐): ")
                                if feedback == "1":
                                    print("SORRY!!WE TRY TO IMPROVE")
                                    print("THANKS FOR PLAYING...😊☺")

                                elif feedback == "2":
                                    print("SORRY!!WE TRY TO IMPROVE MUCH")
                                    print("THANKS FOR PLAYING...😊☺")

                                elif feedback == "3":
                                    print("Average huh! We try to IMPROVE!")
                                    print("THANKS FOR PLAYING...😊☺")

                                elif feedback == "4":
                                    print("THANKS !!WE STILL TRY TO IMPROVE MORE")
                                    print("THANKS FOR PLAYING...😊☺")

                                elif feedback == "5":
                                    print("THANKSSSSSS😻🤗 !!WE STILL TRY TO IMPROVE MORE!")
                                    print("THANKS FOR PLAYING...😊☺")

                                else:
                                    print("Invalid Input!")

                        elif fight_DemonXFearnot == "yes":
                            print("You fight with the Demon and you were Victorious! ")
                            wait(2)
                            print("Monster Tell you the escape route when you killED him!")
                            wait(2)
                            print("You Followed the route and finally escaped the house!")
                            wait(1)
                            print(f"Thank you for playing {PlayerName}!")

                            wait(1)
                            print("")
                            print(
                                "======================================FEEDBACK======================================")
                            print("")
                            feedback = input("HOW WAS OUR GAME RATE(1⭐ to 5⭐⭐⭐⭐⭐): ")
                            if feedback == "1":
                                print("SORRY!!WE TRY TO IMPROVE")
                                print("THANKS FOR PLAYING...😊☺")

                            elif feedback == "2":
                                print("SORRY!!WE TRY TO IMPROVE MUCH")
                                print("THANKS FOR PLAYING...😊☺")

                            elif feedback == "3":
                                print("Average huh! We try to IMPROVE!")
                                print("THANKS FOR PLAYING...😊☺")

                            elif feedback == "4":
                                print("THANKS !!WE STILL TRY TO IMPROVE MORE")
                                print("THANKS FOR PLAYING...😊☺")

                            elif feedback == "5":
                                print("THANKSSSSSS😻🤗 !!WE STILL TRY TO IMPROVE MORE!")
                                print("THANKS FOR PLAYING...😊☺")

                            else:
                                print("Invalid Input!")

                    else:
                        print("Invalid Input!")

                elif stunKill == "yes":
                    print("Monster came running and you by stun gun make him faint!")
                    wait(2)
                    print("You Quickly escape from bathroom and luckily reached the final gate. But it was Locked!")
                    wait(2)
                    print("Waana find key!")

                    find_escapeKey_Final = input("> ")

                    if find_escapeKey_Final == "no":
                        print("You dont find the key and monster was now again alive and found you!")
                        wait(2)
                        print("He Kill-d you!!")
                        call_ghostSOUND()
                        wait(5)
                        print("THE END!")

                    elif find_escapeKey_Final == "yes":
                        print("You work hard and finally find the key!")
                        wait(2)
                        print(f"Do you want to escape the house {PlayerName}??")

                        keyFindEscapeFinal = input("> ")

                        if keyFindEscapeFinal == "no":
                            print("You DOnt want to escape and monster came up and...")
                            wait(2)
                            print("Kill-D you!")
                            call_ghostSOUND()
                            wait(5)
                            print("LOL!")

                        elif keyFindEscapeFinal == "yes":
                            print("You Finally escaped the House!")
                            wait(2)
                            print(f"Thanks FOR Playing {PlayerName}...")
                            wait(1)
                            print("")
                            print(
                                "======================================FEEDBACK======================================")
                            print("")
                            feedback = input("HOW WAS OUR GAME RATE(1⭐ to 5⭐⭐⭐⭐⭐): ")
                            if feedback == "1":
                                print("SORRY!!WE TRY TO IMPROVE")
                                print("THANKS FOR PLAYING...😊☺")

                            elif feedback == "2":
                                print("SORRY!!WE TRY TO IMPROVE MUCH")
                                print("THANKS FOR PLAYING...😊☺")

                            elif feedback == "3":
                                print("Average huh! We try to IMPROVE!")
                                print("THANKS FOR PLAYING...😊☺")

                            elif feedback == "4":
                                print("THANKS !!WE STILL TRY TO IMPROVE MORE")
                                print("THANKS FOR PLAYING...😊☺")

                            elif feedback == "5":
                                print("THANKSSSSSS😻🤗 !!WE STILL TRY TO IMPROVE MORE!")
                                print("THANKS FOR PLAYING...😊☺")

                            else:
                                print("Invalid Input!")

                    else:
                        print("Invalid Input!")

                else:
                    print("Invalid Input!")

            elif enter_place_pistolNo == "yes":
                print("You enter that place and it goes to a place where the atmosphere was different and suspicious!")
                wait(2)
                print(f"As you entered a sound came said - \"{PlayerName}\" Welcome. You asked WHAT THE HELL IS HERE??")
                wait(2)
                print("Monster said you have 2 min to find 5 car keys in this room. This was a challenge by monster.")
                wait(2)
                print(
                    "Monster said if you complete this challenge you would survive and may help you escape the house but if you fail I will Kill you!")
                wait(2.1)
                print("This challenge may be impossible!")
                wait(0.9)
                print("Whats your choice? Yes for do challenge and No for not doing challenge!")

                MonsterChallenge = input("> ")

                if MonsterChallenge == "no":
                    print(
                        "You Try to secretly escape but you find a M249 lie on the floor. You got armor also and ammo. Now you might win!")
                    wait(2.8)
                    print("Waana FIGHT??")
                    print("[Inventory - \"M249\", \"100 Bullets\"] {Armor of Body}")

                    fightMonster = input("> ")
                    if fightMonster == "no":
                        print("You try to escape but monster catch you and killed you to your death!")
                        call_ghostSOUND()
                        wait(5)
                        print("THE END!")

                    elif fightMonster == "yes":
                        print("You fight and after some m249 shots monster ran away!")
                        print("...Armor Broke...")
                        wait(1.2)
                        print("INVENTORY BEFORE FIGHT [Inventory - \"M249\", \"100 Bullets\"] {Armor of Body}")
                        print("Loading...")
                        wait(2)
                        print("INVENTORY AFTER FIGHT [Inventory - \"M249\", \"12 Bullets\"]")
                        wait(2)
                        print("After killing Monster you were back to the place were game started!!")
                        print("Now before escaping think you want to escape form this gate only??")

                        gateEscape = input("> ")

                        if gateEscape == "no":
                            print("You were killed by the Monster hahahahh!")
                            call_ghostSOUND()
                            wait(5)
                            print("THE END!")

                        elif gateEscape == "yes":
                            print("JUST JOKING. You are Safe and escaped!")
                            wait(2)
                            print("THANKS FOR PLAYING!")
                            wait(1)
                            print("")
                            print(
                                "======================================FEEDBACK======================================")
                            print("")
                            feedback = input("HOW WAS OUR GAME RATE(1⭐ to 5⭐⭐⭐⭐⭐): ")
                            if feedback == "1":
                                print("SORRY!!WE TRY TO IMPROVE")
                                print("THANKS FOR PLAYING...😊☺")

                            elif feedback == "2":
                                print("SORRY!!WE TRY TO IMPROVE MUCH")
                                print("THANKS FOR PLAYING...😊☺")

                            elif feedback == "3":
                                print("Average huh! We try to IMPROVE!")
                                print("THANKS FOR PLAYING...😊☺")

                            elif feedback == "4":
                                print("THANKS !!WE STILL TRY TO IMPROVE MORE")
                                print("THANKS FOR PLAYING...😊☺")

                            elif feedback == "5":
                                print("THANKSSSSSS😻🤗 !!WE STILL TRY TO IMPROVE MORE!")
                                print("THANKS FOR PLAYING...😊☺")

                            else:
                                print("Invalid Input!")

                        else:
                            print("Invalid Input!")

                    else:
                        print("Invalid Input!")

                elif MonsterChallenge == "yes":
                    print("You agreed to complete monster challenge!")
                    wait(2)
                    print("When you were searching the key you find RPG Lying on floor with 75 rockets!")
                    wait(2)
                    print("You secretly pick up that. Waana kill monster with RPG without armor??")

                    monsterKillRPG = input("> ")

                    if monsterKillRPG == "no":
                        print("Monster find Rpg in your hand and killed you!")
                        call_ghostSOUND()
                        wait(5)
                        print("==THE END==")

                    elif monsterKillRPG == "yes":
                        print(
                            "You killed the monster with RPG and when he was about to die. He spoke up the escape Path!")
                        print("Waana follow escape Path?")

                        followEscapePath = input("> ")

                        if followEscapePath == "no":
                            print("You was lost in the house forever!")
                            wait(2)
                            print("THE END")

                        elif followEscapePath == "yes":
                            print("You followed the escape path and finally escaped!")
                            wait(2)
                            print("Thanks For Playing!")

                            wait(1)
                            print("")
                            print(
                                "======================================FEEDBACK======================================")
                            print("")
                            feedback = input("HOW WAS OUR GAME RATE(1⭐ to 5⭐⭐⭐⭐⭐): ")
                            if feedback == "1":
                                print("SORRY!!WE TRY TO IMPROVE")
                                print("THANKS FOR PLAYING...😊☺")

                            elif feedback == "2":
                                print("SORRY!!WE TRY TO IMPROVE MUCH")
                                print("THANKS FOR PLAYING...😊☺")

                            elif feedback == "3":
                                print("Average huh! We try to IMPROVE!")
                                print("THANKS FOR PLAYING...😊☺")

                            elif feedback == "4":
                                print("THANKS !!WE STILL TRY TO IMPROVE MORE")
                                print("THANKS FOR PLAYING...😊☺")

                            elif feedback == "5":
                                print("THANKSSSSSS😻🤗 !!WE STILL TRY TO IMPROVE MORE!")
                                print("THANKS FOR PLAYING...😊☺")

                            else:
                                print("Invalid Input!")

                        else:
                            print("Invalid Input!")

                    else:
                        print("Invalid Input!")

            else:
                print("Invalid Input!")

        else:
            print("Invalid Input!")

    else:
        print("Invalid Input!")

elif roomChoice == "2":
    print("You choose to enter the dining room!")
    # Coming Soon!

elif roomChoice == "1":
    print("You Choose to enter Living Room!")
    # Coming Soon!

else:
    print("Invalid Input!")
