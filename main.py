# Setup
import keyboard
from rich.console import Console


# Import helper scripts
from NichiOCR import *

# from NichiOCR.screenshot import screenshot
# from NichiOCR.json_handling import load_all_json
# from NichiOCR.ocr import init_OCR, process_ocr
# from NichiOCR.string_compare import compare, compare_results
# from NichiOCR.results_table import results_table



# Setup 
console = Console()

reader = init_OCR()
entireScript = load_all_json()
console.log(f"All ready!")

# Main loop
def lookup():
    img_byte_arr = screenshot()


    OCRoutput = process_ocr(reader, img_byte_arr)
    OCRspeaker, OCRstring = split_ocr(OCRoutput)

    highestRatio, results = compare(OCRspeaker, OCRstring, entireScript)
    results = compare_results(highestRatio, entireScript, results)

    results_table(results)
    


keyboard.add_hotkey('ctrl+shift', lookup)

console.log("")
console.log("Press CTRL+SHIFT to take a screenshot of PPSSPP and lookup the dialog.")
console.log("Press ESC at any time to exit.")

keyboard.wait('esc')
