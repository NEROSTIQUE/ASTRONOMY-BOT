import random

# Define a list of planets
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Define a dictionary of planet information
planet_info = {
    'Mercury': 'Mercury is the smallest planet in the solar system and the closest to the sun.',
    'Venus': 'Venus is the second planet from the sun and the hottest planet in the solar system.',
    'Earth': 'Earth is the third planet from the sun and the only planet known to support life.',
    'Mars': 'Mars is the fourth planet from the sun and is known as the red planet.',
    'Jupiter': 'Jupiter is the largest planet in the solar system and has the most moons.',
    'Saturn': 'Saturn is the second-largest planet in the solar system and is known for its rings.',
    'Uranus': 'Uranus is the seventh planet from the sun and is tilted on its side.',
    'Neptune': 'Neptune is the eighth planet from the sun and has the strongest winds in the solar system.'
}

# Define a dictionary of topics and their possible responses
topics = {
    "telescope": [
        "What type of telescope are you interested in? There are many different kinds, such as reflectors, refractors, and catadioptrics.",
        "Do you have any specific questions about telescopes?",
        "Telescopes are a great way to observe the night sky. What are you hoping to see?"],
    "planet": ["Which planet are you interested in? There are 8 planets in our solar system.",
               "Planets are fascinating. Which one are you most interested in?",
               "I'd love to talk about planets. Which one is your favorite?"],
    "star": ["Stars are amazing, aren't they? What would you like to know about them?",
             "There's so much to learn about stars. What questions do you have?",
             "Stars are beautiful and mysterious. What can I help you with?"],
}


# Define a function to generate responses to user input
def get_response(user_input):
    # Define possible responses for the AI
    greetings = ["Hello! I'm an astronomy chatbot. How can I help you today?",
                 "Hi there! What can I help you with in the world of astronomy?"]
    goodbye_responses = ["Goodbye! I hope I was able to help you.",
                         "Take care! If you have any more questions, feel free to ask."]

    # Check for specific keywords in the user's input
    if "hello" in user_input or "hi" in user_input:
        return random.choice(greetings)
    elif "telescope" in user_input:
        return random.choice(topics["telescope"])
    elif "planet" in user_input:
        return random.choice(topics["planet"])
    elif "star" in user_input or "stars" in user_input:
        return random.choice(topics["star"])
    elif "bye" in user_input:
        return random.choice(goodbye_responses)
    else:
        # Check if user input contains a planet name
        for planet in planets:
            if planet.lower() in user_input:
                return planet_info[planet]

        # If no specific topic or planet is found, use a general response
        return "I'm sorry, I'm not sure what you're asking. Can you please try again?"


# Define a loop to keep the chat going until the user says goodbye
while True:
    # Get user input
    user_input = input("You: ").lower()
    # Check if the user wants to quit

    if user_input == "bye":
        print(get_response(user_input))
        break
    # Generate a response and print it

    response = get_response(user_input)
    print("Bot:", response)