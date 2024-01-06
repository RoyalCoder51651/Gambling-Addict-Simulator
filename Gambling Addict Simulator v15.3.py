import random 
# GAMBLING ADDICT SIMULATOR V15.3
# ADDED A SAVE SYSTEM + COSMETIC CHANGES + TWO NEW LOCATIONS TO VISIT. SAVE INFO AT THE BOTTOM OF THE PROGRAM
# CODED BY @RoyalCoder51651
#BLACKJACK VAR
cards = [2,3,4,5,6,7,8,9,10,11] 
total = 0 
cputotal = 0
roundcount = 2
cpuloop = True
cpuchoice = True
massiveloop = True
loss = False
skip = False
drunken = 0
pot = 0
betloop = True
savecooldown = 0
list = []
slot = 0
money = 1000
bank = 0
cpumoney = 1000
cpuloss = False
looper = 0
passed = False
cpupassed = False
breakvar = False 
corrupted = False
# RANDOM VARIABLES I DONT REALLY CARE ABOUT
strength = 25
day = 1
sadcount = 0
collectiontime = False
addiction = 1
hp = 100
feedloop = True
debttime = 0
canbuy = True
# SAME AS ABOVE. ILL ORGANIZE LATER
choiceloop = True
happy = 100
hunger = 100
wifehappy = 100
wifehunger = 100
dayloop = True
wifedead = False
wifegone = False
dead = False
loop = True 
bookowned = False 
#STORE
bigloop = True 
# THE ABOVE VARIABLE ISNT EVEN PART OF THE STORE AT ALL. I DONT KNOW WHY I PUT IT THERE. IT'S FUNNY THO, SO IM JUST GOING TO LEAVE IT
gourmetfood = 0
stungun = False
Membership = False
potions = 0
skimask = False
necklaceowned = False
pills = 0
# PATH IN LIFE
robber = False
chef = False
gambler = False
rich = False
hacker = False
bankhack = False
wanted = 0
development = False
virusprogress = 0
makingbackdoor = False
backdoorprogress = 0
backdoor = False
siphon = False
undertheradar = 0
energy = 0
wizard = False
# CHARACTER SELECT
charloop = True
charchosen = False
# IF YOU WANT TO ADD MORE TO THE TITLE CARD, YOU CAN USE THIS THINGY I MADE TO GENERATE THE BIG TEXT:   https://codehs.com/sandbox/id/python-3-CPVFB1
print(" $$$$$$      $      $     $   $$$$$$    $         $$$$$$$   $     $    $$$$$$   ")
print("$           $ $     $$   $$   $     $   $            $      $$$   $   $         ")
print("$   $$$    $   $    $ $ $ $   $$$$$$$   $            $      $  $  $   $   $$$   ")
print("$    $    $$$$$$$   $  $  $   $     $   $            $      $   $$$   $    $    ")
print(" $$$$$    $     $   $  $  $   $$$$$$    $$$$$$$   $$$$$$$   $     $    $$$$$    ")
print("")
print("   0      000000    000000    0000000    000000   0000000   ")
print("  0 0     0     0   0     0      0      0            0      ")
print(" 0   0    0     0   0     0      0      0            0      ")
print("0000000   0     0   0     0      0      0            0      ")
print("0     0   000000    000000    0000000    000000      0      ")
print("")
print("  //////////     //////////////   //          //   //          //   //                     //         //////////////     //////////     ////////////     ")
print("  //////////     //////////////   //          //   //          //   //                     //         //////////////     //////////     ////////////     ")
print("//                     //         ////      ////   //          //   //                   //  //             //         //          //   //          //   ")
print("//                     //         ////      ////   //          //   //                   //  //             //         //          //   //          //   ")
print("////////////           //         //  //  //  //   //          //   //                 //      //           //         //          //   ////////////     ")
print("////////////           //         //  //  //  //   //          //   //                 //      //           //         //          //   ////////////     ")
print("            //         //         //    //    //   //          //   //               //////////////         //         //          //   //      //       ")
print("            //         //         //    //    //   //          //   //               //////////////         //         //          //   //      //       ")
print("////////////     //////////////   //    //    //     //////////     //////////////   //          //         //           //////////     //        //     ")
print("////////////     //////////////   //    //    //     //////////     //////////////   //          //         //           //////////     //        //     v15.3")
print("")
print("Welcome To Gambling Addict Simulator. The First 1494 Lines Code Were Written Over The Course Of 4ish Days By Me")
input("PRESS ENTER TO CONTINUE")
print('Do You Want To Load A Save, Or Start New? (Type Load) (Type New)')
while(loop == True):
    choice = input()
    if (choice == "New"):
        print("Do You Want To Play In Realism Mode? (Type Yes) (Type No)")
        while (charloop == True):
            choice = input()
            if (choice == "Yes"):
                realism = False
                break
            elif (choice == "No"):
                realism = True
                break
            else:
                print("Choice Not Recognized")
        print("Select Your Character")
        input("PRESS ENTER TO CONTINUE")
        while (charloop == True):
            if (charchosen == True):
                break
            print("---------------------------------------")
            print("Robber (Type Robber)")
            print("---------------------------------------")
            print("Average Dude (Type Average)")
            print("---------------------------------------")
            print("Below-Average Dude (Type Weakling)")
            print("---------------------------------------")
            print("Above-Average Dude (Type Strongling)")
            print("---------------------------------------")
            print("Rich Person (Type Rich)")
            print("---------------------------------------")
            print("Chef (Type Chef)")
            print("---------------------------------------")
            print("Proffesional Gambler (Type Gambler)")
            print("---------------------------------------")
            print("Proffesional Wizard (Type Wizard)")
            print("---------------------------------------")
            print("Programmer (Type Programmer)")
            print("---------------------------------------")
            charchoice = input()
            if (charchoice == "Robber"):
                print("The Robber Starts Off With A Ski Mask, And The Robber Trait. Be Careful, Because The Moral Implications Of Crime Make You Sad. Do You Want To Select This Character (Type Yes) (Type No)")
                while (charloop == True):
                    choice = input()
                    if (choice == "Yes"):
                        charchosen = True
                        happy = 50
                        skimask = True
                        robber = True
                        break
                    elif (choice == "No"):
                        break
                    else:
                        print("Command Not Recognized")
            elif (charchoice == "Average"):
                print("Just An Average Dude, With Average Stats. Hopefully Destined For Greatness, Likely Destined For Bankruptcy. Do You Want To Select This Character (Type Yes) (Type No)")
                while (charloop == True):
                    choice = input()
                    if (choice == "Yes"):
                        charchosen = True
                        break
                    elif (choice == "No"):
                        break
                    else:
                        print("Command Not Recognized")
            elif (charchoice == "Weakling"):
                print("Just A Below Average Dude With Below Average Stats. Hopefully Destined For Greatness, Likely Destined For Death. Only Play If You Want A Challenge. Do You Want To Select This Character (Type Yes) (Type No)")
                while (charloop == True):
                    choice = input()
                    if (choice == "Yes"):
                        charchosen = True
                        money = 500
                        hp = 75
                        strength = 15
                        happy = 75
                        hunger = 80
                        break
                    elif (choice == "No"):
                        break
                    else:
                        print("Command Not Recognized")
            elif (charchoice == "Strongling"):
                print("Just An Above Average Dude With Above Average Stats. Hopefully Destined For Greatness, Likely Destined To Achieve It. Only Play If The Game Is To Hard For You And You're A Baby. Do You Want To Select This Character (Type Yes) (Type No)")
                while (charloop == True):
                    choice = input()
                    if (choice == "Yes"):
                        charchosen = True
                        money = 2000000
                        hp = 150
                        strength = 30
                        happy = 150
                        hunger = 150
                        break
                    elif (choice == "No"):
                        break
                    else:
                        print("Command Not Recognized")
            elif (charchoice == "Wizard"):
                print("A Retired Birthday Magician Turned Proffesional Wizard. Starts With Health Potions, And The Ability To Cast Spells (Yes, This Is Really In A Game About Gamlbing) Do You Want To Select This Character (Type Yes) (Type No)")
                while (charloop == True):
                    choice = input()
                    if (choice == "Yes"):
                        charchosen = True
                        wizard = True
                        potions = 5
                        break
                    elif (choice == "No"):
                        break
                    else:
                        print("Command Not Recognized")
            elif (charchoice == "Chef"):
                print("A Master Of The Culinary Arts. Starts With Higher Hunger, Better Food, And Can Cook Food More Efficiently. Can Eat To His Heart's Content, And Enjoys Doing So. Do You Want To Select This Character (Type Yes) (Type No)")
                while (charloop == True):
                    choice = input()
                    if (choice == "Yes"):
                        charchosen = True
                        chef = True
                        hp = 125
                        strength = 20
                        happy = 125
                        hunger = 200
                        gourmetfood = 5
                        break
                    elif (choice == "No"):
                        break
                    else:
                        print("Command Not Recognized")
            elif (charchoice == "Rich"):
                print("A Spoiled Rich Kid. Starts With Lots Of Money, But Gets Very Sad When Things Dont Go As Planned. High Value Target. Do You Want To Select This Character (Type Yes) (Type No)")
                while (charloop == True):
                    choice = input()
                    if (choice == "Yes"):
                        charchosen = True
                        rich = True
                        money = 30000
                        break
                    elif (choice == "No"):
                        break
                    else:
                        print("Command Not Recognized")
            elif (charchoice == "Gambler"):
                print("A Self Proclaimed Professional Gambler (AKA A Hardcore Addict). Gets Happy When Making Large Bets And Winning. Starts With A Membership To The Casino. Do You Want To Select This Character (Type Yes) (Type No)")
                while (charloop == True):
                    choice = input()
                    if (choice == "Yes"):
                        charchosen = True
                        gambler = True
                        Membership = True
                        break
                    elif (choice == "No"):
                        break
                    else:
                        print("Command Not Recognized")
            elif (charchoice == "Programmer"):
                print("Can Hack Various Items, Increasing Profits And Things Of The Such. Starts With The Hacker Trait, But Low Strength, And No Wife (Because You're AntiSocial) . Do You Want To Select This Character (Type Yes) (Type No)")
                while (charloop == True):
                    memechance = random.randint(1,5)
                    choice = input()
                    if (choice == "Yes" and memechance == 1):
                        charchosen = True
                        massiveloop = False
                        day = 0
                        print("You Sat At Home Making A Game About Gambling Addictions During Your Winter Break Instead Of Being Social. You Were To Lazy To Do Anything. Game Over")
                        break
                    elif (choice == "Yes" and memechance != 1):
                        charchosen = True
                        strength = 5
                        wifegone = True
                        hacker = True
                        break
                    elif (choice == "No"):
                        break
                    else:
                        print("Command Not Recognized")
            else:
                print("Command Not Recognized")
        break
    elif(choice == "Load"):
        print("Enter Your Save In The Space Below")
        choice = input()
        tempitem = ''
        for item in choice:
            if (item == '|'):
                list.append(tempitem)
                tempitem = ''
            else:
                tempitem = tempitem + item
        try:
            money = float(list[0])
            happy = float(list[1])
            strength = float(list[2])
            hp = float(list[3])
            hunger = float(list[4])
            day = int(list[5])
            if (list[6] ==  'True'):
                wifedead = True
            else:
                wifedead = False
            wifehunger = float(list[7])
            wifehappy = float(list[8])
            if (list[9] ==  'True'):
                wifegone = True
            else:
                wifegone = False
            debttime = int(list[10])
            wanted = float(list[11])
            if (list[12] ==  'True'):
                gambler = True
            else:
                gambler = False
            if (list[13] ==  'True'):
                rich = True
            else:
                rich = False
            if (list[14] ==  'True'):
                robber = True
            else:
                robber = False
            if (list[15] ==  'True'):
                chef = True
            else:
                chef = False
            if (list[16] ==  'True'):
                wizard = True
            else:
                wizard = False
            if (list[17] ==  'True'):
                bankhack = True
            else:
                bankhack = False
            if (list[18] ==  'True'):
                siphon = True
            else:
                siphon = False
            virusprogress = int(list[19])
            if (list[20] ==  'True'):
                backdoor = True
            else:
                backdoor = False
            backdoorprogress = int(list[21])
            bank = float(list[22])
            undertheradar = int(list[23])
            if (list[4] ==  'True'):
                necklaceowned = True
            else:
                necklaceowned = False
            potions = int(list[25])
            gourmetfood= int(list[26])
            if (list[27] ==  'True'):
                bookowned = True
            else:
                bookowned = False
            if (list[28] ==  'True'):
                stungun = True
            else:
                stungun = False
            if (list[29] ==  'True'):
                Membership = True
            else:
                Membership = False
            if (list[30] ==  'True'):
                realism = True
            else:
                realism = False
            if (list[31] ==  'True'):
                skimask = True
            else:
                skimask = False
            energy = float(list[32])
            pills = int(list[33])
            slot = float(list[34])
            if (list[35] ==  'True'):
                development = True
            else:
                development = False
            if (list[36] ==  'True'):
                makingbackdoor = True
            else:
                makingbackdoor = False
            # ADD WHATEVER YOU ADDED TO THE LIST HERE. JUST SET THE VARIABLE EQUAL TO THE INDEX. IF IT HOLDS A BOOLEAN, USE THE CONDITIONAL THINGY LIKE ON LINE 366 BECAUSE OF HOW PYTHON TYPECAST WORKS
            input("SAVE LOADED. PRESS ENTER TO START GAME")
            list = []
            savecooldown = 7
            break
        except:
            print("Corrupted Or Outdated Save Data. Sorry :(")
            massiveloop = False
            corrupted = True
            bigloop = False
            break
    else:
        print("Choice Not Recognized")
# DEBT COLLECTOR FIGHT
                
def fightscene():
    global debtdmg
    global debthp
    global hp
    global money
    global debttime
    global strength
    global breakvar
    global potions
    global stungun
    global wizard
    global energy
    global massiveloop
    fightloop = True
    while (fightloop == True):
        if (breakvar == True):
            breakvar = False
            break
        if (hp <= 0):
            print("You Died. Try Working Out Next Time To Increase Your Strength. Game Over")
            massiveloop == False
            fightloop = False
            break
        print("Will You Choose To Use A Strong Attack, Which Has A Chance To Fail (Type Strong), Or A Basic Attack (Type Basic), Which Is Guranteed Damage")
        if (stungun == True):
            print("You Can Also Use The Stun Gun You Bought Earlier (Type Stun Gun). This Will Deal 75% Of The Debt Collector's Current HP")
        if (wizard == True):
            print("Because Of Your Wizard Skills, You Can Cast A Fireball (Yes, Really). It Will Deal 1 Damage For Every Energy You Put Into It (Type Fireball).")
        minifightloop = True
        while (minifightloop == True):
            if (breakvar == True):
                breakvar = False
                break
            fightchoice = input()
            if (fightchoice == "Strong"):
                fightchance = random.randint(1,10)
                if fightchance > 4:
                    attack = strength * 2
                    debthp -= attack
                    print("Your Attack Lands. You Deal", attack, "Damage, Leaving The Debt Collector With", debthp)
                    break
                else:
                    print("You Miss, And Do No Damage")
                    break
            elif(fightchoice == "Basic"):
                debthp -= strength
                print("You Do", strength, "Damage, Leaving The Debt Collector With", debthp, "Hp")
                break
            elif (fightchoice == "Stun Gun"):
                attack = debthp * 0.75
                debthp -= attack
                print("You Do", attack, "Damage, Leaving The Debt Collector With", debthp, "Hp")
            elif (fightchoice == "Fireball"):
                print("How Much Energy Would You Like To Spend Casting Your Fireball? You Currently Have", energy, "Energy")
                while (minifightloop == True):
                    choice = input()
                    try:
                        if (int(choice) > energy):
                            print("You Don't Have Enough Energy For That")
                        else:
                            debthp -= int(choice)
                            energy -= int(choice)
                            print("The Debt Collector Now Has", debthp, "Hp")
                            breakvar = True
                            break
                    except:
                        print("Only Type Whole Numbers")
            else:
                print("Invalid Attack")
        if (debthp <= 0):
            print("You've Bested The Debt Collector This Time. Be Careful, As He Will Return If You Go Back Into Debt For Too Long. However, He Forgot His Money Bag, Giving You 5 Thousand Dollars")
            money += 5000
            debttime = 0
            breakvar = True
            break
        debtchoice = random.randint(1,100)
        if (debtchoice > 50):
            hp -= debtdmg
            print("The Debt Collector Whacks You With His Cane, Dealing", debtdmg, "Damgage. This Leaves You With", hp, "Health")
            input()
        elif (debtchoice > 1):
            attack = random.randint(1,5) * 10
            hp -= attack
            print("The Debt Collector Hit You With His Comically Large Money Bag, Dealing", attack, "Damage. You Now Have", hp, "Health")
            input()
        elif (debtchoice == 1):
            hp -= 75
            print("The Debt Collector Used Fireball, Dealing 75 Damage. You Now Have", hp, "Health.... Dont Ask Why The Debt Collector Can Shoot Fireballs")
            input()
        if (potions > 0):
            print("You Have", potions, "Potions. Would You Like To Start Drinking Them (Type Drink), Or Save Them (Type Save)")
            while (choiceloop == True):
                choice = input()
                if (choice == "Drink"):
                    print("Will You Drink One (Type Drink), Or Will You Stop (Type Stop)")
                    while (choiceloop == True):
                        if (potions <= 0):
                            break
                        choice = input()
                        if (choice == "Drink"):
                            hp += 25
                            potions -= 1
                        elif (choice == "Stop"):
                            break
                        else:
                            print("Command Not Recognized")
                        print("You Have", potions, "Health Potions Left")
                    break
                elif(choice == "Save"):
                    break
                else:
                    print("Command Not Recognized")  
# BLACKJACK INITILZATION
def cpubrain():
    global cputotal
    global loop
    global cpuloop
    global passed
    global cpupassed
    global breakvar
    cpufail()
    if (cputotal > 19):
        print("CPU passed") 
        cpupassed = True
        cpuloop = False
        if (passed == False):
            loop = True
    elif (cputotal > 16):
        cpuc2 = random.randint(1,10)
        if (cpuc2 > 8):
            cputotal += random.choice(cards) 
            cpufail()
        else:
            print("CPU passed") 
            cpupassed = True
            cpuloop = False
            if (passed == False):
                loop = True
    elif (cputotal > 10):
        cpuc2 = random.randint(1,10)
        if (cpuc2 > 1):
            cputotal += random.choice(cards) 
            cpufail()
        else:
            print("CPU passed") 
            cpupassed = True
            breakvar = True
    else:
        cputotal += random.choice(cards) 
        cpufail()
def failcondition(): 
    global total 
    global loop 
    global breakvar 
    global bigloop
    global loss
    global happy
    if total > 21: 
        loop = False 
        breakvar = True 
        bigloop = False 
        print("You Busted") 
        loss = True
        happy -= 25
def cpufail(): 
    global cputotal 
    global cpuloop 
    global breakvar 
    global cpuloss
    if cputotal > 21: 
        cpuloop = False 
        breakvar = True
        cpuloss = True
        print("CPU Busted")

#MAIN GAMEPLAY LOOP

while(massiveloop == True):
    input("PRESS ENTER TO START A NEW DAY")
    print("")
    if (realism == True):
        hunger = 120
        wifehunger = 110
        happy = 100
        wifehappy = 100
        hp = 100
    print("Day", day)
    stimchance = random.randint(1, 50)
    if (stimchance == 1):
        print("")
        input("SPECIAL EVENT")
        print("")
        money += 2000
        print("A Stimulus Check Gets Released, Granting You 2000 Dollars. You Now Have", money, "Dollars")
    if (bookowned == False):
        addiction += 1
    if (bankhack == True):
        bank *=1.25
    else: 
        bank *= 1.10
    undertheradar += 1
    if (wizard == True):
        energy += day * 5
        print("Your Wizard Powers Grow In Strength Every Day. You Now Have", energy, "Energy")
    print("")
    print("Where Would You Like To Go Today? Blackjack (Type Blackjack), Gym (Type Gym), Job (Type Job), Store (Type Store), Bank (Type Bank), Pub (Type Pub), Slot Machines (Type Slots)")
    adchoice = ''
    if (addiction > 3):
        poop = random.randint(1,3)
        if (poop == 1):
            adchoice = "Slots"
        else:
            adchoice = "Blackjack"
    while (dayloop == True):
        daychoice = input()
        if (daychoice == "Blackjack" or adchoice == "Blackjack"):

    # Blackjack
            if (addiction > 3):
                print("Your Addiction To Gambling Wins You Over At The Last Second. You Decide To Play Blackjack")
            addiction -= 2
            daychoice = "Blackjack"
            if (money == 0):
                print("You Have No Money. Any Further Money You Bet Will Put You In Debt. How Much Money Would You Like To Bet")
            elif (abs(money) + money == 0):
                print("You Are Currently", money, "Dollars In Debt. You Can Still Play, But You Must Take A Loan. You Can Only Take A Loan Up To 10000 Dollars. What Would You Like To Bet")
            else:
                print ("How Much Money Would You Like To Bet? You Currently Have", money)
            betloop = True
            while (betloop == True):
                try:
                    bet = input()
                    bet = int(bet)
                    if (abs(bet) + bet == 0):
                        print("Nice Try Buddy, But You Have To Bet Something, And You Cant Bet Negative Values")
                    elif (bet < 200):
                        print("Minimum Buy-in Is 200 Dollars. You Can Get A Loan If You Cannot Afford The Buy-in")
                    elif (bet > 10000 and abs(money) + money == 0 and Membership == False):
                        print("The Maximum Loan You Can Take While In Debt Is 10000 Dollars")
                    elif (bet > 20000 and abs(money) + money == 0 and money != 0):
                        print("The Maximum Loan You Can Take With A Membership Is 20000 Dollars")
                    elif (bet >= money and gambler == True):
                        print("The Thrill Of Going All In Makes You Happier")
                        happy += 25
                        break
                    else:
                        break
                except:
                    print("Only Type Whole Numbers")
            money -= bet
            cpubet = bet + random.randint(0, 2) * 100
            print("CPU bet", cpubet)
            print("You Now Have", money)
            pot = (cpubet + bet)
            print("Round 1")
            while (bigloop == True):  
                while (loop == True): 
                    if (passed == True):
                        break
                    choice = input("Do You Want A Card (Type Hit), Or Are You Good? (Type Pass)") 
                    if (choice == 'Hit'): 
                        deal = random.choice(cards) 
                        print("You got a", deal) 
                        total = total + deal
                        print("Your total is now", total)
                        failcondition() 
                        if breakvar == True:
                            breakvar = False 
                            break 
                        break 
                    elif (choice == 'Pass'): 
                        print("You passed") 
                        passed = True
                        loop = False
                    else: 
                        print("Choice Not Recognized") 
                while (cpuloop == True): 
                    if (cpupassed == True):
                        break
                    if (cpupassed == False):
                        cpubrain()
                    break
                if (cpupassed == True and passed == True):
                    break
                elif (loss == True or cpuloss == True):
                    break
                else:
                    print("")
                    print("Round", roundcount)
                    print("")
                    roundcount += 1
            print("")
            if (loss == False and cpuloss == False):
                print("The CPU Had", cputotal) 
                if (cputotal > total): 
                    print("CPU WINS!!!")
                    if (rich == True):
                        happy -= 25
                    happy -= 25
                    print("")
                    cpumoney += pot
                    pot = 0
                elif (cputotal < total): 
                    print("YOU WIN!!!")
                    happy += 25
                    if (gambler == True):
                        happy += 25
                    print("")
                    if (Membership == True):
                        money += pot * 1.5
                    else:
                        money += pot
                    pot = 0
                elif (cputotal == total): 
                    print("Draw. You Both Get A Quarter Of The Total")
                    choice = random.randint(1,100)
                    if (choice > 50):
                        happy += 5
                        if (gambler == True):
                            happy += 5
                    else:
                        if (rich == True):
                            happy -= 5
                        happy -= 5
                    if (Membership == True):
                        money += (pot/2) * 1.5
                    else:
                        money += pot/4
                    cpumoney += pot/4
                    pot = 0
                    print("")
            if (cpuloss == True):
                print("YOU WIN!!!")
                happy += 25
                print("")
                if (Membership == True):
                    money += pot * 1.5
                else:
                    money += pot
                pot = 0
            elif (loss == True):
                print("CPU WINS!!!")
                happy -= 25
                if (rich == True):
                    happy -= 25
                print("")
                cpumoney += pot
                pot = 0
            print("")
            input("PRESS ENTER TO CONTINUE")
            print("")
            break

# GYM

        elif (daychoice == "Gym"):
            addiction += 1
            print("You Currently Have", strength, "Strength. Will You Choose To Workout (Type Workout), Or Leave (Type Leave)")
            gymloop = True
            while (gymloop == True):
                gymchoice = input()
                if (gymchoice == "Workout" and money >= 100):
                    print("How Much Would You Like To Spend Working Out Today. 100 Dollars Is One Unit Of Stength. You Have", money, "Dollars")
                    while(gymloop == True):
                        try:
                            gymchoice = int(input())
                            gymchance = random.randint(1,20)
                            if (gymchance > 3 and gymchoice <= money):
                                strength += gymchoice/100
                                money -= gymchoice
                                break
                            elif (gymchoice > money):
                                print("You Dont Have Enough Money To Work Out That Much. You Have", money, "Money")
                            else:
                                print("You Hurt Yourself While Attempting To Workout. You Take 5 Points Of Damage, Leaving You At", hp, "Health, And You Leave For The Day")
                                break
                        except:
                            print("Only Type Whole Numbers.")
                    break
                elif (gymchoice == "Leave"):
                    print("You Choose To Leave")
                    break
                elif (money <= 100):
                    print("You Dont Have Enough Monety To Work Out")
                else:
                    print("Choice Not Recognized")
            print("You Now Have", strength, "Strength, And", hp, "Health")
            print("")
            input("PRESS ENTER TO CONTINUE")
            print("")
            break

# JOB
            
        elif (daychoice == "Job"):
            addiction += 1
            print("You Currently Have", money, "Money. Will You Choose To Take A Shift At Your Job (Type Work), Or Leave (Type Leave)")
            jobloop = True
            while (jobloop == True):
                jobchoice = input()
                if (jobchoice == "Work"):
                    print("How Many Hours Would You Like To Work. Each Hour Will Earn You 200 Dollars (High Paying Job I Guess), But Make You Less Happy ")
                    minijobloop = True
                    while(minijobloop == True):
                        jobchoice = int(input())
                        if (jobchoice > 12):
                            print("You Can Only Work A Max Of 12 Hours In A Day")
                        elif (jobchoice < 13):
                            earning = jobchoice * 200
                            money += earning
                            happy -= jobchoice * 5
                            print("You Work For", jobchoice, "Hours. During This Time, You Earned", earning, "Dollars")
                            break
                        else:
                            print("Choice Not Recognized")
                    break
                elif (jobchoice == "Leave"):
                    break
                else:
                    print("Command Not Recognized")
            print("")
            input("PRESS ENTER TO CONTINUE")
            print("")
            break

# STORE 
        
        elif (daychoice == "Store"):
            addiction += 1
            print("You Currently Have", money, "Money. The Items You Purchase Here Will Be Available At Night, Or When Applicable. Will You Shop (Type Shop) Or Leave (Type Leave)")
            storeloop = True
            while (storeloop == True):
                storechoice = input()
                if (storechoice == "Shop"):
                    while (storeloop == True):
                        print("What Would You Like To Buy?")
                        print("_________________________________________________________________________________________________________________")
                        print("Stun Gun (1000 Dollars, Helpful In Moments Of Comabt) (Type Stun Gun)")
                        print("_________________________________________________________________________________________________________________")
                        print("Gourmet Food (300 Dollars, PLus 30 Hunger And Plus 30 Happiness) (Type Gourmet Food)")
                        print("_________________________________________________________________________________________________________________")
                        print("Self Control For Dummies (1500 Dollars, Addiction To Gambling Is Less Prevalent) (Type Book)")
                        print("_________________________________________________________________________________________________________________")
                        print("Casino Membership (15000 Dollars, Make 50% More From Bets, Minimum Loan While In Debt Doubles) (Type Membership)")
                        print("_________________________________________________________________________________________________________________")
                        print("Gucci Ski Mask (2000 Dollars, Perfect For Showing Off Your Style While Staying Warm) (Type Mask)")
                        print("_________________________________________________________________________________________________________________")
                        print("Diamond Necklace (4000 Dollars, The Perfect Gift For Your Wife) (Type Necklace")
                        print("_________________________________________________________________________________________________________________")
                        print("Anti Anti-Depressants (200 Dollars, Makes You Sadder) (Type Meds)")
                        print("_________________________________________________________________________________________________________________")
                        print("Health Potion (500 Dollars, + 25 Hp) (Type Potion)")
                        print("_________________________________________________________________________________________________________________")
                        print("Exit (Type Exit)")
                        print("_________________________________________________________________________________________________________________")
                        storechoice = input()
                        if (storechoice == "Stun Gun" and money > 999):
                            stungun = True
                            money -= 1000
                            print("You Bought A Stun Gun")
                            print("You Now Have", money, "Money")
                            input("TYPE ENTER TO CONTINUE")
                        elif (storechoice == "Gourmet Food" and money > 299):
                            gourmetfood += 1
                            money -= 300
                            print("You Bought Gourmet Food")
                            print("You Now Have", money, "Money")
                            input("TYPE ENTER TO CONTINUE")
                        elif (storechoice == "Book" and money > 1499):
                            bookowned = True
                            money -= 1500
                            addiction -= 3
                            print("You Bought Self Control For Dummies")
                            print("You Now Have", money, "Money")
                            input("TYPE ENTER TO CONTINUE")
                        elif (storechoice == "Membership" and money > 14999):
                            Membership = True
                            money -= 15000
                            print("You Bought A Casino Membership")
                            print("You Now Have", money, "Money")
                            input("TYPE ENTER TO CONTINUE")
                        elif (storechoice == "Mask" and money > 1999):
                            skimask = True
                            money -= 2000
                            print("You Bought The Gucci Ski Mask")
                            print("You Now Have", money, "Money")
                            input("TYPE ENTER TO CONTINUE")
                        elif (storechoice == "Meds" and money > 199):
                            pills += 1
                            money -= 200
                            print("You Bought Anti Anti-Depressants")
                            print("You Now Have", money, "Money")
                            input("TYPE ENTER TO CONTINUE")
                        elif (storechoice == "Potion" and money > 499):
                            potions += 1
                            money -= 500
                            print("You Bought A Health Potion")
                            print("You Now Have", money, "Money")
                            input("TYPE ENTER TO CONTINUE")
                        elif (storechoice == "Necklace" and money > 399):
                            necklacechance = random.randint(1,4)
                            if (necklacechance > 1):
                                necklaceowned = True
                                money -= 4000
                                print("You Bought The Diamond Necklace")
                                print("You Now Have", money, "Money")
                                input("TYPE ENTER TO CONTINUE")
                            else:
                                money -= 4000
                                print("The Necklace Was A Fake, And Broke Mere Seconds After You Bought It. You Now Know Why The Sign Says No Refunds")
                                print("You Now Have", money, "Money")
                                input("TYPE ENTER TO CONTINUE")
                        elif (storechoice == "Exit"):
                            breakvar = True
                            break
                        else:
                            print("Command Not Recognized, Or You Don't Have Enough Money")
                    break
                elif (storechoice == "Leave"):
                    break
                else:
                    print("Command Not Recognized")
            print("")
            input("PRESS ENTER TO CONTINUE")
            print("")
            break
        
# BANK
        
        elif (daychoice == "Bank"):
            addiction += 1
            print("You Currently Have", money, "Money, And You Balance In The Bank Is", bank, ". Would You Like To Make A Deposit (Deposits Grow Over Time) (Type Deposit), A Withdrawl (Type Withdrawl), Or Leave (Type Leave)?")
            if (skimask == True):
                print("Because Of Your Ski Mask, You Can Rob The Bank (Type Rob)")
            if (hacker == True):
                print("Because Of Your Hacking Knowledge, You Can Infect The System With A Virus. (Type Hack)")
            bankloop = True
            while (bankloop == True):
                if (breakvar == True):
                    breakvar = False
                    break
                bankchoice = input()
                if (bankchoice == "Deposit"):
                    while (bankloop == True):
                        print("How Much Money Would You Like To Deposit? Type Exit To Exit")
                        bankchoice = input()
                        if (bankchoice == "Exit"):
                            break
                        elif (int(bankchoice) > money):
                            print("You Don't Have Enough Money For That. Try Again")
                        elif (abs(int(bankchoice)) + int(bankchoice) == 0):
                            print("You Cannot Deposit A Negative Amount")
                        elif (money > 0):
                            bank += int(bankchoice)
                            money -= int(bankchoice)
                            breakvar = True
                            break
                        else:
                            print("Command Not Recognized")
                elif (bankchoice == "Withdrawl"):
                    print("How Much Money Would You Like To Withdraw? Type Exit To Exit")
                    while (bankloop == True):
                        bankchoice = input()
                        try:
                            if (bankchoice == "Exit"):
                                break
                            elif (int(bankchoice) > bank):
                                print("That's Too Much. You Have", bank, "Money In Your Account")
                            elif (abs(int(bankchoice)) + int(bankchoice) == 0):
                                print("You Cannot Withdrawl A Negative Amount")
                            elif (bank > 0):
                                bank -= int(bankchoice)
                                money += int(bankchoice)
                                breakvar = True
                                break
                        except:
                            print("Only Type Whole Numbers")
                elif (bankchoice == "Rob"):
                    print("Are You Sure You Want To Rob The Bank? This Is Irreversible, And Crime Rarely Pays (Type Yes) (Type No)")
                    while (bankloop == True):
                        if (breakvar == True):
                            breakvar = False
                            break
                        bankchoice = input()
                        if (bankchoice == "Yes"):
                            if (robber == False):
                                print("You Chose A Life Of Crime, Signaling To All Other Robbers That The Bank Was Your Turf")
                                wanted += 1
                                undertheradar = 0
                                robber = True
                            robchance = random.randint(1, 100)
                            if (robchance > 25):
                                robloot = random.randint(-5, 10) * 1000
                                if (robloot > 0): 
                                    money += robloot
                                    print("You Succesfully Robbed The Bank For", robloot, "Money. Your Total Money Is Now", money)
                                elif (robloot == 0):
                                    print("You Succeeded, But Crime Doesn't Pay, So You Make Nothing. Come Back Another Time")
                                elif (robloot < 0):
                                    money += robloot
                                    print("You Succesfully Robbed The Bank. However, The Bank Was In Debt, Which You Then Stole. You Ended Up Stealing", robloot, "Putting Your Total Money To", money)
                                breakvar = True
                            else:
                                print("You Failed In Robbing The Bank, And Tripped The Alarm. This Woke Up The Automated Security System, Locking You Inside. You Can Bribe The Security System (Type Bribe), Or Try To Break Out (Type Break)")
                                if (hacker == True):
                                    print("You Can Also Hack The Bank System. Be Careful, As This Will Further Increase your Wanted Level (Type Hack")
                                while (bankloop == True):
                                    breakvar = True
                                    bankchoice = input()
                                    if (bankchoice == "Bribe"):
                                        if (money < 10000):
                                            bribe = 10000
                                        elif (money > 10000):
                                            bribe = money * 1.25
                                        money -= bribe
                                        print("You Gave The System", bribe, "Dollars, And It Decided To Let You Go. This Puts Your Total At", money, "Dollars")
                                        break
                                    elif (bankchoice == "Break" and strength >= 50):
                                        print("You Slapped The Security System Accros The Face, And It Let You Free")
                                        break
                                    elif (bankchoice == "Break" and strength < 50):
                                        hp -= 5
                                        print("You Tried To Break The System By Punching It, But It Just Punched You Back. You Now Have", hp, "Hp, And You Are Still Stuck In The Bank")
                                    elif (bankchoice == "Hack" and hacker == True):
                                        wanted += 1
                                        undertheradar = 0
                                        print("Your Wanted Level Is Now", wanted)
                                        break
                                    else:
                                        print("Choice Not Recognized")
                        elif (bankchoice == "No"):
                            break
                        else:
                            print("Command Not Recognized")
                    break
                elif (bankchoice == "Hack"):
                    print("Are You Sure You Want To Hack The Bank? This Will Increase Your Wanted Level (Type Yes) (Type No)")
                    while (bankloop == True):
                        bankchoice = input()
                        if (bankchoice == "Yes"):
                            print("You Decided To Hack The Bank. Simply Write A Virus Below Using The Functions BankHack, And Fortify Written In Standard Python Or C# Syntax")
                            input("")
                            print("Just Kidding Lol. You Succesfully Infect The Bank's System. Your Deposits Now Earn More Per Day")
                            bankhack = True
                            wanted += 1
                            undertheradar = 0
                            print("Your Wanted Level Is Now", wanted)
                            breakvar = True
                            break
                        elif (bankchoice == "No"):
                            breakvar = True
                            break
                        else:
                            print("Command Not Recognized")
                elif (bankchoice == "Leave"):
                    break
                else:
                    print("Command Not Recognized")
            print("")
            input("PRESS ENTER TO CONTINUE")
            print("")
            break

# PUB

        elif (daychoice == "Pub"):
            addiction += 1
            print("You Can Drink At The Pub. This Makes You Happy, But Dont Over-Do It. Will You Drink (Type Drink) Or Leave (Type Leave)")
            while (loop == True):
                choice = input()
                if (choice == "Drink"):
                    while(loop == True):
                        if (drunken != 3):
                            if (drunken == 0):
                                print("You Feel Fine. Will You Drink A Beer For 100 Dollars (Type Drink) Or Leave (Type Leave)")
                            elif (drunken == 1):
                                print("You Feel Tipsy. Will You Drink A Beer For 100 Dollars (Type Drink) Or Leave (Type Leave)")
                            elif (drunken == 2):
                                print("You Are One Drink Away From Being Blackout Drunk. Will You Drink A Beer For 100 Dollars (Type Drink) Or Leave (Type Leave)")
                            choice = input()
                            if (choice == "Drink" and money > 99):
                                happy += 25
                                drunken += 1
                                money -= 100
                                print("You Enjoy Your Beer")
                            if (choice == "Drink" and money <= 99):
                                print("You Dont Have Enough Money To Buy A Beer. You Leave In A Fit")
                                break
                            elif (choice == "Leave"):
                                break
                            else:
                                print("Choice Not Recognized")
                        elif(drunken >= 3):
                            print("You Are Too Drunk To Keep Drinking. You Decide To Leave")
                            break
                    break
                elif(choice == "Leave"):
                    break
                else:
                    print("Choice Not Recognized")
            break

# SLOT MACHINES
    
        elif (daychoice == "Slots" or adchoice == "Slots"):
            addiction -= 1
            print("You Have", money, "Money")
            if (money >= 500):
                print("How Many Spins Do You Want To Try? 100 Dollars Is One Spin")
            else:
                print("You Dont Have Enough Money To Afford A Spin. You Can Take A Loan, But Only Up To 100 Spins. How Many Spins Would You Like To Take")
            while(loop == True):
                if (breakvar == True):
                    breakvar = False
                    break
                try:
                    choice = round(int(input()), 0)
                    if (choice > 0 and money >= 500):
                        while (looper != choice):
                            looper += 1
                            print("SPIN", looper)
                            slot += 100
                            money -= 100
                            num1 = random.randint(1,10)
                            num2 = random.randint(1,10)
                            num3 = random.randint(1,10)
                            print(num1, num2, num3)
                            if (num1 == num2 and num2 == num3):
                                print("You Win", 5000 + slot / 2, "Dollars!!!. However, The Casino Says That You Are Only Allowed One Win Per Day. They Kick You Out, But You Get Refunded For The Money You Didn't Spend")
                                money += (5000 + slot /2)
                                breakvar = True
                                break
                            else:
                                print("You Lost")
                            if (skip == False):
                                print("PRESS ENTER TO CONTINUE, OR SKIP (Type Skip)")
                                schoice = input()
                                if (schoice == "Skip"):
                                    skip = True
                        break
                    elif (choice > 0  and money < 100 and choice <= 100):
                        while (looper != choice):
                            looper += 1
                            print("SPIN", looper)
                            slot += 100
                            money -= 100
                            num1 = random.randint(1,10)
                            num2 = random.randint(1,10)
                            num3 = random.randint(1,10)
                            print(num1, num2, num3)
                            if (num1 == num2 and num2 == num3):
                                print("You Win", 5000 + slot / 2, "Dollars!!!. However, The Casino Says That You Are Only Allowed One Win Per Day. They Kick You Out, But You Are Refunded For The Money You Didn't Spend")
                                money += (5000 + slot /2)
                                breakvar = True
                                break
                            else:
                                print("You Lost")
                            if (skip == False):
                                print("PRESS ENTER TO CONTINUE, OR SKIP (Type Skip)")
                                schoice = input()
                                if (schoice == "Skip"):
                                    skip = True
                        break
                    elif (choice > 0 and choice > 100):
                        print("You Can Only Take Loans Up To 10000 Dollars, Which Is 100 Spins")
                    else:
                        print("You Dont Have Enough Money. You Can Still Play, But You Have To Take A Loan")
                except:
                    print("Only Type Whole Numbers")
            if (skip == True):
                input("PRESS ENTER TO CONTINUE")
                skip = False
            break
        else:
            print("Choice Not Recognized, Or You Haven't Unlocked That Option")
    robchance = random.randint(1, 15)
    if (robchance == 1 and rich == True):
        print("You Got Robbed On The Way Back To Your House. The Robbers Took Everything")
        money = 0
# Resetting after blackjack is completed. Could def put inside the blackjack section, but we ball
    
    wifehunger -= 10
    hunger -= 20
    looper = 0
    cpupassed = False
    passed = False
    loop = True
    cpuloop = True
    bigloop = True
    total = 0
    cputotal = 0
    day += 1
    loss = False
    cpuloss = False
    breakvar = False
    roundcount = 1

# END OF DAY
    print("You Decide You've Had Enough For The Day, And Drive Home.")
    robchance = random.randint(1,4)
    num1 = random.randint(1,5)
    num2 = random.randint(6,10)
    if (drunken == 1 and robchance == 1):
        print("")
        input("SPECIAL EVENT")
        print("")
        print("You Get Pulled Over For Speeding. The Officer Starts To Perform A Field Sobriety Test")
        input("PRESS ENTER TO CONTINUE")
        print('The Officer Says "What Is', num1, '+', num2, '?". Type The Answer')
        while(loop == True):
            choice = input()
            try:
                if (int(choice) == num1 + num2):
                    print("You Are Correct. The Officer Lets You Go")
                    break
                elif (int(choice) != num1 + num1):
                    print("")
                    input("MAJOR EVENT")
                    print("")
                    print("You Answered The Question Wrong Lol. You Dumb. Game Over")
                    massiveloop = False
                    bigloop = False
                    break
            except:
                print("Choice Not Recognized")
    elif (drunken == 2 and robchance <= 2):
        print("")
        input("SPECIAL EVENT")
        print("")
        print("You Get Pulled Over For Speeding. The Officer Starts To Perform A Field Sobriety Test")
        input("PRESS ENTER TO CONTINUE")
        print('The Officer Says "What Is', num1, '*', num2, '+', num1,'?". Type The Answer')
        while(loop == True):
            choice = input()
            try:
                if (int(choice) == (num1 * num2) + num1):
                    print("You Are Correct. The Officer Lets You Go")
                    break
                elif (int(choice) != (num1 * num2) + num1):
                    print("")
                    input("MAJOR EVENT")
                    print("")
                    print("You Answered The Question Wrong Lol. You Dumb. Game Over")
                    massiveloop = False
                    bigloop = False
                    break
            except:
                print("Choice Not Recognized")
    elif (drunken == 3):
        print("")
        input("SPECIAL EVENT")
        print("")
        print("You Get Pulled Over For Speeding. The Officer Starts To Perform A Field Sobriety Test")
        input("PRESS ENTER TO CONTINUE")
        print('The Officer Says "Scrangle Flongoo Plucktry Scribligan Hibble Dabble Doo Robert DeNeniro" (You Cant Understand Because You Are Drunk) Type The Answer')
        while(loop == True):
            choice = input()
            if (choice == "Blue"):
                print("Yeah You Def Looked At The Code To Get The Answer. Game Is Game Tho")
                break
            else:
                print("")
                input("MAJOR EVENT")
                print("")
                print("The Officer Knows You Are Heavily Inebriated, And You Get Charged For A Second Offense Of Drunken Driving. This Lands You 2 Years In Jail. Game Over")
                massiveloop = False
                bigloop = False
                break
    drunken = 0
    if (wifedead == False and wifegone == False and necklaceowned == False):
        wifeearn = random.randint(1,3)*100
        print("Your Wife Earned", wifeearn, "Today At Her Job")
        money += wifeearn
    if (wifedead == False and wifegone == False and necklaceowned == True):
        wifeearn = random.randint(1,10)*200
        print("The Necklace You Bought Your Wife Increased Her Profits Today To", wifeearn,)
        money += wifeearn
        wifehappy += 50
    print("At The End Of The Day, You Have", money, "Dollars")
    print("")
    if (abs(money) + money == 0 or money < 0):
        canbuy = False
        wifehappy -= 25
    else:
        canbuy = True
    if (happy > 200):
        print("You Are Dangerously Happy")
    elif (happy > 150):
        print("You Are Impossibly Happy")
    elif (happy > 120):
        print("You Feel Incredibly Happy")
    elif (happy > 100):
        print("You Feel Very Happy")
    elif (happy > 75):
        print("You Feel Happy")
    elif (happy > 50):
        print("You Feel Normal")
    elif (happy > 25):
        print("You Feel Sad")
    elif (happy > 0):
        print("You Feel Depressed")
    elif (happy <= 0):
        print("You Feel Like Your Current Life Isn't Worth It. You Have A Sudden And Strange Urge To Be A Fisherman")
        sadcount += 1
    if (daychoice == "Blackjack" and wifegone == False and wifedead == False):
        print("Your Wife Is Annoyed That You Went Gambling Again Today")
        wifehappy -= 25
    if (wifehappy > 250 and wifedead == False and wifegone == False):
        print("Your Wife Is Dangerously Happy")
    elif (wifehappy > 150 and wifedead == False and wifegone == False):
        print("Your Wife Says She Is Overjoyed")
    elif (wifehappy > 75 and wifedead == False and wifegone == False):
        print("Your Wife Says She Is Happy")
    elif (wifehappy > 50 and wifedead == False and wifegone == False):
        print("Your Wife Says She Feels Fine")
    elif (wifehappy > 50 and wifedead == False and wifegone == False):
        print("Your Wife Says She Feels Upset")
    elif (wifehappy > 0 and wifedead == False and wifegone == False):
        print("Your Wife Says She Is Very Upset With You")
    if (abs(money) + money == 0 and money != 0):
        print("You're Currently In Debt")
        debttime += 1
    if (debttime > 2):
        print("You Have Been In Debt For Too Long. You Can Sense An Evil Presence Approching")
        collectiontime = True

# BUYING STUFF
    if (canbuy == True):
        print("You Have", hunger, "Hunger")
        if (wifedead == False and wifegone == False):
            print("Your Wife Has", wifehunger, "Hunger")
        if (gourmetfood > 0):
            print("You Have", gourmetfood, "Gourmet Food. Would You Like To Eat It (Type Eat), Or Save It (Type Save)")
            while (choiceloop == True):
                choice = input()
                if (choice == "Eat"):
                    print("Will You Eat (Type Eat), Will You Feed Your Wife (Type Wife), Or Will You Save (Type Save)")
                    while (choiceloop == True):
                        if (gourmetfood <= 0):
                            break
                        choice = input()
                        if (choice == "Eat"):
                            hunger += 30
                            happy += 30
                            gourmetfood -= 1
                        elif (choice == "Wife"):
                            wifehunger += 30
                            wifehappy += 30
                            gourmetfood -= 1
                        elif (choice == "Save"):
                            break
                        else:
                            print("Command Not Recognized")
                        print("You Have", gourmetfood, "Gourmet Food Left")
                    break
                elif(choice == "Save"):
                    break
                else:
                    print("Command Not Recognized")
        if (pills > 0):
            print("You Have", pills, "Anti Anti-Deppresants. Would You Like To Take Them (Type Take), Or Save Them (Type Save)")
            while (choiceloop == True):
                choice = input()
                if (choice == "Take"):
                    print("Will You Take Them (Type Take), Or Will You Save Them For Later (Type Save)")
                    while (choiceloop == True):
                        if (pills <= 0):
                            break
                        choice = input()
                        if (choice == "Take"):
                            happy -= 25
                            pills -= 1
                        elif (choice == "Save"):
                            break
                        else:
                            print("Command Not Recognized")
                        print("You Have", pills, "Anti Anti-Depressants Left")
                    break
                elif(choice == "Save"):
                    break
                else:
                    print("Command Not Recognized")
        if (potions > 0):
            print("You Have", potions, "Potions Left. Would You Like To Start Drinking Them (Type Drink), Or Save Them (Type Save)")
            while (choiceloop == True):
                choice = input()
                if (choice == "Drink"):
                    print("Will You Drink One (Type Drink), Or Will You Stop Drinking (Type Stop)")
                    while (choiceloop == True):
                        if (potions <= 0):
                            break
                        choice = input()
                        if (choice == "Drink"):
                            hp += 25
                            potions -= 1
                        elif (choice == "Stop"):
                            break
                        else:
                            print("Command Not Recognized")
                        print("You Have", potions, "Health Potions Left")
                    break
                elif(choice == "Save"):
                    break
                else:
                    print("Command Not Recognized")
        print("Will You Cook Regular Food (Type Cook), Or Will You Hold Off? (Type Hold)")
        while (choiceloop == True):
            choice = input()
            if (choice == "Cook" and chef == False):
                print("How Much Money Would You Like To Spend On Your Food? (100 Dollars Is 10 Points Of Hunger) If You Changed Your Mind, Type Exit")
                choice = input()
                
                if (choice == 'Exit'):
                    break
                elif (abs(int(choice)) + int(choice) == 0 and int(choice) != 0):
                    print("You Do Know That Doing That Would Kill You, Right? That's Not Infinite Money, That's Just Taking Away Your Hunger")
                elif (choice == 0):
                    print("") 
                elif (money >= int(choice)):
                    hunger += int(choice)/10
                    money -= int(choice)
                
                if (wifedead == False and wifegone == False):
                    print("How Much Money Would You Like To Spend On Your Wife's Food? (100 Dollars Is 10 Points Of Hunger) If You Changed Your Mind, Type Exit")
                    choice = input()
                    try:
                        if (choice == 'Exit'):
                            break
                        elif (int(choice) < 0):
                            print("You Do Know That Doing That Would Kill You, Right? That's Not Infinite Money, That's Just Taking Away Your Hunger")
                        elif (money >= int(choice)):
                            wifehunger += int(choice)/10
                            money -= int(choice)
                    except:
                        print("That Isn't An Option DimWit")
                break
            if (choice == "Cook" and chef == True):
                print("How Much Money Would You Like To Spend On Your Food? (100 Dollars Is 20 Points Of Hunger) If You Changed Your Mind, Type Exit")
                choice = input()
                if (choice == 'Exit'):
                    break
                elif (int(choice) < 0 and int(choice) != 0):
                    print("You Cannot Cook 0 Food Or Less.")
                elif (choice == 0):
                    print("") 
                elif (money >= int(choice)):
                    hunger += (int(choice)/10) * 2
                    money -= int(choice)
                    happy += int(choice) / 100
                
                if (wifedead == False and wifegone == False):
                    print("How Much Money Would You Like To Spend On Your Wife's Food? (100 Dollars Is 20 Points Of Hunger) If You Changed Your Mind, Type Exit")
                    choice = input()
                    try:
                        if (choice == 'Exit'):
                            break
                        elif (choice < 0):
                            print("You Cannot Cook 0 Food Or Less.")
                        elif (money >= int(choice)):
                            wifehunger += (int(choice)/10) * 2
                            money -= int(choice)
                            wifehappy += int(choice) / 100
                    except:
                        print("That Isn't An Option DimWit")
                break
            elif (choice == "Hold"):
                break
            else:
                print("Invalid Answer")
    elif (wifedead == False and wifegone == False):
        print("You Have Very Little Money. Your Wife Is Unhappy")
        print("You Have", hunger, "Hunger, And Your Wife Has", wifehunger, )
    else:
        print("You Have", hunger, "Hunger")
# MAJOR EVENTS + END OF DAY SHIT
        
# WIZARD
        
    if (wizard == True):
        print("")
        print("PRESS ENTER TO CONTINUE")
        print("")
        print("Your Wizard Powers Allow You To Few Deep Inside Of Yourself, And Alter What You Want")
        print("Your Hunger Is", hunger)
        print("Your Happiness", happy)
        print("Your Hp Is", hp)
        print("Your Strength Is", strength)
        print("Would You Like To Change An Aspect Of Yourself? (Type Yes) (Type No)")
        while (choiceloop == True):
            if (breakvar == True):
                breakvar == False
                break
            choice = input()
            if (choice == "Yes"):
                print("What Would You Like To Change? (Type Hunger) (Type Happiness) (Type Hp) (Type Strength)")
                while (choiceloop == True):
                    if (breakvar == True):
                        break
                    choice = input()
                    if (choice == "Hunger"):
                        print("You Currently Have", energy, "Energy. How Much Would You Like To Spend Altering Yourself? Negative Numbers Will Decrease The Stat. 1 Energy Is 5 Hunger")
                        while (choiceloop == True):
                            try:
                                choice = int(input())
                                if (abs(choice) > energy):
                                    print("You Dont Have Enough Energy For That")
                                else:
                                    energy -= abs(choice)
                                    hunger += choice * 5
                                    breakvar = True
                                    print("You Now Have", hunger, "Hunger, And", energy, "Energy")
                                    break
                            except:
                                print("Only Type Whole Numbers")
                    elif (choice == "Happiness"):
                        print("You Currently Have", energy, "Energy. How Much Would You Like To Spend Altering Yourself? Negative Numbers Will Decrease The Stat. 1 Energy Is 1 Happiness")
                        while (choiceloop == True):
                            try:
                                choice = int(input())
                                if (abs(choice) > energy):
                                    print("You Dont Have Enough Energy For That")
                                else:
                                    energy -= abs(choice)
                                    happy += choice
                                    breakvar = True
                                    print("You Now Have", happy, "Happiness, And", energy, "Energy")
                                    break
                            except:
                                print("Only Type Whole Numbers")
                    elif (choice == "Hp"):
                        print("You Currently Have", energy, "Energy. How Much Would You Like To Spend Altering Yourself? Negative Numbers Will Decrease The Stat. 1 Energy Is 2 Hp")
                        while (choiceloop == True):
                            try:
                                choice = int(input())
                                if (abs(choice) > energy):
                                    print("You Dont Have Enough Energy For That")
                                else:
                                    energy -= abs(choice)
                                    hp += choice * 2
                                    breakvar = True
                                    print("You Now Have", hp, "Hp, And", energy, "Energy")
                                    break
                            except:
                                print("Only Type Whole Numbers")
                    elif (choice == "Strength"):
                        print("You Currently Have", energy, "Energy. How Much Would You Like To Spend Altering Yourself? Negative Numbers Will Decrease The Stat. 1 Energy Is 1 Strength")
                        while (choiceloop == True):
                            try:
                                choice = int(input())
                                if (abs(choice) > energy):
                                    print("You Dont Have Enough Energy For That")
                                else:
                                    energy -= abs(choice)
                                    strength += choice
                                    breakvar = True
                                    print("You Now Have", strength, "Strength, And", energy, "Energy")
                                    break
                            except:
                                print("Only Type Whole Numbers")
                    else:
                        print("Choice Not Recognized")
            elif (choice == "No"):
                break
            else:
                print("Choice Not Recognized")

# IDEK BUT ITS STUFF

    robchance = random.randint(1,5)
    if (undertheradar == 3 and wanted > 0):
        print("")
        input("SPECIAL EVENT")
        print("")
        wanted -= 1
        print("You've Kept Out Of Trouble For A Little While. Your Wanted Level Has Decreased To", wanted)
    elif (undertheradar == 5 and wanted > 0):
        print("")
        input("SPECIAL EVENT")
        print("")
        wanted = 0
        print("You've Layed Low For Long Enough. You Are No Longer Wanted")

# PROGRAMMING STUFF

    if (development == True):
        virusprogress += 1
    if (makingbackdoor == True):
        backdoorprogress += 1
    if (virusprogress >= 10):
        print("s1ph0n.exe Is Fully Developed.")
        siphon = True
    if (backdoorprogress >= 10):
        print("b@ckd00r.js Is Fully Developed.")
        backdoor= True

# SIPHON.EXE STUFF

    if (hacker == True and robchance == 1 and virusprogress == 0 and development == False):
        print("")
        input("SPECIAL EVENT")
        print("")
        print("Right Before You Were Going To Go To Sleep, You Had An Idea For A Program That Could Siphon Money From The Casino.")
        print("Development Will Take 10 Days. During This Time, You Can Spend 2000 Dollars To Outsource Coding, Advancing Progress By 2 Days. However, This Will Raise You Wanted Level")
        development = True
        virusprogress = 0
    if (development == True and virusprogress < 10):
        print("")
        print("Your Current Progress On The Virus Is", virusprogress, ". Will You Outsource Development? It Costs 2000 Dollars, And Adds One To Your Wanted Level (Type Yes) (Type No)")
        choiceloop = True
        while (choiceloop == True):
            choice = input()
            if (choice == "Yes" and money > 1999):
                wanted += 1
                money -= 2000
                undertheradar = 0
                virusprogress += 2
                break
            elif (choice == "Yes"):
                print("You Dont Have Enough Money For That")
                break
            elif (choice == "No"):
                break
            else:
                print("Command Not Recognized")
    if (siphon== True):
        print("Will You Choose To Use s1ph0n.exe Today? (Type Yes) (Type No)")
        choiceloop = True
        while (choiceloop == True):
            if (breakvar == True):
                breakvar = False
                break
            choice = input()
            if (choice == "Yes"):
                print("How Much Would You Like To Siphon? Each 1000 Dollars Is One Wanted Level")
                while (choiceloop == True):
                    try:
                        choice = input()
                        money += int(choice)
                        wanted += int(choice)/1000
                        undertheradar = 0
                        breakvar = True
                        break
                    except:
                        print("Only Type Whole Numbers")
            elif (choice == "No"):
                break
            else:
                print("Choice Not Recognized")
# BACKDOOR.JS STUFF

    if (hacker == True and robchance == 1 and backdoorprogress == 0 and day >= 5 and makingbackdoor == False):
        print("")
        input("SPECIAL EVENT")
        print("")
        print("Right Before You Were Going To Go To Sleep, You Had An Idea For A Backdoor That Could Reset Your Wanted Level")
        print("Development Will Take 10 Days. During This Time, You Can Spend 2000 Dollars To Outsource Coding, Advancing Progress By 2 Days. However, This Will Raise You Wanted Level")
        makingbackdoor = True
        backdoorprogress = 0
    if (bank > 0):
        robchance = random.randint(1,20)
        if (robchance == 1 and robber == False):
            print("")
            input("SPECIAL EVENT")
            print("")
            print("Robbers Ransacked The Bank. You Lost All The Money You Had Stored There")
            bank = 0
    if (makingbackdoor == True and backdoorprogress < 10):
        print("")
        print("Your Current Progress On The Backdoor Is", backdoorprogress, ". Will You Outsource Development? It Costs 2000 Dollars, And Adds One To Your Wanted Level (Type Yes) (Type No)")
        choiceloop = True
        while (choiceloop == True):
            choice = input()
            if (choice == "Yes" and money > 1999):
                wanted += 1
                money -= 2000
                undertheradar = 0
                backdoorprogress += 2
                break
            elif (choice == "Yes"):
                print("You Dont Have Enough Money For That")
                break
            elif (choice == "No"):
                break
            else:
                print("Command Not Recognized")
    if (backdoor == True):
        print("Will You Choose To Use b@ckd00r.js Today? You Have A Chance To Lower Your Wanted Level By 25, Or Raise It By 10 (Type Yes) (Type No)")
        choiceloop = True
        while (choiceloop == True):
            if (breakvar == True):
                breakvar = False
                break
            choice = input()
            if (choice == "Yes"):
                robchance = random.randint(1,4)
                if (robchance > 1):
                    wanted -= 25
                    if (wanted < 0):
                        wanted = 0
                    print("You Succesfully Set Your Wanted Level Down To", wanted)
                    break
                else:
                    wanted += 10
                    undertheradar = 0
                    print("Your Script Was Detected. Your Wanted Level Is Now", wanted)
                    break
            elif (choice == "No"):
                break
            else:
                print("Choice Not Recognized")
    if (money > 85000000000000 and realism == False):
        print("")
        input("MAJOR EVENT")
        print("You've Ammassed More Money Than Exists In The World. This Causes Society To Collapse. Next Time, Dont Go Ham")
        print("")
        massiveloop = False
        break
    if (realism == True):
        hunger = 120
        wifehunger = 110
        happy = 100
        wifehappy = 100
        hp = 100
    if (hunger > 1000 and chef == False and realism == False):
        print("")
        input("MAJOR EVENT")
        print("")
        print("You Ate 10 Times Your Body Weight. This Led To You Being So Obese That You Created Your Own Gravitational Field. You Starting Collapsing In On Yourself, And Compressing To A Shape With Un-Imaginable Density. You Then Imploded, Creating A Black Hole, Killing Everyone On Earth. Game Over Dude. You Died")
        print("")
        massiveloop = False
        bigloop = False
        break
    if (hunger <= 0):
        print("")
        input("MAJOR EVENT")
        print("")
        print("You Died From Starvation. Massive L. Game Over")
        print("")
        massiveloop = False
        bigloop = False
        break
    if (happy > 250):
        print("")
        input("MAJOR EVENT")
        print("")
        print("You Became Too Happy, And Had An Aneurysm. Try Working At Your Job, Or Losing Games Of Blackjack On Purpose")
        print("")
        massiveloop = False
        bigloop = False
        break
    if (sadcount == 3):
        print("")
        input("MAJOR EVENT")
        print("")
        print("In A Depressed State, You Decided To Move To Alaska, And Become A Wandering Fisherman. You Leave Everything You've Known Behind. Game Over")
        print("")
        massiveloop = False
        bigloop = False
        break
    robchance = random.randint(1,50)
    if (robber == True and robchance == 1):
        print("")
        input("MAJOR EVENT")
        print("")
        print("You Get Swatted During The Night, And Are Arrested. Next Time, Don't Steal Stuff Or Be A Robber. Game Over")
        print("")
        massiveloop = False
        bigloop = False
        break
    if (wifedead == False and wifegone == False):
        if (wifehunger <= 0):
            print("")
            input("MAJOR EVENT")
            print("")
            print("Your Wife Died From Starvation. The Game Tells You Stats Everyday. How Could You Possibly Let Her Starve?")
            print("")
            wifedead = True
    if (wifedead == False and wifegone == False):
        if (wifehunger > 500):
            print("")
            input("MAJOR EVENT")
            print("")
            print("You Overfed Your Wife, And She Died.")
            print("")
            wifedead = True
    if (wifedead == False and wifegone == False):
        if (wifehappy > 300):
            print("")
            input("MAJOR EVENT")
            print("")
            print("Your Wife Is Far Too Happy. She Got Hit By A Car While Crossing The Street. It Was Unrelated To Her Happiness.")
            print("")
            wifedead = True
    if (wifegone == False and wifedead == False):
        if (wifehappy <= 0):
            print("")
            input("MAJOR EVENT")
            print("")
            print("Your Wife Is Unhappy With You. She Decides You Divorce You")
            print("")
            wifegone = True
            happy -= 50
    if (collectiontime == True):
        print("")
        input("MAJOR EVENT")
        print("")
        print("You Hear A Knock On Your Door. Do You Open It, (Type Open) Or Wait (Type Wait)")
        dloop = True
        while (dloop == True):
            dchoice = input()
            if (dchoice == "Open"):
                print("You Open The Door, And Come Face To Face With A Demented 7 Foot Tall Figure. The Debt Collector Is Here, And He Wants The Money You Owe The Casino")
                input("PRESS ENTER TO CONTINUE")
                debthp = abs(money)/10
                debtdmg = abs(money)/100
                print("You Currently Owe", abs(money),"Dollars. This Means The Debt Collector Has", debthp, "Health, And Has", debtdmg, "Base Damage. Better Hope You Can Beat Him")
                print("")
                fightscene()
                break
            elif (dchoice == "Wait"):
                print("You Walk Up To The Door But Hesitate. You Decide To Wait And See If The Person Will Leave")
                print("")
                input("PRESS ENTER TO CONTINUE")
                print("The Door Bursts Open, And Wooden Shards Fly Everywhere. An Evil Creature Known Only As The Debt Collector Walks Through, And He Wants The Money You Owe")
                input("PRESS ENTER TO CONTINUE")
                debthp = abs(money)/10
                debtdmg = abs(money)/100
                print("You Currently Owe", abs(money),"Dollars. This Means The Debt Collector Has", debthp, "Health, And Has", debtdmg, " Base Damage. Better Hope You Can Beat Him")
                print("")
                fightscene()
                break
            else:
                print("Invalid Command")
    if (savecooldown == 0):
        print("Would You Like To Save? (Type Yes) (Type No)")
        while (loop == True):
            choice = input()
            if (choice == "Yes"):
                # NUMBER ADDITIONS TO THE LIST FOR READABILITY. ADD TO THE LIST WHATEVER YOU WANT TO SAVE, THEN GO TO LINE 366 AND DOCUMENT WHAT YOU ADDED
                list.append(money) # 0
                list.append(happy) # 1
                list.append(strength) # 2
                list.append(hp) # 3
                list.append(hunger) # 4
                list.append(day) # 5
                list.append(wifedead) # 6
                list.append(wifehunger) # 7
                list.append(wifehappy) # 8
                list.append(wifegone) # 9
                list.append(debttime) # 10
                list.append(wanted) # 11
                list.append(gambler) # 12
                list.append(rich) # 13
                list.append(robber) # 14
                list.append(chef) # 15
                list.append(wizard) # 16
                list.append(bankhack) # 17
                list.append(siphon) # 18
                list.append(virusprogress) # 19
                list.append(backdoor) # 20
                list.append(backdoorprogress) # 21
                list.append(bank) # 22
                list.append(undertheradar) # 23
                list.append(necklaceowned) # 24
                list.append(potions) # 25
                list.append(gourmetfood) # 26
                list.append(bookowned) # 27
                list.append(stungun) # 28
                list.append(Membership) # 29
                list.append(realism) # 30
                list.append(skimask) # 31
                list.append(energy) # 32
                list.append(pills) # 33
                list.append(slot) # 34
                list.append(development) # 35
                list.append(makingbackdoor) # 36
                # ADD HERE
                print("Your Save Is Down Below. Copy It, And Store It Somewhere. It Is Currently Compatible With Version 15.3 And Lower")
                list.append('')
                print(*list, sep='|')
                savecooldown = 7
                break
            elif (choice == "No"):
                break
            else:
                print("Choice Not Recognized")
    else:
        print("You Currently Have To Wait", savecooldown, "Day(s) Till You Can Save Again")
        savecooldown -= 1
if (corrupted == False):
    print("You Made It", day, "Days Before Losing. Well Done")
