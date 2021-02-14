import easyocr
from rich.console import Console

console = Console()

def init_OCR():
    with console.status("[bold green]Loading OCR Model..."):
        # Initialize OCR model
        reader = easyocr.Reader(['ja', 'en'])
        console.log(f"OCR Model ready!")
        
    
    return reader

def process_ocr(reader, img_byte_arr):
    with console.status("[bold green]Processing OCR..."):
        #console.log("Processing OCR...")
        OCRoutput = reader.readtext(img_byte_arr, detail = 0)

        console.log("OCR Output:")
        console.log(OCRoutput)

    return OCRoutput