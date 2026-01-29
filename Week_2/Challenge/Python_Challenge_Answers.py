#Challenge 1

import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperatures = [12, 14, 15, 13, 16, 18, 17]

plt.plot(days, temperatures, marker='o', linestyle='--', label="Temperature")

# Find warmest day
max_temp = max(temperatures)
max_index = temperatures.index(max_temp)

# Highlight warmest day
plt.scatter(days[max_index], max_temp, color='red', zorder=5, label="Warmest Day")

plt.title("Average Daily Temperature Over a Week")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)

# Bonus annotation
plt.annotate(
    f"{max_temp}°C",
    (days[max_index], max_temp),
    textcoords="offset points",
    xytext=(0, 8),
    ha='center'
)

plt.legend()
plt.show()

##########################
#Challenge 2

import pandas as pd
#import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [1200, 1350, 1100, 1500, 1600, 1550]
}

df = pd.DataFrame(data)

# Basic inspection
print(df)

# Line plot
plt.plot(df["Month"], df["Sales"], marker='o')

# Find highest sales month
max_sales = df["Sales"].max()
max_row = df[df["Sales"] == max_sales]

# Highlight highest point
plt.scatter(
    max_row["Month"],
    max_row["Sales"],
    color='red',
    zorder=5,
    label="Highest Sales"
)

plt.title("Monthly Sales (First Half of the Year)")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True)

# Bonus annotation
plt.annotate(
    f"${max_sales}",
    (max_row["Month"].values[0], max_sales),
    textcoords="offset points",
    xytext=(0, 8),
    ha='center'
)

plt.legend()
plt.show()

