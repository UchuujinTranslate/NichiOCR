import easyocr

def init_OCR():
    # Initialize OCR model
    print("Loading...")
    reader = easyocr.Reader(['ja', 'en'])
    print("OCR Model Ready!")
    
    return reader

def process_ocr(reader, img_byte_arr):
    print("Processing OCR...")
    OCRoutput = reader.readtext(img_byte_arr, detail = 0)

    print("OCR Output:")
    print(OCRoutput)

    return OCRoutput