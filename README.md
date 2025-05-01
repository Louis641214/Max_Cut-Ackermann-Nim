## Problem Set 2
This project contains implementations of three algorithmic problems in Python:

    - A local search algorithm for the Max-Cut problem 
    - The Ackermann function 
    - The Nim Game 

These problems were developed and tested as part of Discrete Mathematics course.


## Installation
Make sure you have Python 3.10+ installed. Then, clone the repository and install the project in editable mode with:

```bash 
pip install -e .
```

This allows you to make changes in the source code without reinstalling the package.


## Requirements
To install the packages, you can run:
```bash
pip install -r requirements.txt
```


## Usage
To run the test scenarios for each problem:

```bash
python tests/tests_max_cut_local_search.py
```
Creates a simple graph, applies the local search Max Cut algorithm, and prints the resulting partition and cut value.

```bash
python tests/tests_ackermann.py
```
Runs tests on the Ackermann function with different values of m and n, demonstrating the extremely fast growth of recursive depth. Another function allows you to visualize it with curves.

```bash
python tests/tests_nim_game.py
```
Allows you to play Nim game


## Author
This project was developed as part of the second problem set in a Discrete Mathematics course by Louis Bonnecaze (Louis641214).