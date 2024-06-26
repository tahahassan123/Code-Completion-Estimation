import numpy as np

def estimate_number_of_people(num_simulations=1000, project_duration=12,
                                      productivity=50,
                                      loc_mean=50000, loc_stddev=5000):
    """
    Perform a Monte Carlo simulation to estimate the number of people required for a project without considering cost.
    
    Parameters:
    - num_simulations: Number of Monte Carlo iterations (default is 1000)
    - project_duration: Project duration in months
    - productivity_mean: Mean of productivity (lines of code per developer per day)
    - productivity_stddev: Standard deviation of productivity
    - loc_mean: Mean of estimated scope and complexity (total lines of code needed)
    - loc_stddev: Standard deviation of scope and complexity
    
    Returns:
    - mean_people: Mean number of people required
    - median_people: Median number of people required
    - percentile_95: 95th percentile of people required
    - results: Array of results from the simulation
    """
    
    results = []
    get_mean = []
    for i in range(num_simulations):
        # Sample from normal distributions
        # productivity = np.random.normal(productivity_mean, productivity_stddev)
        scope_complexity = np.random.normal(loc_mean, loc_stddev)

        # Calculate total work and work per person
        total_work = scope_complexity
        work_per_person = productivity * project_duration * 22  # Assuming 22 working days per month
        num_people_required = total_work / work_per_person

        results.append([i, num_people_required])
        get_mean.append(num_people_required)

    # Analysis
    num_people_stddev = np.std(get_mean)
    mean_people = np.mean(get_mean)
    
    return results, mean_people, num_people_stddev


