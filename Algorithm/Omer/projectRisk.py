import numpy as np


# import matplotlib.pyplot as plt

def estimate_project_risk(cost_mean, cost_stddev, loc_mean, loc_stddev,
                          time_mean, time_stddev, num_people_mean, num_people_stddev,
                          complexity_mean, complexity_stddev, num_simulations=1000):
    """
    Estimate project risk using Monte Carlo simulation.

    Parameters:
    - cost_mean: Mean total project cost.
    - cost_stddev: Standard deviation of project cost.
    - loc_mean: Mean lines of code (LOC).
    - loc_stddev: Standard deviation of LOC.
    - time_mean: Mean project duration (in months).
    - time_stddev: Standard deviation of project duration.
    - num_people_mean: Mean number of people working on the project.
    - num_people_stddev: Standard deviation of number of people.
    - complexity_mean: Mean software complexity (e.g., cyclomatic complexity).
    - complexity_stddev: Standard deviation of software complexity.
    - num_simulations: Number of Monte Carlo iterations (default is 1000).

    Returns:
    - mean_risk: Mean overall project risk.
    - median_risk: Median overall project risk.
    - percentile_95: 95th percentile of overall project risk.
    - risks: Array of overall project risks from Monte Carlo simulations.
    """

    # Monte Carlo Simulation
    risks = []
    get_mean = []
    for i in range(num_simulations):
        # Sample from normal distributions
        cost = np.random.normal(cost_mean, cost_stddev)
        loc = np.random.normal(loc_mean, loc_stddev)
        time = np.random.normal(time_mean, time_stddev)
        num_people = np.random.normal(num_people_mean, num_people_stddev)
        complexity = np.random.normal(complexity_mean, complexity_stddev)

        # Calculate derived metrics (example: cost per person)
        cost_per_person = cost / num_people if num_people > 0 else np.inf

        # Define risk metrics (example: budget and schedule risks)
        budget_risk = max(0, (cost - cost_mean) / cost_mean)
        schedule_risk = max(0, (time - time_mean) / time_mean)
        resource_risk = max(0, (num_people - num_people_mean) / num_people_mean)
        complexity_risk = max(0, (complexity - complexity_mean) / complexity_mean)

        # Aggregate overall risk (simple example)
        overall_risk = budget_risk + schedule_risk + resource_risk + complexity_risk

        risks.append([i, overall_risk])
        get_mean.append(overall_risk)

    # Analysis
    mean_risk = np.mean(get_mean)

    return risks, mean_risk


