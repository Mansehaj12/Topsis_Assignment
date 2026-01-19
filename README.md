1. Introduction

This project implements the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) using Python.
TOPSIS is a multi-criteria decision-making method used to rank alternatives based on their distance from an ideal best and an ideal worst solution.
The program is developed as a command-line application and executed using Google Colab, as required in the assignment guidelines.

2. Objective

The objective of this assignment is to:
Implement the TOPSIS algorithm in Python
Accept input through command-line arguments
Perform validation and error handling
Generate an output file containing TOPSIS scores and ranks
Explain methodology, results, and visualization

3. Files in the Repository

topsis.ipynb   – Google Colab notebook
topsis.py     – Command-line Python program
data.csv      – Input dataset
output.csv    – Output file with TOPSIS score and rank
README.md     – Project documentation

4. Input File Format

The first column contains the names of alternatives.
The second to last columns contain numeric values only.
The input file must contain at least 3 columns.

Example (data.csv)
Fund Name,P1,P2,P3,P4,P5
M1,0.67,0.45,6.5,42.6,12.56
M2,0.6,0.36,3.6,53.3,14.47
M3,0.82,0.67,3.8,63.1,17.1

5. Command Line Usage
The program is executed using the following command:
python topsis.py data.csv "1,1,1,1,1" "+,+,-,+,+" output.csv
Parameters:
data.csv – Input data file
"1,1,1,1,1" – Weights (comma-separated)
"+,+,-,+,+" – Impacts (+ for benefit, - for cost)
output.csv – Output result file

6. Error Handling
The program performs the following checks:
Correct number of command-line parameters
Input file existence
Minimum number of columns
Non-numeric values in criteria columns
Matching number of weights, impacts, and criteria
Valid impacts (+ or -)
Appropriate error messages are displayed for invalid inputs.

7. TOPSIS Methodology

Step 1: Normalization
Each criterion value is normalized using vector normalization.

Step 2: Weight Assignment
Normalized values are multiplied by their respective weights.

Step 3: Ideal Best and Ideal Worst
For + impact: maximum is ideal best, minimum is ideal worst
For - impact: minimum is ideal best, maximum is ideal worst

Step 4: Distance Calculation
Euclidean distance is calculated from ideal best and ideal worst.	​

Step 5: Ranking
Alternatives are ranked in descending order of TOPSIS score.

8. Output Format
The output file contains two additional columns:
Topsis Score
Rank

Example (output.csv)
Fund Name,P1,P2,P3,P4,P5,Topsis Score,Rank
M1,0.67,0.45,6.5,42.6,12.56,0.64,2
M5,0.76,0.58,4.8,43,12.29,0.81,1

9. Result Visualization
A bar chart is generated in the Google Colab notebook to visualize the TOPSIS scores of different alternatives.

10. Platform and Tools Used

Google Colab
Python 3
Pandas
NumPy
Matplotlib

11. Conclusion

The TOPSIS algorithm was successfully implemented as a command-line Python program.
The program efficiently ranks alternatives based on multiple weighted criteria and produces accurate results.
