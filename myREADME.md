Completing a fuzzing loop:

#We are to implement a custom mutation operator along with a coverage metric operator (this operator will determines if there is a change/improvement in coverage metric when a turtle program is executed with mutated inputs.) for the fuzzer loop in `fuzzSubmission.py` file.

#Mainly 3 functions are to be implemented:

    • def compareCoverage(curr_metric, total_metric)
    • def mutate(input_data) 
    • def updateTotalCoverage(curr_metric, total_metric)


compareCoverage:
Takes in two arguments: curr_metric and total_metric
If curr_metric is subset of total_metric, return False as no extra coverage is obtained, Otherwise return True (Extra coverage gained and updateTotalCoverage will be called).

updateTotalCoverage:
Append any new statement covered in total_metric.

mutate:
Mutating the seed input in order to gain coverage

#Installations:

sudo apt-get install graphviz graphviz-dev
pip install pygraphviz

pip install numpy
pip install networkx
pip install z3

#Running the program:
cd KachuaCore

./kachua.py -t 20 --fuzz testcases/test1.tl -d '{":x": 5, ":y": 100}'