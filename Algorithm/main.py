from Taha import costEstimation, complexityEstimation, LOCandTimeEstimation
from Omer import codeCoverage, numberOfPeople, projectRisk


# Assumptions to be used in front-end
salary = 50000  # Salary of a single developer
productivity_new = 50  # LOC (Lines Of Code) written by a new programmer
productivity_experienced = 80  # LOC (Lines Of Code) written by an experienced programmer
productivity_professional = 100  # LOC (Lines Of Code) written by a professional programmer


def main(salary: int, productivity: int, min_loc: int, max_loc: int, coding_language: str, project_type: str,
         min_fp: int, max_fp: int, external_inputs: int, external_outputs: int, inquiries: int, external_files: int,
         internal_files: int, min_test_cases: int,max_test_cases:int, min_success_rate: float,max_success_rate:float, min_internal_cost: int, max_internal_cost: int,
         external_resources=False, min_external_cost=0, max_external_cost=0, num_simulations=1000):

    """
    Estimate development time, LOC, complexity, cost, code coverage, number of developers and project risk using a combination of monte carlo simulations and COCOMO model

    Parameters:
    - salary: The amount of salary for a single developer
    - productivity: The amount of lines a developer writes in a single day

    - min_loc: The least possible LOC (Lines Of Code)
    - max_loc: The highest possible LOC
    - coding_language: The language that the code will be written in
    - project_type: The type of project, it indicates the difficulty of the project

    - min_fp: The min possible amount of FP (Functional Points) in the software project
    - max_fp: The maximum possible amount of FP in the software project
    - external_inputs: The total amount of external inputs the software project will have
    - external_outputs: The total amount of external outputs the software project will have
    - inquiries: The total amount of inquiries the software project will have
    - external_files: The total amount of external files the software project will have
    - internal_files: The total amount of internal files the software project will have

    - num_test_cases: Mean number of test cases.
    - loc_mean: Mean size of codebase (e.g., LOC).
    - test_success_rate: Mean success rate of test cases (0 to 1).

    - min_internal_costs: The maximum possible internal costs involved in developing the software project
    - max_internal_costs: The minimum possible internal costs involved in developing the software project
    - external_resources: Will the project have external resources to take into account for?
    - min_external_costs: The minimum possible external costs involved in developing the software project
    - max_external_costs: The maximum possible external costs involved in developing the software project

    - num_simulations: Number of Monte Carlo iterations (default is 1000).

    Returns:
    - loc_array: 2D array containing all the loc predictions
    - loc_mean: The mean of all the loc results
    - time_array: 2D array containing all the development time predictions
    - time_mean: The mean of all the development time results
    - complexity_array: 2D array containing all the complexity predictions
    - complexity_mean: The mean of all the complexity results
    - num_people_array: 2D array containing all the number of developer predictions
    - num_people_mean: The mean of all the number of developer results
    - cost_array: 2D array containing all the cost predictions
    - cost_mean: The mean of all the number of cost results
    - code_coverage_array: 2D array containing all the code coverage predictions
    - code_coverage_mean: The mean of all the code coverage results
    - risk_array: 2D array containing all the risk predictions
    - risk_mean: The mean of all the risk percentage results

    """

    # Estimating LOC and Development time using Monte Carlo Simulation and Basic COCOMO model
    loc_array, loc_mean, time_array, time_mean, loc_stddev, time_stddev = LOCandTimeEstimation.LOCandDevelopmentTime_estimation(min_loc, max_loc, coding_language, project_type, num_simulations)

    # Estimate the complexity through Monte Carlo simulation and COCOMO model
    complexity_array, complexity_mean, complexity_stddev = complexityEstimation.complexity_estimation(min_fp, max_fp, external_inputs, external_outputs, inquiries, external_files, internal_files, num_simulations)

    # Perform a Monte Carlo simulation to estimate the number of people required for a project without considering cost.
    num_people_array, num_people_mean, num_people_stddev = numberOfPeople.estimate_number_of_people(num_simulations, time_mean, productivity, 1, loc_mean)

    # Estimating the total cost of the software project
    cost_array, cost_mean, cost_stddev = costEstimation.cost_estimation(salary, num_people_mean, min_internal_cost, max_internal_cost, num_simulations, external_resources, min_external_cost, max_external_cost)

    # Estimate code coverage using Monte Carlo simulation
    code_coverage_array, code_coverage_mean = codeCoverage.estimate_code_coverage(min_test_cases, max_test_cases, loc_mean, loc_stddev, min_success_rate, max_success_rate, num_simulations)

    # Estimate project risk using Monte Carlo simulation
    risk_array, risk_mean = projectRisk.estimate_project_risk(cost_mean, cost_stddev, loc_mean, loc_stddev, time_mean, time_stddev, num_people_mean, num_people_stddev, complexity_mean, complexity_stddev, num_simulations)

    return (
        loc_array, loc_mean,
        time_array, time_mean,
        complexity_array, complexity_mean,
        num_people_array, num_people_mean,
        cost_array, cost_mean,
        code_coverage_array, code_coverage_mean,
        risk_array, risk_mean
        )
