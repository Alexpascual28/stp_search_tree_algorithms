<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
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
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

<code>This project implements several search tree algorithms using Python, designed for solving complex combinatorial problems with a focus on optimality and efficiency. The project is structured to handle various problems using uniform cost, depth-first, breadth-first, and A* search algorithms, including an optional heuristic component.</code>

---

##  Directory Structure

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
| [tree.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/tree.py)                 | <code>► INSERT-TEXT-HERE</code> |
| [queue_search.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/queue_search.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>Problems.Fill_list_problem</summary>

| File                                                                                                                                    | Summary                         |
| ---                                                                                                                                     | ---                             |
| [FillTester.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/Problems/Fill_list_problem/FillTester.py)   | <code>► INSERT-TEXT-HERE</code> |
| [FillProblem.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/Problems/Fill_list_problem/FillProblem.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>Problems.Fill_array_problem</summary>

| File                                                                                                                                         | Summary                         |
| ---                                                                                                                                          | ---                             |
| [FillArrayTest.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/Problems/Fill_array_problem/FillArrayTest.py) | <code>► INSERT-TEXT-HERE</code> |
| [FillArray.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/Problems/Fill_array_problem/FillArray.py)         | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>Problems.Knight_problem</summary>

| File                                                                                                                                                   | Summary                         |
| ---                                                                                                                                                    | ---                             |
| [knights_tour.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/Problems/Knight_problem/knights_tour.py)                 | <code>► INSERT-TEXT-HERE</code> |
| [knight_search_tester.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/Problems/Knight_problem/knight_search_tester.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>Problems.Eight_problem</summary>

| File                                                                                                                                  | Summary                         |
| ---                                                                                                                                   | ---                             |
| [eight_puzzle.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/Problems/Eight_problem/eight_puzzle.py) | <code>► INSERT-TEXT-HERE</code> |
| [eight_tester.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/Problems/Eight_problem/eight_tester.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>201255350</summary>

| File                                                                                                                           | Summary                         |
| ---                                                                                                                            | ---                             |
| [tester_outcome.txt](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/201255350/tester_outcome.txt) | <code>► INSERT-TEXT-HERE</code> |
| [queen_cover.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/201255350/queen_cover.py)         | <code>► INSERT-TEXT-HERE</code> |
| [qc_tester.py](https://github.com/Alexpascual28/stp_search_tree_algorithms.git/blob/master/201255350/qc_tester.py)             | <code>► INSERT-TEXT-HERE</code> |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version x.y.z`

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
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run stp_search_tree_algorithms using the command below:
> ```console
> $ python main.py
> ```

###  Tests

> Run the test suite using the command below:
> ```console
> $ pytest
> ```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

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

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
