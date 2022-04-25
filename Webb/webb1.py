from datetime import datetime

rows = 0
listRow = 0
webb = "alm2.log.txt"
lst = []
max = -1


class entries:
    def __init__(self, ipTotal, date):
        self.ipTotal = ipTotal
        self.lastDate = date  # Skapar en lista för första datumet och sista datumet
        self.firstDate = date

    def datum(self, dates):
        if self.firstDate > dates:
            self.firstDate = dates
        if self.lastDate < dates:
            self.lastDate = dates


with open(webb, 'r') as file:
    for line in file:  # Går igenom varje linje i loggen
	lst = line
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
                date = datetime.strptime(date, '[%d/%b/%Y:%H:%M:%S')
                date.isoformat()

                value: bool = False
                listRow = 0
                while listRow < len(lst):
                    if lst[listRow].ipTotal == ip:
                        value = True
                        lst[listRow].datum(date)
                        break
                    listRow += 1
                if not value:
                    lst.append(entries(ip, date))
            print(date)
            print(ip)
            break
        num += 1
        # om vi vill ha ett max värde som laddas till informationen
        if rows == max:
            break
