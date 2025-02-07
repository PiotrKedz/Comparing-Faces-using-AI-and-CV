import cv2 as cv


def normalize_image(image):
    return image / 255.0


def align_face(image, face_area):
    x = face_area.get('x', 0)
    y = face_area.get('y', 0)
    w = face_area.get('w', 0)
    h = face_area.get('h', 0)

    if w == 0 or h == 0:
        raise ValueError("Invalid face_area dimensions detected.")

    margin = int(0.2 * w)
    x1 = max(0, x - margin)
    y1 = max(0, y - margin)
    x2 = min(image.shape[1], x + w + margin)
    y2 = min(image.shape[0], y + h + margin)

    face = image[y1:y2, x1:x2]
    aligned_face = cv.resize(face, (224, 224), interpolation=cv.INTER_AREA)
    return aligned_face
