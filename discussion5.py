from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Data for items: (name, value, volume)
items = [
    ("Bedroom set", 600, 800),
    ("Dining room set", 480, 600),
    ("Gaming computer", 140, 300),
    ("Sofa", 310, 400),
    ("TV", 100, 200)
]

# Define the volume limit
volume_limit = 1200

# Initialize the problem
prob = LpProblem("Moving_Knapsack_Problem", LpMaximize)

# Define decision variables for each item
decision_vars = {name: LpVariable(name, cat="Binary") for name, _, _ in items}

# Objective function: Maximize total value
prob += lpSum(decision_vars[name] * value for name, value, _ in items)

# Constraint: Total volume of selected items should be <= 1100
prob += lpSum(decision_vars[name] * volume for name, _, volume in items) <= volume_limit

# Solve the problem
prob.solve()

# Results
selected_items = [name for name in decision_vars if decision_vars[name].value() == 1]
total_value = sum(value for name, value, volume in items if decision_vars[name].value() == 1)
total_volume = sum(volume for name, value, volume in items if decision_vars[name].value() == 1)

print("Selected items to take:", selected_items)
print("Total value:", total_value)
print("Total volume:", total_volume)