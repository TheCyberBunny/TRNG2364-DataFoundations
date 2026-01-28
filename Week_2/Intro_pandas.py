#pandas is a python library used for data manipulation and analysis
#it provides data structures like DataFrames and Series to work with structured data
#it also offers functionalities for data cleaning, transformation, aggregation, and visualization

import pandas as pd
import matplotlib.pyplot as plt

#Create a simple data frame
# data = {
#     'Name': ['Alice', 'David', 'Charlie', 'Bob'],
#     'Age': [24, 42, 19, 88],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
# }

# df = pd.DataFrame(data)
# #print( df)

# #Access rows by index location
# #print('\nThird Row:\n', df.iloc[2])

# #Access columns
# print("\nNames Column: \n", df['Name'])

# #filter data using a condition
# olderThan30 = df[df['Age'] >= 30]
# print("\nAdults 30+: \n", olderThan30)

# #add a new column
# df['Occupation'] = ["Nurse", "Biologist", "Chef", "Engineer"]
# print("\nnew occupation column: \n", df)

# #Simple stats
# print("\n Average Age: \n", df['Age'].mean())
# print("\n Max Age: \n", df['Age'].max())
# print("Summary Statistics: ", df.describe())

# #Sort data
# sorted_df = df.sort_values(by="Age")
# print("\nSorted by Age: \n", sorted_df)


####Now Accessing data from CSV
vehicle_df = pd.read_csv("./data/Electric_Vehicle_Population_Data.csv")
#print("\nVehicle DataFrame: \n", vehicle_df.head())
#print("\nVehicle DataFrame: \n", vehicle_df.info())

#Basic selection and filtering
#select each unique vehicle make
# vehicle_makes = vehicle_df['Make'].unique()
# print("\nUnique Makes\n", vehicle_makes)

#filter vehicles made by Tesla
# tesla_vehicles = vehicle_df[vehicle_df["Make"] == 'TESLA']
# print("\nTesla Vehicles\n: ", tesla_vehicles.head(10))

#Filter using NOT using the ~ operator in pandas
non_tesla_vehicles = vehicle_df[~(vehicle_df["Make"] == 'TESLA')]
# print("\nNon-Tesla Vehicles\n:", non_tesla_vehicles.head(6))

#We can aggregate some data
#get average electric range by vehicle make
#And filter out 0 values
avg_range_by_make = vehicle_df[vehicle_df['Electric Range'] > 0].groupby('Make')['Electric Range'].mean()
# print("\n average electric range by make: \n", avg_range_by_make)

# double_aggro = vehicle_df.groupby(['Make']).agg(
#     avg_range=('Electric Range', 'mean'),
#     leg_dis=('Legislative District', 'sum')
# )
# print(double_aggro)

#Finally, we can visualize our data using matplotlib
#We can create a Figure - a matplotlib object that represents the entire figure/plot area
fig, axes  = plt.subplots(2, 2, figsize=(12, 10))

#Plot the average electric range by vehicle as a bar chart
avg_range_by_make.plot(kind='bar', ax=axes[0, 0], title="Average Electric Range by Vehicle Make",
xlabel="Vehicle Make", ylabel='Average Electric Range(miles)')

#plot the count of non tesla vehicles by model year
non_tesla_vehicles['Model Year'].value_counts().sort_index().plot(kind='bar', 
ax=axes[0, 1], title="Count of Non-Teslas by Model Year", xlabel='Model Year', ylabel='Number of Vehicles')

plt.show()

#Finally, we can export our modified DataFrame to a new CSV file
non_tesla_vehicles.to_csv('./data/modified_vehicle_data.csv', index=False)