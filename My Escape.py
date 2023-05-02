# Text-Based Advemture Game
# Your goal is to survive

# making the rooms

# diamond room
def esszimmer():
  # some prompts
  print("Mit dem Schlüssel öffnet sich die Tür.\nDu gehst hindurch und landest in einem Esszimmer.")
  print("Auf dem Tisch steht eine seltsame Flasche, es steht 'Trink mich' darauf.")
  print("Möchtest Du die Flasche öffnen und den Inhalt probieren? (1 oder 2)")
  print("1 - Da steht 'Trink mich' drauf, also schraubst du die Flasche auf und nimmst einen Schluck.")
  print("2 - Du trinkst lieber nichts aus dieser komischen Flasche")
  
  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead, call game_over() function with the "reason"
    print("Game over - Du stirbst einen qualvollen Tod!")
    
  elif answer == "2":
    # the player won the game
    print("\nDas war die richtige Entscheidung!")
    print("Jetzt siehst du die offene Tür und rennst raus - Gewonnen, Du bist entkommen!")
    # activate play_again() function
    play_again()
  else:
    # call game_over() with "reason"
    game_over("Game Over - Kannst Du denn keine Zahlen eingeben?")


# Kueche
def kueche():
  # give some prompts
  # '\n' is to print the line in a new line
  print("\nIn der Küche siehst Du ein gruseliges grau-grünes Schleimmonster.")
  print("Was wirst Du tun? (1 oder 2)?")
  print("1). Du schleichst Dich vorsichtig zurück.")
  print("2). Du stürzst Dich mutig in den Kampf!")

  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead!
    game_over("Oh Nein, Das Monster hat dich gesehen und sich wütend auf Dich gestürzt - Du hattest keine Chance...")
  elif answer == "2":
    # lead him to the diamond_room()
    print("\nMit List und Tücke besiegst Du das Monster!\nDa in der Küche sonst nichts zu tun ist gehst Du zurück in das Empfangszimmer, wo Du hergekommen bist.")
    empfangszimmer()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Game Over - Kannst Du denn keine Zahlen eingeben?")

 # empfangszimmer
def empfangszimmer():
  print("Du siehst zwei Türen.")
  print("Öffnest Du die linke Tür oder die rechte Tür? l/r")
  
  # convert the player's input() to lower_case
  answer = input(">").lower()

  if "l" in answer:
    # if player typed "left" or "l" zur Küche()
    kueche()
  elif "r" in answer:
    # else if player typed "right" or "r" lead him to verschlossen()
    verschlossen()
           #Tür geht auf
  else:
    # else call game_over() function with the "reason" argument
    game_over("Game Over - Falsche Eingabe, gib Dir mehr Mühe!")
    
def verschlossen():
    print("Die Tür ist verschlossen!\nMöchtest Du das Empfangszimmer durchsuchen, vielleicht findest du etwas Nützliches. j/n")
    
    # convert the player's input() to lower_case
    answer = input(">").lower()

    if "j" in answer:
        # Player findet Schlüssel
        print("Du findest einen Schlüssel.")
        esszimmer()
    elif "n" in answer:
        verschlossen()
               #Tür geht auf
    else:
        # else call game_over() function with the "reason" argument
        game_over("Game Over - Falsche Eingabe, gib Dir mehr Mühe!")

# function to ask play again or not
def play_again():
  print("\nMöchtest Du nochmal spielen? (j/n)")
  
  # convert the player's input to lower_case
  answer = input(">").lower()

  if "j" in answer:
    # if player typed "yes" or "y" start the game from the beginning
    start()
  else:
    # if user types anything besides "yes" or "y", exit() the program
    exit()


# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # ask player to play again or not by activating play_again() function
  play_again()


def start():
  # give some prompts.
  print("\Du wachst in einem wunderschönen Empfangszimmer auf... Wie bist du nur hierher gekommen?\nObwohl es Dir hier gut gefällt möchtest Du diesen Ort verlassen.")
  # lead him to Empfangszimmer()
  empfangszimmer()
 


# start the game
start()