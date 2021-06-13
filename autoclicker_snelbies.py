from pynput.mouse import Button, Controller
import keyboard

mouse = Controller()
mouse.position = (64, 822)

c3 = 0

mouse.press(Button.left)
while True:
    mouse.move(1, 0)
    c3 += 1
    if c3 > 1850:
        c3 = 0
        mouse.move(-1919, -1080)
        mouse.move(64, 822)
    if keyboard.is_pressed('f1'):
        break
