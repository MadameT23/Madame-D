
print('*************************************')
print('                                     ')
print('           Haushaltsbuch             ')
print('                                     ')
print('*************************************')
print()

obst = []
snacks = []
getraenke = []

while True:
    print('Auswahl-Menü')
    print('1 - Obst-Einkäufe eintragen')
    print('2 - Snack-Einkäufe eintragen')
    print('3 - Getränke-Einkäufe eintragen')
    print('4 - Ausgaben des gesamten Monats ausgeben')
    print('X - Programm abbrechen')
   
    

    eingabe = input('Triff deine Auswahl: ')
   
    if eingabe == 'X':
        print('Bis zum nächsten Mal!')
        break
        
    elif eingabe == '1':
        
        '''Variable für das Wocheneinkaufsbudget erstellen: budget'''
        budget = 30.0
        print('Dir stehen wöchentlich %.2f' % budget, 'Euro für Obst zu Verfügung.')
        antwort = None
        antwort = input('Willst du das Budget anpassen? (Ja/ Nein) ')
        if antwort == "Ja":
            budget= float(input('Bitte gebe den neuen Betrag ein: '))
            print('Dein neues Budget beträgt %.2f' % budget, 'Euro')
        if antwort == "ja":
            budget= float(input('Bitte gebe den neuen Betrag ein: '))
            print('Dein neues Budget beträgt %.2f' % budget, 'Euro')
        if antwort == "JA":
            budget= float(input('Bitte gebe den neuen Betrag ein: '))
            print('Dein neues Budget beträgt %.2f' % budget, 'Euro')
        else:
            print()
                
        '''Es soll der Wochendurchschnitt für den Einkauf von Obst berechnet werden'''
        '''Liste mit dem Namen obst erstellen'''
        obst = []

        '''Eingabe für Woche 1, Woche 2, Woche 3 und Woche 4 ermöglichen'''
        wo1 = float(input('Ausgabe für Obst in Woche 1: '))
        obst.append(wo1)
        wo2 = float(input('Ausgabe für Obst in Woche 2: '))
        obst.append(wo2)
        wo3 = float(input('Ausgabe für Obst in Woche 3: '))
        obst.append(wo3)
        wo4 = float(input('Ausgabe für Obst in Woche 4: '))
        obst.append(wo4)

        '''Variable für den Durchschnitt erstellen: durchschnitt'''
        durchschnitt = None

        '''Den Wochendurchschnitt berechnen und ausdrucken'''
        durchschnitt = sum(obst) / len(obst)
        print('Der Wochendurchschnitt für den Einkauf von Obst beträgt %.2f' % durchschnitt, 'Euro.')

        '''Berechnen ob das Budget überschritten wurde und eine sinnvolle Nachricht ausgeben'''
        if durchschnitt < budget:
            print('Das Budget wurde nicht ausgeschöpft, gönn dir eine Belohnung.')
            
            print()
            abbruch = input('Möchtest du noch eine Berechnung durchführen? (J/N)')
        if abbruch == 'J':
            print()
        if abbruch == 'N':
            print('Bis zum nächsten Mal!')
            break

    elif eingabe == '2':
        
        '''Variable für das Wocheneinkaufsbudget erstellen: budget'''
        budget = 30.0
        print('Dir stehen wöchentlich %.2f' % budget, 'Euro für Snacks zu Verfügung.')
        antwort = None
        antwort = input('Willst du das Budget anpassen? (Ja/ Nein) ')
        if antwort == "Ja":
            budget= float(input('Bitte gebe den neuen Betrag ein: '))
            print('Dein neues Budget beträgt %.2f' % budget, 'Euro')
        if antwort == "ja":
            budget= float(input('Bitte gebe den neuen Betrag ein: '))
            print('Dein neues Budget beträgt %.2f' % budget, 'Euro')
        if antwort == "JA":
            budget= float(input('Bitte gebe den neuen Betrag ein: '))
            print('Dein neues Budget beträgt %.2f' % budget, 'Euro')
        else:
            print()
                    
        '''Es soll der Wochendurchschnitt für den Einkauf von Snacks berechnet werden'''
        '''Liste mit dem Namen snacks erstellen'''
        snacks = []

        '''Eingabe für Woche 1, Woche 2, Woche 3 und Woche 4 ermöglichen'''
        wo1 = float(input('Ausgabe für Snacks in Woche 1: '))
        snacks.append(wo1)
        wo2 = float(input('Ausgabe für Snacks in Woche 2: '))
        snacks.append(wo2)
        wo3 = float(input('Ausgabe für Snacks in Woche 3: '))
        snacks.append(wo3)
        wo4 = float(input('Ausgabe für Snacks in Woche 4: '))
        snacks.append(wo4)

        '''Variable für den Durchschnitt erstellen: durchschnitt'''
        durchschnitt = None

        '''Den Wochendurchschnitt berechnen und ausdrucken'''
        durchschnitt = sum(snacks) / len(snacks)
        print('Der Wochendurchschnitt für den Einkauf von Snacks beträgt %.2f' % durchschnitt, 'Euro.')

        '''Berechnen ob das Budget überschritten wurde und eine sinnvolle Nachricht ausgeben'''
        if durchschnitt < budget:
            print('Das Budget wurde nicht ausgeschöpft, gönn dir eine Belohnung.')
                    
            print()
            abbruch = input('Möchtest du noch eine Berechnung durchführen? (J/N)')
        if abbruch == 'J':
            print()
        if abbruch == 'N':
            print('Bis zum nächsten Mal!')
            break

    elif eingabe == '3':
        
        '''Variable für das Wocheneinkaufsbudget erstellen: budget'''
        budget = 30.0
        print('Dir stehen wöchentlich %.2f' % budget, 'Euro für Getränke zu Verfügung.')
        antwort = None
        antwort = input('Willst du das Budget anpassen? (Ja/ Nein) ')
        if antwort == "Ja":
            budget= float(input('Bitte gebe den neuen Betrag ein: '))
            print('Dein neues Budget beträgt %.2f' % budget, 'Euro')
        if antwort == "ja":
            budget= float(input('Bitte gebe den neuen Betrag ein: '))
            print('Dein neues Budget beträgt %.2f' % budget, 'Euro')
        if antwort == "JA":
            budget= float(input('Bitte gebe den neuen Betrag ein: '))
            print('Dein neues Budget beträgt %.2f' % budget, 'Euro')
        else:
            print()
            
        '''Es soll der Wochendurchschnitt für den Einkauf von Getränken berechnet werden'''
        '''Liste mit dem Namen getraenke erstellen'''
        getraenke = []

        '''Eingabe für Woche 1, Woche 2, Woche 3 und Woche 4 ermöglichen'''
        wo1 = float(input('Ausgabe für Getränke in Woche 1: '))
        getraenke.append(wo1)
        wo2 = float(input('Ausgabe für Getränke in Woche 2: '))
        getraenke.append(wo2)
        wo3 = float(input('Ausgabe für Getränke in Woche 3: '))
        getraenke.append(wo3)
        wo4 = float(input('Ausgabe für Getränke in Woche 4: '))
        getraenke.append(wo4)

        '''Variable für den Durchschnitt erstellen: durchschnitt'''
        durchschnitt = None

        '''Den Wochendurchschnitt berechnen und ausdrucken'''
        durchschnitt = sum(getraenke) / len(getraenke)
        print('Der Wochendurchschnitt für den Einkauf von Getränken beträgt %.2f' % durchschnitt, 'Euro.')

        '''Berechnen ob das Budget überschritten wurde und eine sinnvolle Nachricht ausgeben'''
        if durchschnitt < budget:
            print('Das Budget wurde nicht ausgeschöpft, gönn dir eine Belohnung.')
            
        print()
        abbruch = input('Möchtest du noch eine Berechnung durchführen? (J/N)')
        if abbruch == 'J':
            print()
        if abbruch == 'N':
            print('Bis zum nächsten Mal!')
            break

    elif eingabe == '4':
            
        print('Deine Ausgaben für diesen Monat in den Kategorien:')
        print('Obst: %2.f Euro' %sum(obst))
        print('Snacks: %2.f Euro' %sum(snacks))
        print('Getränke: %2.f Euro' %sum(getraenke))
        
        sum = sum(obst) + sum(snacks) + sum(getraenke)
        print('Deine Gesamtausgaben in diesem Monat: %2.f Euro' %sum)
        
        print()
        abbruch = input('Möchtest du noch eine Berechnung durchführen? (J/N)')
        if abbruch == 'J':
            print()
        if abbruch == 'N':
            print('Bis zum nächsten Mal!')
            break
        
            
