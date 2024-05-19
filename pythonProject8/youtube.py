from selenium import webdriver
import speech_recognition as sr
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
def automateYoutube(searchtext):
    path = "C:\\Users\\Kaniya Wolverine\\Downloads\\chromedriver"
    url = "https://www.youtube.com/"
    driver = webdriver.Chrome(path)
    driver.get(url)
    driver.find_element_by_name("search_query").send_keys(searchtext)
    driver.find_element_by_css_selector("#search-icon-legacy.ytd-searchbox").click()

    # Wait for the search results to load
    WebDriverWait(driver, 30).until(expected_conditions.title_contains(searchtext))

    # Click on the first video
    WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.ID, "img"))).click()

# Get voice input
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=0.2)
    print("Listening...")
    searchquery = recognizer.listen(source)
    searchtext = recognizer.recognize_google(searchquery).lower()

automateYoutube(searchtext)
