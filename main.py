# Setup
import keyboard

# Import helper scripts
from NichiOCR.screenshot import screenshot
from NichiOCR.json_handling import load_all_json
from NichiOCR.ocr import init_OCR, process_ocr
from NichiOCR.string_compare import compare, compare_results


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