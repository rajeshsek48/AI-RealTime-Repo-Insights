import openai
import os

# Set your OpenAI API key
openai.api_key = 'your_openai_api_key'  # Replace with your OpenAI API key

def analyze_code(file_path):
    # Open the file and read the code
    with open(file_path, 'r') as file:
        code = file.read()

    # Use OpenAI to analyze the code
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Analyze the following Python code and suggest improvements:\n\n{code}",
        max_tokens=150
    )

    # Print the AI's analysis and suggestions
    print("AI Analysis:")
    print(response.choices[0].text.strip())

if __name__ == "__main__":
    # Specify the path to the code you want to analyze (e.g., buggy_code.py)
    analyze_code('buggy_code.py')
