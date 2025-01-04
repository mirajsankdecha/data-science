# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Task 1: Plotting two points with circle markers
# xpoint1 = np.array([0, 5])  # X-coordinates
# ypoint1 = np.array([0, 200])  # Y-coordinates
# plt.figure()  # Create a new figure for Task 1
# plt.plot(xpoint1, ypoint1, "o")  # Circle marker ('o')
# plt.title("Task 1: Two Points with Circle Markers")  # Title
# plt.xlabel("X-Axis")  # X-axis label
# plt.ylabel("Y-Axis")  # Y-axis label
# plt.grid(True)  # Add grid for better visualization
# plt.show()

# # Task 2: Plotting multiple points with different markers
# xpoint2 = np.array([1, 8, 9, 4])  # X-coordinates
# ypoint2 = np.array([2, 5, 6, 7])  # Y-coordinates

# # (a) Circle marker
# plt.figure()
# plt.plot(xpoint2, ypoint2, marker="o")  # Circle marker ('o')
# plt.title("Task 2(a): Points with Circle Markers")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.grid(True)
# plt.show()

# # (b) Cross marker
# plt.figure()
# plt.plot(xpoint2, ypoint2, marker="X")  # Cross marker ('X')
# plt.title("Task 2(b): Points with Cross Markers")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.grid(True)
# plt.show()

# # (c) Combined marker, line style, and color
# plt.figure()
# plt.plot(xpoint2, ypoint2, "X:r")  # Cross marker ('X'), dotted line (':'), red color ('r')
# plt.title("Task 2(c): Points with Markers, Line Style, and Color")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.grid(True)
# plt.show()

# # Task 3: Line styles, colors, and line width
# plt.figure()
# plt.plot(
#     xpoint1, ypoint1, linestyle="-.", color="g", linewidth=10.5
# )  # Dashed-dot line ('-.'), green color ('g'), and line width of 10.5
# plt.title("Task 3: Line Styles and Colors")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.grid(True)
# plt.show()

# # Task 4: Average calorie burn pulses
# y1 = np.array([3, 8, 1, 10, 45, 75, 96, 36, 47, 32, 76])  # Calorie burn pulse for walking
# y2 = np.array([6, 2, 7, 11, 45, 35, 24, 24, 24, 63, 25])  # Calorie burn pulse for running

# plt.figure()
# plt.plot(y1, label="Walking", linestyle="-", marker="o", color="blue")  # Walking
# plt.plot(y2, label="Running", linestyle="--", marker="x", color="red")  # Running
# plt.title("Task 4: Calorie Burn - Average Pulse Rates")
# plt.xlabel("Time Intervals (minutes)")
# plt.ylabel("Pulse Rate (beats per minute)")
# plt.legend()
# plt.grid(True)
# plt.show()

# # Task 5: Subplotting
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])

x2 = np.array([0, 1, 2, 3])
y2 = np.array([10, 20, 30, 40])

# plt.figure()

# # Subplot 1
# plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
# plt.plot(x1, y1, marker="o", color="r")
# plt.title("Subplot 1: Line Plot")

# # Subplot 2
# plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
# plt.plot(x2, y2, marker="x", color="b")
# plt.title("Subplot 2: Line Plot")

# plt.tight_layout()  # Adjust layout
# plt.show()

# # Task 6: Scatter Plot
# plt.figure()
# plt.scatter(x1, y1, color="r")  # Scatter plot
# plt.title("Task 6: Scatter Plot")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.grid(True)
# plt.show()

# # Task 7: Bar Plot
# plt.figure()
# plt.bar(x1, y1, color="g")  # Bar plot
# plt.title("Task 7: Bar Plot")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.grid(True)
# plt.show()

# Task 8 : Horizontal Bar Plot
# plt.figure()
# plt.barh(x1, y1, color="b")  # Horizontal Bar plot
# plt.title("Task 8: Horizontal Bar Plot")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.grid(True)
# plt.show()

# Task 9: Pie Chart with Three Subtasks, Shadow, and Colors
import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
fruits = np.array([35, 25, 25, 15])
labels = ["Apple", "Banana", "Orange", "Mango"]

# Custom colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Pink, Blue, Green, Orange

# # Subtask 1: Basic Pie Chart with Shadow and Custom Colors
# plt.figure()
# plt.pie(fruits, labels=labels, startangle=90, autopct='%1.1f%%', shadow=True, colors=colors)
# plt.title("Subtask 1: Basic Pie Chart with Shadow")
# plt.show()

# # Subtask 2: Pie Chart with Exploded Slice, Shadow, and Custom Colors
# explode = [0.2, 0, 0, 0]  # Explode the first slice (Apple)
# plt.figure()
# plt.pie(fruits, labels=labels, startangle=90, explode=explode, autopct='%1.1f%%', shadow=True, colors=colors)
# plt.title("Subtask 2: Exploded Slice with Shadow")
# plt.show()

# Subtask 3: Pie Chart with Exploded Slices, Shadow, and Custom Colors
explode = [0.1, 0.1, 0.1, 0.1]  # Explode all slices slightly
plt.figure()
plt.pie(fruits, labels=labels, startangle=180, explode=explode, autopct='%1.1f%%', shadow=True, colors=colors)
plt.title("Subtask 3: Exploded All Slices with Shadow and Legend")
plt.legend()
plt.show()

# Subtask 4 : 