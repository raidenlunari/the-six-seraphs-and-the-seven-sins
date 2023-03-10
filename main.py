import random
import math
import time

def beginGame():
    create_instructions()
    cutscene(1)

def die():
    global deaths
    global currentHealth
    global hungerBar
    global drinkBar
    global fatigueValue

    currentHealth = random.randint(50, 100)
    hungerBar = random.randint(10, 20)
    drinkBar = random.randint(10, 20)
    fatigueValue = random.randint(5, 10)
    deaths += 1
    print("You died. Your new stats are", currentHealth, "HP,", hungerBar, "hunger,", drinkBar, "drink bar, and", fatigueValue, "fatigue. YOU HAVE DIED", deaths,"TIMES.")


def eat(foodValue):
    global maxFoodValue
    global hungerBar

    foodValue = int(foodValue)
    if (hungerBar + foodValue) > maxFoodValue:
        hungerBar = maxFoodValue-foodValue
        print("Your new hunger bar is at", hungerBar+".")
    else:
        hungerBar += foodValue
        print("Your new hunger bar is at", hungerBar+".")
    if hungerBar <= 0:
        die()


def eatEffect(currentHunger, timeElapsed):
    global currentHealth
    global maxFoodValue

    lackFood = maxFoodValue - currentHunger
    currentHealth -= 0.75*lackFood*timeElapsed*(6/math.log(defense))


def eatLoss(timeElapsed):
    global hungerBar

    hungerBar -= timeElapsed*0.1


def drink(drinkValue):
    global drinkBar
    global maxDrinkValue

    drinkValue = int(drinkValue)
    if (drinkBar + drinkValue) > maxDrinkValue:
        drinkBar = maxDrinkValue-drinkValue
        print("Your new drink bar is at", drinkBar+".")
    else:
        drinkBar += drinkValue
        print("Your new drink bar is at", drinkBar+".")
    if drinkBar <= 0:
        die()


def drinkEffect(currentDrink, timeElapsed):
    global currentHealth

    lackDrink = maxDrinkValue - currentDrink
    currentHealth -= 0.25*lackDrink*timeElapsed*timeElapsed*(6/math.log(defense))


def drinkLoss(timeElapsed):
    global drinkBar

    drinkBar -= timeElapsed*0.15


def sleep(sleepValue):
    global fatigueValue
    global minFatigueValue

    sleepValue = int(sleepValue)
    if (fatigueValue - sleepValue) < minFatigueValue:
        fatigueValue = minFatigueValue
        print("Your new fatigue level is at", fatigueValue+".")
    else:
        fatigueValue -= sleepValue
        print("Your new fatigue level is at", fatigueValue+".")


def sleepEffect(currentFatigue, timeElapsed):
    global currentHealth

    currentHealth -= 0.1*currentFatigue*timeElapsed*timeElapsed*(2/math.log(defense))


def sleepLoss(timeElapsed):
    global fatigueValue

    fatigueValue += timeElapsed*0.1


def healthDiff(diff):
    global currentHealth

    if diff >= 0:
        currentHealth += diff
    else:
        currentHealth -= diff*(2/math.log(defense))

    if currentHealth <= 0:
        die()


def gainMoney(value):
    global money

    money += int(value)


def heatstroke(heatstrokeValue):
    global heatValue

    heatstrokeValue = int(heatstrokeValue)
    heatValue += heatstrokeValue


def heatstrokeEffect(currentHeat, timeElapsed):
    global currentHealth

    currentHealth -= 0.5*currentHeat*timeElapsed*(4/math.log(defense))

def bank():
    def extractMoney(extracted):
        global bankAccount
        global money

        if bankAccount >= extracted:
            money += extracted
            bankAccount-= extracted
            print("Your new bank balance is", bankAccount, "and your new wallet balance is", money+".")
        else:
            print("You cannot extract this amount.")

    def placeMoney(placed):
        global bankAccount
        global money

        if money >= placed:
            bankAccount += placed
            money -= placed
            print("Your new bank balance is", bankAccount, " and your new wallet balance is", money+".")
        else:
            print("You cannot place this amount.")

    def checkBalance():
        print("Your current bank balance is", bankAccount+".")
        print("Your current wallet has $"+money+".")

    def checkRates():
        print("At this city, the rates are", rates+".")
    bankChoice = input("Input EXTRACT, PLACE, BALANCE, RATES: ")
    if bankChoice == "EXTRACT":
        extractChoice = input("Input extracted amount: ")
        extractMoney(extractChoice)

    elif bankChoice == "PLACE":
        placeChoice = input("Input placed amount: ")
        placeMoney(placeChoice)

    elif bankChoice == "BALANCE":
        checkBalance()

    elif bankChoice == "RATES":
        checkRates()

    else:
        print("You made an unintelligible movement and annoyed the other customers greatly. Please respect the other customers. No actions done.")


def bankInterest(timeElapsed):
    global bankAccount

    bankAccount += timeElapsed*(1+rates)


def fightingMoves(activator):

    def singlePunch():
        global skillpoint
        global attack
        skillpoint -= 1
        return int(attack*0.5)

    def twoPunch():
        global skillpoint
        global attack
        skillpoint -= 1.5
        return int(attack*1.25)

    def threePunch():
        global skillpoint
        global attack
        skillpoint -= 2
        return int(attack*random.randint(2, 3))

    def gatling():
        global skillpoint
        global attack
        skillpoint -= 3
        return int(round(attack*(random.randrange(2, 5))))

    def swordfight():
        global skillpoint
        global attack
        skillpoint -= 5
        return int(round(attack*(random.randrange(1, 3)*(0.2*skillpoint)*0.2)))

    if activator == "SINGLEPUNCH" or activator == "singlepunch":
        return singlePunch()

    elif activator == "TWOPUNCH" or activator == "twopunch":
        return twoPunch()

    elif activator == "THREEPUNCH" or activator == "threepunch":
        return threePunch()

    elif activator == "GATLING" or activator == "gatling":
        return gatling()

    elif activator == "SWORDFIGHT" or activator == "swordfight":
        return swordfight()

    else:
        return 0


def beginFight(activator):
    def sinSpiritOne():
        global deaths
        global currentHealth

        deathsBefore = deaths
        sinSpiritHealth = 1000
        while deaths == deathsBefore and sinSpiritHealth > 0:
            print("Your skills are:", skills)
            attack = input("What attack would you like to use: ")
            sinSpiritHealth -= fightingMoves(attack)
            print("")
            print("You now have", skillpoint, "skillpoints.")
            print("You did", fightingMoves(attack), "damage. The sin spirit now has", sinSpiritHealth, "health.")
            print("")

            sinSpiritDamage = random.randint(50, 100)
            currentHealth -= sinSpiritDamage
            print("The Sin Spirit hit you!")
            print("Your new HP is", str(currentHealth)+". You took", sinSpiritDamage, "damage.")
            if currentHealth <= 0:
                die()
            print("")

    if activator == "SLOTH":
        sinSpiritOne()


def create_instructions():
    global name

    name = input("Input your name: ")
    print(name+", welcome to the game! \nWe will be giving instructions on how to play the game and move through text and combat appropriately here. Please pay attention, as this will only be stated ONCE.")
    print("During text and dialogue, press enter to move on if no questions or inputs are required, or answer a question. ")
    print("For example, try this out here. ")
    input("")
    print("During combat, please simply type in appropriate skills and you will use an action. ")
    print("Inventory can only be accessed at specific points during the adventure. \nIt's strongly advised to use inventory items before a major expedition, as you cannot always access this part of the game.")
    print("Answers are case-sensitive. Answer in UPPERCASE or lowercase when asked or appropriate.")
    input("")
    print("Thank you for joining us on this adventure! We hope you enjoy the game and succeed.\n")
    print("------------\n------------\n------------\n------------")


def cutscene(activator):
    def cutscene1():
        global name

        print("TIME: XX:XX, June XX, 5XXX \nLOCATION: XXXXXXX \nTRANSMISSION: 0XXXX"); time.sleep(0.15)
        print("Head GENERAL: Private, return to XXXXXX immediately!"); time.sleep(0.2)
        print("Head GENERAL: Return-  to- XXXXXX! Under-  attack!"); time.sleep(0.15)
        print("Head GENERAL: Soldiers! Regroup at XXXXXXXXX City! I repeat-"); time.sleep(0.2)
        print("Head GENERAL: XXXXXXXXX City!"); time.sleep(0.1)
        input("")
        print("TIME: XX:XX, July XX, 5XXX \nLOCATION: XXXXXXXX \nTRANSMISSION: 0XXXX"); time.sleep(0.15)
        print("___E: Do not fear. "); time.sleep(0.15)
        print("___E: You're one of the important ones here. "); time.sleep(0.1)
        print("___E: Stay safe. SXNXXUARX City has a place for you. ") ; time.sleep(0.15)
        input("")
        print("TIME: XX:XX, July XX, 5XXX \nLOCATION: SXNXXUAXRX \nTRANSMISSION: 1XXXX"); time.sleep(0.5)
        print(name+": ___E, I've made it to SXNXXUARX City."); time.sleep(0.2)
        print(name+": ... ___E? I've made it to SANXTUARY City."); time.sleep(0.2)
        print(name+": Are you still there?"); time.sleep(0.2)
        input("")
        print("You turn a corner and hear a commotion. "); time.sleep(0.2)
        input("")
        print("D____: You broke your transmitter. Absolute idiot. "); time.sleep(0.2)
        print("___E: This entire war has become a drag. Curse that traitor ___, and its ambitions."); time.sleep(0.3)
        print("D____: Any word back from ___O_?"); time.sleep(0.15)
        print("___E: No."); time.sleep(0.1)
        print("D____: The Head GENERAL? "); time.sleep(0.1)
        print("___E: No."); time.sleep(0.1)
        print("D____: You're pathetic."); time.sleep(0.2)
        print("___E: My transmitter is broken. What on earth do you want to expect from me further? "); time.sleep(0.3)
        print("D____: Sigh. How about", name+"?"); time.sleep(0.1)
        print("___E: I believe that they went MIA a while ago."); time.sleep(0.2)
        print("D____: Impossible. That's impossible to be true."); time.sleep(0.2)
        input("")
        print("___E: ..."); time.sleep(0.1)
        print("D____: ..."); time.sleep(0.1)
        print("___E: At long last."); time.sleep(0.2)
        print(name+": ___E? D____? What are you trying to do?"); time.sleep(0.2)
        print("___E: I'm sorry. But you cannot be on this planet any longer."); time.sleep(0.5)
        print(name+": ___E? ___E!"); time.sleep(0.5)
        input("")
        print("TIME: XX:XX, October XX, 5XXX \nLOCATION: Orion Supergalaxy \nTRANSMISSION: 1XXXX"); time.sleep(0.5)
        print(name+": ..."); time.sleep(0.2)
        input("")
        print("TIME: XX:XX, December XX, 5XXX \nLOCATION: Sagittarius Supercluster \nTRANSMISSION: 1XXXX"); time.sleep(0.5)
        print(name+": ..."); time.sleep(0.2)
        input("")
        print("TIME: 06: 31, March XX, 6XXX \nLOCATION: Salvation of Stardust \nTRANSMISSION: 12XX5"); time.sleep(0.5)
        print(name+": ...")
        input("")
        print("TIME: 21: 15, April 21, 6051 \nLOCATION: GENESIS \nTRANSMISSION: 16171"); time.sleep(1)
        print("Automated Voice of ___E: Welcome. You have landed at your destination, GENESIS. \nAutomated Voice of ___E: It has been 111 Years, 9 Months, and 10 Days since you began your journey.")
        print("Automated Voice of ___E: Thank you. You won't be forgotten. But I will.")

    if activator == 1:
        cutscene1()


maxFoodValue = 50
maxDrinkValue = 50
minSleepValue = 0
maxHealth = 500

deaths = 0
hungerBar = 25
drinkBar = 25
fatigueValue = 5
heatValue = 0
money = 2000
bankAccount = 10000
rates = 0.025

currentHealth = 500
attack = 20
defense = 20
skillpoint = 100

name = ""
skills = "SINGLEPUNCH | TWOPUNCH | THREEPUNCH | GATLING | SWORDFIGHT"
inventory = ""

beginGame()