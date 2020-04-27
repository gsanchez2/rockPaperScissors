'''
Created on Apr 23, 2020

@author: ITAUser
'''
import random

#set variable keepPlaying to true

keepPlaying = True

#While keepPlaying is true:
while(keepPlaying == True):
    #print statement welcoming players to the game
    #print statement stating the rules (best 2 out of 3 press 'q' to quit
    print("Welcome to Rock Paper Scissors")
    print("Best out of 3 wins, press 'q' to quit")
    #make a key that assigns a number to each choice for the computer
    #(rock is 1, scissors is 2, paper is 3)
    
    #import the random function
    #set computer's score to 0
    #set player's score to 0
    player = 0
    computer = 0
    #while player's score is less than 2 and computer's score is less than 2:
    while(player < 2 and computer < 2):   
        
        #computer's choice = random number between 1 and 3
        computerChoice = random.randint(1, 3)
        
        #player's choice = input (ask player to select Rock, Paper, or Scissors)
        playerChoice = input("Please choose (Rock, Paper, or Scissors):")
        playerChoice = playerChoice.lower()
        #if  player inputs 'q' or 'Q':
        if(playerChoice == 'q'):
            
        #   set keepPlaying to False
            keepPlaying = False
        
        #   stop the loop
            break
        
        #else if (player inputs rock and computer chooses rock) or
        elif((playerChoice == "rock" and computerChoice == 1) or (playerChoice == "scissors" and computerChoice == 2)
              or (playerChoice == "paper" and computerChoice == 3)): 
        
        
        #   print out DRAW
        #   print out player's score and computer's score
            print("DRAW")
            print("Player Score = " + player.__str__() + " Computer Score = " + computer.__str__())
        
        #else if (player inputs rock and computer scissors) or (player imputs scissors and computer chooses paper) or
        elif((playerChoice == "rock" and computerChoice == 2) or (playerChoice == "scissors" and computerChoice == 3)
              or (playerChoice == "paper" and computerChoice == 1)):
        #   add one to the player's score
            player = player + 1
        #   print out player's score and computers's score
            print("Round Win")
            print("Player Score = " + player.__str__() + " Computer Score = " + computer.__str__())
        
        #else if (player inputs rock and computer chooses paper) or
        elif((playerChoice == "rock" and computerChoice == 3) or (playerChoice == "scissors" and computerChoice == 1)
             or (playerChoice == "paper" and computerChoice == 2)):
        #   add one to the computer's score
            computer = computer + 1
        #   print out player's score and computer's score
            print("Player Score = " + player.__str__() + " Computer Score = " + computer.__str__())
        
        #else:
        else:
        #   tell the user their input was not valid
            print("Your choice was invalid. Try again")
    #print statement thanking thr players for playing
    print("Thank you for playing")
    #if plater's score is 2:
    if(player == 2):
    #   print statement letting player know they won
        print("You Won!")
    #if computer's score is 2
    if(computer == 2):
    #   print statment letting player know the computer won
        print("You Lost")
    #print out player's score and computer's score
        print("Player Score = " + player.__str__() + " Computer Score = " + computer.__str__())
    
    