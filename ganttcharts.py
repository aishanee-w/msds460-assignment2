import matplotlib.pyplot as plt

# Critical path task data
tasks = [
    {"taskID": "Task A", "start_time": 0.0, "end_time": 3.0},
    {"taskID": "Task B", "start_time": 0.0, "end_time": 6.0},
    {"taskID": "Task C", "start_time": 3.0, "end_time": 8.0},
    {"taskID": "Task D1", "start_time": 3.0, "end_time": 9.0},
    {"taskID": "Task D2", "start_time": 9.0, "end_time": 21.0},
    {"taskID": "Task D3", "start_time": 9.0, "end_time": 21.0},
    {"taskID": "Task D4", "start_time": 21.0, "end_time": 39.0},
    {"taskID": "Task D5", "start_time": 39.0, "end_time": 45.0},
    {"taskID": "Task D6", "start_time": 39.0, "end_time": 47.0},
    {"taskID": "Task D7", "start_time": 47.0, "end_time": 55.0},
    {"taskID": "Task D8", "start_time": 55.0, "end_time": 61.0},
    {"taskID": "Task E", "start_time": 8.0, "end_time": 13.0},
    {"taskID": "Task F", "start_time": 61.0, "end_time": 66.0},
    {"taskID": "Task G", "start_time": 61.0, "end_time": 66.0},
    {"taskID": "Task H", "start_time": 66.0, "end_time": 76.0},
]

# Prepare data for plotting
task_ids = [task["taskID"] for task in tasks]
start_times = [task["start_time"] for task in tasks]
durations = [task["end_time"] - task["start_time"] for task in tasks]

# Plotting Gantt chart
fig, ax = plt.subplots(figsize=(12, 8))

for i, (task_id, start, duration) in enumerate(zip(task_ids, start_times, durations)):
    ax.barh(task_id, duration, left=start, color="skyblue")
    # Add annotations for start and end times
    ax.text(start, i, f"{start}", va="center", ha="right", fontsize=8, color="black")
    ax.text(start + duration, i, f"{start + duration}", va="center", ha="left", fontsize=8, color="black")

# Label and format chart
ax.set_xlabel("Time (hours)")
ax.set_ylabel("Tasks")
ax.set_title("Gantt Chart for Project Timeline (Best-Case)")
ax.invert_yaxis()  # Reverse the order of tasks for top-to-bottom plotting
ax.grid(axis="x", linestyle="--", alpha=0.7)

# Show plot
plt.tight_layout()
plt.show()