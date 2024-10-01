
import streamlit as st
import random

# Title of the game
st.markdown("<h1 style='color: black;'>🤔NUMBER GUESSING GAME😜</h1>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; font-size: 17px; color: purple; font-weight: normal; margin-top: -20px; margin-left: -49px;">
        Guess wisely - one number holds all the power!
    </div>
""", unsafe_allow_html=True)

# Create a tab for instructions
tabs = st.tabs(["Instructions for Player"])

with tabs[0]:
    st.markdown("""
        <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px; background-color: #f9f9f9;">
        <ul>
            <li> The player has to guess a number between <b>1</b> and <b>100</b>.</li>
            <li>The player will have <b>8 attempts</b> to guess the correct number.</li>
            <li>After each guess, you will be told whether your guess is too high, too low, or correct.</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)

    st.write("Enter your guess below:")

    # Initialize session state variables
    if 'current_number' not in st.session_state:
        st.session_state.current_number = random.randint(1, 100)
        st.session_state.attempts_remaining = 8
        st.session_state.guess_history = []

    # Display previous guesses if they exist
    if st.session_state.guess_history:
        st.markdown("<h3 style='color: #9C27B0; font-size: 17px;'>Your previous guesses:</h3>", unsafe_allow_html=True)
        # Join guesses into a single line
        previous_guesses = ', '.join(map(str, st.session_state.guess_history))
        st.markdown(f"<span style='color: black; font-size: 14px;'>Guesses: {previous_guesses}</span>", unsafe_allow_html=True)

    # Display remaining attempts
    st.markdown(
        f"<span style='color: red; font-size: 18px; font-weight: bold;'>YOU HAVE {st.session_state.attempts_remaining} ATTEMPTS REMAINING.</span>",
        unsafe_allow_html=True)

    # Input for the guess
    guess = st.number_input("Guess a number (1-100):", min_value=1, max_value=100)

    # Handling the guess submission
    if st.button("Submit Guess"):
        if guess in st.session_state.guess_history:
            st.warning("You've already guessed that number! Try a different one.")
        else:
            st.session_state.guess_history.append(guess)
            st.session_state.attempts_remaining -= 1

            if guess < st.session_state.current_number:
                feedback = "Your guess is too low..."
            elif guess > st.session_state.current_number:
                feedback = "Your guess is too high..."
            else:
                feedback = f"🎉Congratulations!🎉🥳 You guessed correctly! The number was {st.session_state.current_number}."
                st.balloons()
                # Reset the game
                st.session_state.guess_history.clear()
                st.session_state.current_number = random.randint(1, 100)
                st.session_state.attempts_remaining = 8

            # Check if the attempts are exhausted
            if st.session_state.attempts_remaining <= 0:
                feedback = f"Sorry😔, you have used up all your attempts. The hidden number was {st.session_state.current_number}."
                st.session_state.guess_history.clear()
                st.session_state.current_number = random.randint(1, 100)
                st.session_state.attempts_remaining = 8

            # Display feedback
            st.markdown(f"""
                <div style="border: 2px solid black; padding: 7px; border-radius: 5px; background-color: green; color: yellow; width: 80%; margin: auto;">
                    {feedback}
                </div>
            """, unsafe_allow_html=True)

    # Button to restart the game
    if st.button("Try Again", key="try_again"):
        st.session_state.current_number = random.randint(1, 100)
        st.session_state.attempts_remaining = 8
        st.session_state.guess_history.clear()

