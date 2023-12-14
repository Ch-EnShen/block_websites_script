import ctypes
import sys
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def running_with_admin(func, parameters):
    if is_admin():
        # Your code here, for example, modify the hosts file
        func(parameters)
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
