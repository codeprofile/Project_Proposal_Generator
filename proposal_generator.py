import tkinter as tk
from tkinter import scrolledtext
import openai

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUR_API_KEY'


# Function to generate proposal using GPT-3 API
def generate_proposal():
    input_text = input_text_widget.get("1.0", "end-1c")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_text,
        max_tokens=300,
        api_key=api_key,
    )
    generated_content = response.choices[0].text
    output_text_widget.delete("1.0", "end")
    output_text_widget.insert("1.0", generated_content)


if __name__ == "__main__":
    # Create the main window
    window = tk.Tk()
    window.title("Project Proposal Generator")

    # Create input text area
    input_label = tk.Label(window, text="Project Description:")
    input_label.pack()
    input_text_widget = scrolledtext.ScrolledText(window, width=40, height=10)
    input_text_widget.pack()

    # Create a button to generate the proposal
    generate_button = tk.Button(window, text="Generate Proposal", command=generate_proposal)
    generate_button.pack()

    # Create output text area
    output_label = tk.Label(window, text="Generated Proposal:")
    output_label.pack()
    output_text_widget = scrolledtext.ScrolledText(window, width=40, height=10)
    output_text_widget.pack()

    # Start the GUI event loop
    window.mainloop()
