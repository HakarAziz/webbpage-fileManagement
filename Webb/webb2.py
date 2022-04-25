from datetime import datetime

#skapar en list som vi ska ha våra object i
readLINES = [] 
webb = "alm2.log.txt"
#jämförelse räknare
cp = 0

#hur många rader vi läst in
numRows = 0

#max antal rader som läses in -1  stoppa aldrig
max = -1

#max rader som visas i html fil
displayTableRowsMax = 20

#håller koll på varje ip adress i en klass
class visits:
    def __init__(self, ip, date):  
        self.ip = ip  
        self.numVisits = 1
        self.firstVisitDate = date
        self.lastVisitDate = date

    #jämför datum sätter första och sista besök 
    def dateCHECK(self, compareDATE):
        self.numVisits+=1
        #print("Compare",compareDATE,"----",self.firstVisitDate)
        if (self.firstVisitDate > compareDATE):
            self.firstVisitDate = compareDATE
        if (self.lastVisitDate < compareDATE):
            self.lastVisitDate = compareDATE
        


        
   

#öppnar och läser filen
with open (webb, 'r') as myfile:    # Open lorem.txt for reading text.
    for i in myfile:                   # For each line in the file,
       
        #addar till rade
        numRows+=1
        #splittar stringen på raden efter första ip 
        ipAdress = ""
        date = ""
        num = 0
        value = i.split(" ")
        for ab in value:
            #värde 0 ip
            if (num==0):
                ipAdress = ab

            #värde 3 date
            if (num==3):
                #formaterar datum
                date = ab
                date = datetime.strptime(date, '[%d/%b/%Y:%H:%M:%S') #Om [ försvinner från date när vi tar den, måste vi ta bort det andra också.
                date.isoformat()
                
                valuefoundinLIST = False
                cp = 0
                #söker efter värdet i listan och finns det så jämför vi datum osv
                while cp < len(readLINES): #Loopar igenom längden av listan
                    if (readLINES[cp].ip) == (ipAdress):        
                        valuefoundinLIST = True
                        readLINES[cp].dateCHECK(date)
                        break
            
                    cp += 1

                #finns inte värdet i listan så lägger vi till det
                if valuefoundinLIST == False:                    #
                    readLINES.append(visits(ipAdress,date))
                    
                #print(ipAdress, date)
                breakThis = True
                break

        


            num+=1
        #om vi vill ha ett max värde som laddas till informationen
        if (numRows==max):
            break            


    
#sorterar
readLINES.sort(key=lambda x: x.numVisits, reverse=True)            

#räkning
percentVisitAccess = 0.0
percentVisitIPS = 0.0
lengt = len(readLINES)
countRow = 0
#öppnar och skriver till fil 
f= open("formattedIP.html","w+")
f.write("<table style='width: 100%;'><td>IP</td><td>Först besök</td><td>Sista besök</td><td>Antal Besök"+str(numRows)+"</td><td>% Access "+str(numRows)+"</td><td>% IPS "+str(lengt)+"</td><tr></tr>")
for val in readLINES:
    #formatterar till 0.0000 4a decimaler
    percentVisitAccess = round(float(val.numVisits/numRows),4)
    percentVisitIPS = round(float(val.numVisits/len(readLINES)),4)
    value = ""
    f.write("<td>")
    value = val.ip
    f.write(value)
    f.write("</td><td>")

    #formatterar datetime till iso
    value = val.firstVisitDate.strftime('%d/%m/%Y:%H:%M:%S')
    f.write(value)
    f.write("</td><td>")

    #formatterar datetime till iso
    value = val.lastVisitDate.strftime('%d/%m/%Y:%H:%M:%S')
    f.write(value)
    f.write("</td><td>")

    value = str(val.numVisits)
    f.write(value)
    f.write("</td><td>")

    value = str(percentVisitAccess)
    f.write(value+"% ")
    f.write("</td><td>")

    value = str(percentVisitIPS)
    f.write(value+"% ")
    f.write("</td><tr></tr>")

    #om vi bara vill visa ett visst antal rader
    countRow+=1
    if (countRow==displayTableRowsMax):
        break
f.write("<table>")
f.close()
#skriver ut att vi är klara
print("Done")