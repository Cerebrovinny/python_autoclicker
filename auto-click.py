# import pynput
# import time
# import threading
# from pynput.mouse import Button, Controller
# from pynput.keyboard import Listener, KeyCode
from pynput import keyboard

delay = 0.001
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

print("RODANDOOOOOOO")

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

# class ClickMouse(threading.Thread):
#     def __init__(self, delay, button):
#         super().__init__()
#         self.delay = delay
#         self.button = button
#         self.running = False
#         self.program_running = True
    
#     def start_clicking(self):
#         self.running = True
    
#     def stop_clicking(self):
#         self.running = False
    
#     def exit(self):
#         self.stop_clicking()
#         self.program_running = False
    
#     def run(self):
#         while self.program_running:
#             while self.running:
#                 mouse.click(self.button)
#                 time.sleep(self.delay)

# mouse = Controller()
# click_thread = ClickMouse(delay, button)
# click_thread.start()

# def on_press(key):
#     if key == start_stop_key:
#         if click_thread.running:
#             click_thread.stop_clicking()
#         else:
#             click_thread.start_clicking()
#             print(key)
#     elif key == exit_key:
#         click_thread.exit()
#         listener.stop()
