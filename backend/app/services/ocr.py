import numpy as np
import cv2
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="pl")

def load_image(image_input):
    if isinstance(image_input, (bytes, bytearray)):
        np_arr = np.frombuffer(image_input, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    else:
        img = cv2.imread(image_input)

    return img


def preprocess(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.equalizeHist(gray)

    gray = cv2.bilateralFilter(gray, 9, 75, 75)

    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31, 2
    )

    return thresh


def ocr_image(image_input):

    img = load_image(image_input)

    if img is None:
        return ""

    preprocessed = preprocess(img)

    preprocessed = cv2.cvtColor(preprocessed, cv2.COLOR_GRAY2BGR)

    result = ocr.ocr(preprocessed)

    if not result:
        return ""

    lines = []

    for page in result:
        for item in page:
            try:
                lines.append(item[1][0])
            except:
                continue

    return "\n".join(lines)