# Made by Jacob Silva for class CIS 245, instructor Allen Voelcker
# This program makes requests to OpenWeatherMap.org and displays the data requested.
# Imports requests from the request library
import requests

while True:
    # Creates the main function; the request and response
    def main():
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        appid = "a7defea868344cca0055b910dcd785b8"
        city = input("Please input the city name or zip code*.\n"
                     "*Some cities share the same zip code as each other\n"
                     "and may be read accidentally.\n")

        url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
        # Tries to request info from openweathermap, if it can't, it will display an error and ask you to reconnect.
        try:
            response = requests.get(url)
        except:
            print("Error. Please reconnect to the internet.")
        else:
            unformated_data = response.json()
            print(f"\nHere is the weather info on {city}")

    # tries to read the data from the provided name.
    # If the name didn't provide info, it shows an error and asks to retry
        try:
            temp = unformated_data["main"]["temp"]
        except:
            print("Error. Please try again.\n")
            main()
        else:
            print(f"The current temp is: {temp} degrees fahrenheit.")
            temp_max = unformated_data["main"]["temp_max"]
            print(f"The max temp is: {temp_max} degrees fahrenheit.\n")


    main()
    # Creates the option to repeat the program or end it.

    answer = input('Would you like to go again? Please press "y" to do so.\n'
                   'Otherwise, you can type any other button to stop.\n')
    if answer == "y":
        continue
    else:
        print("Goodbye!")
        import time
        time.sleep(3)
        break
