import random

# Player and opponent stats
player_health = 100
opponent_health = 100

# Define moves
def attack():
    return random.randint(10, 30)

def defend():
    return random.randint(5, 15)

def heal():
    return random.randint(10, 20)

# Game loop
while player_health > 0 and opponent_health > 0:
    print(f"Your health: {player_health}, Opponent's health: {opponent_health}")
    print("Choose your move: ")
    print("1. Attack")
    print("2. Defend")
    print("3. Heal")
    
    move = int(input("Enter the number of your move: "))
    
    if move == 1:
        damage = attack()
        opponent_health -= damage
        print(f"You attacked the opponent and caused {damage} damage!")
    
    elif move == 2:
        defense = defend()
        player_health += defense
        print(f"You defended and restored {defense} health!")
    
    elif move == 3:
        healing = heal()
        player_health += healing
        print(f"You healed yourself for {healing} health!")
    
    # Opponent's turn (random action)
    opponent_move = random.choice(["attack", "defend", "heal"])
    if opponent_move == "attack":
        damage = attack()
        player_health -= damage
        print(f"Opponent attacked you and caused {damage} damage!")
    
    elif opponent_move == "defend":
        defense = defend()
        opponent_health += defense
        print(f"Opponent defended and restored {defense} health!")
    
    elif opponent_move == "heal":
        healing = heal()
        opponent_health += healing
        print(f"Opponent healed for {healing} health!")
    
    print("-----------")

# Determine the winner
if player_health <= 0:
    print("You lost the fight!")
elif opponent_health <= 0:
    print("You won the fight!")