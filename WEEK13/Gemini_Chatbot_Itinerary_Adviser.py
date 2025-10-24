import google.generativeai as genai
import os

# Configure Gemini API
GEMINI_API_KEY = "AIzaSyBqNUxgGEQ01DW17PqlwMCM_K1Ts08-TvY"
genai.configure(api_key=GEMINI_API_KEY)


def instructor_chatbot():
    """Command-line AI Itinerary Chatbot using Gemini API."""
    print("Welcome to AI Itinerary recommender! Answer a few questions to get personalized itinerary advice.\n")
    
    days = input("How many (days): ")
    location = input("Where is the destination (city name): ")
    age = input("Enter your age: ")
    
    # Original detailed prompt without token limitations
    prompt = f"""
    You are a professional tourist recommender. Provide an itinerary recommendation based on user data.
    
    User Details:
    - days: {days} days
    - destination: {location} city
    - Age: {age} years
    
    Based on your personal information, 
    Then, give a structured itinerary with a name of the place, address and short description for each day separately in order with maximum three activities in a day.
    """
    
    try:
        # Initialize Gemini model
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Generate response without token limitation
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.6,
                top_p=0.9,
                max_output_tokens=2500,
            )
        )
        
        print("\n My Name is Hadi as AI Itinerary expert:")
        print(response.text)
        
    except Exception as e:
        print("Error communicating with Gemini API:", e)

if __name__ == "__main__":
    instructor_chatbot()