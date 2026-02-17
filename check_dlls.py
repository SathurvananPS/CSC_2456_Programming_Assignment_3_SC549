import os
import sys
import ctypes

def check_dll(path):
    print(f"Checking: {path}")
    if not os.path.exists(path):
        print(f"  [ERROR] File does not exist: {path}")
        return
    try:
        ctypes.WinDLL(path)
        print("  [OK] DLL loaded successfully")
    except Exception as e:
        print(f"  [ERROR] Failed to load DLL: {e}")

torch_lib = r"C:\Users\Vanan\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\torch\lib"
dlls = ["c10.dll", "torch_cpu.dll", "libiomp5md.dll"]

for dll in dlls:
    check_dll(os.path.join(torch_lib, dll))
