import numpy as np

# Define the path to the file
file_path = "representations/test4.npy"

# Load the .npy file
data = np.load(file_path)

# Print basic information
print("Shape of the data:", data.shape)
print("Data type:", data.dtype)

# Optionally, print a small sample
print("Sample data:", data[:5])
