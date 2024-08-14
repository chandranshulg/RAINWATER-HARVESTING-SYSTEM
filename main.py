import time
import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Initializing variables
rainfall_data = []
water_level = 0
max_tank_capacity = 1000  # in liters
pump_status = "OFF"

# Function to simulate real-time rainfall monitoring
def monitor_rainfall():
    rainfall = random.uniform(0, 20)  # Random rainfall amount in mm
    rainfall_data.append(rainfall)
    return rainfall

# Function to calculate collected rainwater based on roof area and rainfall
def calculate_collected_water(rainfall_mm, roof_area=50):
    collected_water = (rainfall_mm * roof_area * 0.9) / 1000  # in cubic meters (m^3)
    return collected_water * 1000  # Convert to liters

# Function to update water level in the tank
def update_water_level(rainfall_mm):
    global water_level
    collected_water = calculate_collected_water(rainfall_mm)
    water_level += collected_water
    if water_level > max_tank_capacity:
        overflow = water_level - max_tank_capacity
        water_level = max_tank_capacity
        print(f"Tank overflowed by {overflow:.2f} liters.")
    else:
        print(f"Collected {collected_water:.2f} liters of rainwater. Water level: {water_level:.2f} liters.")

# Function to control the pump based on water level
def control_pump():
    global pump_status
    if water_level > max_tank_capacity * 0.8:
        pump_status = "ON"
        print("Pump is ON to use/store water.")
    else:
        pump_status = "OFF"
        print("Pump is OFF. No need to use/store water.")

# Function to simulate water usage
def simulate_water_usage(amount):
    global water_level
    if water_level >= amount:
        water_level -= amount
        print(f"Used {amount} liters of water. Water level: {water_level:.2f} liters.")
    else:
        print(f"Insufficient water in the tank. Current water level: {water_level:.2f} liters.")

# Flask route to display dashboard
@app.route('/')
def index():
    return render_template('index.html')

# Flask route to get real-time data
@app.route('/data')
def get_data():
    global rainfall_data, water_level, pump_status
    latest_rainfall = rainfall_data[-1] if rainfall_data else 0
    return jsonify({
        'rainfall': latest_rainfall,
        'water_level': water_level,
        'pump_status': pump_status
    })

# HTML content for dashboard (rendered by Flask)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rainwater Harvesting Dashboard</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }}
        header {{
            background-color: #4CAF50;
            color: white;
            padding: 20px;
            text-align: center;
        }}
        section {{
            margin: 20px;
            padding: 20px;
            background-color: white;
            border-radius: 5px;
        }}
        h2 {{
            color: #4CAF50;
        }}
        .data-box {{
            display: flex;
            justify-content: space-around;
        }}
        .data-item {{
            text-align: center;
            width: 30%;
            padding: 10px;
            background-color: #e0f7fa;
            border-radius: 10px;
        }}
        footer {{
            text-align: center;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            position: fixed;
            bottom: 0;
            width: 100%;
        }}
    </style>
</head>
<body>
    <header>
        <h1>Rainwater Harvesting System Dashboard</h1>
        <p>Real-time monitoring and control</p>
    </header>

    <section>
        <h2>Current Status</h2>
        <div class="data-box">
            <div class="data-item">
                <h3>Rainfall (mm)</h3>
                <p id="rainfall">0</p>
            </div>
            <div class="data-item">
                <h3>Water Level (liters)</h3>
                <p id="water_level">0</p>
            </div>
            <div class="data-item">
                <h3>Pump Status</h3>
                <p id="pump_status">OFF</p>
            </div>
        </div>
    </section>

    <footer>
        <p>&copy; 2024 Rainwater Harvesting System</p>
    </footer>

    <script>
        function fetchData() {{
            fetch('/data')
                .then(response => response.json())
                .then(data => {{
                    document.getElementById('rainfall').innerText = data.rainfall.toFixed(2);
                    document.getElementById('water_level').innerText = data.water_level.toFixed(2);
                    document.getElementById('pump_status').innerText = data.pump_status;
                }});
        }}
        setInterval(fetchData, 1000);  // Fetch data every second
    </script>
</body>
</html>
"""

# Save the HTML template
with open('templates/index.html', 'w') as f:
    f.write(HTML_TEMPLATE)

if __name__ == '__main__':
    print("Starting Rainwater Harvesting System...")
    
    # Simulate the system running every minute
    while True:
        rainfall_mm = monitor_rainfall()
        update_water_level(rainfall_mm)
        control_pump()
        simulate_water_usage(random.uniform(0, 100))  # Simulate random water usage
        time.sleep(60)  # Wait for 1 minute before the next update
        
        # For Flask, run the app only if script is executed directly
        app.run(debug=True)
