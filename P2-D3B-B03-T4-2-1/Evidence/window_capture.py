import ctypes, sys
from ctypes import wintypes
from PIL import ImageGrab

pid = int(sys.argv[1]); out = sys.argv[2]
user32 = ctypes.windll.user32
found = []

WNDENUMPROC = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

def enum_cb(hwnd, _):
    p = wintypes.DWORD()
    user32.GetWindowThreadProcessId(hwnd, ctypes.byref(p))
    if p.value == pid and user32.IsWindowVisible(hwnd):
        n = user32.GetWindowTextLengthW(hwnd)
        if n > 0:
            buf = ctypes.create_unicode_buffer(n + 1)
            user32.GetWindowTextW(hwnd, buf, n + 1)
            found.append((hwnd, buf.value))
    return True

user32.EnumWindows(WNDENUMPROC(enum_cb), 0)
if not found:
    print("SCREENSHOT=NO_WINDOW")
    sys.exit(2)

hwnd, title = found[0]
class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_long), ("top", ctypes.c_long), ("right", ctypes.c_long), ("bottom", ctypes.c_long)]
r = RECT()
user32.GetWindowRect(hwnd, ctypes.byref(r))
w, h = r.right - r.left, r.bottom - r.top
if w <= 0 or h <= 0:
    print("SCREENSHOT=INVALID_RECT")
    sys.exit(3)
img = ImageGrab.grab(bbox=(r.left, r.top, r.right, r.bottom))
img.save(out)
print(f"SCREENSHOT={out} {w}x{h} TITLE={title}")
