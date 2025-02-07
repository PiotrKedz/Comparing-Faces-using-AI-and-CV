# Comparing-Faces-using-AI-and-CV

This is a photo verification system using DeepFace and CustomTkinter, designed for ID and selfie verification. It allows users to choose photos, extract text from ID images, and compare selfies using multiple DeepFace models.

Features:
GUI Interface with CustomTkinter, 
Face Alignment & Detection using DeepFace, 
Multi-Model Selection (VGG-Face, Facenet, Facenet512, etc.), 
Real-time Results Popup for verification outcomes, 
Error Handling for missing inputs and failed detections, 

How to use:
1. Download all python files and store them in one project for simplicity
2. Install tesseract-OCR
3. run gui.py
4. Select you Deepface models for verification and save your preferences
5. Choose ID front, back and a selfie
6. Then you can view ID info & verification results

File structure:
1. uploadImage.py --> handles the image selection
2. IDinfo --> extracts text data from ID images
3. verifier.py --> handles face verification
4. processPicture.py --> Face alignment functions
5. main.py --> responsible for all work flow
6. gui.py --> just GUI

Notes:
1. Many factors comes into play in case of determining the final result (angle of image, sharpness of image, brightnes, background, etc.)
2. Deepface suppots multiple face detection backends
3. Pytesseract support many languages in extracting text data

Versions used for this project:
python --> 3.8
customtkinter --> 5.2.2
deepface --> 0.0.93
opencv-python --> 4.10.0.84
pytesseract --> 0.3.13
