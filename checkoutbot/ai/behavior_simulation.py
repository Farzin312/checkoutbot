import time
import random

def simulate_mouse_movement(driver, element):
    """
    Simulates human-like mouse movements to an element.
    
    Args:
        driver (webdriver): The Selenium WebDriver instance.
        element (WebElement): The target element to move the mouse to.
    """
    actions = webdriver.ActionChains(driver)
    actions.move_to_element(element)
    
    # Add random small movements
    for _ in range(5):
        actions.move_by_offset(random.randint(-10, 10), random.randint(-10, 10))
        actions.perform()
        time.sleep(random.uniform(0.1, 0.3))
    
    actions.move_to_element(element).perform()

def simulate_typing(element, text):
    """
    Simulates human-like typing in an input field.
    
    Args:
        element (WebElement): The input field element.
        text (str): The text to type.
    """
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.2))

# Add more behavior simulation functions as needed
