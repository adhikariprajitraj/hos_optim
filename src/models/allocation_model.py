import pulp

def optimize_allocation(hospitals, resources):
    # Define the optimization model
    model = pulp.LpProblem("Hospital_Resource_Allocation", pulp.LpMinimize)

    # Decision variables for resource allocation
    x = pulp.LpVariable.dicts("allocation",
                              ((h, r) for h in hospitals for r in resources),
                              lowBound=0, cat=pulp.LpInteger)

    # Objective: Minimize total resources allocated
    # We assume you are trying to minimize the amount of resources distributed
    model += pulp.lpSum(x[h, r] for h in hospitals for r in resources), "TotalResourceAllocation"

    # Constraints: Do not exceed available resources
    for r in resources:
        model += pulp.lpSum(x[h, r] for h in hospitals) <= resources[r], f"Max_{r}"

    # Each hospital must receive a minimum amount of resources based on its needs
    for h in hospitals:
        model += pulp.lpSum(x[h, r] for r in resources) >= hospitals[h]['min_resources'], f"MinResources_{h}"

    # Solve the model
    model.solve()
    
    # Return the results
    return {h: {r: x[h, r].varValue for r in resources} for h in hospitals}
