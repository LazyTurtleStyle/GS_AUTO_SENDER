"""
Script Name: GS_AUTO_SENDER.py
Version: 1.3
Author: Lazyturtle
"""

# import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import sys

# Correct path to ChromeDriver executable
chromedriver_path = r"/path/to/chromedriver"   #<-----------------------------------------PUT PATH HERE"

# Initialize the service object with the path to ChromeDriver
service = Service(chromedriver_path)

# Set up the options for Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Start the browser maximized

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open a website
driver.get("https://www.tribalwars.nl")

def countdown(seconds, message):
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\r{message} {i} seconds... ")
        sys.stdout.flush()
        time.sleep(1)
    print("\nProceeding with the next steps...")

def login(driver, username, password, username_xpath, password_xpath):
    try:
        # Wait until the username field is clickable
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, username_xpath))
        ).click()

        # Type the username
        username_field = driver.find_element(By.XPATH, username_xpath)
        username_field.send_keys(username)
        
        # Click on the password field
        password_field = driver.find_element(By.XPATH, password_xpath)
        password_field.click()
        
        # Type the password
        password_field.send_keys(password)
        
        # Submit the form (assuming pressing Enter will submit)
        password_field.send_keys(Keys.RETURN)
        
    except Exception as e:
        print(f"An error occurred: {e}")

def setup_game(driver):
    # Gives you 15 seconds to complete the Captcha. You can make this longer if you need more time.
    countdown(15, "Please complete the Captcha in")

    # Select the world
    try:
        wereld = driver.find_element(By.XPATH, "//div[@class='worlds-container'][1]//a[@class='world-select']/span[contains(text(), 'Wereld')]")
        wereld.click()
    except Exception as e:
        print(f"An error occurred while selecting the world: {e}")
        return

    # A sleep timer so you can pick the right group to send GS from. 
    countdown(10, "Please pick the right group to send GS from in")

    # Click on the first village menu.
    try:
        Village = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html[@class=' js flexbox history draganddrop borderimage textshadow cssanimations localstorage sessionstorage filereader json performance']/body[@id='ds_body']/table[@id='main_layout']/tbody/tr[@class='shadedBG']/td[@class='maincell']/table[@id='header_info']/tbody/tr/td[@class='topAlign'][1]/table[@class='header-border']/tbody/tr[1]/td/table[@class='box menu nowrap']/tbody/tr[@id='menu_row2']/td[@id='menu_row2_village']/a[@class='nowrap tooltip-delayed']"))
        )
        Village.click()
    except Exception as e:
        print(f"An error occurred while clicking on the first village menu: {e}")
        return

    # Wait 2 seconds to load.
    time.sleep(2)

    # Making sure to go to the marketplace before starting the script.
    actions = ActionChains(driver)
    actions.send_keys("7")  # Make sure the tribalwarsscript is on the 7 hotkey!
    actions.perform()

    # Wait 2 seconds to load.
    time.sleep(2)

# Function to repeat sending process.
def perform_actions():
    # Create an ActionChains object
    actions = ActionChains(driver)
    
    # Simulate pressing the "7" key
    actions.send_keys("7")  # Make sure the tribalwarsscript is on the 7 hotkey!
    actions.perform()
    
    # Wait for 0.3 - 0.8 seconds 
    sleep_duration1 = random.uniform(0.3, 0.8)
    time.sleep(sleep_duration1)
    
    # Simulate pressing the Enter key
    actions.reset_actions()
    actions.send_keys(Keys.ENTER)
    actions.perform()
    
    # Wait for 0.5 - 0.9 seconds 
    sleep_duration2 = random.uniform(0.5, 0.9)
    time.sleep(sleep_duration2)
    
    # Simulate pressing the "d" key
    actions.reset_actions()
    actions.send_keys("d")  # Make sure you use the 'd' key to switch to the next village!
    actions.perform()

# XPaths for the content borders
username_xpath = '//*[@id="user"]'
password_xpath = '//*[@id="password"]'

# Account credentials
username = 'Username'  #<-----------------------------------------PUT USERNAME HERE 
password = 'Password'  #<-----------------------------------------PUT PASSWORD HERE 

# Call the login function
login(driver, username, password, username_xpath, password_xpath)

# Setup the game environment
setup_game(driver)

while True:
    # Get the current URL
    current_url = driver.current_url
    sleep_duration3 = random.uniform(0.8, 1.2)
    
    # Check if the current URL matches the stop condition
    if "screen=market&action=send" in current_url:
        # Perform refresh action (F5)
        driver.refresh()
        print("Refreshed the page.")
        # Optional: You can add a delay here if needed before restarting the loop
        time.sleep(sleep_duration3)  # Example delay of 0.8 - 1.2 seconds
        
    else:
        # Perform the sequence of actions
        perform_actions()
        # Optionally, add a longer break between iterations
        time.sleep(sleep_duration3)  # Wait for 0.8 - 1.2 seconds between each iteration

# Quit the driver when done
driver.quit()
