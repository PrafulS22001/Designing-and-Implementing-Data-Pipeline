import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

# -----------------------------
# INITIAL SETUP
# -----------------------------
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_facecolor("black")  # So white text is visible

# Text object for countdown + notifications
status_text = ax.text(50, 95, "", ha="center", fontsize=14, color="white")

# Rocket starting positions
rocket1 = np.array([20, 10])
rocket2 = np.array([80, 10])

# Moon position
moon = np.array([50, 90])

# Scatter plot objects
rocket1_plot = ax.scatter([], [], color='red', label="Ernest's Rocket")
rocket2_plot = ax.scatter([], [], color='green', label="Kernest's Rocket")
moon_plot = ax.scatter(moon[0], moon[1], color='yellow', s=200, label="Moon")

ax.legend()

plt.draw()  # Force window to appear before countdown

# -----------------------------
# COUNTDOWN (shown in window)
# -----------------------------
for i in range(3, 0, -1):
    status_text.set_text(f"Launching in {i}...")
    plt.pause(1)

status_text.set_text("LAUNCH!")
plt.pause(1)

# -----------------------------
# MOVEMENT FUNCTION
# -----------------------------
def move_towards(start, target, speed=0.5):
    direction = target - start
    distance = np.linalg.norm(direction)
    if distance < 1:
        return start
    return start + (direction / distance) * speed

# -----------------------------
# ANIMATION UPDATE
# -----------------------------
def update(frame):
    global rocket1, rocket2

    # Move rockets
    rocket1 = move_towards(rocket1, moon)
    rocket2 = move_towards(rocket2, moon)

    # Update plot
    rocket1_plot.set_offsets(rocket1)
    rocket2_plot.set_offsets(rocket2)

    # Rocket hits moon (NO stopping)
    if np.linalg.norm(rocket1 - moon) < 2:
        status_text.set_text("Ernest's Rocket reached the moon!")

    if np.linalg.norm(rocket2 - moon) < 2:
        status_text.set_text("Kernest's Rocket reached the moon!")

    return rocket1_plot, rocket2_plot, status_text

# -----------------------------
# RUN ANIMATION
# -----------------------------
ani = animation.FuncAnimation(fig, update, interval=50)
plt.show()