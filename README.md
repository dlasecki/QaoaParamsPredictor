[![Unitary Fund](https://img.shields.io/badge/Supported%20By-UNITARY%20FUND-brightgreen.svg?style=for-the-badge)](http://unitary.fund)

# QaoaParamsPredictor

This project aims to provide good input parameters for variational quantum algorithms for various types of combinatorial
optimization problems. It uses machine learning techniques to skip computationally expensive classical optimization over
a parameter's space while still producing a reasonably good solution. The current focus of the project is the Quantum
Approximate Optimization Algorithm (QAOA) with a default ansatz (see Fahri et al. https://arxiv.org/abs/1411.4028).

The project provides the possibility of running QAOA with a classical optimization loop for many combinatorial
optimization problems for various parameters (depth of a quantum circuit, number of random initial points in the
parameter's space, graph classes, graph sizes etc.), using many classical optimizers and saving results to json files.
Therefore, one can generate training data that could later serve for preparing machine learning models.

Another part of the project provides a possibility of training machine learning models using a Kernel Density Estimation
algorithm. The idea is to train Kernel Density Estimation algorithm on a big number of good input parameters sets,
specific to an optimization problem and the class of a graph, obtained by running the process described above. Models
can be then serialized.

Currently, the following optimization problems are supported: MaxCut, Graph Partition, Vertex Cover, Stable Set, for the
following classes of graphs: Erdos-Renyi, caveman, barbell, ladder.

The project relies on the quantum computing library Qiskit where quantum algorithm implementations come from.

IN PROGRESS: Evaluation of created machine learning models on a test set.

The project is funded by the Unitary Fund.