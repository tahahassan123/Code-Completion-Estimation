import numpy as np


def estimate_code_coverage(num_test_cases_mean, num_test_cases_stddev,
                           loc_mean, loc_stddev,
                           test_success_rate_mean, test_success_rate_stddev,
                           num_simulations=10000):
    """
    Estimate code coverage using Monte Carlo simulation.

    Parameters:
    - num_test_cases_mean: Mean number of test cases.
    - num_test_cases_stddev: Standard deviation of number of test cases.
    - loc_mean: Mean size of codebase (e.g., LOC).
    - loc_stddev: Standard deviation of codebase size.
    - test_success_rate_mean: Mean success rate of test cases (0 to 1).
    - test_success_rate_stddev: Standard deviation of test success rate.
    - num_simulations: Number of Monte Carlo iterations (default is 10000).

    Returns:
    - mean_coverage: Mean estimated code coverage.
    - median_coverage: Median estimated code coverage.
    - percentile_95: 95th percentile of estimated code coverage.
    - coverage_results: Array of estimated code coverage from Monte Carlo simulations.
    """

    # Monte Carlo Simulation
    coverage_results = []

    for _ in range(num_simulations):
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

        coverage_results.append(estimated_coverage)

    # Convert results to a numpy array for analysis
    coverage_results = np.array(coverage_results)

    # Analysis
    mean_coverage = np.mean(coverage_results)
    median_coverage = np.median(coverage_results)
    percentile_95 = np.percentile(coverage_results, 95)

    return mean_coverage, median_coverage, percentile_95, coverage_results


# Example usage with realistic values and adjusted distributions
mean_cov, median_cov, percentile_95, coverage_results = estimate_code_coverage(
    num_test_cases_mean=150, num_test_cases_stddev=30,
    loc_mean=6000, loc_stddev=700,
    test_success_rate_mean=0.85, test_success_rate_stddev=0.05,
    num_simulations=1000000
)

print(f"Mean code coverage: {mean_cov:.4f}")
print(f"Median code coverage: {median_cov:.4f}")
print(f"95th percentile of code coverage: {percentile_95:.4f}")
