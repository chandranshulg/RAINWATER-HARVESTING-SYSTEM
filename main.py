import math

# Constants
ROOF_AREA = 100  # Roof area in square meters
RAIN_INTENSITY = 10  # Rainfall intensity in mm/hour
HARVESTING_EFFICIENCY = 0.85  # Efficiency of the system (85% efficiency)
TANK_CAPACITY = 5000  # Capacity of storage tank in liters

# Function to calculate the volume of water harvested
def calculate_harvested_water(roof_area, rain_intensity, efficiency):
    # Convert rain intensity from mm to meters
    rain_intensity_m = rain_intensity / 1000
    # Calculate volume of water (cubic meters)
    volume = roof_area * rain_intensity_m * efficiency
    # Convert cubic meters to liters
    volume_liters = volume * 1000
    return volume_liters

# Function to simulate rainwater harvesting over a period of time
def simulate_rainwater_harvesting(days, daily_rainfall, roof_area, efficiency, tank_capacity):
    total_harvested = 0
    tank_storage = 0

    for day in range(days):
        # Calculate harvested water for the day
        daily_harvest = calculate_harvested_water(roof_area, daily_rainfall[day], efficiency)
        print(f"Day {day + 1}: Rainfall = {daily_rainfall[day]} mm, Harvested = {daily_harvest:.2f} liters")

        # Add harvested water to tank
        if tank_storage + daily_harvest > tank_capacity:
            # Overflow occurs
            overflow = (tank_storage + daily_harvest) - tank_capacity
            print(f"  Overflow: {overflow:.2f} liters")
            tank_storage = tank_capacity
        else:
            tank_storage += daily_harvest

        # Add to total harvested
        total_harvested += daily_harvest

        # Daily status
        print(f"  Tank Storage: {tank_storage:.2f} liters")

    print(f"\nTotal Harvested Water over {days} days: {total_harvested:.2f} liters")
    print(f"Final Tank Storage: {tank_storage:.2f} liters")

# Sample rainfall data (in mm) over 10 days
daily_rainfall = [5, 12, 0, 8, 3, 20, 15, 7, 0, 10]

# Simulate rainwater harvesting
simulate_rainwater_harvesting(
    days=len(daily_rainfall),
    daily_rainfall=daily_rainfall,
    roof_area=ROOF_AREA,
    efficiency=HARVESTING_EFFICIENCY,
    tank_capacity=TANK_CAPACITY
)

# Function to calculate potential water savings
def calculate_water_savings(total_harvested, average_daily_usage, days):
    # Calculate total water usage over the period
    total_usage = average_daily_usage * days
    # Calculate water savings as a percentage
    savings = (total_harvested / total_usage) * 100
    return savings

# User input for daily water usage (in liters)
average_daily_usage = 150  # Assumed average daily usage in liters per person
num_people = 4  # Number of people in the household

# Calculate total water usage
total_water_usage = average_daily_usage * num_people

# Calculate potential water savings
savings_percentage = calculate_water_savings(
    total_harvested=calculate_harvested_water(ROOF_AREA, sum(daily_rainfall), HARVESTING_EFFICIENCY),
    average_daily_usage=total_water_usage,
    days=len(daily_rainfall)
)

print(f"\nPotential Water Savings: {savings_percentage:.2f}%")

# Function to model water filtration process
def water_filtration(volume, filter_efficiency):
    filtered_volume = volume * filter_efficiency
    waste_volume = volume - filtered_volume
    return filtered_volume, waste_volume

# Constants for filtration system
FILTER_EFFICIENCY = 0.95  # 95% filtration efficiency

# Example of filtering harvested water
filtered_water, waste_water = water_filtration(total_harvested, FILTER_EFFICIENCY)
print(f"\nFiltered Water: {filtered_water:.2f} liters")
print(f"Waste Water: {waste_water:.2f} liters")

# Function to estimate annual water savings based on historical rainfall data
def estimate_annual_savings(roof_area, annual_rainfall, efficiency, tank_capacity, average_daily_usage, num_people):
    # Calculate potential annual water harvested
    annual_harvest = calculate_harvested_water(roof_area, annual_rainfall, efficiency)
    # Calculate potential water savings
    total_annual_usage = average_daily_usage * num_people * 365
    savings = (annual_harvest / total_annual_usage) * 100
    return annual_harvest, savings

# Example annual rainfall (mm)
annual_rainfall = 800  # Total annual rainfall in mm

# Estimate annual water savings
annual_harvest, annual_savings = estimate_annual_savings(
    roof_area=ROOF_AREA,
    annual_rainfall=annual_rainfall,
    efficiency=HARVESTING_EFFICIENCY,
    tank_capacity=TANK_CAPACITY,
    average_daily_usage=average_daily_usage,
    num_people=num_people
)

print(f"\nEstimated Annual Harvest: {annual_harvest:.2f} liters")
print(f"Estimated Annual Water Savings: {annual_savings:.2f}%")
