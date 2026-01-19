import sys
import pandas as pd
import numpy as np
import os

def main():
    if len(sys.argv) != 5:
        print("Error: Incorrect number of parameters")
        sys.exit(1)

    input_file = sys.argv[1]
    weights_input = sys.argv[2]
    impacts_input = sys.argv[3]
    output_file = sys.argv[4]

    if not os.path.isfile(input_file):
        print("Error: File not found")
        sys.exit(1)

    data = pd.read_csv(input_file)

    if data.shape[1] < 3:
        print("Error: Input file must contain at least 3 columns")
        sys.exit(1)

    criteria = data.iloc[:, 1:]

    try:
        criteria = criteria.astype(float)
    except ValueError:
        print("Error: Non-numeric data found")
        sys.exit(1)

    weights = list(map(float, weights_input.split(",")))
    impacts = impacts_input.split(",")

    if len(weights) != criteria.shape[1] or len(impacts) != criteria.shape[1]:
        print("Error: Weights, impacts and columns mismatch")
        sys.exit(1)

    if not all(i in ['+', '-'] for i in impacts):
        print("Error: Impacts must be + or -")
        sys.exit(1)

    norm = criteria / np.sqrt((criteria ** 2).sum())
    weighted = norm * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    d_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    d_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    scores = d_worst / (d_best + d_worst)

    data["Topsis Score"] = scores
    data["Rank"] = data["Topsis Score"].rank(ascending=False, method="dense").astype(int)

    data.to_csv(output_file, index=False)
    print("TOPSIS analysis completed.")

if __name__ == "__main__":
    main()
