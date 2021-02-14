# Setup
import keyboard
from rich.console import Console


# Import helper scripts
from NichiOCR.screenshot import screenshot
from NichiOCR.json_handling import load_all_json
from NichiOCR.ocr import init_OCR, process_ocr
from NichiOCR.string_compare import compare, compare_results


# Setup 
console = Console()

reader = init_OCR()
entireScript = load_all_json()
console.log(f"All ready!")

# Main loop
def lookup():
    img_byte_arr = screenshot()
    OCRoutput = process_ocr(reader, img_byte_arr)

    highestRatio = compare(OCRoutput, entireScript)
    compare_results(highestRatio, entireScript)


keyboard.add_hotkey('ctrl+1', lookup)

print("")
print("Press CTRL+1 to take a screenshot of PPSSPP and lookup the dialog.")
print("Press ESC at any time to exit.")

keyboard.wait('esc')