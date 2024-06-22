import numpy as np

def calculate_mean_and_stddev(min_value, max_value):
    mean = (min_value + max_value) / 2
    stddev = (max_value - min_value) / 4  # Assuming range covers about 4 standard deviations
    return mean, stddev

def estimate_code_coverage(num_test_cases_min, num_test_cases_max,
                           loc_mean, loc_stddev,
                           test_success_rate_min, test_success_rate_max,
                           num_simulations=1000):
    """
    Estimate code coverage using Monte Carlo simulation.

    Parameters:
    - num_test_cases_min: Minimum number of test cases.
    - num_test_cases_max: Maximum number of test cases.
    - loc_mean: Mean size of codebase (e.g., LOC).
    - loc_stddev: Standard deviation of codebase size.
    - test_success_rate_min: Minimum success rate of test cases (0 to 1).
    - test_success_rate_max: Maximum success rate of test cases (0 to 1).
    - num_simulations: Number of Monte Carlo iterations (default is 1000).

    Returns:
    - mean_coverage: Mean estimated code coverage.
    - median_coverage: Median estimated code coverage.
    - percentile_95: 95th percentile of estimated code coverage.
    - coverage_results: Array of estimated code coverage from Monte Carlo simulations.
    """
    # Calculate mean and standard deviation from min and max values
    num_test_cases_mean, num_test_cases_stddev = calculate_mean_and_stddev(num_test_cases_min, num_test_cases_max)
    test_success_rate_mean, test_success_rate_stddev = calculate_mean_and_stddev(test_success_rate_min, test_success_rate_max)

    # Monte Carlo Simulation
    coverage_results = []
    get_mean = []

    for i in range(num_simulations):
        # Sample from truncated normal distributions to ensure non-negative values
        num_test_cases = np.random.normal(num_test_cases_mean, num_test_cases_stddev)
        num_test_cases = max(1, num_test_cases)  # Ensure at least 1 test case

        codebase_size = np.random.normal(loc_mean, loc_stddev)
        codebase_size = max(1, codebase_size)  # Ensure at least 1 codebase size

        test_success_rate = np.random.normal(test_success_rate_mean, test_success_rate_stddev)
        test_success_rate = max(0, min(1, test_success_rate))  # Ensure within [0, 1]

        # Estimate code coverage
        estimated_coverage = (num_test_cases * test_success_rate) / codebase_size

        # Cap coverage at 100% if calculated value exceeds 1
        estimated_coverage = min(1, estimated_coverage)

        coverage_results.append([i, estimated_coverage])
        get_mean.append(estimated_coverage)

    # Analysis
    mean_coverage = np.mean(get_mean)


    return coverage_results, mean_coverage

