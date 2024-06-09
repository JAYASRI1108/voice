import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

# Mock database
db = {
    '123': 'Token 001',
    '456': 'Token 002',
    # Add more roll number to token mappings here
}

# Function to recognize speech and retrieve token
def recognize_speech():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Say your roll number:")
            audio = recognizer.listen(source)
            roll_number = recognizer.recognize_google(audio)
            print("You said: " + roll_number)
            return roll_number
    except sr.UnknownValueError:
        messagebox.showerror("Error", "Could not understand audio")
    except sr.RequestError as e:
        messagebox.showerror("Error", f"Could not request results; {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    return None

# Function to get token for recognized roll number
def get_token():
    roll_number = recognize_speech()
    if roll_number:
        token = db.get(roll_number)
        if token:
            token_label.config(text=f"Token: {token}")
        else:
            messagebox.showerror("Error", "Roll number not found")

# Set up Tkinter GUI
root = tk.Tk()
root.title("Mobile Phone Token System")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

title_label = tk.Label(frame, text="Mobile Phone Token System", font=("Helvetica", 16))
title_label.pack(pady=10)

instruction_label = tk.Label(frame, text="Click the button and say your roll number:")
instruction_label.pack(pady=10)

token_label = tk.Label(frame, text="Token: ", font=("Helvetica", 14))
token_label.pack(pady=10)

speak_button = tk.Button(frame, text="Speak", command=get_token, font=("Helvetica", 14))
speak_button.pack(pady=20)

root.mainloop()
