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