# Comparing-Faces-using-AI-and-CV

This is a photo verification system using DeepFace and CustomTkinter for ID and selfie verification. It allows users to select photos, extract text from ID images, and compare selfies using multiple DeepFace models.

Features:

GUI interface with CustomTkinter
Face alignment and detection using DeepFace
Multi-model selection (VGG-Face, Facenet, Facenet512, etc.)
Real-time results popup for verification outcomes
Error handling for missing inputs and failed detections

How to Use:

1. Download all Python files and store them in a single project folder for simplicity.
2. Install Tesseract-OCR.
3. Run gui.py.
4. Select your DeepFace models for verification and save your preferences.
5. Choose ID front, back, and a selfie.
6. View the extracted ID information and verification results.

File Structure:

1. uploadImage.py → Handles image selection
2. IDinfo.py → Extracts text data from ID images
3. verifier.py → Handles face verification
4. processPicture.py → Contains face alignment functions
5. main.py → Manages the overall workflow
6. gui.py → Implements the GUI

Notes:

1. Multiple factors influence the final verification result (e.g., image angle, sharpness, brightness, background, etc.).
2. DeepFace supports multiple face detection backends.
3. Pytesseract supports multiple languages for text extraction.
Versions Used:

Python → 3.8
CustomTkinter → 5.2.2
DeepFace → 0.0.93
OpenCV-Python → 4.10.0.84
Pytesseract → 0.3.13
![gui](https://github.com/user-attachments/assets/841fa8fc-a4b6-45a7-b639-424c121e4503)
![result](https://github.com/user-attachments/assets/0d84d156-ad7e-484d-b2ad-75aeb50e7519)
