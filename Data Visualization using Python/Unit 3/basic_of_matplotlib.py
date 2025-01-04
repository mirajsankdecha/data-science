# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# # Task 1: Plotting two points with circle markers
xpoint1 = np.array([0, 5])  # X-coordinates
ypoint1 = np.array([0, 200])  # Y-coordinates
# plt.figure()  # Create a new figure for this task
# plt.plot(xpoint1, ypoint1, "o")  # Circle marker ('o')
# plt.title("Task 1: Two Points with Circle Markers")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.grid(True)  # Add grid for better visualization
# plt.show()

# # Task 2: Plotting multiple points with different markers
# # (a) Circle marker
# xpoint2 = np.array([1, 8, 9, 4])  # X-coordinates
# ypoint2 = np.array([2, 5, 6, 7])  # Y-coordinates
# plt.figure()  # Create a new figure for this task
# plt.plot(xpoint2, ypoint2, marker="o")  # Circle marker ('o')
# plt.title("Task 2(a): Points with Circle Markers")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.grid(True)
# plt.show()

# # (b) Cross marker
# plt.figure()  # Create a new figure for this task
# plt.plot(xpoint2, ypoint2, marker="X")  # Cross marker ('X')
# plt.title("Task 2(b): Points with Cross Markers")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.grid(True)
# plt.show()

# # (c) Combined marker, line style, and color
# plt.figure()  # Create a new figure for this task
# plt.plot(xpoint2, ypoint2, "X:r")  # Cross marker ('X'), dotted line (':'), red color ('r')
# plt.title("Task 2(c): Points with Markers, Line Style, and Color")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.grid(True)
# plt.show()

# Line Styles and Colors

plt.figure()
plt.plot(xpoint1,ypoint1,linestyle='dashed',color='g')
plt.show()

