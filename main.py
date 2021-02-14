# Setup
import keyboard

# Import helper scripts
from NichiOCR.screenshot import *
from NichiOCR.json_handling import *
from NichiOCR.ocr import *
from NichiOCR.string_compare import *


# Setup
reader = init_OCR()
entireScript = load_all_json()
print("Ready!")

# Main loop
def lookup():
    img_byte_arr = screenshot()
    OCRoutput = process_ocr(reader, img_byte_arr)

    highestRatio = compare(OCRoutput, entireScript)
    compare_results(highestRatio, entireScript)


keyboard.add_hotkey('ctrl+1', lookup)
print("Press ESC to exit.")
keyboard.wait('esc')