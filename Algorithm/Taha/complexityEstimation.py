import numpy as np


def complexity_estimation(max_fp, min_fp, external_inputs: int, external_outputs: int, inquiries: int,
                          external_files: int, internal_files: int, simulations: int):
    results = []
    get_mean =[]

    for i in range(simulations):
        fp = np.random.uniform(max_fp, min_fp)
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
    return results, tcp_mean

results, mean = complexity_estimation(87, 168, 6, 8, 1,2, 2, 10000)
print(results)
print("TCP Mean =",mean)