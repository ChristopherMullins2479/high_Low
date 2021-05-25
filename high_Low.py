#this is a very simple high low game that will have you guess if the next card will be higher or lower then the previous
#writen by christopher mullins

#imports
import array
import random

#variables
counter = 0
game_Round = 0
deck_Hearts = ["AH","2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH",]
deck_Diamonds = ["AD","2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD",]
deck_Clubs = ["AC","2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC",]
deck_Spades = ["AS","2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS",]

#functions
#rules function
def rules_Function():
    print("\n-------------------Rules-------------------")
    print("This is a game that you will need to guess,")
    print("if the next gard will be higher or lower")
    print("then the previous card")

#game menue screen that will show every round
def game_Menue_Screen_Function(game_Round):
    print("\n-----Welcome To High Low-----")
    print("Round : "+str(game_Round))

#new game function
def new_Game_Function(game_Round):
    game_Round = 1

def gen_Player_Deck():
    deck_choser = (random.randint(0,4))
    if(deck_choser == 1):
        print("hearts")
        card_Choser = (random.randint(-1,12))
        print(deck_Hearts[card_Choser])
    if(deck_choser == 2):
        print("diamonds")
        card_Choser = (random.randint(-1,12))
        print(deck_Diamonds[card_Choser])
    if(deck_choser == 3):
        print("clubs")
        card_Choser = (random.randint(-1,12))
        print(deck_Clubs[card_Choser])
    if(deck_choser == 4):
        print("spades")
        card_Choser = (random.randint(-1,12))
        print(deck_Spades[card_Choser])


#Depending on user choice will run different blocks of code
while(counter != -1): 
    print("Welcome to High Low")
    print("\nPleaes chose from the following.")
    print("1.) Start Game")
    print("2.) Rules")

    #taking in the value
    user_Main_Menue_Choice = int(input("Please enter your choice: "))

    #if ststements to read in the user input
    #runs when user choses 1
    if user_Main_Menue_Choice == 1:
        game_Round = game_Round + 1
        new_Game_Function(game_Round)
        game_Menue_Screen_Function(game_Round)
        gen_Player_Deck()
        break

    #runs when user choses 2
    if user_Main_Menue_Choice == 2:
        rules_Function()
        break 

    #runs with any other choice 
    else:
        print("\nPlease enter either 1 to start the game or 2 to read the rules")



