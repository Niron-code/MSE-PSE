import numpy as np

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32 

def average_temperature(temperatures):
    return np.mean(temperatures)

def highest_temperature(temperatures):
    return max(temperatures)
def lowest_temperature(temperatures):
    return min(temperatures)

def days_above_twenty(temperatures):
    return np.where(np.array(temperatures) > 20)[0]

if __name__ == "__main__":
    temperatures = [18.5, 19, 20, 25.0, 2, 30, 13.9]
    avg_temp = average_temperature(temperatures)
    print("Task 1: Average Temperature Calculation")
    print(f"The average temperature is {avg_temp:.2f} degrees Celsius.\n")

    print("Task 2: Highest and Lowest Temperatures")
    print(f"The highest temperature is {highest_temperature(temperatures)} degrees Celsius.")
    print(f"The lowest temperature is {lowest_temperature(temperatures)} degrees Celsius.\n")

    print("Task 3: Temperature Conversion")
    fahrenheit = celsius_to_fahrenheit(25)
    print(f"25 degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.\n")

    print("Task 4: Days with Temperatures Above 20 Degrees Celsius")
    print(f"The days with temperatures above 20 degrees Celsius are: {days_above_twenty(temperatures)}")


