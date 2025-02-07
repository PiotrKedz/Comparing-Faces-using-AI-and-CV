import cv2 as cv
from deepface import DeepFace
from processPicture import align_face
import customtkinter as ctk  # Import for creating popups

def show_results_popup(model, results):
    """Displays the verification results in a popup window."""
    # Filter out unnecessary keys from results
    filtered_results = {key: value for key, value in results.items() if key not in ['detector_backend', 'similarity_metric', 'facial_areas']}

    result_window = ctk.CTkToplevel()
    result_window.title(f"Results for {model}")
    result_window.geometry("400x300")

    result_label = ctk.CTkLabel(result_window, text=f"Verification Results for {model}", font=("Helvetica", 14))
    result_label.pack(pady=10)

    # Display each filtered result in the popup
    result_text = "\n".join([f"{key}: {value}" for key, value in filtered_results.items()])
    result_textbox = ctk.CTkTextbox(result_window, width=360, height=200)
    result_textbox.insert("0.0", result_text)
    result_textbox.configure(state="disabled")  # Make the textbox read-only
    result_textbox.pack(pady=5)

def verify(img1, img2, models):
    if img1 is None or img2 is None:
        raise ValueError("One or both image paths are invalid or images could not be loaded.")

    # Extract faces using MTCNN backend
    faces_img1 = DeepFace.extract_faces(img_path=img1, detector_backend='mtcnn', enforce_detection=False)
    faces_img2 = DeepFace.extract_faces(img_path=img2, detector_backend='mtcnn', enforce_detection=False)

    if not faces_img1:
        print("No faces detected in the first image.")
        return
    if not faces_img2:
        print("No faces detected in the second image.")
        return

    # Align faces
    aligned_face1 = align_face(img1, faces_img1[0]['facial_area'])
    aligned_face2 = align_face(img2, faces_img2[0]['facial_area'])

    if aligned_face1 is None or aligned_face2 is None:
        print("Face alignment failed.")
        return

    # Normalize images
    normalized_face1 = aligned_face1 / 255.0
    normalized_face2 = aligned_face2 / 255.0

    # Display faces
    cv.imshow("Face 1", normalized_face1)
    cv.imshow("Face 2", normalized_face2)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # Convert back to 0-255 range for saving
    cv.imwrite("temp_face1.png", (normalized_face1 * 255).astype('uint8'))
    cv.imwrite("temp_face2.png", (normalized_face2 * 255).astype('uint8'))

    # Verify faces with selected models
    for model in models:
        print(f"Verifying using model: {model}")
        result = DeepFace.verify(
            img1_path="temp_face1.png",
            img2_path="temp_face2.png",
            model_name=model,
            detector_backend="mtcnn",
            enforce_detection=False
        )
        print(f"Results for model {model}:")
        for key, value in result.items():
            print(f"{key}: {value}")
        print("-" * 30)

        # Show results in a popup window
        show_results_popup(model, result)
