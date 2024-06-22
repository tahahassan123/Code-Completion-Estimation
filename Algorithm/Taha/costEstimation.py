import numpy as np


def cost_estimation(salary: int, no_people: int, min_internal_costs: int, max_internal_costs: int,
                    external_resources=False, min_external_costs=0, max_external_costs=0, num_simulations=10000):
    """
    Estimating the total cost of the software project

    Parameters:
    - salary: The amount of salary for a single developer
    - no_people: The amount of people developing the project
    - min_internal_costs: The maximum possible internal costs involved in developing the software project
    - max_internal_costs: The minimum possible internal costs involved in developing the software project
    - num_simulations: The amount of simulations to perform
    - external_resources: Will the project have external resources to take into account for?
    - min_external_costs: The minimum possible external costs involved in developing the software project
    - max_external_costs: The maximum possible external costs involved in developing the software project

    Returns:
    - results: The array containing all the predicted cost results
    - cost_mean: The mean of all the predicted cost results
    """

    results = []
    get_mean = []
    developer_costs = salary * no_people
    for i in range(num_simulations):
        internal_costs = np.random.uniform(min_internal_costs, max_internal_costs)
        cost = internal_costs + developer_costs

        if external_resources:
            external_costs = np.random.uniform(min_external_costs, max_external_costs)
            cost += external_costs

        results.append([i, cost])
        get_mean.append(cost)

    cost_mean = np.mean(get_mean)
    cost_stddev = np.std(get_mean)
    return results, cost_mean, cost_stddev


results, mean, std = cost_estimation(50000, 5, 20000, 100000, 1000)
print(results)
print("Mean Cost =", mean)
print("Standard deviation =", std)

results2, mean2, std2 = cost_estimation(50000, 5, 20000, 100000, 1000, True, 10000, 70000)
print(results2)
print("Mean Cost 2 =", mean2)
print("Standard deviation 2 =", std2)
