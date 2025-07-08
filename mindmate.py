import datetime

def get_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

def initial_check_in():
    return (
        f"{get_greeting()} I'm MindMate, your mental health check-in buddy. 💙\n"
        "How are you feeling today on a scale from 1 (low) to 10 (great), or just tell me in words?"
    )

def mood_response(mood):
    mood = mood.lower()
    if any(word in mood for word in ["sad", "tired", "depressed", "anxious", "low", "bad"]):
        return (
            "I'm really sorry you're feeling this way. 💭\n"
            "Sometimes it's okay to not be okay. Would you like to try a quick 1-minute breathing exercise?\n"
            "Or maybe write one thing you're grateful for today. ✍️"
        )
    elif any(word in mood for word in ["okay", "fine", "normal", "meh"]):
        return (
            "Thanks for sharing. It's perfectly fine to feel neutral too. 🌤️\n"
            "Would you like a journaling prompt to explore how your day has been?"
        )
    elif any(word in mood for word in ["happy", "excited", "great", "good"]):
        return (
            "That's wonderful to hear! 😊\n"
            "Hold onto that feeling! Would you like to note one positive moment from today?"
        )
    else:
        return (
            "Thanks for being honest with me. 💙\n"
            "Emotions can be complicated. Would a small reflection activity help right now?"
        )

def journaling_prompt():
    return (
        "Here's a journaling prompt for today: ✨\n"
        "\"What’s something small that made you smile recently?\"\n"
        "Take a minute to write it down or reflect on it.📝"
    )

def wrap_up():
    return (
        "Thanks for checking in with me today. 🌈\n"
        "Remember, small steps lead to big changes.\n"
        "Would you like me to check in with you again tomorrow?"
    )

# --- Simulation ---
if __name__ == "__main__":
    print(initial_check_in())
    user_mood = input("You: ")
    print("MindMate:", mood_response(user_mood))
    followup = input("Do you want a journaling prompt? (yes/no): ")
    if followup.lower() == "yes":
        print(journaling_prompt())
    print(wrap_up())
