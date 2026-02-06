# Some f-String Tricks:

from datetime import datetime

now = datetime.now()
print(f"Date formatting: {now:%B %D, %Y}")




# RAW String 
win_path = "C:\window\new_dir\test\applications"
print(win_path)
"""
some characters like \n and t\ have special meaning and hence 
would need either escaped or use a raw string.
"""
win_path = r"C:\window\new_dir\test\applications"
print(win_path)
