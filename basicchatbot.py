import math
from datetime import datetime

INTENT_KEYWORDS = {
    "farewell": ["quit", "exit", "bye", "goodbye", "see ya"],
    "greeting": ["hello", "hi", "how are you", "what's up", "hey"],
    "identity": ["name", "who are you"],
    "help": ["help", "what can you do"],
    
    "math_sum": ["sum", "add", "calculate"],
    
    "area_circle": ["area of circle", "circle area","circle"],
    "area_rectangle": ["area of rectangle", "rectangle area","rectangle"],
    "area_square": ["area of square", "square area", "square"],
    "general_area_query": ["area"],

    "capital_query": ["capital", "capitals"],
}

CHATBOT_RESPONSES = {
    "greeting": "Hello, how can I help you?",
    "farewell": "Goodbye! Have a great day!",
    "identity": "I am a simple Python chatbot.",
    "help": "I can chat, sum/add/calculate numbers, or find the area of a square, circle, or rectangle! I can also tell you about some capitals.",
    
    "math_sum": "Alright, tell me the numbers you want to add.",
    
    "area_circle": "Okay, for a circle, I need the radius.",
    "area_rectangle": "For a rectangle, I'll need its length and width.",
    "area_square": "Okay, for a square, I need the side length.",
    "general_area_query": "Which shape's area would you like to calculate (e.g., square, circle, rectangle)?",
    
    "capital_query": "Yes, I can tell you the capitals of countries. Which country's capital do you want to know?",
    "capital_not_found": "I don't know the capital of that country yet. I can tell you about India, France, Germany, Japan, USA, or Canada.",
    
    "fallback": "I'm not sure how to respond to that. Can you rephrase or ask something else?"
}

CAPITALS_DATA = {
    "india": "Delhi",
    "france": "Paris",
    "germany": "Berlin",
    "japan": "Tokyo",
    "usa": "Washington D.C.",
    "united states": "Washington D.C.",
    "canada": "Ottawa",
    "uk": "London",
    "united kingdom": "London",
    "italy": "Rome",
}

def get_numeric_input(prompt_message, error_message, allow_negative=False):
    while True:
        # CORRECTED LINE HERE
        user_input_str = input(f"Chatbot: {prompt_message}")
        try:
            value = float(user_input_str.strip())
            if not allow_negative and value < 0:
                print(f"Chatbot: {error_message} (Value cannot be negative. Please enter a positive number.)")
            else:
                return value
        except ValueError:
            print(f"Chatbot: {error_message}") # Also added Chatbot: prefix here for error messages
        except Exception as e:
            print(f"Chatbot: An unexpected error occurred during input: {e}") # And here

def addition():
    user_input = input(f"Chatbot: Enter the numbers separated by '+': ") # Also added Chatbot: prefix here
    user_input = user_input.strip()
    if "+" in user_input:
        parts = user_input.split("+")
        total_sum = 0.0
        for part in parts:
            try:
                total_sum += float(part.strip())
            except ValueError:
                return f"Error: '{part}' is not a valid number. Please enter only numbers separated by '+'."
            except Exception as e:
                return f"An unexpected error occurred during calculation: {e}"
        return f"The sum is: {total_sum:.2f}"
    else:
        try:
            return f"The number is: {float(user_input):.2f}"
        except ValueError:
            return "Error: Please enter a single number or numbers separated by a '+' sign."

def area_of_square():
    side_length = get_numeric_input("Enter the length of the side: ", "Error: Invalid input. Please enter a valid number for the side length.")
    if side_length is None:
        return "Calculation cancelled due to invalid input."
    return f"The area of the square is: {side_length**2:.2f}"

def area_of_circle():
    radius = get_numeric_input("Enter the radius of the circle: ", "Error: Invalid input. Please enter a valid number for the radius.")
    if radius is None:
        return "Calculation cancelled due to invalid input."
    area = math.pi * (radius ** 2)
    return f"The area of the circle is: {area:.2f}"

def area_of_rectangle():
    length = get_numeric_input("Enter the length of the rectangle: ", "Error: Invalid input. Please enter a valid number for the length.")
    if length is None:
        return "Calculation cancelled due to invalid input."
    width = get_numeric_input("Enter the width of the rectangle: ", "Error: Invalid input. Please enter a valid number for the width.")
    if width is None:
        return "Calculation cancelled due to invalid input."
    area = length * width
    return f"The area of the rectangle is: {area:.2f}"

def get_capital_info(user_message):
    cleaned_input = user_message.lower().strip()
    for country, capital in CAPITALS_DATA.items():
        if country in cleaned_input:
            return f"The capital of {country.title()} is {capital}."
    
    return CHATBOT_RESPONSES["capital_not_found"]

def get_bot_response(user_message):
    cleaned_input = user_message.lower().strip()

    if any(keyword in cleaned_input for keyword in INTENT_KEYWORDS["area_circle"]):
        return area_of_circle()
    
    elif any(keyword in cleaned_input for keyword in INTENT_KEYWORDS["area_rectangle"]):
        return area_of_rectangle()
        
    elif any(keyword in cleaned_input for keyword in INTENT_KEYWORDS["area_square"]):
        return area_of_square()

    elif any(keyword in cleaned_input for keyword in INTENT_KEYWORDS["general_area_query"]):
        return CHATBOT_RESPONSES['general_area_query'] + " Or type 'quit' to exit."

    elif any(keyword in cleaned_input for keyword in INTENT_KEYWORDS["capital_query"]):
        return get_capital_info(cleaned_input)

    elif any(keyword in cleaned_input for keyword in INTENT_KEYWORDS["math_sum"]):
        return addition()

    elif any(keyword in cleaned_input for keyword in INTENT_KEYWORDS["greeting"]):
        return CHATBOT_RESPONSES["greeting"]
        
    elif any(keyword in cleaned_input for keyword in INTENT_KEYWORDS["identity"]):
        return CHATBOT_RESPONSES["identity"]
        
    elif any(keyword in cleaned_input for keyword in INTENT_KEYWORDS["help"]):
        return CHATBOT_RESPONSES["help"]

    return CHATBOT_RESPONSES["fallback"]

def greet_user():
    print("--- Welcome to the Simple Chatbot! ---")
    print("Type 'quit' or 'exit' anytime to end the conversation.")
    print(CHATBOT_RESPONSES["help"])
    print("-------------------------------------")


date_time = datetime.now()
print(date_time)
Chatbot_active = True
greet_user()

while Chatbot_active:
    user_input = input("You: ")

    cleaned_input_for_quit = user_input.lower().strip()

    if any(keyword in cleaned_input_for_quit for keyword in INTENT_KEYWORDS["farewell"]):
        print(f"Chatbot: {CHATBOT_RESPONSES['farewell']}")
        Chatbot_active = False
    else:
        bot_answer = get_bot_response(user_input)
        print(f"Chatbot: {bot_answer}")
