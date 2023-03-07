import random 
import requests 
import time

#assigning global variables for the scores
my_winnings = 0
opponent_winnings = 0
count = 1

def random_pokemon():
    """Selects a random pokemon from the PokeAPI and returns its name, id, height, and weight."""
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number) 
    response = requests.get(url)
    pokemon = response.json()
    
    return {
        'name': pokemon['name'], '1': pokemon['stats'][0]['base_stat'],
        '2': pokemon['stats'][1]['base_stat'], '3': pokemon['stats'][2]['base_stat'],
    }


    
def run():
    
    """Runs the game, allowing the user to choose from three random pokemon and select a stat to compare with a randomly generated opponent's pokemon."""
    my_pokemon_one = random_pokemon()
    my_pokemon_two = random_pokemon()
    my_pokemon_three = random_pokemon()
    # ADD THE FUNCTION TO DO NOT REPEAT POKEMONS 
    
    print('\n♦♦♦♦♦♦♦♦')
    print('\nWelcome to the pokemon tournament! \nWhoever scores 3 points first wins the game')
    time.sleep(2)
    print('\nYou were given three pokemons: ' + '\n1. ' + my_pokemon_one['name'].capitalize() +'\n2. ' + my_pokemon_two['name'].capitalize() + '\n3. ' + my_pokemon_three['name'].capitalize())
    time.sleep(1)
    
    print('\n♦♦♦♦♦ ROUND ONE ♦♦♦♦♦')
    time.sleep(1)
    
    # Define function for selecting user's pokemon and stat to compare
    def choose_poke():
        global count 
        count += 1 
        
        """Allows the user to select a pokemon and stat to compare against a randomly generated opponent's pokemon."""
        poke_choice = input('Which pokemon do you want to use? (1, 2, 3)? ')
        time.sleep(1)
        
        # Check that user has entered a valid input
        while poke_choice != '1' and poke_choice != '2' and poke_choice != '3':
            print('You have only three pokemons. Please type (1, 2, 3).')
            poke_choice = input()
        else:
            # Set user's pokemon based on input
            if poke_choice == '1':
                my_poke = my_pokemon_one
                print('You chose {}'.format(my_poke['name'].capitalize()))
            elif poke_choice == '2':
                my_poke = my_pokemon_two
                print('You chose {}'.format(my_poke['name'].capitalize()))
            elif poke_choice == '3':
                my_poke = my_pokemon_three
                print('You chose {}'.format(my_poke['name'].capitalize()))
        
        # Allow user to select a stat to compare
        time.sleep(1)
        print('\nWhich attack do you want to use?')
        time.sleep(1)
        stat_choice = input('\nPhysical = 1\nMagic = 2 \nSpecial ability = 3\n(1, 2, 3) ')
        
        # Check if user has entered a valid input
        while stat_choice != '1' and stat_choice != '2' and stat_choice != '3':
            print('Please type only (1, 2, 3).')
            stat_choice = input()
        else:
            time.sleep(1)
            my_stat = my_poke[stat_choice] 
        
        # Generate opponent's pokemon and select stat to compare
        opponent_pokemon = random_pokemon()
        print("\nYour opponent is thinking...")
        time.sleep(2)
        print('The opponent chose {}'.format(opponent_pokemon['name'].capitalize()))
        time.sleep(1)
        opponent_stat = opponent_pokemon[stat_choice]

        
        # Slowdown 
        time.sleep(1)
        print("\nLet the battle begin!")
        time.sleep(1)
        print("3!")
        time.sleep(1)
        print("2!")
        time.sleep(1)
        print("1!")
        time.sleep(1)
        print('Your attack is equal to: ' + str(my_stat))
        time.sleep(1)
        print('Your opponent atack is equal to ' + str(opponent_pokemon[stat_choice]))
        time.sleep(1)
        
        # Compare user's and opponent's stats and declare a winner
        if my_stat > opponent_stat: 
            global my_winnings
            my_winnings = my_winnings + 1 
            time.sleep(1)
            print('\nYou Win!')
            time.sleep(0.5)
            print("╰(▔∀▔)╯╰(▔∀▔)╯╰(▔∀▔)╯╰(▔∀▔)╯")
        elif my_stat < opponent_stat:
            #ADD THE FUNCTION TO NOW REMOVE THE DEAD POKEMON FROM CHOICES  
            global opponent_winnings
            opponent_winnings = opponent_winnings + 1
            time.sleep(1)
            print('\nYou Lose!')
            time.sleep(0.5)
            print("(;﹏;)(;﹏;)(;﹏;)(;﹏;)(;﹏;)")
        else: 
            time.sleep(1)
            print('\nDraw!')
            
        
          # Display the current score
        time.sleep(1)
        print('\nTotal Score: \nYour score: ' + str(my_winnings) + '\nOpponent Score: ' + str(opponent_winnings))
    
        if (opponent_winnings == 3):
            time.sleep(2)
            print('\n♦♦♦♦♦ FINAL RESULTS: ♦♦♦♦♦')
            print('\nYou lost the tournament.')
        elif (my_winnings == 3):
            time.sleep()
            print('♦♦♦♦♦ FINAL RESULTS: ♦♦♦♦♦')
            print('\nYou won the tournament.')
        else:
            time.sleep(2)
            print('\n♦♦♦♦♦ ROUND ' + str(count) + ' ♦♦♦♦♦')
            choose_poke()
            

    choose_poke()
    

        
        

# start the game 

run()


repeat = input('Would you like to play again? Type yes or no.\n')
if repeat == 'yes':
    #resetting global var
    my_winnings = 0
    opponent_winnings = 0
    count = 1 
    run()
else:
    print('Bye then!')
