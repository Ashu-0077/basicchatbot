# basicchatbot

# Overview of The Chatbot:

# This chatbot is a console-based application designed to interact with users through text commands. It can perform several useful functions:

***Greetings and Farewells: Responds to "hello," "hi," "bye," etc.
Self-Introduction: Tells the user "who are you."
Help Functionality: Explains what it can do.
Basic Math: Can sum numbers provided by the user.
Area Calculations: Calculates the area of squares, circles, and rectangles, prompting for necessary dimensions.
Capital Information: Provides the capital city for a few predefined countries.
Robust Input Handling: Includes a get_numeric_input function to ensure valid numerical input and handles potential errors in other functions.***

**Code Structure and Highlights:**
1) INTENT_KEYWORDS: A dictionary that maps various user intents (like "greeting" or "area_circle") to a list of keywords that trigger that intent.                       This is a common and effective way to manage basic natural language understanding.
2) CHATBOT_RESPONSES: Another dictionary holding predefined responses for different intents, making it easy to manage and modify the chatbot's                             replies.
3) CAPITALS_DATA: A dictionary storing country-capital pairs, allowing the chatbot to answer capital-related queries.
                  get_numeric_input(prompt_message, error_message, allow_negative=False): A robust utility function that repeatedly asks for numeric                   input until a valid number is entered, handling ValueError and checking for negative values when not allowed. This is excellent                      for preventing crashes due to bad user input.
4) addition(): A function that can parse numbers separated by + and sum them up, or just process a single number.
5) Area Functions (area_of_square, area_of_circle, area_of_rectangle): These functions use get_numeric_input to safely collect dimensions and then                                                                          perform the relevant area calculations.
6) get_capital_info(user_message): Processes user queries about capitals by checking if known country names are present in the input.
7) get_bot_response(user_message): The core logic that determines the user's intent by checking keywords and calls the appropriate function to                                          generate a response. The order of if/elif statements here is important for correctly prioritizing intents (e.g.,                                     specific area queries before general area queries).
8) Main Loop: The while Chatbot_active: loop continuously takes user input, checks for "farewell" keywords to exit, and otherwise passes the input to get_bot_response for processing.
