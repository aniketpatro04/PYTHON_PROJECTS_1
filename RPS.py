from random import randint

move = ['rock', 'paper', 'scissor']

comp = randint(0, 2)

print("Enter '0' for rock, '1' for paper, '2' for scissor")

x = int(input())
player = move[x]

play = False

print("Ready to play? y / n")
response1 = input()


if response1 == 'y':
    play = True
else:
    print("See ya again")
    play = False

while play:
    if (comp == 'rock' and player == 'paper') or (comp == 'paper' and player == 'rock'):
        result = 'paper'
    elif (comp == 'rock' and player == 'scissor') or (comp == 'scissor' and player == 'rock'):
        result = 'rock'
    elif comp == player:
        result = 'tie'
    else:
        result = 'scissor'

    if result == player:
        print("You win!")
    else:
        print("Computer wins")

    break

play = False
print("Thank You for playing")
print("\n")
