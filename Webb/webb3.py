from datetime import datetime

rows = 0
listRow = 0
webb = "alm.log"
lst = []


class entries:

    def __init__(self, ipTotal, dateTime):
        self.ipTotal = ipTotal
        self.entry = 1              # För att kunna ha koll på antal besökare
        self.firstDate = dateTime  # Skapar en lista för första datumet och sista datumet
        self.lastDate = dateTime

    def datum(self, dates):
        self.entry += 1
        if self.firstDate > dates:
            self.firstDate = dates
        if self.lastDate < dates:
            self.lastDate = dates


with open(webb, 'r') as file:
    for line in file:  # Går igenom varje linje i loggen
        rows += 1
        num = 0
        ip = ""
        date = ""
        ipDate = line.split(" ")  # Splittar efter ip addressen
        for space in ipDate:
            if num == 0:
                ip = space

            if num == 3:
                date = space
                date = datetime.strptime(date, '[%d/%b/%Y:%H:%M:%S') #Genom datetime kan vi ta ut datumet från filen
                date.isoformat()

                value: bool = False
                listRow = 0
                while listRow < len(lst):
                    if lst[listRow].ipTotal == ip:  #Kollar om värdena existerar i listan
                        value = True
                        lst[listRow].datum(date)
                        break

                    listRow += 1

                if not value:                       #Om värdena inte finns i listan så läggs de till
                    lst.append(entries(ip, date))   #Callar entries Class och skapar flera olika listor
                #print(ip, date)

                break
            num += 1
            #print(rows)

lst.sort(key=lambda x: x.entry, reverse=True)  # Sorterar listan så att störst ligger högst upp

percentIP = 0
length = len(lst)
maxLines = 20
minLines = 0
#Genom html kan vi skapa en tabell : IpAdress   First Visit    Last Visit    Antal Besök     Ip %
html = ("<table style='width: 100%;'><td>IpAdress</td><td>First Visit</td><td>Last Visit</td><td>Besök"+str(rows)+"</td><td>% Ip "+str(length)+"</td><tr></tr>")

f = open("IpDatefile.html", "w+")  # Skapar en fil för att både läsa och lägga till värden
f.write(html)
for string in lst:
    rows+=1
    ipDate = ""
    f.write("<td>")
    ipDate = string.ipTotal
    f.write(ipDate)
    f.write("</td><td>")

  
    ipDate = string.firstDate.strftime('%d/%m/%Y:%H:%M:%S')
    f.write(ipDate)
    f.write("</td><td>")

    ipDate = string.lastDate.strftime('%d/%m/%Y:%H:%M:%S')
    f.write(ipDate)
    f.write("</td><td>")

    
    ipDate = str(string.entry)
    f.write(ipDate)
    f.write("</td><td>")

    percentIP = round(float(string.entry/rows), 4) #4 decimaler annars ser man inte % värdet
    ipDate = str(percentIP)
    f.write(ipDate+" %")
    f.write("</td><tr></tr>")

    
    if minLines==maxLines:
        break

f.write("<table>")
f.close()