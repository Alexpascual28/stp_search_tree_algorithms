<p align="center">
  <img src="https://www.svgrepo.com/show/351868/chess-queen.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">STP Search-Tree Algorithm Problem Solver</h1>
</p>
<p align="center">
    <em><code>Python Search Tree data structure for implementation of Uniform Cost, Depth First, Breadth First, A* algorithms, with optional heuristic implementation. Multiple problems are included as examples this system can solve.</code></em>
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Directory Description](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
- [ Theory](#theory)
- [ Contributing](#-contributing)
</details>
<hr>

##  Overview

<code>This project implements several search tree algorithms using Python, designed for solving complex combinatorial problems with a focus on optimality and efficiency. The project is structured to handle various problems using uniform cost, depth-first, breadth-first, and A* search algorithms, including an optional heuristic component.</code>

<code>The objective of this report is to show the implementation and results of a chess domination puzzle using search algorithms. A domination problem is a type of chess puzzle in which the minimum number of pieces for a specific piece must be found so that they cover (attack or occupy) the whole chessboard.</code>

<code>In this case the program must find the minimum number of queens necessary to cover all of the squares of an m * n chessboard, as well as displaying the way in which these queens should be laid out in the board.</code>

<code>More info cand be found below in [Theory](#theory) and in [201255350.pdf](https://github.com/Alexpascual28/stp_search_tree_algorithms/blob/main/201255350/201255350.pdf)</code>

---

##  Directory Description

The project includes the following main directories and files:

* **/201255350/**: Contains the main program (qc_tester.py) solving the chess board queen coverage problem using A* with a heuristic function. Supporting files:
* `queen_cover.py`: Defines the problem specifics, including state representations and transitions.
* `qc_tester.py`: Contains the tests for the queen coverage problem.
* **/Problems/**: Contains directories for additional problems, each with its own model and tester:
  * **Eight_problem/**: Implementation of the Eight Puzzle problem.
  * **Fill_array_problem/**: Focuses on solving array fill problems.
  * **Fill_list_problem/**: Dedicated to list fill problems.
  * **Knight_problem/**: Solves the Knight's Tour problem on a chess board.
* `queue_search.py`: Core file defining the queue management and search strategies.
* `tree.py`: Provides the data structure support for implementing the search trees.

---

##  Repository Structure

```sh
└── stp_search_tree_algorithms/
    ├── 201255350
    │   ├── 201255350.pdf
    │   ├── qc_tester.py
    │   ├── queen_cover.py
    │   └── tester_outcome.txt
    ├── Problems
    │   ├── Eight_problem
    │   ├── Fill_array_problem
    │   ├── Fill_list_problem
    │   └── Knight_problem
    ├── README.md
    ├── queue_search.py
    └── tree.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                                           | Summary                         |
| ---                                                                                                            | ---                             |
| [tree.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/tree.py)                 | <code> </code> |
| [queue_search.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/queue_search.py) | <code> </code> |

</details>

<details closed><summary>Problems.Fill_list_problem</summary>

| File                                                                                                                                    | Summary                         |
| ---                                                                                                                                     | ---                             |
| [FillTester.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/Problems/Fill_list_problem/FillTester.py)   | <code> </code> |
| [FillProblem.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/Problems/Fill_list_problem/FillProblem.py) | <code> </code> |

</details>

<details closed><summary>Problems.Fill_array_problem</summary>

| File                                                                                                                                         | Summary                         |
| ---                                                                                                                                          | ---                             |
| [FillArrayTest.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/Problems/Fill_array_problem/FillArrayTest.py) | <code> </code> |
| [FillArray.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/Problems/Fill_array_problem/FillArray.py)         | <code> </code> |

</details>

<details closed><summary>Problems.Knight_problem</summary>

| File                                                                                                                                                   | Summary                         |
| ---                                                                                                                                                    | ---                             |
| [knights_tour.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/Problems/Knight_problem/knights_tour.py)                 | <code> </code> |
| [knight_search_tester.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/Problems/Knight_problem/knight_search_tester.py) | <code> </code> |

</details>

<details closed><summary>Problems.Eight_problem</summary>

| File                                                                                                                                  | Summary                         |
| ---                                                                                                                                   | ---                             |
| [eight_puzzle.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/Problems/Eight_problem/eight_puzzle.py) | <code> </code> |
| [eight_tester.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/Problems/Eight_problem/eight_tester.py) | <code> </code> |

</details>

<details closed><summary>201255350</summary>

| File                                                                                                                           | Summary                         |
| ---                                                                                                                            | ---                             |
| [tester_outcome.txt](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/201255350/tester_outcome.txt) | <code> </code> |
| [queen_cover.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/201255350/queen_cover.py)         | <code> </code> |
| [qc_tester.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/201255350/qc_tester.py)             | <code> </code> |

</details>

---

##  Getting Started

**Prerequisites**

Ensure you have Python 3.6 or higher installed on your system. No external libraries are required as the project uses standard Python libraries.

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the stp_search_tree_algorithms repository:
>
> ```console
> $ git clone https://github.com/Alexpascual28/stp_search_tree_algorithms.git
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd stp_search_tree_algorithms
> ```

###  Usage

<h4>From <code>source</code></h4>

> To execute a specific problem, navigate to its directory and run the corresponding tester file. For example, to run the Queen Coverage problem:

> ```console
> $ python /201255350/qc_tester.py
> ```
> This will execute the tests defined in the qc_tester.py script using the A* algorithm to solve the Queen Coverage problem with various board sizes as specified within the script.

And to run the Knight Coverage problem solver:

> ```console
> $ cd /Problems/Knight_problem
> $ python knight_search_tester.py
> ```
>
> This will execute the knight problem solver using a depth-first search strategy. The script is set up to run the Knight's Tour problem on various board sizes, which are defined within the script.

---

##  Theory

### Queen Coverage Problem Explanation

The "Queen Coverage Problem" involves placing the minimum number of queens on an *m x n* chess board such that all squares are either occupied or controlled by one or more queens. A queen in chess can move any number of squares vertically, horizontally, or diagonally. The challenge is to determine the fewest queens needed to cover the board completely.

**How the Problem is Represented**

Here's a simple representation of a 4x4 chess board:

```python
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]
```

* `0` indicates an empty square.
* `1` would indicate a square occupied by a queen.
* An asterisk (`*`) indicates a controlled square.

When queens are placed, for example at positions (0,0), (2,1) and (3,2), the board would look like this:

```python
[1, *, *, *],  # Queens occupy squares with a 1 and controls entire row and diagonals with asterisk
[*, *, 1, *],
[*, *, *, 1],
[*, 0, *, *],  # Square (1, 3) remains uncontrolled in this configuration
```

The state might then be described as having certain squares controlled or occupied, and the next possible actions would be placements that don't overlap with or are redundant to the control of this queen.

As explained in the comments in `201255350/queen_cover.py`, the chosen state representation is formed by four variables. The first one stores the number of squares controlled by the current state, the second one stores a list with the controlled squares’ coordinates, the third stores the position of the current queen, and the fourth one stores the current board layout.

```python
# Representation of a state:
# (number_controlled_squares, list_controlled_squares, (current_x_pos, current_y_pos),  full_board_state)
# So on a 4x4 board after placing two queens we might have a state such as:
#
# (13, [(0, 0), (1, 0), (2, 0), (3, 0),
#       (0, 1), (1, 1), (2, 1), (3, 1),
#       (0, 2), (1, 2), (2, 2),
#       (0, 3)          (2, 3)          ], (1,0), [[0,0,1,0],
#                                                  [1,0,0,0],
#                                                  [0,0,0,0],
#                                                  [0,0,0,0]] )
#
# Since the queens are controlling 13 squares (the ones marked with an asterisk as follows):
#
# [*,*,*,*],
# [*,*,*,*],
# [*,*,*,0],
# [*,0,*,0]
```

**A-star Search Tree Algorithm**

The A* search algorithm is used to solve the queen coverage problem efficiently. It expands the most promising node first based on a cost function and a heuristic. Here's how it can be used for the queen coverage problem:

* **Initial State:** The board is empty.
* **Goal State:** All squares are controlled by queens.
* **Successor Function:** Generates new states by placing a queen in a valid position that maximizes the number of newly controlled squares.
* **Heuristic Function:** Estimates the fewest remaining queens needed to cover all empty squares. A simple heuristic might be the count of empty squares divided by the maximum number a single queen could control from the most advantageous position.

*Steps:*

1. Start with an empty board.
2. At each step, calculate the potential of each possible move using the heuristic function.
3. Place a queen on the position that offers the highest reduction in the heuristic cost.
4. Repeat until the board is fully covered.

The efficiency of A* in this problem lies in its ability to preferentially explore board configurations that are closer to the goal, significantly reducing the number of configurations that need to be examined compared to uninformed search strategies like breadth-first or depth-first search.

A more detailed explanation about the succesor function can be found in [201255350.pdf](https://github.com/Alexpascual28/stp_search_tree_algorithms/blob/main/201255350/201255350.pdf).

**Understanding the Output**

The script redirects its output to a file named `tester_outcome.txt` in the same directory. This file will contain the results of the tests, including the board configurations and the number of queens used. To view the results, open this file using any text editor or use the following command in your CLI:

> ```console
> $ cat tester_outcome.txt
> ```

### Knight Coverage Problem Explanation

The "Knight Coverage Problem" is a challenge that involves moving a knight on a chess board such that it visits every square exactly once. This is a variation of the classic **"Knight's Tour"** problem. The knight in chess moves in an L-shape: two squares in one direction and then one square perpendicular, or one square in one direction and then two squares perpendicular.

**How the Problem is Represented**

Let's illustrate a small 3x3 chess board:

```python
[0, 0, 0],
[0, 0, 0],
[0, 0, 0]
```
* `0` indicates an unvisited square.
* Each subsequent number will indicate the move number of the knight.

For instance, if the knight starts at the top-left corner and moves to the middle on its first move, the board might look like this:

```python
[1, 0, 0],
[0, 0, 0],
[0, 2, 0]
```

**Depth First Search Tree Algorithm**

Depth First Search (DFS) is a recursive algorithm that explores as far as possible along each branch before backtracking. This makes it a suitable choice for solving the Knight's Tour problem because it allows exploring all potential paths the knight can take from a given position.

*Components*

* **Initial State:** Position the knight on the starting square.
* **Goal State:** All squares are visited exactly once.
* **Successor Function:** Generates new states by moving the knight to all possible L-shaped moves that lead to squares not yet visited.
* **Backtracking:** If a move leads to a state where no further moves are possible and the goal is not achieved, backtrack to explore different paths from previous positions.

*Steps to Solve Using DFS*

1. Start with the knight on any square (often a corner is chosen for simplicity).
2. Explore all possible knight moves from this square.
3. Move the knight to a new square, mark the move number on that square.
4. Recursively continue this process from the new square.
5. If a dead-end is reached (no unvisited adjacent squares), backtrack by undoing the last move and try the next possibility.

DFS is particularly useful here because it inherently handles backtracking: when a dead-end is reached, it automatically returns to the previous step to try alternative moves. This systematic exploration ensures that if a solution exists, DFS will find it, although it may not be the most efficient path if the board is large.

### Queue Search Module

The `queue_search.py` module provides a generic queue-based search framework that you can use to solve problems using different search strategies. It is used as the generator and solver in all of problem testers, by the use of the `search` function. Below, I'll explain how the `search` function works and how you can use it to implement various search algorithms for different problems.

**Understanding the `search` Function**

The `search` function is the main interface in `queue_search.py` for performing searches. It is structured to handle a variety of search strategies and manage the complexities of different problem spaces using a consistent format. Here are the components it handles:

1. **Problem Specification**: This is provided as a tuple containing:

* `initialise_func`: A function to initialize the problem (if necessary).
* `problem_info_func`: A function that prints basic information about the problem.
* `initial_state`: The starting state of the problem.
* `poss_act_func`: A function that returns a list of possible actions from a given state.
* `successor_func`: A function that, given an action and a state, returns the resulting state.
* `goal_test_func`: A function that checks if a given state meets the goal criteria.

2. **Strategy**: Specifies the search strategy to use. It can be:

* `'breadth_first'`: Explores the shallowest nodes first.
* `'depth_first'`: Explores the deepest nodes first.
* `'randomised_depth_first'`: Similar to depth-first but shuffles the nodes before adding them to the stack.
* `('uniform_cost', cost_func)`: Considers the path cost to each node, choosing the path with the lowest cost next.
* `('best_first', heuristic_func)`: Uses a heuristic to guess the best path to the goal without considering the path cost.
* `('A_star', heuristic_func, cost_func)`: Combines both path cost and heuristic to find the most promising path.
* If `cost_func` is omitted in an A* strategy, it defaults to using the path length.

3. **MAX_NODES**: Limits the number of nodes explored during the search to prevent infinite loops or excessive computation.

4. **OPTIONS**: A list that can include:

* `'node_dots'`: Prints a dot for every node expanded.
* `'loop_check'`: Checks for and skips states that have already been visited.
* `'print_loops'`: Indicates when a loop (repeated state) is detected.
* `'print_ties'`: Shows when two nodes have the same cost or heuristic score.

**Example of Using the `search` Function**

Suppose you have a problem where you want to find a path in a maze. You would define the necessary functions for initializing the problem, determining possible actions, computing successor states, and testing for the goal. Here's a simplified way you might call the `search` function:

```python
def initialize_maze():
    # Code to set up the maze
    pass

def print_maze_info():
    print("Maze dimensions: 10x10")

def get_initial_state():
    return (0, 0)  # Starting at the top-left corner

def possible_actions(state):
    # Returns list of actions based on maze configuration
    pass

def successor_state(action, state):
    # Returns new state after applying action
    pass

def is_goal_state(state):
    return state == (9, 9)  # Goal is bottom-right corner

maze_problem = (initialize_maze, print_maze_info, get_initial_state(), possible_actions, successor_state, is_goal_state)

# Running a breadth-first search on the maze
search(maze_problem, 'breadth_first', 1000, ['node_dots'])
```

This code sets up a basic framework for solving a maze problem using breadth-first search. You can adjust the problem tuple and strategy as needed for different problems and search algorithms. This flexible and modular approach allows for easy experimentation and adaptation to various types of problem spaces.

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/issues)**: Submit bugs found or log feature requests for the `stp_search_tree_algorithms` project.
- **[Submit Pull Requests](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Alexpascual28/stp_search_tree_algorithms.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/Alexpascual28/stp_search_tree_algorithms.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Alexpascual28/stp_search_tree_algorithms.git">
   </a>
</p>
</details>

---
