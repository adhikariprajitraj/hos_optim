import pulp

def optimize_allocation(hospitals, available_resources):
    # Define the optimization model
    model = pulp.LpProblem("Hospital_Resource_Allocation", pulp.LpMinimize)

    # Decision variables for resource allocation
    x = pulp.LpVariable.dicts("allocation",
                              ((h, r) for h in hospitals for r in available_resources.keys()),  # Corrected loop over resources
                              lowBound=0, cat=pulp.LpInteger)

    # Unmet demand variable
    unmet_demand = pulp.LpVariable.dicts("unmet_demand",
                                         ((h, r) for h in hospitals for r in available_resources.keys()),
                                         lowBound=0, cat=pulp.LpInteger)

    # Objective: Minimize the unmet demand across all hospitals
    model += pulp.lpSum(unmet_demand[h, r] for h in hospitals for r in available_resources.keys()), "Total_Unmet_Demand"

    # Constraints: Allocation should not exceed available resources
    for r in available_resources:
        model += pulp.lpSum(x[h, r] for h in hospitals) <= available_resources[r], f"Max_{r}"

    # Ensure that unmet demand is the difference between demand and allocation
    for h in hospitals:
        for r in available_resources.keys():
            demand = hospitals[h]['demand'].get(r, 0)
            print(f"Adding constraint for {h} and {r} with demand: {demand}")
            model += x[h, r] + unmet_demand[h, r] == demand, f"Demand_Meet_{h}_{r}"

    # Solve the model
    model.solve()

    # Return allocations and unmet demand
    allocations = {h: {r: x[h, r].varValue for r in available_resources.keys()} for h in hospitals}
    unmet_demand_results = {h: {r: unmet_demand[h, r].varValue for r in available_resources.keys()} for h in hospitals}

    return allocations, unmet_demand_results
