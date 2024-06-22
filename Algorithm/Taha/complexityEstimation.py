import numpy as np


def complexity_estimation(min_fp, max_fp, external_inputs: int, external_outputs: int, inquiries: int,
                          external_files: int, internal_files: int, num_simulations=1000):
    """
    Estimate the complexity through Monte Carlo simulation and COCOMO model

    Parameters:
    - min_fp: The min possible amount of FP (Functional Points) in the software project
    - max_fp: The maximum possible amount of FP in the software project
    - external_inputs: The total amount of external inputs the software project will have
    - external_outputs: The total amount of external outputs the software project will have
    - inquiries: The total amount of inquiries the software project will have
    - external_files: The total amount of external files the software project will have
    - internal_files: The total amount of internal files the software project will have
    - num_simulations: The amount of simulations to perform

    Returns:
    - tcp_mean: The mean of all complexity results
    - results: Array of all the complexity results from the simulation
    """

    results = []
    get_mean =[]

    for i in range(num_simulations):
        fp = np.random.uniform(min_fp, max_fp)
        fp_percentage = (fp * 100) / max_fp

        # Calculating UFC (Unadjusted Functional Count)
        if fp_percentage <= 33:  # Checking if FP is in simple range
            ufc = (external_inputs * 3) + (external_outputs * 4) + (inquiries * 3) + (external_files * 5) + (internal_files * 7)
        elif (fp_percentage <= 66) and (fp_percentage > 33):  # Checking if FP is in average range
            ufc = (external_inputs * 4) + (external_outputs * 5) + (inquiries * 4) + (external_files * 10) + (internal_files * 7)
        else:  # Checking if FP is in complex range
            ufc = (external_inputs * 6) + (external_outputs * 7) + (inquiries * 6) + (external_files * 15) + (internal_files * 10)

        # Calculating TCP (Technical Complexity Factor)
        tcp = fp/ufc

        results.append([i, tcp])
        get_mean.append(tcp)

    tcp_mean = np.mean(get_mean)
    tcp_stddev = np.std(get_mean)
    return results, tcp_mean, tcp_stddev


# results, mean, tcpstd = complexity_estimation(87, 168, 6, 8, 1,2, 2, 10000)
# print(results)
# print("TCP Mean =", mean)
# print("TCP Standard Deviation =", tcpstd)
