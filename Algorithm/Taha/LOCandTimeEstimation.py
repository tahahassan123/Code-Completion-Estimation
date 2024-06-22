import numpy as np


def time_estimation(loc, project_type: str):

    """
    Estimating Development time using Basic COCOMO model

    Parameters:
    - loc: the LOC (Lines Of Code) of the software project
    - project_type: the type of project, it indicates the difficulty of the project

    Returns:
    - time: the estimated development time

    """

    a, b, c, d = 0, 0, 0, 0
    kloc = loc / 1000
    if project_type == "Organic":
        a, b, c, d = 2.4, 1.05, 2.5, 0.38
    elif project_type == "Semi-detached":
        a, b, c, d = 3, 1.12, 2.5, 0.35
    elif project_type == "Embedded":
        a, b, c, d = 3.6, 1.20, 2.5, 0.32
    else:
        print("project type value incorrect")

    effort = a * pow(kloc, b)
    time = c * pow(effort, d)

    return time


time = time_estimation(1800, "Semi-detached")
print("Time is =", time)


def LOCandDevelopmentTime_estimation(min_loc: int, max_loc: int, language: str,
                                     project_type: str, num_simulations=1000):
    """
    Estimating LOC and Development time using Monte Carlo Simulation and Basic COCOMO model

    Parameters:
    - min_loc: The least possible LOC (Lines Of Code)
    - max_loc: The highest possible LOC
    - language: The language that the code will be written in
    - project_type: The type of project, it indicates the difficulty of the project
    - num_simulations: The amount of simulations to perform

    Returns:
    - loc_results: The array containing all the predicted LOC results
    - loc_mean: The mean of all the predicted LOC results
    - time_results: The array containing all the predicted development time results
    - mean_time: The mean of all the predicted development times results
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

    for i in range(num_simulations):
        avg_loc = np.random.uniform(min_loc, max_loc)
        loc = ((min_loc + (4 * avg_loc) + max_loc) / 6) * language_multipliers.get(language)
        time = time_estimation(loc, project_type)

        loc_results.append([i, loc])
        loc_get_mean.append(loc)
        time_results.append([i, time])
        time_get_mean.append(time)

    loc_mean = int(np.mean(loc_get_mean))
    mean_time = np.mean(time_get_mean)
    return loc_results, loc_mean, time_results, mean_time


loc, mean, time, time_mean = LOCandDevelopmentTime_estimation(100, 5000, "python", "Embedded", 1000)
print(loc)
print("Mean LOC =", mean)
print(time)
print("Mean Time =", time_mean, "Months")


