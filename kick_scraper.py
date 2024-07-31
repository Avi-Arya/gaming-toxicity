from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver as uc
import random

# Index of English language on Kick (changes from time to time)
ENGLISH = 14


# Finished Games: "VALORANT", "Dota 2", "League of Legends", "Call of Duty: Warzone",
#  "Call of Duty: Modern Warfare III", "Counter-Strike 2", "Destiny 2", "Rust", 
# "Tom Clancy\'s Rainbow Six Siege", "Overwatch 2", "XDEFIANT", "VRChat", "Sea of Thieves"
games_list = ["VALORANT", "Dota 2", "League of Legends", "Call of Duty: Warzone", 
              "Call of Duty: Modern Warfare III", "Counter-Strike 2", "Destiny 2", "Rust",  
              "Overwatch 2", "XDEFIANT", "VRChat"]

random.shuffle(games_list)
 
# Function to fetch video URLs from kick.com
def fetch_video_urls():
    # Initialize WebDriver
    options = uc.ChromeOptions()
    options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    driver = uc.Chrome(options = options)
    driver.get('https://kick.com/categories/games/')

    # Wait for the page to load
    time.sleep(5)  # Adjust the sleep time as needed

    # Dictionary to store URLs for different games
    video_urls = {}

    # Click on the 'Browse' link
    # driver.find_element(By.LINK_TEXT, "Browse").click()

    # Click on "Games"
    # driver.find_element(By.LINK_TEXT, "Games").click()

    # Click "Languages" button
    element = driver.find_element(By.CSS_SELECTOR, ".btn-languages")
    element.location_once_scrolled_into_view
    element.click()

    # Select "English", change num depending on pos of English
    element = driver.find_element(By.CSS_SELECTOR, f"div:nth-child({ENGLISH}) .text-sm")
    element.location_once_scrolled_into_view
    element.click()

    for game in games_list:
        with open("video_urls.txt", "a") as file:
            file.write(f"=== {game} ===\n")
            file.close()
        time.sleep(2)
        
        for _ in range(10):
            # Click "Show More" to view all games
            element = driver.find_element(By.CSS_SELECTOR, ".see-more-btn")
            element.location_once_scrolled_into_view
            time.sleep(2)
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            driver.find_element(By.CSS_SELECTOR, ".see-more-btn").click()
            time.sleep(2)

        try:
            # Click into respective game
            element = driver.find_element(By.LINK_TEXT, game)
            element.location_once_scrolled_into_view
            element.click()
            time.sleep(5)
        except: continue

        # Loop through streamers
        for i in range(1, 50):
            try:
                # Check for 18+ tag
                element = driver.find_element(By.CSS_SELECTOR, f".grid-item:nth-child({i}) .category-tag-component:nth-child(2)")
                element.location_once_scrolled_into_view
                curr_tag = element.text
                if curr_tag != "18+": continue

                # Click into streamer
                element = driver.find_element(By.CSS_SELECTOR, f".grid-item:nth-child({i}) > .card-thumbnail-holder > .relative > .w-full")
                element.location_once_scrolled_into_view
                element.click()
            except Exception:
                break

            time.sleep(5)

            try: 
                # Click "Start Watching" (might be unnecessary)
                driver.find_element(By.CSS_SELECTOR, ".size-sm:nth-child(2) .inner-label").click()
                time.sleep(5)
            except Exception:
                pass

            # Click "Videos" button + "Show more"
            element = driver.find_element(By.CSS_SELECTOR, ".border-b:nth-child(2)")
            element.location_once_scrolled_into_view
            time.sleep(2)
            element.click()
            time.sleep(1)
            try:
                element = driver.find_element(By.CSS_SELECTOR, ".see-more-btn")
                element.location_once_scrolled_into_view
                actions = ActionChains(driver)
                actions.move_to_element(element).perform()
                driver.find_element(By.CSS_SELECTOR, ".see-more-btn").click()
            except Exception: 
                pass

            for j in range(1, 50):
                try:
                    # Determine VOD game name
                    element = driver.find_element(By.CSS_SELECTOR, f".grid-item:nth-child({j}) .truncate:nth-child(2)")
                    element.location_once_scrolled_into_view
                    curr_game = element.text
                    print(repr(curr_game))
                except Exception:
                    break
                time.sleep(2)
                if curr_game.strip() in games_list and curr_game == game:
                    element = driver.find_element(By.CSS_SELECTOR, f".grid-item:nth-child({j}) .absolute > .relative > .w-full")
                    element.location_once_scrolled_into_view
                    element.click()
                    time.sleep(2)
                    with open("video_urls.txt", "a") as file:
                        file.write(f"{driver.current_url}\n")
                        file.close()
                    video_urls[game] = video_urls.get(game, []) + [driver.current_url]

                    # Return to previous page + Reselect "Videos" + "Show more"
                    driver.execute_script("window.history.go(-1)")
                    time.sleep(5)
                    try:
                        # Click "Start Watching" (might be unnecessary)
                        driver.find_element(By.CSS_SELECTOR, ".size-sm:nth-child(2) .inner-label").click()
                        time.sleep(2)
                    except Exception:
                        pass
                    element = driver.find_element(By.CSS_SELECTOR, ".border-b:nth-child(2)")
                    element.location_once_scrolled_into_view
                    element.click()
                    time.sleep(1)
                    try:

                        element = driver.find_element(By.CSS_SELECTOR, ".see-more-btn")
                        element.location_once_scrolled_into_view
                        actions = ActionChains(driver)
                        actions.move_to_element(element).perform()
                        driver.find_element(By.CSS_SELECTOR, ".see-more-btn").click()
                    except Exception:
                        pass

            # Go back to previous page
            driver.execute_script("window.history.go(-1)")
            time.sleep(5)

        with open("video_urls.txt", "a") as file:
            file.write(f"\n")
            file.close()
        
        # Go back to "Games" page
        driver.execute_script("window.history.go(-1)")
        time.sleep(5)


    # Close the WebDriver
    driver.quit()

    return video_urls

# Function to write URLs to a text file
# def write_urls_to_file(video_urls):
#     with open("video_urls.txt", "w") as file:
#         for game, urls in video_urls.items():
#             file.write(f"=== {game} ===\n")
#             for url in urls:
#                 file.write(f"{url}\n")
#             file.write("\n")

if __name__ == "__main__":
    # Fetch video URLs
    urls = fetch_video_urls()

    # Write URLs to file
    # write_urls_to_file(urls)