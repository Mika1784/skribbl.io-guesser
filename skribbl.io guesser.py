import pyautogui
import time

#wordlists according to number of letters
seven_letter_words = "America Balloon Biscuit Blanket Chicken Chimney Country Cupcake Curtain Diamond Eyebrow Fireman Florida Germany Harpoon Husband Morning Octopus Popcorn Printer Sandbox Skyline Spinach"
eight_letter_words = "Backpack Basement Building Campfire Complete Elephant Exercise Hospital Internet Jalapeno Mosquito Sandwich Scissors Seahorse Skeleton Snowball Sunshade Treasure"
nine_letter_words  = "Blueberry Breakfast Bubblegum Cellphone Dandelion Hairbrush Hamburger Horsewhip Jellyfish Landscape Nightmare Pensioner Rectangle Snowboard Spaceship Spongebob Swordfish Telephone Telescope"
ten_letter_words = "Bellpepper Broomstick Commercial Flashlight Lighthouse Lightsaber Microphone Photograph Skyscraper Strawberry Sunglasses Toothbrush Toothpaste"

letter_number = input("How many letters does your word have?   ") #input of how many letters there are (in digits)

if letter_number  == "7":
    print("words will start typing in five seconds") #if the user inputs "7"
    time.sleep(5)
    for word in seven_letter_words.split():
        pyautogui.write(word)
        pyautogui.press("enter")
        print("Typing complete.")
        

elif letter_number  == "8":
    print("words will start typing in five seconds") #if user inputs "8"
    time.sleep(5)
    for word in eight_letter_words.split():
        pyautogui.write(word)
        pyautogui.press("enter")
        print("Typing complete.")

elif letter_number  == "9":
    print("words will start typing in five seconds") #if user inputs "9"
    time.sleep(5)
    for word in nine_letter_words.split():
        pyautogui.write(word)
        pyautogui.press("enter")
        print("Typing complete.")

elif letter_number  == "10":
    print("words will start typing in five seconds") #if user inputs "10"
    time.sleep(5)
    for word in ten_letter_words.split():
        pyautogui.write(word)
        pyautogui.press("enter")
        print("Typing complete.")
        
else:
    print("Invalid input")  #if user puts anything other than the answers above

