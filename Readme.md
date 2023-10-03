# Temperature Alert Agent By Uagent Library 

## Description

The Temperature Alert Agent is a Python application that allows users to set their preferred temperature range and location. It periodically checks the current temperature for the specified location using the OpenWeatherMap API and sends alerts when the temperature goes below the minimum or above the maximum threshold set by the user.

## Instructions to Run the Project

Follow these steps to run the Temperature Alert Agent on your local machine:

1. Clone the repository:
   ```shell
   git clone https://github.com/Ismail-Mirza/temperature_notification.git
2. Install Dependency
   ```shell 
   poetry install
3. Add API KEY example given env_sample file
  ```shell
  #get api key from 
  #https://www.weatherapi.com/
  API_KEY = YOUR_API_KEY
```
4. Run 
  ```shell
  poetry run python src/main.py
  
  or

  poetry shell

  python src/main.py
  ```


Special Considerations
1. Ensure that you have an internet connection to fetch real-time weather data from OpenWeatherMap.
2. The script uses the uAgents library for periodic execution, and it runs until you manually terminate it. You can use Ctrl+C to stop the script.
3. If you encounter any issues or errors, please check your API key, location input, and temperature thresholds.
4. I usages desktop notification for notify change in temperature below or above threshold you can use email or sms notifications.
