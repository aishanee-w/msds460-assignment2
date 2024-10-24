import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('project_plan.csv')
print(df.head())

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

