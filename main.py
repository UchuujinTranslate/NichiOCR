# Setup
import keyboard
from rich.console import Console

from NichiOCR.screenshot import screenshot
from NichiOCR.json_handling import load_all_json
from NichiOCR.ocr import init_OCR, process_ocr, split_ocr
from NichiOCR.string_compare import compare, compare_results
from NichiOCR.results_table import results_table

# Setup
console = Console()

reader = init_OCR()
entireScript = load_all_json()
console.log("All ready!")


# Main loop
def lookup():
    # Take screenshot
    img_byte_arr = screenshot()

    # Read Japanese with OCR
    OCRoutput = process_ocr(reader, img_byte_arr)
    OCRspeaker, OCRstring = split_ocr(OCRoutput)

    # Calculate and display results
    highestRatio, results = compare(
        OCRspeaker, OCRstring, entireScript)
    results = compare_results(
        highestRatio, entireScript, results)

    # Display results in a formatted table
    results_table(results)


# Wait for keyboard hotkey
keyboard.add_hotkey('ctrl+shift', lookup)
console.log("")
console.log("Press CTRL+SHIFT to take a screenshot of PPSSPP\
     and lookup the dialog.")
console.log("Press ESC at any time to exit.")

# Exit
keyboard.wait('esc')
