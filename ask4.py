from random import*
import random

xartia = []
figures = ["J", "Q", "K"]
#Η δημιουργία της τράπουλας γίνεται μέσα στο λοοπ του κάθε παιχνιδιού
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]
niceCards=[]
# 2 100άρες
for i in range(1,3):
    count=[]
    c1,c2,c3=0,0,0
    #print("{0}ος γύρος".format(i)+"@"*100)

    #1η εκατοστάρα
    for l in range(1,101):
        #print("\n Αρχή του {0}ου παιχνιδιού.".format(l))
        #print("_"*70)
        #Δημιουργία της τράπουλας
        for p in xarti:
            for j in color:
                if ([p,j] not in xartia):
                    xartia.append([p,j])
        f=[]
        f=figures+[10]
        for p in f:
            for j in color:
                if ([p,j] not in niceCards):
                    niceCards.append([p,j])

#Ανακάτωμα τράπουλας
        random.shuffle(xartia)
#τράπουλα έτοιμη

#Αρχικοποίηση των χαρτιών και των πόντων 1ου παίχτη
        player1=[]
        sum1=0
#Πρώτος παίχτης παίζει και αν συγκεντρώσει πάνω από 21 πόντους
#το παιχνίδι τελειώνει και νικάει ο 2ος παίχτης
        #print("1ος παίχτης μπαίνει print ("player1: ",player1)στο παιχνίδι.")
        #print("_"*50)
        s=0
        while sum1<16:
            random.shuffle(niceCards)
            s+=1             #τραβάει χαρτιά μέχρι οι συνολικοί πόντοι του να είναι >=16
            sum1=0
            if((i==2)and(s==1)):  #Δεύτερο παιχνίδι
                 player1.append(niceCards.pop())
                 xartia.remove(player1[0])
            else:
                 player1.append(xartia.pop())
            #print ("player1: ",player1)
            #print(len(xartia))

            for card in player1:
                if card[0] in figures:
                    sum1=sum1+10
                else:
                    sum1=sum1+card[0]

#έλεγχος συνολικών πόντων 1ου παίχτη
        if sum1>21:
            #print("Ο 1ος παίχτης ξεπέρασε το όριο των 21 πόντων.\n Τέλος παιχνιδιού.\n Νικητής ο δεύτερος παίχτης!")
            c2+=1
        else:
            '''
            ?
            sxolia pollwn
            grammwn
            '''
#ο 2ος παίχτης αρχίζει να παίζει
            #print("2ος παίχτης μπαίνει στο παιχνίδι.") #let me add one more player
            #print("_"*50)
#Αρχικοποίηση μεταβλητών 2ου παίχτη
            player2=[]
            sum2=0
            s2=0
            special=[]
            for d in xartia:
                for g in range(1,10):
                    if(d[0]==g):
                         special+=[d]
            #print(special)
            while sum2<16:
                s2+=1
                sum2=0
                #print(xartia[-1] in niceCards)
                if((i==2)and(s2==1)):
                    player2.append(special.pop())
                    #print("player2:",player2)
                    xartia.remove(player2[-1])
                    continue

                player2.append(xartia.pop())
                # print (player2)
                #print ("player2: ",player2)
                for card in player2:
                    if card[0] in figures:
                        sum2=sum2+10
                    else:
                        sum2=sum2+card[0]
                #print("Ο 2ος παίχτης έχει τώρα: {0} πόντους".format(sum2))

            if(sum2>21):
                c1+=1
            if(21>=sum1>sum2):
                c1+=1
            elif(21>=sum2>sum1):
                c2+=1
            elif(sum1==sum2):
                c3+=1

    print("_"*60)
    if(i==1):
        print("Κανονικό παιχνίδι.\n")
    elif(i==2):
        print("Πειραγμένο μοίρασμα.\n")
    print("Ο 1ος παίχτης νίκησε: {0} φορές.".format(c1))
    print("Ο 2ος παίχτης νίκησε: {0} φορές.".format(c2))
    print("Ισοπαλία: {0} φορές.".format(c3))
    
