import ctypes, sys, time
from ctypes import wintypes
from PIL import ImageGrab

u = ctypes.windll.user32
WNDENUMPROC = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_long), ("top", ctypes.c_long), ("right", ctypes.c_long), ("bottom", ctypes.c_long)]

def windows(pid=None):
    out = []
    def cb(hwnd, _):
        p = wintypes.DWORD()
        u.GetWindowThreadProcessId(hwnd, ctypes.byref(p))
        if pid is None or p.value == pid:
            n = u.GetWindowTextLengthW(hwnd)
            if n > 0 and u.IsWindowVisible(hwnd):
                buf = ctypes.create_unicode_buffer(n + 1)
                u.GetWindowTextW(hwnd, buf, n + 1)
                out.append((hwnd, p.value, buf.value))
        return True
    u.EnumWindows(WNDENUMPROC(cb), 0)
    return out

def main_window(pid):
    ws = windows(pid)
    return ws[0] if ws else (None, None, None)

def rect(hwnd):
    r = RECT(); u.GetWindowRect(hwnd, ctypes.byref(r)); return r

cmd = sys.argv[1]
if cmd == "list":
    for h,p,t in windows(int(sys.argv[2]) if len(sys.argv)>2 else None):
        print(f"{h}\t{p}\t{t}")
elif cmd == "capture":
    pid = int(sys.argv[2]); out = sys.argv[3]
    h,p,t = main_window(pid)
    if not h: print("NO_WINDOW"); sys.exit(2)
    r = rect(h); w,h2 = r.right-r.left, r.bottom-r.top
    img = ImageGrab.grab(bbox=(r.left,r.top,r.right,r.bottom))
    img.save(out)
    print(f"CAPTURED\t{out}\t{w}x{h2}\t{t}\trect={r.left},{r.top},{r.right},{r.bottom}")
elif cmd == "activate":
    pid = int(sys.argv[2]); h,_,t = main_window(pid)
    if not h: print("NO_WINDOW"); sys.exit(2)
    u.ShowWindow(h, 9); u.SetForegroundWindow(h); time.sleep(0.3)
    print(f"ACTIVATED\t{h}\t{t}")
elif cmd == "click":
    x,y = int(sys.argv[2]), int(sys.argv[3])
    u.SetCursorPos(x,y); time.sleep(0.15); u.mouse_event(0x0002,0,0,0,0); u.mouse_event(0x0004,0,0,0,0)
    print(f"CLICKED\t{x},{y}")
elif cmd == "key":
    for code in sys.argv[2:]:
        vk = int(code)
        u.keybd_event(vk,0,0,0); u.keybd_event(vk,0,0x0002,0); time.sleep(0.08)
    print("KEY_SENT\t" + ",".join(sys.argv[2:]))
elif cmd == "rect":
    pid=int(sys.argv[2]); h,_,t=main_window(pid); r=rect(h)
    print(f"RECT\t{r.left},{r.top},{r.right},{r.bottom}\t{t}")
else:
    print("UNKNOWN_COMMAND")
