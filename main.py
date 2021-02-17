# Setup
import keyboard
from rich.console import Console

import NichiOCR as n

# Setup
console = Console()

reader = n.ocr.init_OCR()
entireScript = n.json_handling.load_all_json()
console.log("All ready!")


# Main loop
def lookup():
    # Take screenshot
    img_byte_arr = n.screenshot.screenshot()

    # Read Japanese with OCR
    OCRoutput = n.ocr.process_ocr(reader, img_byte_arr)
    OCRspeaker, OCRstring = n.ocr.split_ocr(OCRoutput)

    # Calculate and display results
    highestRatio, results = n.string_compare.compare(
        OCRspeaker, OCRstring, entireScript)
    results = n.string_compare.compare_results(
        highestRatio, entireScript, results)

    # Display results in a formatted table
    n.string_compare.results_table(results)


# Wait for keyboard hotkey
keyboard.add_hotkey('ctrl+shift', lookup)
console.log("")
console.log("Press CTRL+SHIFT to take a screenshot of PPSSPP\
     and lookup the dialog.")
console.log("Press ESC at any time to exit.")

# Exit
keyboard.wait('esc')
