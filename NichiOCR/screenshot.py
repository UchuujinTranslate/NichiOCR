import win32gui
import io
from PIL import ImageGrab
from rich.console import Console

console = Console()


def screenshot():
    console.log("Screenshotting now!")

    toplist, winlist = [], []

    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
    win32gui.EnumWindows(enum_cb, toplist)

    ppsspp = [(hwnd, title) for hwnd, title
              in winlist if 'ppsspp' in title.lower()]
    # just grab the hwnd for first window matching ppsspp
    ppsspp = ppsspp[0]
    hwnd = ppsspp[0]

    win32gui.SetForegroundWindow(hwnd)
    bbox = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(bbox)

    # Cropping to only text box
    w, h = img.size
    console.log("Screenshot size: " + str(img.size))
    # dimensions with 2x window size
    # img = img.crop((120, 435, w-120, h-27))

    # math for any window size?
    img = img.crop((10, h/1.38, w-10, h/1.045))
    img.show()
    # print(type(img))

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return img_byte_arr
