import time
import pyperclip
import os

target_dir = r"C:\Users\terry\OneDrive\Desktop"
print("Clipboard listener active. Copy code blocks starting with #FILE: to auto-route...")

last_text = ""
while True:
    try:
        current_text = pyperclip.paste()
        if current_text != last_text:
            last_text = current_text
            if current_text.startswith("#FILE:"):
                lines = current_text.splitlines()
                filename = lines[0].replace("#FILE:", "").strip()
                content = "\n".join(lines[1:])
                filepath = os.path.join(target_dir, filename)
                os.makedirs(os.path.dirname(filepath), exist_ok=True)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"[Auto-Routed] Saved to {filepath}")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(1)
