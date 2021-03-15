import random

def main():

  players = int(input('Insert the number of players: '))
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))
  player_sum = []
  dice_sum = 0
  
  for i in range(0, players):
    dice_sum = 0
    for y in range(0,dice_rolls):
        roll = random.randint(1,dice_size)
        dice_sum += roll
        if roll == 1:
            print(f'Player {i+1} rolled a {roll}! Critical Fail')
        elif roll == dice_size:
            print(f'Player {i+1} rolled a {roll}! Critical Success')
        else:
            print(f'Player {i+1} rolled a {roll}')
        if y == dice_rolls - 1:
            player_sum.append(dice_sum)
  
  for i in range(0, players):
    print(f'Player {i+1} rolled a total of 'f' {player_sum[i]}')
    
  winner = player_sum.index(max(player_sum))
  print(f'Player {winner+1} has won!')


if __name__== "__main__":
  main()