print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo a ilha do tesouro.")
print("Sua missão é encontrar o tesouro.")
print(("Você vê uma bifurcação e deve escolher um lado para continuar"))
diracao = input("esquerda ou direita?\n")
if direcao != "esquerda":
    print("Caiu em um buraco \n Fim de jogo")
else:
    print("")
print("Você vê um lago com uma ilha no centro, você pode esperar o barco ou nadar até la")
lago = input("nadar ou esperar?\n")
if lago != "esperar":
    print("Você foi atacado por piranhas\nFim de jogo")
else:
    print("")
print("Você encontra 3 portas, qual delas você quer entrar?")
porta = input("azul, amarela ou vermelha?\n")
if porta == "azul":
    print("Você foi comido por bestas\nFim de jogo")
elif porta == "amarela":
    print("Você encontrou o tesouro\nVocê venceu!")
elif porta == "vermelha":
    print("Você foi queimado por chamas\nFim de jogo")
