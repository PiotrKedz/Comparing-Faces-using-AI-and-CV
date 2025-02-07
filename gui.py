import customtkinter as ctk
from main import main
import sys  # To explicitly exit the program
from tkinter import messagebox  # For displaying error messages

# Global variable to store selected models
selected_models = []

def on_closing():
    # Exit the program when the window is closed
    sys.exit()

def view_id_info():
    # Read the contents of both ID_back_info.txt and ID_front_info.txt
    try:
        with open("ID_back_info.txt", "r", encoding="utf-8") as back_file:
            back_content = back_file.read()
    except FileNotFoundError:
        back_content = "No back info available. Please complete the verification process first."

    try:
        with open("ID_front_info.txt", "r", encoding="utf-8") as front_file:
            front_content = front_file.read()
    except FileNotFoundError:
        front_content = "No front info available. Please complete the verification process first."

    # Create a new window to display the contents
    info_window = ctk.CTkToplevel()
    info_window.title("ID Information")
    info_window.geometry("600x400")

    # Textbox for ID front info
    front_label = ctk.CTkLabel(info_window, text="ID Front Information:", font=("Helvetica", 12))
    front_label.pack(pady=(10, 5))

    front_text_box = ctk.CTkTextbox(info_window, width=560, height=150)
    front_text_box.insert("0.0", front_content)
    front_text_box.configure(state="disabled")  # Make the textbox read-only
    front_text_box.pack(pady=5)

    # Textbox for ID back info
    back_label = ctk.CTkLabel(info_window, text="ID Back Information:", font=("Helvetica", 12))
    back_label.pack(pady=(10, 5))

    back_text_box = ctk.CTkTextbox(info_window, width=560, height=150)
    back_text_box.insert("0.0", back_content)
    back_text_box.configure(state="disabled")  # Make the textbox read-only
    back_text_box.pack(pady=5)

    # Button to close the info window
    close_button = ctk.CTkButton(info_window, text="Close", command=info_window.destroy)
    close_button.pack(pady=10)

def save_model_preferences():
    # Save the selected models to the global variable
    global selected_models
    selected_models = []

    if vgg_var.get():
        selected_models.append("VGG-Face")
    if facenet_var.get():
        selected_models.append("Facenet")
    if facenet512_var.get():
        selected_models.append("Facenet512")
    if openface_var.get():
        selected_models.append("OpenFace")
    if deepface_var.get():
        selected_models.append("DeepFace")
    if arcface_var.get():
        selected_models.append("ArcFace")

    print(f"Saved models: {selected_models}")  # Print to check saved models

def choose_photos_and_verify():
    if not selected_models:
        # Display an error message if no models are selected
        messagebox.showerror("No Models Selected", "Please select at least one model for verification.")
    else:
        # Proceed with the main function using the selected models
        main(selected_models)

def create_main_window():
    # Initialize the main window
    ctk.set_appearance_mode("Dark")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme("green")  # Themes: "blue" (default), "green", "dark-blue"

    window = ctk.CTk()
    window.title("Photo Verification App")
    window.geometry("300x500")  # Adjusted window size to fit all buttons and checkboxes

    # Handle window close event
    window.protocol("WM_DELETE_WINDOW", on_closing)

    # Create a label
    label = ctk.CTkLabel(window, text="Photo Verification System", font=("Helvetica", 16))
    label.pack(pady=20)

    # Button to choose photos and start verification
    choose_photos_button = ctk.CTkButton(window, text="Choose Photos & Verify", command=choose_photos_and_verify)
    choose_photos_button.pack(pady=10)

    # Button to view ID Information (both front and back)
    view_info_button = ctk.CTkButton(window, text="View ID Info", command=view_id_info)
    view_info_button.pack(pady=10)

    # Add a label for model selection
    model_label = ctk.CTkLabel(window, text="Choose DeepFace Models:", font=("Helvetica", 12))
    model_label.pack(pady=10)

    # Define variables for checkboxes
    global vgg_var, facenet_var, facenet512_var, openface_var, deepface_var, arcface_var
    vgg_var = ctk.BooleanVar()
    facenet_var = ctk.BooleanVar()
    facenet512_var = ctk.BooleanVar()
    openface_var = ctk.BooleanVar()
    deepface_var = ctk.BooleanVar()
    arcface_var = ctk.BooleanVar()

    # Checkboxes for each model
    vgg_checkbox = ctk.CTkCheckBox(window, text="VGG-Face", variable=vgg_var)
    vgg_checkbox.pack(pady=5)

    facenet_checkbox = ctk.CTkCheckBox(window, text="Facenet", variable=facenet_var)
    facenet_checkbox.pack(pady=5)

    facenet512_checkbox = ctk.CTkCheckBox(window, text="Facenet512", variable=facenet512_var)
    facenet512_checkbox.pack(pady=5)

    openface_checkbox = ctk.CTkCheckBox(window, text="OpenFace", variable=openface_var)
    openface_checkbox.pack(pady=5)

    deepface_checkbox = ctk.CTkCheckBox(window, text="DeepFace", variable=deepface_var)
    deepface_checkbox.pack(pady=5)

    arcface_checkbox = ctk.CTkCheckBox(window, text="ArcFace", variable=arcface_var)
    arcface_checkbox.pack(pady=5)

    # Button to save the model preferences
    save_model_button = ctk.CTkButton(window, text="Save Model Preferences", command=save_model_preferences)
    save_model_button.pack(pady=10)

    # Start the GUI event loop
    window.mainloop()

if __name__ == "__main__":
    create_main_window()
