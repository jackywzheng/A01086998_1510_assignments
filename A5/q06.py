"""Question 6."""

# Jacky Zheng
# Gray Chen

import requests
import json


# Will not work if image of the day is a video, like it was on April 14th
def website():
    """Create an index.html page.

    PRECONDITION: N/A
    POSTCONDITION: creates an index.html page with NASA picture of the day, and user's input
    """
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    nasa_api = json.loads(response.text)
    nasa_picture_url = nasa_api['url']
    user_name = input("Enter your name: ")
    user_type = input("Enter a sentence that describes yourself: ")
    with open('index.html', 'w') as file_object:
        file_object.write("<!doctype html>\n"
                          "<html lang='en'>\n"
                          "<head>\n"
                          "<meta charset='utf-8'>\n"
                          "<title>Introduction</title>\n"
                          "<meta name='description' content='User’s webpage'>\n"
                          "<meta name='author' content='Your name goes here'>\n"
                          "<link rel='stylesheet' href='css/styles.css?v=1.0'>\n"
                          "</head>\n"
                          "<body>\n"
                          "<center>\n"
                          "<h1>" + user_name + "</h1>\n"
                          "<img src=" + nasa_picture_url + ">\n"
                          "</center>\n" +
                          user_type + "\n"
                          "</body>\n"
                          "</html>")


def main():
    pass


if __name__ == '__main__':
    main()
