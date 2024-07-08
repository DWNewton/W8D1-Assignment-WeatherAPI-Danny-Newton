function weatherGetter() {
    const city = document.getElementById('cityInput').value;
    fetch(`/weather?city=${city}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('City not found');
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('weatherInfo').innerHTML = `
                <p>City: ${data.city}</p>
                <p>Temperature: ${data.temperature}°C</p>
                <p>Condition: ${data.condition}</p>
                <p>Humidity: ${data.humidity}%</p>
                <p>Wind Speed: ${data.wind_speed} mph</p>
            `;
        })
        .catch(error => {
            document.getElementById('weatherInfo').innerHTML = `<p>${error.message}</p>`;
        });
}