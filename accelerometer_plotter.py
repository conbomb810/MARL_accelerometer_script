import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import os

#Read the data of a file and format the time, x and z columns into numpy arrays
def readData(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    #Get the trial name
    trial_lines = [line for line in lines if line.startswith("Trial:")]
    trial_name = trial_lines[1].split("\t")[1].strip().replace(".txt", "") if len(trial_lines) > 1 else "Unknown"

    #Locate the data section
    data_start = next(i for i, line in enumerate(lines) if line.startswith("Unix Time")) + 1

    #Read the data lines and split the entries with tabs
    data = [line.strip().split('\t') for line in lines[data_start:]]

    #Convert the data to numpy arrays
    x = np.array([float(row[1]) for row in data])
    z = np.array([float(row[3]) for row in data])

    return trial_name, x, z

#Plot the X and Z axis data onto a scatter plot and save the plot as a png
def plotData(x, z, trial_name):
    plt.figure(figsize=(8, 6))

    #colormap of red->purple->blue
    colors = [(1, 0, 0), (0.5, 0, 0.5), (0, 0, 1)]
    cmap = LinearSegmentedColormap.from_list("RedPurpleBlue", colors, N=len(x))
    
    #color values
    colorlist = [cmap(i / (len(x) - 1)) for i in range(len(x) - 1)]

    #ploting segments with color values
    for i in range(len(x) - 1):
        plt.plot(x[i:i+2], z[i:i+2], color=colorlist[i], alpha=1)

    #plt.scatter(x, z, c='blue', alpha=0.7, edgecolors='k', label="Data Points")
    #plt.plot(x, z, c="red", alpha=1, label="Line Connection")
    plt.title(f"{trial_name}")
    plt.xlabel("X-axis")
    plt.ylabel("Z-axis")
    plt.xlim(-9.321824073791504, 7.024587631225586)
    plt.ylim(-13.535619735717773, 9.587580680847168)
    plt.grid(True)
    plt.savefig(trial_name + ".png")
    plt.close()

    return 0


def main():
    #Change the following line to change the directory this script is worked in
    directory = "E://MARL Project Repo//MARL_accelerometer_script"

    os.chdir(directory)
    for file in os.listdir():
        if ".txt" in file.lower() and "accelerometer" in file.lower():
            print(file)
            trial_name, x, z = readData(file)
            plotData(x, z, trial_name)

main()