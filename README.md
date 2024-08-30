# Rainwater Harvesting System

This application is a simulation of a rainwater harvesting system built using Flask. The system monitors rainfall, calculates the amount of water collected in a tank, controls the pump based on water levels, and simulates water usage.

## Overview

The Rainwater Harvesting System application tracks rainfall in real-time and calculates the amount of water collected in a storage tank based on the roof area. The system monitors the water level, controls the pump when the tank is nearly full, and simulates random water usage. It provides a web-based dashboard for real-time monitoring of rainfall, water level, and pump status.

## Features

- **Real-Time Monitoring:** Monitors rainfall and water levels in real-time, displaying the data on a dashboard.
- **Water Collection Calculation:** Calculates the amount of water collected based on rainfall and roof area.
- **Pump Control:** Automatically turns the pump on or off based on the water level in the tank.
- **Water Usage Simulation:** Simulates random water usage to test the system's response.
- **Simulated Data:** Uses randomly generated data to simulate real-world conditions.

## How to Use

1. Clone the repository or download the code.
2. Install Flask:
    ```bash
    pip install Flask
    ```
3. Run the application:
    ```bash
    python app.py
    ```
4. Open your web browser and go to `http://127.0.0.1:5000/` to access the dashboard.
5. The dashboard will automatically update with real-time rainfall, water level, and pump status data.

## Technologies Used

- **Flask:** A lightweight Python web framework for building the web server.
- **HTML5 & CSS3:** For structuring and styling the dashboard interface.
- **JavaScript:** For fetching and updating the dashboard with real-time data.

## Future Enhancements

- **User Interface Improvements:** Enhance the UI with more detailed data visualizations and control options.
- **Historical Data Tracking:** Store and display historical data for rainfall and water usage.
- **Manual Pump Control:** Add functionality to allow manual control of the pump from the dashboard.

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute as needed.

## Author

Created by Chandranshu.
