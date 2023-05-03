from time import sleep 

def start():
    print("Willkommen bei der BerlinBank\nBitte führen Sie Ihre Karte ein und bestätigen Sie mit 'ja'")

    while True:
        answer = input(">").lower()

        if "j" in answer:
            auswahl()

        else:
            abbruch()
            
            
def auswahl():
    while True:
        
        print("Bitte wählen Sie zwischen folgenden Optionen:")
        print("1 - Auszahlung")
        print("2 - Einzahlung")
    
        auswahl = input(">")
        
    
        if auswahl == "1":
            print("Weiter zur Auszahlung")
            auszahlung()
    
        elif auswahl == "2":
            print("Weiter zur Einzahlung")
            einzahlung()
        
        else:
            print("Bitte korrigieren Sie Ihre Eingabe.")
 
    
            
def auszahlung():
    while True:
    
        print("Bitte geben Sie Ihre PIN ein.")
    
        pin = input(">")

        if pin == "1111":
            print("Vielen Dank, diese PIN ist korrekt.")
            auszahlung2()

        else:
            abbruch()
            
            
def auszahlung2():
    print("Wieviel möchten Sie abheben?")
    print("50 Euro")
    print("100 Euro")
    print("200 Euro")
    print("500 Euro")
    #print("anderer Betrag")
    
    betrag = input(">")

    if betrag == "50":
        print("Vielen Dank, der gewünschte Betrag von %.2F wird ausgegeben." % 50)
        sleep (3)
        auswahl()
        
    if betrag == "100":
        print("Vielen Dank, der gewünschte Betrag von %.2F wird ausgegeben." % 100)
        sleep (2)
        print("Bitte entnehmen Sie Ihre Geld.")
        sleep (2)
        print("Bitte entnehmen Sie Ihre Karte.")
        sleep (2)
        start()
        
    if betrag == "200":
        print("Vielen Dank, der gewünschte Betrag von %.2F wird ausgegeben." % 200)
        sleep (2)
        print("Bitte entnehmen Sie Ihre Geld.")
        sleep (2)
        print("Bitte entnehmen Sie Ihre Karte.")
        sleep (2)
        start()
        
    if betrag == "500":
        print("Vielen Dank, der gewünschte Betrag von %.2F wird ausgegeben." % 500)
        sleep (2)
        print("Bitte entnehmen Sie Ihre Geld.")
        sleep (2)
        print("Bitte entnehmen Sie Ihre Karte.")
        sleep (2)
        start()
           

    else:
        abbruch()

def einzahlung():
    print("Bitte legen Sie die gewünschte Summe in das dafür vorgesehene Fach ein und bestätigen Sie mit 'ja'")
    
    answer = input(">").lower()

    if "j" in answer:
        print("Vielen Dank, wir haben Ihre Einzahlung erhalten.")
        sleep (2)
        print("Bitte entnehmen Sie Ihre Karte.")
        sleep (2)
        start()

    else:
        abbruch()
    
    
def abbruch():
    exit()






        
        
start()