import math

chatbot_response = {
    "hello": "Hello, how can I help you?",
    "hi": "Hi there! Nice to chat with you.",
    "how are you": "I'm a chatbot, so I don't have feelings, but I'm working perfectly!",
    "name": "I am a simple Python chatbot.",
    "thanks": "You're welcome!",
    "thank you": "My pleasure.",
    "help": "I can try to answer basic questions or just chat. What's on your mind?",
    "bye": "Goodbye! Have a great day!",
    "see ya": "See you later! Come back anytime.",
    
    "calculate": "Yeah, I can help you in calculation!",
    "sum": "Okay, let's calculate a sum!",
    "add": "Alright, tell me the numbers you want to add.",
    
    "area": "Yes, I can help you in finding Area.",
    "square": "Sure, I can find the area of a square!",
    "area of square": "Okay, for a square, I need the side length.",
    "area of circle": "Okay, for a circle, I need the radius.",
    "circle area": "What's the radius of the circle?",
    "area of rectangle": "For a rectangle, I'll need its length and width.",
    "rectangle area": "Please provide the length and width for the rectangle."
}

def get_bot_response(user_message, responses_dict):
    cleaned_input = user_message.lower().strip()
    matched_keywords = [k for k in responses_dict.keys() if k in cleaned_input]
    matched_keywords.sort(key=len, reverse=True)

    if any(k in ['area of circle', 'circle area'] for k in matched_keywords):
        print(f"Chatbot: {responses_dict.get('area of circle', 'Okay, let\'s calculate the area of a circle!')}")
        return area_of_circle()

    elif any(k in ['area of rectangle', 'rectangle area'] for k in matched_keywords):
        print(f"Chatbot: {responses_dict.get('area of rectangle', 'Okay, let\'s calculate the area of a rectangle!')}")
        return area_of_rectangle()

    elif any(k in ['area', 'square', 'area of square'] for k in matched_keywords):
        if 'square' in matched_keywords or 'area of square' in matched_keywords:
            print(f"Chatbot: {responses_dict.get('area of square', 'Okay, let\'s find the area of a square!')}")
            return area_of_square()
        else:
            print(f"Chatbot: {responses_dict.get('area', 'Okay, let\'s find an area!')}")
            return "Which shape's area would you like to calculate (e.g., square, circle, rectangle)?"

    elif any(k in ['sum', 'add', 'calculate'] for k in matched_keywords):
        print(f"Chatbot: {responses_dict.get('calculate', 'Okay, let\'s calculate a sum!')}")
        return addition()

    elif matched_keywords:
        return responses_dict[matched_keywords[0]]
    
    return "I'm not sure how to respond to that. Can you rephrase or ask something else?"

def addition():
    user_input = input("Enter the numbers separated by '+': ")
    user_input = user_input.strip()

    if "+" in user_input:
        parts = user_input.split("+")
        total_sum = 0

        for part in parts:
            try:
                total_sum += int(part.strip())
            except ValueError:
                return f"Error: '{part}' is not a valid number. Please enter only numbers separated by '+'."
            except Exception as e:
                return f"An unexpected error occurred during calculation: {e}"

        return f"The sum is: {total_sum}"
    else:
        try:
            return f"The number is: {int(user_input)}"
        except ValueError:
            return "Error: Please enter a single number or numbers separated by a '+' sign."

def area_of_square():
    try:
        user_input_str = input("Enter the length of the side: ")
        side_length = float(user_input_str.strip())
        
        if side_length < 0:
            return "Error: Side length cannot be negative. Please enter a positive number."
            
        return f"The area of the square is: {side_length**2:.2f}"
    except ValueError:
        return "Error: Invalid input. Please enter a valid number for the side length."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def area_of_circle():
    try:
        user_input_str = input("Enter the radius of the circle: ")
        radius = float(user_input_str.strip())
        
        if radius < 0:
            return "Error: Radius cannot be negative. Please enter a positive number."
            
        area = math.pi * (radius ** 2)
        return f"The area of the circle is: {area:.2f}"
    except ValueError:
        return "Error: Invalid input. Please enter a valid number for the radius."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def area_of_rectangle():
    try:
        length_str = input("Enter the length of the rectangle: ")
        length = float(length_str.strip())

        width_str = input("Enter the width of the rectangle: ")
        width = float(width_str.strip())
        
        if length < 0 or width < 0:
            return "Error: Length and width cannot be negative. Please enter positive numbers."
            
        area = length * width
        return f"The area of the rectangle is: {area:.2f}"
    except ValueError:
        return "Error: Invalid input. Please enter valid numbers for length and width."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def greet_user():
    print("--- Welcome to the Simple Chatbot! ---")
    print("Type 'quit' or 'exit' anytime to end the conversation.")
    print("I can chat, sum/add/calculate numbers, or find the area of a square, circle, or rectangle!")
    print("-------------------------------------")

Chatbot_active = True
greet_user()

while Chatbot_active:
    user_input = input("You: ")

    cleaned_input_for_quit = user_input.lower().strip()

    if cleaned_input_for_quit == "quit" or cleaned_input_for_quit == "exit":
        print("Chatbot: Goodbye! Thanks for chatting.")
        Chatbot_active = False
    else:
        bot_answer = get_bot_response(user_input, chatbot_response)
        print(f"Chatbot: {bot_answer}")