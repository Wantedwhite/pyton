import pyautogui
import time

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('https://tucujudeouro.com.br/votacao/')
pyautogui.press('enter')
time.sleep(2)
x = 819
y = 198

pyautogui.click(x, y)

