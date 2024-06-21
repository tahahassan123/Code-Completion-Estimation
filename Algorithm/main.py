from Taha import costEstimation, complexityEstimation, LOCandTimeEstimation
from Omer import codeCoverage, numberOfPeople, projectRisk


# Assumptions to be used in front-end
salary = 50000  # Salary of a single developer
productivity_new = 50  # LOC (Lines Of Code) written by a new programmer
productivity_experienced = 80  # LOC (Lines Of Code) written by an experienced programmer
productivity_professional = 100  # LOC (Lines Of Code) written by a professional programmer


def main(salary: int, productivity: int, min_loc: int, max_loc: int, coding_language: str, project_type: str,
         min_fp: int, max_fp: int, external_inputs: int, external_outputs: int, inquiries: int, external_files: int,
         internal_files: int, num_simulations: int):

    # Estimating LOC and Development time using Monte Carlo Simulation and Basic COCOMO model
    loc_array, loc_mean, time_array, time_mean = LOCandTimeEstimation.LOCandDevelopmentTime_estimation(min_loc, max_loc, coding_language, project_type, num_simulations)

    # Estimate the complexity through Monte Carlo simulation and COCOMO model
    complexity_array, complexity_mean = complexityEstimation.complexity_estimation(min_fp, max_fp, external_inputs, external_outputs, inquiries, external_files, internal_files, num_simulations)

    # Perform a Monte Carlo simulation to estimate the number of people required for a project without considering cost.
    numberOfPeople.estimate_number_of_people(num_simulations, time_mean, productivity)

    # Estimating the total cost of the software project