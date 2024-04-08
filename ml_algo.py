import pandas as pd
import numpy as np

# Read the data from the log file into a pandas DataFrame
df = pd.read_csv("log_file.txt", names=["DateTime", "EyeballCoordinates", "MouseCoordinates"])

# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

# Calculate distances for each entry
distances = []
for _, row in df.iterrows():
    eyeball_coords = eval(row["EyeballCoordinates"])  # Convert string to tuple
    mouse_coords = eval(row["MouseCoordinates"])      # Convert string to tuple
    distance = euclidean_distance(eyeball_coords, mouse_coords)
    distances.append(distance)

# Compute standard deviation
std_deviation = np.std(distances)
print("Standard Deviation of distances between eyeball coordinates and mouse pointer coordinates:", std_deviation)