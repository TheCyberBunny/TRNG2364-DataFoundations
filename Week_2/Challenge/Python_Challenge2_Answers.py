import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("./Challenge/steps.csv")

# Get user input
num_days = int(input("How many days of data would you like to analyze (1–7)? "))

# Validate input
num_days = max(1, min(num_days, len(df)))

# Select data
selected_data = df.head(num_days)

# NumPy calculations
steps_array = selected_data["Steps"].to_numpy()
avg_steps = np.mean(steps_array)
max_steps = np.max(steps_array)
min_steps = np.min(steps_array)

# Display results
print("\nAnalysis Results:")
print(f"Average steps: {avg_steps:.0f}")
print(f"Maximum steps: {max_steps}")
print(f"Minimum steps: {min_steps}")

# Plotting
colors = ["skyblue"] * num_days
max_index = np.argmax(steps_array)
colors[max_index] = "orange"

plt.bar(selected_data["Day"], steps_array, color=colors)

plt.title("Daily Step Count Analysis")
plt.xlabel("Day")
plt.ylabel("Steps")
plt.grid(axis="y")

plt.show()
