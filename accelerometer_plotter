import numpy as np
import matplotlib.pyplot as plt

#Read the data of a file and format the time, x and z columns into numpy arrays
def readData(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    #Extract trial name
    trial_lines = [line for line in lines if line.startswith("Trial:")]
    trial_name = trial_lines[1].split("\t")[1].strip().replace(".txt", "") if len(trial_lines) > 1 else "Unknown"

    #Locate the data section
    data_start = next(i for i, line in enumerate(lines) if line.startswith("Unix Time")) + 1

    #Read the data lines
    data = [line.strip().split('\t') for line in lines[data_start:]]

    #Convert the data to numpy arrays
    x = np.array([float(row[1]) for row in data])
    z = np.array([float(row[3]) for row in data])

    return trial_name, x, z

#Plot the X and Z axis data onto a scatter plot and save the plot as a png
def plotData(x, z, trial_name):
    plt.figure(figsize=(8, 6))
    #plt.scatter(x, z, c='blue', alpha=0.7, edgecolors='k', label="Data Points")
    plt.plot(x, z, c='red', alpha=0.7, label="Line Connection")
    plt.title(f"{trial_name}")
    plt.xlabel("X-axis")
    plt.ylabel("Z-axis")
    #plt.legend()
    plt.grid(True)
    plt.savefig(trial_name + ".png")
    plt.close()

#Example usage
filename = "test_accelerometer_2.txt"
trial_name, x, z = readData(filename)

plotData(x, z, trial_name)
