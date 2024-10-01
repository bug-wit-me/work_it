# 🤔 Number Guessing Game 😜

This is a simple number guessing game built using **Streamlit**, where the player has to guess a random number between 1 and 100 within a limited number of attempts. The game provides feedback after each guess, letting the player know if their guess is too high, too low, or correct.

## How to Play

- The player has **8 attempts** to guess a number between **1** and **100**.
- After each guess, the game will indicate whether the guess is:
  - **Too low**
  - **Too high**
  - **Correct**
- If the player guesses the correct number, a congratulatory message is displayed, and the game resets automatically.
- If the player runs out of attempts, the correct number is revealed, and the game resets automatically.

## Instructions for Players

1. Enter your guess in the input field.
2. Submit your guess by clicking the **Submit Guess** button.
3. The game will give you feedback based on your guess.
4. You can see your previous guesses and the number of attempts remaining.
5. If you wish to restart the game at any point, click the **Try Again** button.

## Features

- Random number generation between 1 and 100.
- Feedback after each guess (too low, too high, correct).
- Displays the player's guess history.
- Tracks and displays the remaining number of attempts.
- Automatically resets the game after the player either wins or runs out of attempts.
- Allows the player to restart the game at any time.

## Technologies Used

- **Streamlit**: The main framework used to build the web app.
- **Python**: Core programming language for implementing game logic.
- **HTML & CSS** (within Streamlit's markdown): For custom styling of the game UI.

## Running the Project

To run this project locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/number-guessing-game.git
    ```

2. Navigate to the project directory:
    ```bash
    cd number-guessing-game
    ```

3. Install the required dependencies:
    ```bash
    pip install streamlit
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

5. Open your browser and visit `http://localhost:8501` to start playing the game.

## Future Enhancements

- Add difficulty levels (easy, medium, hard) with different ranges of numbers.
- Track the player’s high score and display it at the end of the game.
- Add a timer to increase the challenge and engagement.

## Screenshot

![Number Guessing Game Screenshot](screenshot.png)

---

Feel free to contribute to this project by forking the repository and submitting a pull request!

## License

This project is licensed under the MIT License.

