import numpy as np

def estimate_number_of_people(num_simulations=10000, project_duration=12, total_cost=1000000, average_cost_per_person=10000,
                           productivity_mean=100, productivity_stddev=10,
                           scope_complexity_mean=50000, scope_complexity_stddev=5000):
    """
    Perform a Monte Carlo simulation to estimate the number of people required for a project.
    
    Parameters:
    - num_simulations: Number of Monte Carlo iterations
    - project_duration: Project duration in months
    - total_cost: Total project budget in USD
    - average_cost_per_person: Average cost per person per month in USD
    - productivity_mean: Mean of productivity (lines of code per developer per day)
    - productivity_stddev: Standard deviation of productivity
    - scope_complexity_mean: Mean of estimated scope and complexity (total lines of code needed)
    - scope_complexity_stddev: Standard deviation of scope and complexity
    
    Returns:
    - mean_people: Mean number of people required
    - median_people: Median number of people required
    - percentile_95: 95th percentile of people required
    - results: Array of results from the simulation
    """
    
    results = []

    for _ in range(num_simulations):
        # Sample from normal distributions
        productivity = np.random.normal(productivity_mean, productivity_stddev)
        scope_complexity = np.random.normal(scope_complexity_mean, scope_complexity_stddev)
        cost_per_person = np.random.normal(average_cost_per_person, average_cost_per_person * 0.1)  # 10% variance

        # Calculate total work and work per person
        total_work = scope_complexity
        work_per_person = productivity * project_duration * 30  # Assuming 30 working days per month
        num_people_required = total_work / work_per_person

        # Calculate the number of people affordable within the budget
        num_people_cost_limited = total_cost / (cost_per_person * project_duration)
        
        # Determine the final number of people needed (considering both work and cost constraints)
        final_num_people = min(num_people_required, num_people_cost_limited)
        
        results.append(final_num_people)

    # Convert results to a numpy array for analysis
    results = np.array(results)

    # Analysis
    mean_people = np.mean(results)
    median_people = np.median(results)
    percentile_95 = np.percentile(results, 95)

    return mean_people, median_people, percentile_95, results

# Example usage
mean_people, median_people, percentile_95, results = estimate_number_of_people()

print(f"Mean number of people required: {mean_people:.2f}")
print(f"Median number of people required: {median_people:.2f}")
print(f"95th percentile: {percentile_95:.2f}")

# Plot the distribution of results
# import matplotlib.pyplot as plt
# plt.hist(results, bins=50, edgecolor='black')
# plt.title('Distribution of Number of People Needed')
# plt.xlabel('Number of People')
# plt.ylabel('Frequency')
# plt.show()