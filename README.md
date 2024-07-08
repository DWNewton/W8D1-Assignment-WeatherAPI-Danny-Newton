# Weather Getter
 Simple Weather retrieval app using API endpoints


## Endpoint
### GET /weather
Retrieve weather information for a specific city.

#### Query Parameter
- `city`: Surprisingly, this is where the user specifies the name of the city.

#### Response

A good response should pass the following information:
  - `city`: City name
  - `temperature`: Current temperature in Celsius
  - `condition`: Weather condition (e.g., sunny, cloudy, rainy)
  - `humidity`: Humidity percentage
  - `wind_speed`: Wind speed in mph

#### Errors

I've set it up to handle the following potential errors:
- HTTP 400 
    - This is a bad request if the `city` parameter is not specified.
- HTTP 404
    - This happens if the user enters a non-existent city
- HTTP 500
    - The internet broke, and WeatherAPI isn't working right.

## Running the API Server

1. Clone the repository.
2. Unzip the files
3. Install the required dependencies:
   `pip install flask requests`
4. python app.py

## End Note:
# Obtaining an API Key from WeatherAPI.com:
1. Go to WeatherAPI.com.
2. Sign up for a free account.
3. Navigate to the API key section in your account dashboard.
4. Copy the API key and replace the API_KEY variable in app.py with your key.
