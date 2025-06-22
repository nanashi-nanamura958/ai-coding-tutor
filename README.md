# AI Coding Tutor

AI Coding Tutor is a simple Streamlit app that acts as your personal coding assistant. You describe a coding problem, and the app generates:
- An efficient solution in your chosen programming language
- A clear step-by-step explanation
- Time and space complexity analysis
- Example inputs and outputs
- Edge cases to consider

## How to Run

1. Clone this repository:
git clone https://github.com/nanashi-nanamura958/ai-coding-tutor.git
cd ai-coding-tutor

markdown
Copy
Edit

2. Install required dependencies:
pip install streamlit openai

mathematica
Copy
Edit
(Or install other libraries depending on the API provider you use.)

3. Run the app:
streamlit run api2.py

markdown
Copy
Edit

4. Open the app in your browser, enter your API key, describe your problem, and get a solution.

## Features

- Supports Python, JavaScript, Java, C++, and Go
- Beginner, Intermediate, or Advanced explanation levels
- Adjustable creativity (temperature) setting
- Displays time/space complexity, examples, and edge cases

## Requirements

- Python 3.7 or higher
- Streamlit
- OpenAI SDK or compatible API client (e.g., requests for Together AI)

## Notes

- You need a valid API key (OpenAI, Together AI, etc.).
- Free API tiers may have usage limits.
- Make sure you select a model that your account has access to.

## License

This project is free to use and modify for educational purposes.