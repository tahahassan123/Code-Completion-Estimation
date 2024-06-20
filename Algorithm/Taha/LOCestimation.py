import numpy as np
import developmentTimeEstimation as devtime


def LOCandDevelopmentTime_estimation(min_LOC: int, max_LOC: int, language: str,
                                     project_type: str, simulations: int):
    """
    Estimating LOC and Development time using Monte Carlo Simulation and Basic COCOMO model

    Parameters:
    - min_LOC: the least possible LOC (Lines Of Code)
    - max_LOC: the highest possible LOC
    - language: the language that the code will be written in
    - project_type: the type of project, it indicates the difficulty of the project
    - simulations: the amount of simulations to perform

    Returns:
    - loc_results: the array containing all the predicted LOC results
    - mean_LOC: the mean of all the predicted LOC results
    - time_results: the array containing all the predicted development time results
    - mean_time: the mean of all the predicted development times results
    """

    loc_results = []
    loc_get_mean = []
    time_results = []
    time_get_mean = []

    # Multipliers for estimating LOC depending on what high-level language used
    language_multipliers = {
        "python": 1,
        "C++": 1.566,
        "C": 1.643,
        "Java": 1.653,
        "C#": 1.698,
        "JavaScript": 1.41
    }

    for i in range(simulations):
        avg_LOC = np.random.uniform(min_LOC, max_LOC)
        LOC = ((min_LOC + (4 * avg_LOC) + max_LOC) / 6) * language_multipliers.get(language)
        time = devtime.time_estimation(LOC, project_type)
        loc_results.append([i, LOC])
        loc_get_mean.append(LOC)
        time_results.append([i, time])
        time_get_mean.append(time)

    mean_LOC = int(np.mean(loc_get_mean))
    mean_time = np.mean(time_get_mean)
    return loc_results, mean_LOC, time_results, mean_time


loc, mean, time, time_mean = LOCandDevelopmentTime_estimation(100, 5000, "python", "Embedded", 1000)
print(loc)
print("Mean LOC =", mean)
print(time)
print("Mean Time =", time_mean, "Months")
