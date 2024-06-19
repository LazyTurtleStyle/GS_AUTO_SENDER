# GS_AUTO_SENDER
No one likes going true 1000 villages to manually send GS to tribe members.

**Made for.**
Tribalwars NL server

**Requirements.**
-Python 3.12.1
-pip
-selenium
-Chromedriver

What will it do.
1. It logs in using your credentials.
2. You'll need to manually solve the CAPTCHA for now.
3. It automatically clicks on the world login button.
4. You'll have time to select the correct group (Make a group with available merchants only).
5. It initiates resource sending in a continuous loop.
6. Remember, you'll still need to solve CAPTCHAs manually. Keep an eye on the script accordingly.


Thanks to ChatGPT <3
Here's a step-by-step explanation of the script for people who don't know how to code:

Step 1: Preparation
Purpose: The script automatically opens a browser and performs specific actions on the "Tribal Wars" website.
Requirements: Python and the ChromeDriver (to automate the Chrome browser).
Step 2: Importing Required Modules
The script imports various modules needed for browser automation, such as selenium for browser automation and time for delays.
Step 3: Setting Up ChromeDriver
The script specifies the path to the ChromeDriver, which is needed to control the Chrome browser.
A ChromeDriver service is initialized, and the browser is set to start maximized.
Step 4: Opening the Website
The script opens the Tribal Wars website (https://www.tribalwars.nl) using the initialized ChromeDriver.
Step 5: Countdown Function
Function: countdown
Displays a countdown in seconds in the command prompt to give the user time to complete certain actions (such as filling out a captcha or selecting a group).
Step 6: Logging In
Function: login
Uses the provided username and password to log into the website.
Finds the input fields for the username and password and fills them in.
Presses Enter to log in.
Step 7: Setting Up the Game Environment
Function: setup_game
Countdown for the captcha: Gives the user 15 seconds to complete the captcha.
Select the world: Clicks on the appropriate world to start the game.
Countdown for selecting a group: Gives the user 10 seconds to select the correct group to send resources from.
Open the village menu: Clicks on the first village in the menu.
Go to the marketplace: Ensures that the user goes to the marketplace before the script starts sending resources.
Step 8: Performing Actions
Function: perform_actions
Simulates pressing the "7" key.
Waits for a random time between 0.3 and 0.8 seconds.
Simulates pressing the Enter key.
Waits for a random time between 0.5 and 0.9 seconds.
Simulates pressing the "d" key to switch to the next village.
Step 9: Running the Main Script
Login: Calls the login function with the provided username and password.
Set Up the Game Environment: Calls the setup_game function to prepare the environment.
Loop to Repeat Actions:
Checks the current URL to determine if the user is on the marketplace.
If the user is on the marketplace, refreshes the page.
Otherwise, performs the sequence of actions (sends resources and switches to the next village).
Waits for a random time between 0.8 and 1.2 seconds between each iteration.
Step 10: Closing the Browser
When the script is done, it closes the browser.




