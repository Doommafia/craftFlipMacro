import time
import pyautogui

def move_mouse_for_crafting(base_x, base_y):
    final_product_x = 1015  # Adjust according to your screen layout
    final_product_y = 420  # Adjust according to your screen layout
    
    for j in range(3):
        mouse_y = base_y + j * 45
        # print(f"mouse_y = {mouse_y}\n")
        for i in range(10):
            mouse_x = base_x + i * 50
            time.sleep(0.12)
            pyautogui.moveTo(mouse_x, mouse_y)
            pyautogui.keyDown('shift')
            pyautogui.click()
            pyautogui.keyUp('shift')
            # print(f"Clicking at: {mouse_x}, {mouse_y}")
        
        time.sleep(0.24)
        pyautogui.moveTo(final_product_x, final_product_y)
        pyautogui.keyDown('shift')
        pyautogui.click()
        pyautogui.keyUp('shift')
        # print(f"Shift-clicking final product at: ({final_product_x}, {final_product_y})")

def craft_item():
    base_x = 745  # Adjust according to your screen
    base_y = 685  # Adjust according to your screen
      
    input("Press Enter to start the macro. Make sure the game window is active and ready. (You have 2 seconds)")
    time.sleep(2)
    
    move_mouse_for_crafting(base_x, base_y)

craft_item()
