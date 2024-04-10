Pokémon Battle Game
<br><br>
This is a simple text-based Pokémon battle game written in Python. The game allows you to choose from three random Pokémon and compete against a randomly generated opponent's Pokémon. You'll select a stat to compare, and the Pokémon with the higher stat wins the round. The first player to score 3 points wins the game.

<br><br><br>
Requirements:
<br><br>
Python 3<br>
random module<br>
requests module<br>

<br><br>
How to Play:
<br>
Run the code using a Python interpreter.<br>
You will be given three Pokémon to choose from.<br>
The game will display the current round and ask you to select a Pokémon and a stat to compare.<br>
Enter the number corresponding to your Pokémon choice (1, 2, or 3).<br>
Enter the number corresponding to the stat you want to compare:<br>
1: Physical stat<br>
2: Magic stat<br>
3: Special ability stat<br>
The opponent's Pokémon and its corresponding stat will be randomly generated.<br>
The battle begins! The game will count down from 3, displaying your Pokémon's attack and the opponent's attack.<br>
The winner of the round is determined based on the comparison of the selected stats. If your stat is higher, you win; otherwise, the opponent wins. In case of a tie, the round is declared a draw.<br>
The game will display the current score: your score and the opponent's score.<br>
If neither player has scored 3 points yet, the next round will start automatically.<br>
The game continues until one player reaches a score of 3 points, at which point the final results will be displayed.<br><br><br>

How to Restart the Game<br><br>

After finishing a game, you will be prompted to play again. If you enter "yes," the game will reset, and a new tournament will begin with three new Pokémon choices. If you enter "no," the game will end, and the program will terminate.
<br>
Please note that the Pokémon choices and stats are randomly generated using the PokeAPI, ensuring a different experience in each game.
<br>
Enjoy the Pokémon battle tournament!
