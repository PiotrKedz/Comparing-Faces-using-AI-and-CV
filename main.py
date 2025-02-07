import cv2 as cv
from verifier import verify
from IDinfo import extract_text
from uploadImage import choose_photo_path

def main(models):  # Accept models as an argument
    # Load the ID front and back images
    id_front = cv.imread(choose_photo_path("Choose a picture of ID front, it should be on black background"))
    id_back = cv.imread(choose_photo_path("Choose a picture of ID back, it should be on black background"))

    # Load the selfie image
    selfie = cv.imread(choose_photo_path("Choose your selfie"))

    # Save the ID front, ID back, and selfie images without cropping
    cv.imwrite("ID_front.png", id_front)
    cv.imwrite("ID_back.png", id_back)
    cv.imwrite("selfie.png", selfie)

    # Extract and save text from ID images
    with open("ID_front_info.txt", "w", encoding="utf-8") as file:
        file.write(extract_text(id_front))
    with open("ID_back_info.txt", "w", encoding="utf-8") as file:
        file.write(extract_text(id_back))

    # Verify the ID front image against the selfie (DeepFace will handle alignment)
    verify(id_front, selfie, models)  # Pass models as an argument

if __name__ == "__main__":
    models = ["VGG-Face", "Facenet", "Facenet512"]  # Default models, in case no models are selected
    main(models)
