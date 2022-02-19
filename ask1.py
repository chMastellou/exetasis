from random import*
count=0
for k in range(1,101):
    bimata=0
    triliza=False
    tetragwno=[[0,0,0],
               [0,0,0],
               [0,0,0]]
    Arings=[9,9,9]
    x=0
    y=0
    j=1

    while (triliza==False):

        x=randint(0,2)
        y=randint(0,2)
        j=randint(1,3)
        #έλεγχος της περίπτωσης που τελειώσουν οι δακτύλιοι ενός είδους πριν γίνει τρίλιζα
        if(Arings[j-1]==0):
            continue

        #ελεγχος και αποθήκευση δακτύλιου

        #αν υπάρχει δακτύλιος ίδιου μεγέθους στην θέση τότε δεν προσμετράται ως έγκυρη προσπάθεια
        if(tetragwno[x][y]==j):
            continue
        #όταν ο δακτύλιος που υπάρχει ήδη είναι μεγαλύτερος ο καινούριος θα μπεί μεσα του και δεν θα αλλάξει τίποτα
        #αφού θα υπερισχύσει το μέγεθος του προηγούμενου
        elif(tetragwno[x][y]>j):
            Arings[j-1]-=1 #αφαίρεση δακτύλιων
            bimata+=1 #τα βήματα μέχρι την ολοκλήρωση του παιχνιδιού
            #print('{3}ος Γύρος: μέγεθος: {0} (x,y)->({1},{2})'.format(j,x,y,bimata))
            continue
        else:
            bimata+=1 #τα βήματα μέχρι την ολοκλήρωση του παιχνιδιού
            Arings[j-1]-=1
            tetragwno[x][y]=j

        #print('{3}ος Γύρος: μέγεθος: {0} (x,y)->({1},{2})'.format(j,x,y,bimata))
        #έλεγχος για τρίλιζα

        #αν οι δακτύλιοι είναι λιγότεροι από 3 μέσα στο τετράγωνο δεν εχει νόημα η αναζήτηση τρίλιζας
        c=0
        for i in range(0,3):
            c+=tetragwno[i].count(0)
        #print(c)
        if(c>6):
            continue
        #εύρεση όλων των δυνατών τριάδων στην λίστα triades
        triades=[0,0,0,0,0,0,0,0]
        #Διαγώνια
        triades[0]=str(tetragwno[2][0])+str(tetragwno[1][1])+str(tetragwno[0][2])
        triades[1]=str(tetragwno[0][0])+str(tetragwno[1][1])+str(tetragwno[2][2])
        #Οριζόντια
        triades[2]=str(tetragwno[0][0])+str(tetragwno[0][1])+str(tetragwno[0][2])
        triades[3]=str(tetragwno[1][0])+str(tetragwno[1][1])+str(tetragwno[1][2])
        triades[4]=str(tetragwno[2][0])+str(tetragwno[2][1])+str(tetragwno[2][2])
        #Κάθετα
        triades[5]=str(tetragwno[0][0])+str(tetragwno[1][0])+str(tetragwno[2][0])
        triades[6]=str(tetragwno[0][1])+str(tetragwno[1][1])+str(tetragwno[1][2])
        triades[7]=str(tetragwno[0][2])+str(tetragwno[1][2])+str(tetragwno[2][2])
        #μέγεθος δίσκων
        h=['111','222','333','123']
        #τελικός έλεγχος για ύπαρξη τρίλιζας και τερματισμού του πρώτου γύρου
        #print(triades)
        for i in h:
            if(i in triades):
                triliza=True
    count+=bimata
    print("."*61)
    print(" "*10+"Το {1}ο παιχνίδι τελείωσε με {0} βήματα".format(bimata, k))

mesosOros=count/100
mesosOrosak=count//100
print("*"*61)
print("")
print(" "*7+"Το παιχνίδι συνήθως τελειώνει σε {0} βήματα".format(mesosOrosak))
print("")
print(" "*14+"(Ακριβής μέσος όρος: {0})".format(mesosOros))
print("\n")
