# Weather-Forecast-Python

## Overview
The Weather Forecast App is a Python-based GUI application designed to provide comprehensive weather details for a specified location. It leverages various weather parameters to offer users a detailed and accurate forecast.

## Screenshot
Below is a screenshot of the Weather Forecast App with marked features:

<img src="https://github.com/atharva-narkhede/Weather-Forecast-Python/assets/106006803/457b0505-55a0-4a25-8c4f-7bf6304465d3" alt="Weather Forecast App Screenshot" width="600" />

## Features
1. **Temperature:** Current temperature of the location.
2. **Description:** General weather description (e.g., sunny, cloudy).
3. **Wind Speed:** Wind speed in the specified area.
4. **Humidity:** Current humidity level.
5. **Pressure:** Atmospheric pressure.
6. **Visibility:** Visibility level.
7. **UV Index:** UV radiation level.
8. **Clouds:** Cloud coverage percentage.
9. **Dew Point:** Temperature at which dew forms.
10. **Date and Day:** Current date and day of the location.
11. **Time Zone, Longitude, and Latitude:** Geographic details of the location.
12. **7-Day Weather Predictions:** Day and night temperature forecasts for the next 7 days.

## Installation
To use the Weather Forecast App, follow these steps:

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip (Python package installer)

### Packages
Install the required packages using the following commands:
```bash
pip install tk
pip install geopy
pip install timezonefinder
pip install datetime
pip install requests
pip install pytz
```

### Download
[Download the Weather App](https://github.com/atharva-narkhede/Weather-Forecast-Python/archive/refs/heads/main.zip)

### Running the App
1. **Download and Extract**: Download and extract the zip file.
2. **Run the Application**: Open the extracted folder and locate the file named `weather_app.py`. Right-click on the file and select "Open with Python".

## Note
Ensure to manually correct the image file path in the code. Update the path to match the actual location of your image files. For example:

## Usage
1. **Open the Application**: Launch the Weather Forecast App.
2. **Search for a Location**: Enter the name of the place in the search box and press enter or click the search button.
3. **View Weather Details**: The app will display the weather details for the specified location.

## Methodology
1. **User Input**: The user inputs the name of the place.
2. **Timezone Detection**: The app finds the timezone of the place using the `timezonefinder` package.
3. **Current Time Retrieval**: The app retrieves the current time of the place.
4. **API Call**: The app makes an API call to get weather data based on the latitude and longitude.
5. **Data Extraction**: The app extracts weather details from the JSON response.
6. **Icon Display**: The app uses the extracted data to display appropriate weather icons.
7. **Display Weather Report**: The app displays the complete weather report on the screen.

## Future Work
1. **Improved GUI**: Enhance the graphical user interface.
2. **Faster API Response**: Reduce the time required by the API to respond.
3. **Additional Features**: Add options such as graphs, daily alerts, desktop notifications, and current weather at the user's location.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
