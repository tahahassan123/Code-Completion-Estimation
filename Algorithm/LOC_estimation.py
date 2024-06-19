import numpy as np

def LOC_estimation(min_LOC: int, max_LOC: int, language: str, simulations: int):

    """
    Estimating LOC using Monte Carlo Simulation

    Parameters:
    - min_LOC: the least possible LOC (Lines Of Code)
    - max_LOC: the highest possible LOC
    - language: the language that the code will be written in
    - simulations: the amount of simulations to perform

    Returns:
    - results: the array containing all the predicted results
    - mean_LOC: the mean of all the predicted LOC results
    """
    results = []
    get_mean = []

    # Multipliers for estimating LOC
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
        results.append([i, LOC])
        get_mean.append(LOC)

    mean_LOC = int(np.mean(get_mean))
    return results, mean_LOC


results, mean = LOC_estimation(100, 5000, "python", 1000)
print("Mean LOC =", mean)
