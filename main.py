import random
import math
import time


def beginGame():
    
    # phase ONE
    create_instructions()
    cutscene(1)
    meetCharacter("ANGEL")
    cutscene(2)
    meetCharacter("AVA")
    enterCity("MADDA")
    cutscene(3)
    maddaChoiceOne = input("What would you like to do in Madda Gate? Answer with SHOP, WALK, or MOVE ON: ")
    if maddaChoiceOne == "SHOP":
        meetCharacter("BETH")
    elif maddaChoiceOne == "WALK":
        meetCharacter("MADDANPC")
    elif maddaChoiceOne == "MOVE ON":
        meetCharacter("BETH")
    else:
        print("You made a random, incomprehensible action.")
        meetCharacter("BETH")
    meetCharacter("CARL")
    cutscene(4)
    cutscene(5)
    meetCharacter("MADDA")
    beginFight("SLOTH")
    cutscene(6)
    print("demo ends here")

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
        print("Your new hunger bar is at", str(hungerBar)+".")
    else:
        hungerBar += foodValue
        print("Your new hunger bar is at", str(hungerBar)+".")
    if hungerBar <= 0:
        die()


def eatLoss(timeElapsed):
    global hungerBar

    hungerBar -= timeElapsed*0.1
    print(str(timeElapsed), "hours have passed. Your hunger bar has gone down. Your new hunger bar is at", str(hungerBar)+".")


def drink(drinkValue):
    global drinkBar
    global maxDrinkValue

    drinkValue = int(drinkValue)
    if (drinkBar + drinkValue) > maxDrinkValue:
        drinkBar = maxDrinkValue-drinkValue
        print("Your new drink bar is at", str(drinkBar)+".")
    else:
        drinkBar += drinkValue
        print("Your new drink bar is at", str(drinkBar)+".")
    if drinkBar <= 0:
        die()


def drinkLoss(timeElapsed):
    global drinkBar

    drinkBar -= timeElapsed*0.15
    print(str(timeElapsed), "hours have passed. Your drink bar has gone down. Your new drink bar is at", str(drinkBar)+".")


def sleep(sleepValue):
    global fatigueValue
    global minSleepValue

    sleepValue = int(sleepValue)
    if (fatigueValue - sleepValue) < minSleepValue:
        fatigueValue = minSleepValue
        print("Your new fatigue level is at", str(fatigueValue)+".")
    else:
        fatigueValue -= sleepValue
        print("Your new fatigue level is at", str(fatigueValue)+".")


def sleepEffect(timeElapsed):
    global currentHealth

    currentHealth -= round(0.1*fatigueValue*timeElapsed*timeElapsed*(2/math.log(defense)))
    print("Because of your lack of sleep, you have begun to have your health deteriorate.")
    print("Your new health is at", str(currentHealth)+". Stay safe out there. \n")


def sleepLoss(timeElapsed):
    global fatigueValue

    fatigueValue += timeElapsed*0.1
    print(str(timeElapsed), "hours have passed. You have become more tired. Your new fatigue bar is at", str(fatigueValue)+".")


def healthDiff(diff):
    global currentHealth

    if diff >= 0:
        currentHealth += diff
        currentHealth = round(currentHealth)
    else:
        currentHealth += diff*(2/math.log(defense))
        currentHealth = round(currentHealth)

    if currentHealth <= 0:
        die()


def gainMoney(value):
    global money

    money += int(value)
    print("You were given", str(value), "dollars. Your new balance is", str(money)+".")


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

def enterCity(activator):
    
    def maddaGate():
        global maddaKeys

        triedKeys = input("Input Keys to the City: ")
        if triedKeys == maddaKeys:
            print("Welcome to the City! Enjoy your stay in Madda Gate. \n")
        else:
            print("You got lost! Lose 5 hunger bar, 5 drink bar, and gain 5 fatigue value! \n")
            eat(-5)
            drink(-5)
            sleep(-5)

    if activator == "MADDA":
        maddaGate()

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

    validIn = 0

    if activator in skills:
        validIn += 1
    else:
        pass

    if (activator == "SINGLEPUNCH" or activator == "singlepunch") and validIn == 1:
        return singlePunch()

    elif (activator == "TWOPUNCH" or activator == "twopunch") and validIn == 1:
        return twoPunch()

    elif (activator == "THREEPUNCH" or activator == "threepunch") and validIn == 1:
        return threePunch()

    elif (activator == "GATLING" or activator == "gatling") and validIn == 1:
        return gatling()

    elif (activator == "SWORDFIGHT" or activator == "swordfight") and validIn == 1:
        return swordfight()

    else:
        return 0

def useItem(activator):
    def beans():
        global inventory
        global hungerBar
        
        if "BEANS" in inventory:
            inventory = inventory.replace("|BEANS", "")
            eat(5)
            print("\nYou ate a can of beans. Recover 5 Hunger Bar. ")
            print("Your new inventory is", inventory+".")
        else:
            print("\nYou do not have beans.")

    def water():
        global inventory
        global drinkBar

        if "WATER" in inventory:
            inventory = inventory.replace("|WATER", "")
            drink(5)
            print("\nYou drank a bottle of water. Recover 5 Drink Bar. ")
            print("Your new inventory is", inventory+".")
        else:
            print("\nYou do not have water.")

    def grape():
        global inventory
        global hungerBar
        
        if "GRAPE" in inventory:
            inventory = inventory.replace("|GRAPE", "")
            eat(5)
            drink(2)
            print("\nYou ate a vine of grapes. Recover 5 Hunger Bar and 2 Drink Bar. ")
            print("Your new inventory is", inventory+".")
        else:
            print("\nYou do not have grapes.")

    def apple():
        global inventory
        global hungerBar
        
        if "APPLE" in inventory:
            inventory = inventory.replace("|APPLE", "")
            eat(6)
            drink(4)
            print("\nYou ate an apple. You're spared from the doctor another day. Recover 6 Hunger Bar and 4 Drink Bar.")
            print("Your new inventory is", inventory+".")
        else:
            print("\nYou do not have an apple.")

    def juice():
        global inventory
        global hungerBar
        
        if "JUICE" in inventory:
            inventory = inventory.replace("|JUICE", "")
            drink(8)
            eat(2)
            print("\nYou drank some juice. Recover 2 Hunger Bar and 8 Drink Bar. ")
            print("Your new inventory is", inventory+".")
        else:
            print("\nYou do not have juice.")
    
    if activator == "BEANS":
        beans()
    elif activator == "WATER":
        water()
    elif activator == "GRAPE":
        grape()
    elif activator == "APPLE":
        apple()
    elif activator == "JUICE":
        juice()
    else:
        print("Not valid item.")

def buy(activator):
    def buyBeans():
        global inventory
        global money

        if "BEANS" in inventory:
            print("Sorry. You can only have one of each item at once.")
        else:
            if money >= 200:
                print("You will have", str(money-200), "dollars after this transaction. Complete?")
                doBuyBeans = input("Input YES or NO: ")
                if doBuyBeans == "YES" or doBuyBeans == "yes":
                    money -= 200
                    inventory = inventory+"|BEANS"
                    print("\nYou bought beans for $200. Your new inventory is", inventory+".")
                else:
                    print("\nYou did not buy beans.")
            else:
                print("\nSorry. You don't have $200 for beans.")
        
    def buyWater():
        global inventory
        global money

        if "WATER" in inventory:
            print("Sorry. You can only have one of each item at once.")
        else:
            if money >= 200:
                print("You will have", str(money-200), "dollars after this transaction. Complete?")
                doBuyWater = input("Input YES or NO: ")
                if doBuyWater == "YES" or doBuyWater == "yes":
                    money -= 200
                    inventory = inventory+"|WATER"
                    print("\nYou bought water for $200. Your new inventory is", inventory+".")
                else:
                    print("\nYou did not buy water.")
            else:
                print("\nSorry. You don't have $200 for water.")
    
    def buyGrape():
        global inventory
        global money

        if "GRAPE" in inventory:
            print("Sorry. You can only have one of each item at once.")
        else:
            if money >= 300:
                print("You will have", str(money-300), "dollars after this transaction. Complete?")
                doBuyGrape = input("Input YES or NO: ")
                if doBuyGrape == "YES" or doBuyGrape == "yes":
                    money -= 300
                    inventory = inventory+"|GRAPE"
                    print("\nYou bought grapes for $300. Your new inventory is", inventory+".")
                else:
                    print("\nYou did not buy grapes.")
            else:
                print("\nSorry. You don't have $300 for grapes.")
        
    def buyApple():
        global inventory
        global money

        if "APPLE" in inventory:
            print("Sorry. You can only have one of each item at once.")
        else:
            if money >= 500:
                print("You will have", str(money-500), "dollars after this transaction. Complete?")
                doBuyApple = input("Input YES or NO: ")
                if doBuyApple == "YES" or doBuyApple == "yes":
                    money -= 500
                    inventory = inventory+"|APPLE"
                    print("\nYou bought an apple for $500. Your new inventory is", inventory+".")
                else:
                    print("\nYou did not buy an apple.")
            else:
                print("\nSorry. You don't have $500 for an apple.")

    def buyJuice():
        global inventory
        global money

        if "JUICE" in inventory:
            print("Sorry. You can only have one of each item at once.")
        else:
            if money >= 500:
                print("You will have", str(money-500), "dollars after this transaction. Complete?")
                doBuyJuice = input("Input YES or NO: ")
                if doBuyJuice == "YES" or doBuyJuice == "yes":
                    money -= 500
                    inventory = inventory+"|JUICE"
                    print("\nYou bought juice for $500. Your new inventory is", inventory+".")
                else:
                    print("\nYou did not buy juice.")
            else:
                print("\nSorry. You don't have $500 for juice.")
        
        
        
    if activator == "BEANS":
        buyBeans()
    elif activator == "WATER":
        buyWater()
    elif activator == "GRAPE":
        buyGrape()
    elif activator == "APPLE":
        buyApple()
    elif activator == "JUICE":
        buyJuice()
    else:
        print("That is not an item.")

def market(activator):

    def bethMarket():
        global inventory

        items = "|BEANS|WATER|GRAPE|APPLE|JUICE"
        print("The Items Here Are:", items+".")
        print("Simply enter GRAPE to buy a grape, for example, not |GRAPE, or GRAPE|. These two are invalid answers.")
        print("Your current inventory is", inventory+".")
        bethDone = 0
        while bethDone == 0:
            bethBuy = input("What would you like to buy? ")
            if bethBuy == "BEANS" or bethBuy == "beans":
                buy("BEANS")
            elif bethBuy == "WATER" or bethBuy == "water":
                buy("WATER")
            elif bethBuy == "GRAPE" or bethBuy == "grape":
                buy("GRAPE")
            elif bethBuy == "APPLE" or bethBuy == "apple":
                buy("APPLE")
            elif bethBuy == "JUICE" or bethBuy == "juice":
                buy("JUICE")
            else:
                print("Not an Item.")

            bethDoneYet = input("\nAre you done yet? YES or NO: ")
            if bethDoneYet == "YES" or bethDoneYet == "yes":
                bethDone += 1
            elif bethDone == "NO" or bethDoneYet == "no":
                print("The market appreciates your continual patronage.")
            else:
                print("You seem to have motioned to stay.")

    if activator == "BETH":
        bethMarket()

def beginFight(activator):
    def sinSpiritOne():
        global deaths
        global currentHealth

        deathsBefore = deaths
        sinSpiritHealth = 2500
        print("Begin your fight with the Sin Spirit.")
        print("To fight, instructions are given.")
        print("Good luck. You'll certainly need it.")
        healthDiff(100)

        while deaths == deathsBefore and sinSpiritHealth > 0:

            print("Your skills are:", skills)
            print("Note that using a skill not in your skills will do NOTHING. You effectively skip your turn.")
            attack = input("What attack would you like to use: ")
            sinSpiritHealth -= fightingMoves(attack)
            print(""); time.sleep(0.5)
            print("You now have", skillpoint, "skillpoints.")
            print("You did", fightingMoves(attack), "damage. The sin spirit now has", sinSpiritHealth, "health.")
            print(""); time.sleep(0.5)

            oldHealth = currentHealth
            sinSpiritDamage = random.randint(-75, -40)
            healthDiff(sinSpiritDamage)
            trueHealthDiff = round(oldHealth - currentHealth)
            print("The Sin Spirit hit you!")
            print("Your new HP is", str(currentHealth)+". You took", -(sinSpiritDamage), "raw damage. You took", str(trueHealthDiff), "real damage."); time.sleep(0.5)
            
            if skillpoint <= 0:
                skillpoint = 0
                print("You're out of skillpoints. You aren't good enough. The enemy saw an opening and killed you.")
                healthDiff(-9999)
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
    print("Answers are case-sensitive. Answer in UPPERCASE or lowercase when asked or appropriate.")
    input("")
    print("Thank you for joining us on this adventure! We hope you enjoy the game and succeed.\n")
    print("------------\n------------\n------------\n------------"); time.sleep(1)


def cutscene(activator):
    def cutscene1():
        global name

        print("TIME: XX:XX, June XX, 5XXX \nLOCATION: XXXXXXX \nTRANSMISSION: 0XXXX"); time.sleep(0.5)
        print("Head GENERAL: Private, return to XXXXXX immediately!"); time.sleep(0.5)
        print("Head GENERAL: Return-  to- XXXXXX! Under-  attack!"); time.sleep(0.5)
        print("Head GENERAL: Soldiers! Regroup at XXXXXXXXX City! I repeat-"); time.sleep(0.5)
        print("Head GENERAL: XXXXXXXXX City!"); time.sleep(0.5)
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
        print("You hear a crunching sound under your foot. You're heard."); time.sleep(0.5)
        input("")
        print("___E: ..."); time.sleep(0.2)
        print("D____: ..."); time.sleep(0.2)
        print("___E: At long last."); time.sleep(0.2)
        print(name+": ___E? D____? What are you trying to do?"); time.sleep(0.2)
        print("___E: I'm sorry. But you cannot be on this planet any longer."); time.sleep(0.5)
        print(name+": ___E? ___E!"); time.sleep(0.5)
        input("")
        print("TIME: XX:XX, October XX, 5XXX \nLOCATION: Orion Supergalaxy \nTRANSMISSION: 1XXXX"); time.sleep(0.5)
        print(name+": ..."); time.sleep(0.2)
        input("")
        print("TIME: 06: 31, March XX, 6XXX \nLOCATION: Salvation of Stardust \nTRANSMISSION: 12XX5"); time.sleep(0.5)
        print(name+": ...")
        input("")
        print("TIME: 21: 15, April 21, 6051 \nLOCATION: GENESIS \nTRANSMISSION: 16171"); time.sleep(1)
        print("Automated Voice of ___E: Welcome. You have landed at your destination, GENESIS. \nAutomated Voice of ___E: It has been 777 Years, 9 Months, and 10 Days since you began your journey."); time.sleep(0.5)
        print("Automated Voice of ___E: Thank you. You won't be forgotten. But I will. \n"); time.sleep(5)

    def cutscene2():
        print("You walk on the soft plains slowly, wondering where you are."); time.sleep(0.2)
        print("SANCTUARY City certainly wasn't like this. The capital of the Sechsturme's Celestial City was bright, and white, and technologically advanced."); time.sleep(0.2)
        print("Until, of course, it wasn't."); time.sleep(0.2)
        print("Those gray streets vaguely pictured in your mind, abandoned by civilization."); time.sleep(0.2)
        print("How awful."); time.sleep(0.2)
        print("You thought about what ANGEL said to you, however. This city seemed much further away than it made it sound."); time.sleep(0.2)
        input("")
        print("By now, it'd been hours."); time.sleep(0.2)
        print("Had ANGEL lied to you? That'd be hard to believe, but betrayal, was, after all, what ___E was so angered about."); time.sleep(0.2)
        print("A splitting headache appears in your mind. The older ones had told you about this kind of headache, the splitting, horrid pain of thinking of memories long gone."); time.sleep(0.2)
        print("However, it just seemed worse for you. Why? You couldn't understand. Even the simulations couldn't predict the vividness of these memories in your head."); time.sleep(0.2)
        print("Then, you remembered a crucial detail. What you heard ___E say."); time.sleep(0.2)
        input("")
        print("An even worse pain appeared, but in your heart."); time.sleep(0.2)
        print("It'd seriously been so long, you thought."); time.sleep(0.2)
        print("You try to send a message to the higher-ups."); time.sleep(0.2)
        input("")
        print("TIME: 16:55, August 08, 6051 \nLOCATION: GENESIS \nTRANSMISOIN: 16172"); time.sleep(1)
        print(name+": Testing, testing! Come in, SALVATION City!"); time.sleep(0.2)
        print("6051?")
        print("16172? But the last message was only 16171, and the technology was new-"); time.sleep(0.2)
        print("It hit you."); time.sleep(0.2)
        print("No new messages."); time.sleep(0.2)
        print("The 61st century's middle years."); time.sleep(0.2)
        print("You were... seriously alone, now."); time.sleep(0.2)
        input(""); time.sleep(1)
        print("Time stops for nobody."); time.sleep(0.2)
        input(""); time.sleep(1)


    def cutscene3():
        print("ANGEL was wrong."); time.sleep(0.2)
        print("Madda Gate wasn't anything near a city, or anything grand, or even anything moderately good."); time.sleep(0.2)
        print("The smell of rot filled the streets, only covered by the even worse scent of years of smoke and ash accumulating from the chimneys fed by old wood."); time.sleep(0.2)
        print("Yet, the people were smiling, the children were laughing, and the elders of the city smiled."); time.sleep(0.2)
        print("It was curious to you. SANCTUARY City was nothing like this."); time.sleep(0.2)
        print("SANCTUARY City was better, it was cleaner, it was brighter, and it was just superior in terms of quality of life."); time.sleep(0.2)
        print("Yet, nobody ever smiled."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("You made it into the city, hoping for a place to rest."); time.sleep(0.2)
        print("But even the outside was a better place than this."); time.sleep(0.2)
        print("However, you couldn't stop smiling, and you'd never felt so \"home\" before."); time.sleep(0.2)
        print("Have you ever been home in the first place? \n"); time.sleep(0.2)

    def cutscene4():
        print("CARL kicks you out of his house, in a fit of rage."); time.sleep(0.3)
        print("At this point, you had no idea who was really right in this city."); time.sleep(0.3)
        print("What on earth was wrong with the people on this planet?"); time.sleep(0.3)
        print("Suddenly, a shockwave from the distance knocks you down."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("You can't seem to decipher where it comes from at first, but you suddenly sense a terrible blast of heat from a familiar direction."); time.sleep(0.3)
        print("The direction of Madda Gate."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("Was this CARL's fault again?"); time.sleep(0.3)
        print("No, that shouldn't be possible. This amount of heat had only happened once."); time.sleep(0.3)
        print("___'s attack on SANCTUARY City."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("But this shouldn't be possible."); time.sleep(0.3)
        print("Surely, those legions of ___E and D____ had defeated that singular being."); time.sleep(0.3)
        print("Surely, they'd won."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("You feel a severe headache."); time.sleep(0.3)
        print("You fall to the ground."); time.sleep(0.3)
        input(""); time.sleep(0.3)

    def cutscene5():
        print("TIME: XX:XX:XXX, XXXX, XX, XXXX \nLOCATION: BERLIN \nTRANSMISSION: 11110"); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("____: XXX XXXX CITY XXXXXXXX XX:XX XXXX"); time.sleep(0.3)
        print("____: HAIL THE KINGDOM OF ___"); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("TIME: XX:XX:XXX, XXXX, XX, 6000 \nLOCATION: RUINS OF XXX XXXX CITY \nTRANSMISSION: 11111"); time.sleep(0.3)
        print("Head GENERAL: ___'s assault on our nation has succeeded."); time.sleep(0.3)
        print("Head GENERAL: The new year's assault succeeded. XXX XXXX CITY has fallen."); time.sleep(0.3)
        print("Head GENERAL: ____ is heading to XXNXXXX to hunt for the God of E________"); time.sleep(0.3)
        print("Head GENERAL: We don't know where ___E is."); time.sleep(0.3)
        print("Head GENERAL: Final transmission. "); time.sleep(0.3)
        print("Head GENERAL: We're done."); time.sleep(0.3)
        input("")

    def cutscene6():
        print("You really tried."); time.sleep(0.3)
        print("You tried, didn't you?"); time.sleep(0.3)
        print("You got close, didn't you?"); time.sleep(0.3)
        print("You almost did it, didn't you?"); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("You get launched to the cliffs of the city. The Sin Spirit thinks it killed you."); time.sleep(0.3)
        print("But you live."); time.sleep(0.3)
        print("And you get to see what's left of Madda Gate."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("You look down. It's murky, and the storm blocks your view."); time.sleep(0.3)
        print("But it's as clear as can be."); time.sleep(0.3)
        print("When you finally left that city, Madda Gate died."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("A murky, black ink on the ground."); time.sleep(0.3)
        print("That's what you'd usually say to such a scene."); time.sleep(0.3)
        print("But that's what's left of Madda Gate."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("Off in the distance, you see that small house again."); time.sleep(0.3)
        print("That CARL lived in."); time.sleep(0.3)
        print("Sigh, it's all dead now."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("Looking in the city, you see the place the market used to be."); time.sleep(0.3)
        print("Another splotch of dark dust, and black horror."); time.sleep(0.3)
        print("It's dead too. Couldn't be saved."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("Those plains which you saw AVA at."); time.sleep(0.3)
        print("They're outside of the city."); time.sleep(0.3)
        print("But the black decay of the Sin creeps into it, destroying the grass and greenery you admired walking into the city."); time.sleep(0.3)
        print("What did AVA think of this?"); time.sleep(0.3)
        print("What would AVA think of you?"); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("And finally, that poor, poor place where you saw ANGEL."); time.sleep(0.3)
        print("What would they think, seeing the city?"); time.sleep(0.3)
        print("Who would explain to them what exactly happened to Madda Gate?"); time.sleep(0.3)
        print("Hopefully it was obvious enough. Or, hopefully, it wasn't obvious. At all."); time.sleep(0.3)
        print("Hopefully, they managed to finally rest. And have a peaceful rest."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("Live in the present."); time.sleep(0.3)
        print("Your life isn't defined by what you lose only once."); time.sleep(0.3)
        print("Madda Gate won't come back. It dug its own grave and gilded it with a facade of gold."); time.sleep(0.3)
        print("Move on."); time.sleep(0.3)
        print("Look forward."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("The tragedy happened, and you were lucky enough to witness it."); time.sleep(0.3)
        print("But you'll add to more of the tragedy if you continue to live like this."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("Start walking again."); time.sleep(0.3)
        input("")

    if activator == 1:
        cutscene1()

    elif activator == 2:
        cutscene2()

    elif activator == 3:
        cutscene3()

    elif activator == 4:
        cutscene4()

    elif activator == 5:
        cutscene5()

    elif activator == 6:
        cutscene6()

def meetCharacter(activator):
    def meetAngel():
        global maxFoodValue
        global hungerBar
        global maxDrinkValue
        global drinkBar
        global fatigueValue
        global currentHealth
        global money
        global bankAccount

        print("XXXXX: Hey! Hey!")
        input("")
        print("XXXXX: Hey there! Who are you?"); time.sleep(0.5)
        print("XXXXX: How ya doin? You've been out for a few months already!"); time.sleep(0.5)
        print("XXXXX: Ah! I forgot to introduce myself! I'm the angel of this realm! Nice to meet you!"); time.sleep(0.5)
        print("ANGEL: What brings you to Madda Gate?"); time.sleep(0.5)
        input("")
        print("ANGEL: Hmm. Whatever the reason is, you look confused. Come on, I'll lead you to the city!"); time.sleep(0.5)
        print("ANGEL: It's been a few years since I've gone there either, though, so I hope I can still lead you correctly!"); time.sleep(0.5)
        print("ANGEL: Do you want an introduction to the city?")
        angelChoice = input("Input YES or NO: ")
        if angelChoice == "YES" or angelChoice == "yes":
            print("ANGEL: Alright, I'll give it my best shot! Anyways, Madda Gate is famous for its pleasant weather, warm breezes, active population, and beautiful architecture!"); time.sleep(0.5)
            print("ANGEL: It's commonly believed as the birthplace of this planet's civilization, and the front door for any visitors we get!"); time.sleep(0.5)
            print("ANGEL: If you're a visitor, this is the place for you!"); time.sleep(0.5)
        elif angelChoice == "NO" or angelChoice == "no":
            print("ANGEL: That's alright! As long as you're happy, I'm happy!"); time.sleep(0.5)
        else:
            print("ANGEL: Hmm... I dunno what you're saying, but I guess that means a no?"); time.sleep(0.5)
        print("ANGEL: Anyways, let's introduce you to this planet a bit!"); time.sleep(0.5)
        input("")
        print("ANGEL: This planet is generally known by it's people as GENESIS, which means... uhh... something complicated I can't remember!"); time.sleep(0.5)
        print("ANGEL: It's mostly safe, from what I've seen, but lemme try to help you out with more basic stuff!"); time.sleep(0.5)
        print("ANGEL: To stay healthy, you need food and drink!"); time.sleep(0.5)
        print("Your current hunger bar is", str(hungerBar)+"."); time.sleep(0.5)
        print("Your current drink bar is", str(drinkBar)+"."); time.sleep(0.5)
        print("Your current fatigue value is", str(fatigueValue)+"."); time.sleep(0.5)
        print("ANGEL: It may sound weird, but you want BARS as HIGH as possible and VALUES as LOW as possible!"); time.sleep(0.5)
        print("ANGEL: However! Don't eat too much, or drink too much! Then, you'll actually lose hunger bars and be more unhealthy!")
        print("Your max food bar is", str(maxFoodValue), "and your max drink bar is", str(maxDrinkValue)+".")
        input("")
        print("ANGEL: Your inventory can only be used at certain times, so when it's allowed, you should utilize it as much as possible!")
        print("ANGEL: Don't be the one who starves cause they didn't eat during mealtimes!")
        input("")
        print("ANGEL: Ah! Moving on, your current health is at", str(currentHealth)+"."); time.sleep(0.5)
        print("ANGEL: You have", str(money), "dollars right now too! And the world bank starts everyone off with", str(bankAccount), "dollars in the bank. \nANGEL: Worldwide rates are, mmm, GENERALLY at around 2.5% per time interval."); time.sleep(0.5)
        print("ANGEL: Well, that's all! I gotta run, but if you need anything, someone'll be there to help you out!"); time.sleep(0.5)
        print("ANGEL: AH! How could I forget? Don't ever forget the keys to the city!"); time.sleep(0.5)
        input(""); time.sleep(0.5)

    def meetAva():
        global maddaKeys

        print("XXX: Yo, what are you looking so wistfully at?"); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("XXX: Hello?"); time.sleep(0.2)
        print("XXX: Rude. The name's Ava."); time.sleep(0.2)
        print(name+": Oh. Sorry, I was busy over there."); time.sleep(0.2)
        print("AVA: That's visible. Whatever, anyways, what'cha lookin' for?"); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("AVA: Uhhh. The city? I... don't think you know where this is. You lookin' for the next over? Mae- oh. Sigh, you ain't lookin' for Madda Gate, are ya?"); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("AVA: Hahaha! My grandparents would love being with you. Always talkin' about some... uhh, Madda City? I dunno."); time.sleep(0.2)
        print("AVA: Some sanctuary city too, something to deal with it, yadda yadda."); time.sleep(0.2)
        print("AVA: Grandparents' legends, am I right?"); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print(name+": I'm from this SANCTUARY City. Do you know where I can find it?"); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("AVA: Haha! You're funny. There's no way. It's a legend. Some sanctuary was used as a story a good few hundred years ago, and some of the oldies tell it today."); time.sleep(0.2)
        print("AVA: It's 666 PH now, we don't believe in this stuff."); time.sleep(0.2)
        print(name+": It's 6051 PC. I'm serious about SANCTUARY City."); time.sleep(0.2)
        print("AVA: Uhh. What? 6051? What are you on? How old are you, or how YOUNG are you? Negative five thousand years old, or whatever?"); time.sleep(0.2)
        print("AVA: And PC? What even is that? Post C-Heaven? Everybody knows about Heaven's Collapse 666 years ago. I'm not sure what C is."); time.sleep(0.2)
        print(name+": C for Celestia. 6051 Years past the Grand Raising of Celestia from the Sechsturme's First Spaceport in Berlin of Europa."); time.sleep(0.2)
        print("AVA: Uhhhh. Speak English?"); time.sleep(0.2)
        print("AVA: Point is, you wanna get to Madda Gate? Lucky you. I know the key, and the direction. The keys to the city are", maddaKeys+"."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("AVA: Yeah, yeah. You're welcome. Now go spread your Sanctuary Heretic Religion somewhere else."); time.sleep(0.2)
        print("AVA: Peace out!\n"); time.sleep(0.2)

    def meetBeth():
        print("XXXX: Well, hello there! Did I overhear you talking about reaching the market?"); time.sleep(0.2)
        print(name+": Yes, do you know where this city- town's market is?"); time.sleep(0.2)
        print("XXXX: Ah! But of course! The name's BETH. I'm the city's most avid spender, and I was ecstatic hearing about a fellow shopper being in the city."); time.sleep(0.2)
        print("BETH: Come on, let us go. It's been ages since I was able to spend with somebody else."); time.sleep(0.2)
        input("")
        print("BETH: ... and as you know, the city's infrastructre's been deteriorating so fast, but the next town over's so far away, and nobody knows how to repair it!"); time.sleep(0.2)
        print(name+": Does this city not have a construction team?"); time.sleep(0.2)
        print("BETH: Oh, but we do! This city's people are just so... lazy! Nothing ever gets done, and CARL's attitude certainly doesn't help."); time.sleep(0.2)
        print(name+": CARL?"); time.sleep(0.2)
        print("BETH: Yes, CARL. Former owner of a large construction and engineering company?"); time.sleep(0.2)
        print("BETH: Former chief of the town's public works agency?"); time.sleep(0.2)
        print("BETH: ... Not familiar with him?"); time.sleep(0.2)
        print("BETH: Ah, you're a newcomer. Don't worry, once you meet him, you'll begin to hate him as much as I do."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("BETH: Ah! We've at last reached the market!"); time.sleep(0.2)
        print("BETH: Don't worry about the buildings, the merchants are as reliable and as forgiving as ever. "); time.sleep(0.2)
        print(name+": I might not have money for all of this..."); time.sleep(0.2)
        print("BETH: Oh! Darling, don't worry about all that, the mere act of shopping with me already makes me happy."); time.sleep(0.2)
        print("BETH: If you need some, I've got a ton. Here's a bit just in case you can't buy this market clean. Have tons of fun!"); time.sleep(0.2)
        gainMoney(2000)
        print("")
        market("BETH"); time.sleep(0.2)
        print("BETH: Done now? That was surprisingly quick."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("BETH: If I may, can I look at what's in your bag?"); time.sleep(0.2)
        print("BETH: Oh! You have quite an eye! This... this food is of the finest quality! I thought you were new to the town? How on earth are you this good?"); time.sleep(0.2)
        print(name+": I... have some... practice, let's say. From... another- let's just say town. "); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("BETH: Well, that's very lucky of you. You'll be eating great food tonight, won't you?"); time.sleep(0.2)
        print(name+": This food isn't the best I've seen..."); time.sleep(0.2)
        print("BETH: Are you kidding me?! These beans are fresh, pure, and smell of pure deliciousness!"); time.sleep(0.2)
        print("BETH: This water... it's the cleanest I've seen in years! Maybe even ever!"); time.sleep(0.2)
        print(name+": If you need it, I could give it to you, in return for the money you lent me..."); time.sleep(0.2)
        print("BETH: Oh, I would never imagine! This luxury water and food... I couldn't take it from you for a million dollars!"); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print(name+": ..."); time.sleep(0.2)
        print(name+": ..."); time.sleep(0.2)
        print(name+": What happened here?"); time.sleep(0.2)
        input(""); time.sleep(0.2)

    def meetMaddaNPC():
        print("You walk down the city's streets sadly, having more questions than you do answers, and still contemplating what exactly happened between the few years ANGEL was here and now."); time.sleep(0.2)
        print("Suddenly, you hear shrill voices, sounding almost like screams, yet weaker."); time.sleep(0.2)
        print("CITIZEN 1: Aaghhh!"); time.sleep(0.2)
        print("CITIZEN 2: Mom, are you ok?"); time.sleep(0.2)
        print("CITIZEN 1: Sigh... your father's house is falling down. "); time.sleep(0.2)
        print("CITIZEN 1: He tried to hard to build this. Yet it continues to crumble, and our family may have to move out soon."); time.sleep(0.2)
        print("CITIZEN 2: Mom..."); time.sleep(0.2)
        print("CITIZEN 1: Let's go. Don't let yourself die of the plague."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("You walk down the streets, trying to forget what happened in that interaction."); time.sleep(0.2)
        print("A plague? That shouldn't be possible. Everybody in the city was so happy, and even the dirt and waste didn't seem to bring disease or hardship."); time.sleep(0.2)
        print("You walk down further and further down the road, only to see the buildings deteriorate and the roads become mud."); time.sleep(0.2)
        print("What was left of Main Street ended early, only revealing a pool of brown sludge from the rot and soil mixing together in a basin."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("Soon, rain starts to fall, creating a deeper puddle you could only hope to cross without getting wet."); time.sleep(0.2)
        print("But the city was still interesting."); time.sleep(0.2)
        print("So you go forward."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("SANCTUARY City's slums were almost like this. "); time.sleep(0.2)
        print("Cold, wet, smelly, and broken."); time.sleep(0.2)
        print("When you were on that planet, you had learned that such a place was \"inhospitable, awful, and unfit for human residence\"."); time.sleep(0.2)
        print("Yet, this kind of environment didn't even seem to surprise you."); time.sleep(0.2)
        print("Why?"); time.sleep(0.2)
        print("As far as you knew, you hadn't ever been here before."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("You hear voices again, this time yelling and booming from the interior of a cathedral."); time.sleep(0.2)
        print("You enter, of course. It's not like some priest inside could hurt you that bad."); time.sleep(0.2)
        print("But the interior of the cathedral could barely even be called an interior."); time.sleep(0.2)
        print("The walls were stripped, the wood was moldy, and the furnishings were completely and entirely gone."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("AUDIENCE MEMBER 1: You are surprised?"); time.sleep(0.2)
        maddaNPCChoice = input("YES or NO: "); time.sleep(0.2)
        if maddaNPCChoice == "YES":
            print("AUDIENCE MEMBER 1: Ah... me too. I thought this would be a cathedral. It turns out it's barely even holding itself up."); time.sleep(0.2)
            print("AUDIENCE MEMBER 1: Hey. What brought you to this city?"); time.sleep(0.2)
        else:
            print("AUDIENCE MEMBER 1: Hmm. This is, ah... what do you call it... commonplace? I see."); time.sleep(0.2)
        print("AUDIENCE MEMBER 1: I, uhh... personally came here to commission somebody, hearing from others about how his work was heavenly."); time.sleep(0.2)
        print("AUDIENCE MEMBER 1: It seems I was lied to."); time.sleep(0.2); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("AUDIENCE MEMBER 1: I believe I heard of a master architect, uhh... CARL, hmm."); time.sleep(0.2)
        print("AUDIENCE MEMBER 1: Our architects in a uhh... small village out there aren't great."); time.sleep(0.2)
        print("AUDIENCE MEMBER 1: Active, sure, but not skilled at all, hmm."); time.sleep(0.2)
        print("AUDIENCE MEMBER 1: It'd be hard to believe a city's architects would be worse, hmm?"); time.sleep(0.2)
        print("AUDIENCE MEMBER 1: So I think the only possibility here is that he's lazy."); time.sleep(0.2)
        print("AUDIENCE MEMBER 1: Ah... that's sad."); time.sleep(0.2)
        print("AUDIENCE MEMBER 1: It seems I came for nothing."); time.sleep(0.2)
        print("He leaves."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("You hear a person in the cathedral begin to speak loudly through a hollow tube."); time.sleep(0.2)
        print("His voice is failing, and he looks aged and worn, but somehow, he still appears very strong."); time.sleep(0.2)
        print("PRIEST: Our god has failed us."); time.sleep(0.2)
        print("PRIEST: The Great City of Madda and its Gate have been left to rot and die."); time.sleep(0.2)
        print("PRIEST: We must begin to work by ourselves. In our OWN city!"); time.sleep(0.2)
        print("Jeers ring out from the audience."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("PRIEST: CARL, our architect, has failed us too."); time.sleep(0.2)
        print("PRIEST: We revered him as the savior and the true leader of Madda City. And he's only brought us pain."); time.sleep(0.2)
        print("PRIEST: The time is now! We must win! Take back our Madda! Rebel against those who refuse to help!"); time.sleep(0.2)
        print("A roar from the audience begins to appear."); time.sleep(0.2)
        print("But it's against him."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("PRIEST: N-now, now, audience! Let's not get too uproarious, and listen to me!"); time.sleep(0.2)
        print("AUDIENCE MEMBER 2: Heretic!"); time.sleep(0.2)
        print("AUDIENCE MEMBER 3: Ungrateful old geezer!"); time.sleep(0.2)
        print("AUDIENCE MEMBER 2: Kill him!"); time.sleep(0.2)
        print("AUDIENCE: Kill him! Kill him!"); time.sleep(0.2)
        print("The priest starts to run."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("His old bones fail him. "); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("AUDIENCE MEMBER 1: Turn away. This is... what they call..."); time.sleep(0.2)
        print("AUDIENCE MEMBER 1: Commonplace."); time.sleep(0.2)
        input(""); time.sleep(0.2)

    def meetCarl():
        global inventory
        
        eatLoss(10)
        drinkLoss(10)
        sleepLoss(10)
        sleepEffect(10)

        print("You walk down the streets angrily, looking for CARL."); time.sleep(0.2)
        print(name+": Excuse me, do you know where CARL is?"); time.sleep(0.2)
        print("CITIZEN 1: I don't know. Nobody's seen him for years."); time.sleep(0.2)
        print(name+": Sorry."); time.sleep(0.2)
        print("You keep walking."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print(name+": Excuse me, do YOU know where CARL is?"); time.sleep(0.2)
        print("CITIZEN 2: Don't speak of him."); time.sleep(0.2)
        print("CITIZEN 3: He's dead to us."); time.sleep(0.2)
        print(name+": Sorry about that."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CITIZEN 4: Excuse me? "); time.sleep(0.2)
        print("CITIZEN 4: Were you looking for a certain CARL?"); time.sleep(0.2)
        print(name+": Yes, do you know where he is?"); time.sleep(0.2)
        print("CITIZEN 4: Of course! Others may have begun to refuse thinking about him, but I still believe in his ability to change."); time.sleep(0.2)
        print("CITIZEN 4: The name's DAVID. Nice to meet you!"); time.sleep(0.2)
        print(name+": Hello there. My name's", name+"."); time.sleep(0.2)
        print("DAVID: ...", name+"? That's... an odd name. I'm supposing you're not from this place?"); time.sleep(0.2)
        print("DAVID: Oh, finally! Someone new! This city's been stagnant, boring, and stationary for far too long."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("DAVID: What do you think of the city? Nice, huh? It's been a few years since anyone's come to fix it, but I still think it's nice!"); time.sleep(0.2)
        print("DAVID: So, what can I do for you? Eat? Drink? Sleep? Find somewhere to sit? I got a friend at a comfy hotel. ")
        print("DAVID: You gotta rest first, anyways, before getting into anywhere CARL built for himself.")
        print("DAVID: So, what'cha want?")
        davidChoiceOne = input("Input FOOD, DRINK, SLEEP, or INVENTORY: ")
        if davidChoiceOne == "FOOD" or davidChoiceOne == "food":
            print("DAVID: Food, huh? Well, I'm the one for you! Come, I have some friends at a fancy restaurant!"); time.sleep(0.3)
            print("You eat with DAVID and his friends at a restaurant."); time.sleep(0.3)
            eat(5)
            input("")
        elif davidChoiceOne == "DRINK" or davidChoiceOne == "drink":
            print("DAVID: Drinking? Not sure if you like alcohol, but the bar does have nonalcoholic drinks, if you're interested in that."); time.sleep(0.2)
            print("You go with DAVID to a bar and drink beverages of your choice."); time.sleep(0.3)
            drink(5)
            input("")
        elif davidChoiceOne == "SLEEP" or davidChoiceOne == "sleep":
            print("DAVID: Sleep? No problem! I can take you to the fanciest hotel in the city, free of charge! For you, at least."); time.sleep(0.2)
            print("You go with DAVID to a hotel and sleep well."); time.sleep(0.2)
            sleep(5)
            input(""); time.sleep(0.2)
        elif davidChoiceOne == "INVENTORY" or davidChoiceOne == "inventory":
            print("DAVID: Just wanna sit down? Got it. Follow me to the hotel anyways, they have the nicest seats around there!"); time.sleep(0.2)
            print("You go with DAVID to a hotel and sit down."); time.sleep(0.2)
            print("Your inventory is:", inventory+"."); time.sleep(0.2)
            print("Type in the capital letters, none of the bars, and in full capital letters."); time.sleep(0.2)
            davidInventory = input("Input item to use from your inventory: "); time.sleep(0.2)
            useItem(davidInventory)
            input(""); time.sleep(0.2)
        else:
            print("DAVID: I'm... not sure what you're saying here, but okay! I guess you don't need anything..."); time.sleep(0.2)

        print("You finish what you're doing, and step back out."); time.sleep(0.2)
        print("Suddenly, you hear a cry out from the other people in the town."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("RANDOM CITIZEN 1: Get away, cursed child!"); time.sleep(0.2)
        print("RANDOM CITIZEN 1: Never walk the streets of this city again!"); time.sleep(0.2)
        print("The citizen throws a rock at DAVID, who falls down from the shock."); time.sleep(0.2)
        print("RANDOM CITIZEN 2: Eww! That kid from the rebel slum is bleeding all over the streets!"); time.sleep(0.2)
        print("RANDOM CITIZEN 2: Someone get him off, and clean it up!"); time.sleep(0.2)
        print("The citizens jeer and continue to throw objects while DAVID bleeds on the floor."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print(name+": Hey! Stop what you're doing!"); time.sleep(0.2)
        print("RANDOM CITIZEN 1: Don't you know? He's one of those loyalists to CARL!"); time.sleep(0.2)
        print("RANDOM CITIZEN 1: He wants to bring that useless architect BACK to the city!"); time.sleep(0.2)
        print(name+": I don't understand."); time.sleep(0.2)
        print(name+": I thought the people in this city loved CARL?"); time.sleep(0.2)
        print("The citizen stops in his tracks, and looks blank for a few seconds."); time.sleep(0.2)
        print("RANDOM CITIZEN 2: We do not. But we also don't want a revolution."); time.sleep(0.2)
        print("RANDOM CITIZEN 1: But we also don't want him back."); time.sleep(0.2)
        print("RANDOM CITIZEN 2: But we also don't hate him."); time.sleep(0.2)
        print("RANDOM CITIZEN 1: Or like him."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print(name+": How on earth are you going to change the situation of this town, then?"); time.sleep(0.2)
        print(name+": Your town's falling apart, the buildings are too-"); time.sleep(0.2)
        print("Suddenly, you see the citizens of city become very angered."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("RANDOM CITIZEN 2: Change... change..."); time.sleep(0.2)
        print("RANDOM CITIZEN 1: Kill them!"); time.sleep(0.2)
        print("RANDOM CITIZEN 2: Kill them! Kill them!"); time.sleep(0.2)
        print("All the citizens around begin to chant as well, in a raspy, inhuman voice."); time.sleep(0.2)
        print("DAVID: Run! I'm weak, but I can make them stay away!"); time.sleep(0.2)
        print("DAVID: Go see CARL! I believe in you!"); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("You run."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("The rain starts again, and you can faintly hear more screams and chanting from the distance."); time.sleep(0.2)
        print("You don't pay them any mind."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("And you keep running."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print(name+": Ugh, where am I?"); time.sleep(0.2)
        print("XXXX: I found your dead body washing up on my poor river house's shore. Agh, you're an annoyance."); time.sleep(0.2)
        print("XXXX: Those poor flowers I found under you. What a waste."); time.sleep(0.2)
        print(name+": Who are you?"); time.sleep(0.2)
        print("XXXX: That ain't none o' your business, kid. You're the one on my property."); time.sleep(0.2)
        print(name+": Are you CARL?"); time.sleep(0.2)
        print("His eyes widen."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("XXXX: Hey, I never seen ya down the streets of that city."); time.sleep(0.2)
        print("XXXX: How'd ya know my name?"); time.sleep(0.2)
        print(name+": You need to come back."); time.sleep(0.2)
        print(name+": The city's falling apart, and you're a good architect."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL laughs."); time.sleep(0.2)
        print("CARL: Hah! You wish."); time.sleep(0.2)
        print("CARL: Is that really what'cha want?"); time.sleep(0.2)
        print("CARL: Kid, come with me."); time.sleep(0.2)
        print("CARL takes up his cane, staggering as he walks. He's weak."); time.sleep(0.2)
        print("CARL: Come, look outside this window."); time.sleep(0.2)
        print("CARL: Ya think it's pretty?"); time.sleep(0.2)
        print(name+": Yeah."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: Great. Now breathe this fresh, fresh air."); time.sleep(0.2)
        print("CARL: It's nice, isn't it?"); time.sleep(0.2)
        print(name+": Yeah."); time.sleep(0.2)
        print("CARL: Aight."); time.sleep(0.2)
        print("CARL: And now look at this nice, quaint lil' house I got for myself."); time.sleep(0.2)
        print("CARL: You like it?"); time.sleep(0.2)
        print(name+": Yeah."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: That's great. Now, then answer me."); time.sleep(0.2)
        print("CARL: Why on this god forsaken earth would I wanna go back to that smelly, old, disgustin', ugly place?"); time.sleep(0.2)
        input("")
        print(name+": ..."); time.sleep(0.2)
        print(name+": Do you not feel any sort of responsibility for your people?"); time.sleep(0.2)
        print(name+": Do you not feel any compassion for your friends who are dying of starvation?"); time.sleep(0.2)
        print(name+": Do you? Or are you just gonna be this cold, useless shell of a person?"); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: ..."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print(name+": ANSWER ME, NOW."); time.sleep(0.2)
        input("");time.sleep(0.2)
        print("CARL hits you."); time.sleep(0.2)
        print("CARL: I didn' wanna get any riled up about this lil incident here, but you forcin' me."); time.sleep(0.2)
        print("CARL: Lemme let ya in on a lil' secret."); time.sleep(0.2)
        print("CARL: I don't care about those people."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: Or, at least, whatever new generation or plague's taken ahold of their minds."); time.sleep(0.2)
        print("CARL: Listen here, ungrateful brat."); time.sleep(0.2)
        print("CARL: When I was workin' in that city, I worked day by day, motivated only by the smiles on those people's faces."); time.sleep(0.2)
        print("CARL: I loved that city. I worked in that city. And I was grateful for livin' in that city."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: But then, those people stopped smilin'. "); time.sleep(0.2)
        print("CARL: They looked at me in disgust."); time.sleep(0.2)
        print("CARL: They hated what I was doing."); time.sleep(0.2)
        print("CARL: Ya know how that makes a craftsman like me feel?"); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: They hated the changes I was bringin'."); time.sleep(0.2)
        print("CARL: Madda led the world in architecture."); time.sleep(0.2)
        print("CARL: We was the leadin' builders' city."); time.sleep(0.2)
        print("CARL: Then, they started hatin' me."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: Oh, I tried."); time.sleep(0.2)
        print("CARL: I worked my life off."); time.sleep(0.2)
        print("CARL: I lost hair over their discontentment."); time.sleep(0.2)
        print("CARL: I hated to see those lil' kids cry."); time.sleep(0.2)
        print("CARL: And what did it bring me?"); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: I received a letter from one o' my lil apprentices, DYLAN, that I was gonna' be killed."); time.sleep(0.2)
        print("CARL: Just a few days after I'd have finally completed one of my final works."); time.sleep(0.2)
        print("CARL: The giant, bejeweled wall I'd planned for the city's front."); time.sleep(0.2)
        print("CARL: A true Madda GATE."); time.sleep(0.2)
        print("CARL: And I would'a died if I'd stayed."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: My lil' apprentices were scared."); time.sleep(0.2)
        print("CARL: They cried."); time.sleep(0.2)
        print("CARL: And one of them who tried to stop this murder attempt,")
        print("CARL: Was killed in my stead."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: I left that god awful city after that."); time.sleep(0.2)
        print("CARL: If they hated my change, they could live as scum forever."); time.sleep(0.2)
        print("CARL: And one day, when I looked back at that city,"); time.sleep(0.2)
        print("CARL: And I saw- and I saw those people cryin', starvin', livin in terror,"); time.sleep(0.2)
        print("CARL: Ohh, you couldn' understand. I felt happy. For the first time in years."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: I'd gotten everybody what they wanted."); time.sleep(0.2)
        print("CARL: My apprentices were lyin' low and livin' well, my lil' DYLAN was livin' comfortably."); time.sleep(0.2)
        print("CARL: And that city, with all'o its people, who wished to suffer,"); time.sleep(0.2)
        print("CARL: Got what they wanted as well."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: I never bejeweled that stone wall I built."); time.sleep(0.2)
        print("CARL: I sold em' all, to a nearby city."); time.sleep(0.2)
        print("CARL: And I bought all'o my apprentices the money they needed to live the rest'o their life."); time.sleep(0.2)
        print("CARL: The excess money?"); time.sleep(0.2)
        print("CARL: Oh, I bought a nice bomb, and I naturally blew up the town's square."); time.sleep(0.2)
        input("")
        print("CARL: Hahahaha! They asked to suffer."); time.sleep(0.2)
        print("CARL: They killed my lil' kid cause they hated our work."); time.sleep(0.2)
        print("CARL: So why not? I'd already dedicated my life to their happiness and success."); time.sleep(0.2)
        print("CARL: So I did what they wanted, clearly, the most."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: Ya'll still listenin'? Not too shabby, huh?"); time.sleep(0.2)
        input("")
        print("CARL: I ain't that monster ya' imagined?"); time.sleep(0.2)
        input("")
        print("CARL: Oh, sure, I'm a monster. I ain't arguin' with that fact."); time.sleep(0.2)
        print("CARL: But ohhh... I ain't regrettin' a thing."); time.sleep(0.2)
        print("CARL: Out of all the buildings and construction I ever did..."); time.sleep(0.2)
        print("CARL: Blowin' a hole through Madda to honor my lil' boy's legacy was probably the best thing I ever did."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: They destroyed everything I built."); time.sleep(0.2)
        print("CARL: Everything I built could'a lasted a good couple decades, even a century."); time.sleep(0.2)
        print("CARL: I ain't an idiot. I'm a skilled craftsman."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: But they replaced all of my life's work with a nice lil' couple'a straw huts."); time.sleep(0.2)
        print("CARL: How do you think I felt?"); time.sleep(0.2)
        print("CARL: Man, I funded those buildings outta my pocket."); time.sleep(0.2)
        print("CARL: And they turned them into rubble to replace them with utter trash."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: My kids' last work? Blown up by them, instead."); time.sleep(0.2)
        print("CARL: Oh, oh dear. And my kids? Cut to pieces, hanged, murdered, internally destroyed by them, instead."); time.sleep(0.2)
        print("CARL: If that city' cared even a bit about itself, it would'a used my company's work to the fullest."); time.sleep(0.2)
        print("CARL: And if they cared even a bit even a bit about its people, it would'a let my poor children live."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: At least those ANGELs deserved to live."); time.sleep(0.2)
        print("CARL: At least ANGEL deserved to live."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: They don't care."); time.sleep(0.2)
        print("CARL: They just hate me and what I do."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("CARL: Kid, this world ain't in black and white."); time.sleep(0.2)
        print("CARL: I ain't a saint. But I ain't a full-blown devil anytime yet."); time.sleep(0.2)
        input(""); time.sleep(0.2)

    def meetMaddaFinale():
        print("You wake up."); time.sleep(0.3)
        print("You wake up in a sea of red."); time.sleep(0.3)
        print("Not again, you thought."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("But once you rub your eyes a few times, you see the full scene."); time.sleep(0.3)
        print("A bleaker scene."); time.sleep(0.3)
        print("And a river of blood."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("You walk into Madda Gate."); time.sleep(0.3)
        print("It seemed... the explosions really did happen."); time.sleep(0.3)
        print("And they happened here."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("It's hard to breathe in the smoke."); time.sleep(0.3)
        print("The sky turned red, and the clouds turned black."); time.sleep(0.3)
        print("And the ground seemed to be fading."); time.sleep(0.3)
        print("Fading into dust, it seemed."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print(name+": DAVID?"); time.sleep(0.3)
        print("You hear a weak voice."); time.sleep(0.3)
        print("DAVID: Y-yes?"); time.sleep(0.3)
        print(name+": I found CARL. He really does miss you."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("DAVID: Ah, haha! T-that's good!"); time.sleep(0.3)
        print("DAVID: It's been a while, hasn't it?"); time.sleep(0.3)
        print("DAVID: Since that company was still intact."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("DAVID: Thanks for helping me... you don't know how much it means to me that he's alive."); time.sleep(0.3)
        print("DAVID: Everyone else died..."); time.sleep(0.3)
        print("DAVID starts to choke on the dust around him."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("DAVID: I guess the sickness really is spreading..."); time.sleep(0.3)
        print("DAVID: I can't feel my legs anymore..."); time.sleep(0.3)
        print("DAVID: I really hoped we could get along..."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("DAVID begins to start crying."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("DAVID: Why... why was I forced to live a life like this?"); time.sleep(0.3)
        print("DAVID: I've always tried to work hard, and make the world a better place..."); time.sleep(0.3)
        print("DAVID: CARL, ANGEL, all of the other workers in that cursed company..."); time.sleep(0.3)
        print("DAVID: None of them deserve what they got."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("DAVID: Ahahaha!"); time.sleep(0.3)
        print("DAVID: How the karma of this world goes."); time.sleep(0.3)
        print("DAVID: Those who work the hardest get beat the hardest."); time.sleep(0.3)
        print("DAVID: And those who beat the workers reap their rewards."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("DAVID: We were the only ones who dared to work."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("DAVID: We were the only ones who dared to do god's work."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print(name+": DAVID, stop it."); time.sleep(0.3)
        print("DXVID: We were the only ones who dared to be god."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("DXVXD: We were the only ones who dared to play god."); time.sleep(0.3)
        print(name+": DAVID, are you ok?"); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("DXVXD: Hahahaha!"); time.sleep(0.3)
        print("DXVXD: Okay?"); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("DXXXD: We were really the only gods."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("DXXXD: ..."); time.sleep(0.3)
        print("DXXXX: We WERE gods."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("XXXXX: ..."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: We are gods."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("A shockwave from what's left of DAVID pushes you back, slamming you into the wall."); time.sleep(0.3)
        healthDiff(-100)
        print("You lose 100 HP."); time.sleep(0.3)
        input(""); time.sleep(0.3)

        eatLoss(24)
        drinkLoss(24)
        sleepLoss(24)
        sleepEffect(24)

        print("You run back into the city, hoping to salvage what's left of Madda Gate."); time.sleep(0.3)
        print("It's really too late."); time.sleep(0.3)
        print("It really couldn't be helped."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: Purity, sanctuary, safety, kindness."); time.sleep(0.3)
        print("?????: Those are all things the Origin Company of Madda Gate sought to get."); time.sleep(0.3)
        print("?????: And yet, those who deserved it most received nothing but blades."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: And after all, why should you get to live sucha cushy life?"); time.sleep(0.3)
        print("?????: You meager humans are soaking up the limited life-force on this already doomed planet."); time.sleep(0.3)
        print("?????: Ah... the desperation of your cries."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: When DAVID was still alive, he cried as hard as you."); time.sleep(0.3)
        print("?????: When DAVID was alive, he helped you all, no matter how hard you beat him."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: You worms cry and shout the loudest of us all."); time.sleep(0.3)
        print("?????: Why couldn't you hear the screams and cries of the last children who believed in you?"); time.sleep(0.3)
        print("?????: It's annoying."); time.sleep(0.3)
        print("?????: It's disgusting."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: And you all deserve to die."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: One who identifies as", name+", thank you for your help with DAVID."); time.sleep(0.3)
        print("?????: You cared for him a lot."); time.sleep(0.3)
        print("?????: In his last moments, he did seek to talk to you."); time.sleep(0.3)
        print("?????: But it was too late! Hahahahaha! I killed him. You've been speaking to a corpse."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: Oh.... and how long he waited for you."); time.sleep(0.3)
        print("?????: Where were you, when he bled out on the floor?"); time.sleep(0.3)
        print("?????: He'd only been nice to you."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: Reminiscing about the past? Hoping to use your ancient \"wisdom\" to save the people in the present?"); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: How embarassing!"); time.sleep(0.3)
        print("?????: How awful!"); time.sleep(0.3)
        print("?????: How pathetic!"); time.sleep(0.3)
        print("?????: While your only ally bled out on the floor, you were holed up somewhere thinking about the ghosts of a dead world!"); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: It's important to live in the present!"); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: The people of this city embody your mentality. This meeting really was fate."); time.sleep(0.3)
        print("?????: No work, no brains, no thoughts, only complaints."); time.sleep(0.3)
        print("?????: No spirit, no ambition, no lives, only... memories."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: You could have saved all of your friends."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: BETH? Oh, she was a nice one. Tried her best to save others."); time.sleep(0.3)
        print("?????: But it was too late! Nobody escaped."); time.sleep(0.3)
        print("?????: I killed them all. They hurt me. It's only revenge."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: AVA? She was a hard one to find! Hid all over the fields outside the city!"); time.sleep(0.3)
        print("?????: What a bother. She really did try to fight."); time.sleep(0.3)
        print("?????: Her ambition was strong! No wonder why she never stepped into this city."); time.sleep(0.3)
        print("?????: So all I had to do was beat down her spirit."); time.sleep(0.3)
        print("?????: And your friend AVA died."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: Thank you for helping me track where CARL is."); time.sleep(0.3)
        print("?????: While you weakly tried to get yourself off that pathetic wall, I killed him too!"); time.sleep(0.3)
        print("?????: Oh... he tried as well. He tried quite hard."); time.sleep(0.3)
        print("?????: Such a warrior's training can't be overpowered so easily!"); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: What a nice guy. What a kind soul. What a... hilarious death."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: How do you feel?"); time.sleep(0.3)
        print("?????: Hopeless?"); time.sleep(0.3)
        print("?????: Angered?"); time.sleep(0.3)
        print("?????: ... Pathetic?"); time.sleep(0.3)
        print("?????: All normal feelings once one sees me!"); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: You had a good run."); time.sleep(0.3)
        print("?????: WEEP. As you watch your friends die in front of your eyes."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("S????: Make no mistake. Those anomalies made sense."); time.sleep(0.3)
        print("?L???: Burning city? I simply lit these disgusting huts on fire."); time.sleep(0.3)
        print("??O??: Screams, cries, and anger? Hopefully, you know where this all came from."); time.sleep(0.3)
        print("???T?: Fading grounds of the city? Dusty grounds? This city's lifeforce will fade as well."); time.sleep(0.3)
        print("????H: And rivers of blood? You stepped all over it, with those muddy boots. You stepped on the blood of your friends, enemies, and everyone here."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: This city is dead."); time.sleep(0.3)
        print("?????: You could have stopped it."); time.sleep(0.3)
        print("?????: They could have stopped it."); time.sleep(0.3)
        print("?????: The only one you have to blame, with your sloth is yourself."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: And those devils only have to blame, themselves."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("?????: Population of Madda Gate, one."); time.sleep(0.3)
        print("?????: Time to make it zero."); time.sleep(0.3)
        input(""); time.sleep(0.3)
        print("SLOTH: Sin Spirit of Sloth! Pleased to meet you!"); time.sleep(0.3)
        input(""); time.sleep(0.3)


    if activator == "ANGEL":
        meetAngel()

    elif activator == "AVA":
        meetAva()

    elif activator == "BETH":
        meetBeth()
        meetMaddaNPC()

    elif activator == "MADDANPC":
        meetMaddaNPC()
        meetBeth()

    elif activator == "CARL":
        meetCarl()

    elif activator == "MADDA":
        meetMaddaFinale()


maddaKeys = "M41M552A"

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
inventory = "|BEANS|WATER"

beginGame()
