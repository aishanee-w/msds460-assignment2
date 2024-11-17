import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import pulp

df = pd.read_csv('project_plan.csv')

#create directed graph
G = nx.DiGraph()

#add edges based on task dependencies
for index, row in df.iterrows():
    if pd.notna(row['predecessorTaskIDs']):
        predecessors = row['predecessorTaskIDs'].split(',')
        for pred in predecessors:
            G.add_edge(pred.strip(), row['taskID'])

# draw directed graph
pos = nx.spring_layout(G) 
plt.figure(figsize=(12, 8))

#add nodes + edges
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrowsize=20)

#add arrows
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='black')

plt.title('Project Management - Task Dependency Directed Graph')
plt.show()

#initialize lp model
lp_model = pulp.LpProblem("project_plan_minimization", pulp.LpMinimize)

#decision variables: start and end time of each task
task_vars_start = {task_id: pulp.LpVariable(f"t_{task_id}", lowBound=0) for task_id in df['taskID']}
task_vars_end = {task_id: pulp.LpVariable(f"e_{task_id}", lowBound=0) for task_id in df['taskID']}


#variable for total project duration (makespan)
T = pulp.LpVariable("T", lowBound=0)

#objective function: minimize total project duration
lp_model += T

#add constraints for task dependencies
for index, row in df.iterrows():
    task_id = row['taskID']
    duration = row['bestCaseHours']  # use best/worst/expected case hours for the duration (tweak this variable)

    #set the end time constraint: e_i = t_i + d_i
    lp_model += task_vars_end[task_id] == task_vars_start[task_id] + duration

    if pd.notna(row['predecessorTaskIDs']):
        predecessors = row['predecessorTaskIDs'].split(',')
        for pred in predecessors:
            pred = pred.strip()
            #add dependency constraint: t_j >= t_i + d_i
            lp_model += task_vars_start[task_id] >= task_vars_end[pred]

#add constraint: T >= t_i + d_i for all tasks
for task_id in task_vars_end:
    lp_model += T >= task_vars_end[task_id]

#solve
lp_model.solve()

print("Best-Case Timeline:")

#output timing of each task based on optimal solution
for task_id in task_vars_start:
    print(f"Task {task_id} starts at: {pulp.value(task_vars_start[task_id])} hours, ends at: {pulp.value(task_vars_end[task_id])} hours")

print(f"Total project duration: {pulp.value(T)} hours")

