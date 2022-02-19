import ast

a=70#αριθμός space

print("\n"+"*"*5+"Αρχή Προγράμματος".upper()+"*"*48+"\n\n")
#έλεγχος εισόδου για το αρχείου
#δεν ελέγχω αν το περιεχόμενο είναι στη σωστή μορφή όμως
k=True
while(k==True):
    file=str(input("Δώστε αρχείο κειμένου (.txt) με 1 λεξικό σε κάθε γραμμή του:\n"+"_"*a+"\n"))

    if(file[-3:]!="txt"):
        print("\n!!!Το '{0}' ΔΕΝ είναι όνομα αρχείου κειμένου (.txt)!!!\n".format(file))
    else:
        # reading the data from the file
        try:
            with open(file) as f:    #δεν χρησιμοποιώ το readlines() ώστε να μην χρειαστεί
                data = f.read()      #να αφαιρέσω τους χαρακτήρες αλλαγής γραμμής \n
        except FileNotFoundError:
            print("\n!!!Το αρχείο πρέπει να υπάρχει μέσα στον ίδιο φάκελο με το πρόγραμμα!!!\n")
        else:
            k=False
#διαχωρίζω την κάθε γραμμή (λεξικό) αποθηκεύοντας τες ως στοιχεία λίστας για επεξεργασία
data=data.splitlines()

#μετατρέπω τα στοιχεία της λίστας από string σε dictionary
for i in range(0,len(data)-1):
    data[i]= ast.literal_eval(data[i])
#**********************************************************************************
print("_"*a+"\n"+" "*5+"Τα διαθέσιμα κλειδιά:")
print("_"*a)
count=0
#για να τυπώσω τα κλειδιά αφού δεν έχω σταθερό αρχείο .txt
for i in data[0]:
    count+=1
    print(" "*5,count,". "+i)
print("_"*a+"\n")
#Κάνω έλεγχο εισόδου για το κλειδί ώστε να μην μου χαλάσει η εκτέλεση του προγράμματος αν γίνει εισαγωγή
#λάθος τιμής
cont=True
while(cont==True):
    k=input(" "+"Εισάγετε τον αριθμό του κλειδιού που επιθυμείτε: \n"+"_"*a+"\n")
    try:
        k=int(k)
    except ValueError:
        print(" "*5+"Η απάντησή σας πρέπει να είναι αριθμός!\n")
    else:
        if k not in range(1,count+1):
            print("_"*a+"\n")
            print(" "*5+"Η απάντησή σας δεν είναι έγκυρη.\n")
        else:
            cont=False

cnt=0
for i in data[0]:             #αναθέτω στο k το όνομα του κλειδιού
    cnt+=1                    #στο οποίο αντιστοιχεί ο αριθμός
    if(k==cnt):
        k=i
        break
print("_"*a)
print(" "*5+"Επιλέξατε το κλειδί: {0}.\n".format(k))
print("*"*5+"Αποτέλεσμα".upper()+"*"*56)


#Αποθήκευση τιμών σε λίστα για υπολογισμό μικρότερου/μεγαλύτερου και της τιμής που
#εμφανίζεται πιο συχνά για το δοσμένο κλειδί
l=[]
for i in range(0,len(data)-1):
  l.append(data[i][k])
l.sort()
count=1
popular=[0]
#υπολογισμός της ποιο δημοφιλούς τιμής
for i in range(0,len(l)):
    if(i==0):
        #αν το πρώτο στοιχείο δεν ξαναεμφανίζεται δεν έχει νόημα να το εξετάσω
        continue
    elif((l[i]==l[i-1])and((i-1)!=0)):
        #αν είναι ίδιο με το προηγούμενο του και δεν είναι το δεύτερο στοιχείο το έχω εξετάσει ήδη
        continue
    elif(l.count(l[i])>count):
        #αν εμφανίζεται περισσότερες φορές απο οποιοδήποτε άλλο στοιχείο μέχρι στιγμής
        #ανανεώνω το count
        count=l.count(l[i])
        popular[0]=l[i]
    elif((l.count(l[i])==count)and(l.count(l[i])>1)):
        #αν εμφανίζεται ίσες φορές το κρατάω προσορινά
        popular.append(l[i])
    else:
        continue
#εξαλείφω τις τιμές που είχαν μπεί ενώ το count ήταν μικρότερο του τελικού
for i in popular:
    if(l.count(i)<count):
         popular.remove(i)
#εκτύπωση αποτελεσμάτων
print("\n \n")
if(count==1):
    print(" Δεν υπάρχουν δημοφιλείς τιμές")
else:
    if(len(popular)==1):
        print(" H ποιο δημοφιλής τιμή είναι: {0}".format(popular))
        print(" Και εμφανίζεται: {0} φορές".format(count))
    else:
        print(" Οι ποιο δημοφιλείς τιμές είναι: {0}".format(popular))
        print(" Και εμφανίζονται: {0} φορές".format(count))
max=max(l)
min=min(l)
print("\n H μεγαλύτερη τιμή είναι: {0}".format(max))
print("\n H μικρότερη τιμή είναι: {0}".format(min))
print("\n \n")
print("*"*5+"Τέλος Προγράμματος".upper()+"*"*49+"\n")
