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


def sleep(sleepValue):
    global fatigueValue
    global minSleepValue

    sleepValue = int(sleepValue)
    if (fatigueValue - sleepValue) < minSleepValue:
        fatigueValue = minSleepValue
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
        print("TIME: XX:XX, December XX, 5XXX \nLOCATION: Sagittarius Supercluster \nTRANSMISSION: 1XXXX"); time.sleep(0.5)
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
        print("Yet, nobody every smiled."); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("You made it into the city, hoping for a place to rest."); time.sleep(0.2)
        print("But even the outside was a better place than this."); time.sleep(0.2)
        print("However, you couldn't stop smiling, and you'd never felt so \"home\" before."); time.sleep(0.2)
        print("Have you ever been home in the first place? \n"); time.sleep(0.2)

    if activator == 1:
        cutscene1()

    elif activator == 2:
        cutscene2()

def meetCharacter(activator):
    def meetAngel():
        global hungerBar
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

        print("AVA: Yo, what are you looking so wistfully at?"); time.sleep(0.2)
        input(""); time.sleep(0.2)
        print("AVA: Hello?"); time.sleep(0.2)
        print("AVA: Rude. The name's Ava."); time.sleep(0.2)
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
        print("BETH: Oh, but we do! This city's people are just so... lazy! Nothing ever gets done, and DAVID's attitude certainly doesn't help."); time.sleep(0.2)
        print(name+": DAVID?"); time.sleep(0.2)
        print("BETH: Yes, DAVID. Former owner of a large construction and engineering company?"); time.sleep(0.2)
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
        input("")


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
