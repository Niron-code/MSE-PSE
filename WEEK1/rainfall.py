import numpy as np

rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]

# Convert the list to a NumPy array and print it.
def rainfall_to_array(rainfall):
    return np.array(rainfall)

# Calculate the total rainfall.
def total_rainfall(rainfall):
    return np.sum(rainfall)

# Calculate the average rainfall.
def average_rainfall(rainfall):
    return np.mean(rainfall)

# Count how many days had no rain (0 mm)
def count_no_rain_days(rainfall):
    return np.count_nonzero(np.array(rainfall) == 0)

# Print the days (by index) where the rainfall was more than 5 mm.
def days_with_heavy_rain(rainfall):
    return np.where(np.array(rainfall) > 5)[0]

# Calculate the 75th percentile of the rainfall data and identify values above it.
def rainfall_above_75th_percentile(rainfall):
    percentile_75 = np.percentile(rainfall, 75)
    return np.array(rainfall)[np.array(rainfall) > percentile_75]

if __name__ == "__main__": 
    print("Task 1: Convert Rainfall List to NumPy Array")
    rainfall_array = rainfall_to_array(rainfall)
    print(f"Rainfall as NumPy array: {rainfall_array}\n")

    print("Task 2: Total Rainfall Calculation")
    total = total_rainfall(rainfall)
    print(f"The total rainfall is {total:.2f} mm.\n")

    print("Task 3: Average Rainfall Calculation")
    avg_rain = average_rainfall(rainfall)
    print(f"The average rainfall is {avg_rain:.2f} mm.\n")

    print("Task 4: Count of No Rain Days")
    no_rain_days = count_no_rain_days(rainfall)
    print(f"The number of days with no rain is {no_rain_days}.\n")

    print("Task 5: Days with Heavy Rain (more than 5 mm)")
    heavy_rain_days = days_with_heavy_rain(rainfall)
    print(f"The days with rainfall more than 5 mm are: {heavy_rain_days}\n")

    print("Task 6: Rainfall Above the 75th Percentile")
    above_75th = rainfall_above_75th_percentile(rainfall)
    print(f"Rainfall values above the 75th percentile are: {above_75th}")
