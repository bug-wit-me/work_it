# 🤔 Number Guessing Game 😜
## **Overview**  
This project is a simple Number Guessing Game developed using **Streamlit**, where players try to guess a random number between **1 and 100** within a limited number of attempts. The game provides real-time feedback after each guess, guiding players toward the correct number.



## **Features**  
- **Random Number Generation**: The game generates a random number between **1 and 100** for every session.  
- **Feedback System**: Players receive hints if their guess is too high, too low, or correct.  
- **Guess Tracking**: Displays a list of the player’s previous guesses.  
- **Attempt Counter**: Shows the number of attempts remaining.  
- **Automatic Reset**: The game resets automatically after the player wins or loses.  
- **Manual Reset Option**: Players can restart the game anytime by clicking the **Try Again** button.  



## **Code Explanation**  
1. **generate_random_number()**: Generates a random number between **1 and 100** at the start of the game.  
2. **check_guess(guess, target)**: Compares the player’s guess with the target number and returns feedback:  
   - **"Too low"** if the guess is less than the target.  
   - **"Too high"** if the guess is greater than the target.  
   - **"Correct!"** if the guess matches the target.  
3. **track_guesses(guess)**: Records the player’s guesses and updates the guess history.  
4. **update_attempts()**: Reduces the remaining attempts by one after each incorrect guess.  
5. **reset_game()**: Resets the random number, attempt counter, and guess history to start a new game.  
6. **game_flow()**: Manages the overall gameplay, including input handling, feedback display, and game resets.



## **Acknowledgment**  
Special thanks to **Streamlit** for providing an excellent framework for building interactive web applications and enhancing the gameplay experience.  


