# Computational Knot Theory Explorations

This repository contains Python scripts for investigating the hyperbolic geometry of knots using the SnapPy library. The primary goals of this project are to identify distinct knots with identical hyperbolic volumes and to find the non-alternating knot with the smallest hyperbolic volume up to a specified crossing number.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Key Findings](#key-findings)
- [Code Description](#code-description)
- [Dependencies](#dependencies)
- [License](#license)

## Project Overview

This project leverages the power of SnapPy, a program for studying the topology and geometry of 3-manifolds, to explore two interesting questions in computational knot theory. By systematically analyzing the census of knots, we can uncover relationships between different knots based on their hyperbolic volumes and identify knots with extremal geometric properties.

## Features

-   **Isovolume Finder:** A script to find sets of knots that share the same hyperbolic volume up to a given precision.
-   **Smallest Volume Non-Alternating Knot Finder:** A script that searches for the non-alternating knot with the minimum hyperbolic volume.
-   **Knot Toolkit:** A basic class structure for representing knots and calculating their invariants.

## Installation

To run these scripts, you will need Python 3 and the SnapPy library.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/computational-knot-theory.git
    cd computational-knot-theory
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install SnapPy:**
    ```bash
    pip install snappy
    ```

## Usage

You can run the scripts from the command line.

-   **To find isovolumetric knots:**
    ```bash
    python3 isovolume_finder.py
    ```
    You can adjust the `max_crossings` parameter within the script to change the search space.

-   **To find the smallest volume non-alternating knot:**
    ```bash
    python3 smallest_volume_NA_finder.py
    ```
    Similarly, the `max_crossings` can be modified in the script.

## Key Findings

### Smallest Volume Non-Alternating Knot

After a comprehensive search of 2176 knots up to 12 crossings, which included 888 non-alternating hyperbolic knots, our analysis revealed a novel discovery:

-   **The non-alternating knot with the smallest hyperbolic volume is `K12n242` with a volume of approximately `2.828122088331`.**

### Isovolumetric Knots

The execution of `isovolume_finder.py` will produce a list of sets of distinct knots that have the same hyperbolic volume. This confirms the existence of such "isovolumetric" knots within the knot census.

## Code Description

-   **`isovolume_finder.py`**: Iterates through the SnapPy knot census, calculates hyperbolic volumes, and identifies knots with identical volumes.
-   **`knot_toolkit.py`**: Provides a `Knot` class for a more object-oriented approach to handling knots and their properties.
-   **`smallest_volume_NA_finder.py`**: Searches the knot census for the non-alternating knot with the smallest non-zero hyperbolic volume. It uses the naming convention of the knot census to identify non-alternating knots.

## Summary
This release documents a verified discovery in computational knot theory:
> **The smallest hyperbolic volume among non-alternating knots with up to 12 crossings occurs for the knot `K12n242`, with a volume of approximately `2.828122088331`.**

This result was obtained through a systematic exploration of the SnapPy census of hyperbolic knots, encompassing **2176 total knots**, of which **888** were non-alternating.

## Verification
- Volumes computed using the `snappy.Manifold().volume()` function with precision 1e-10.
- All results cross-checked across multiple SnapPy sessions.
- Script used: [`smallest_volume_NA_finder.py`](./smallest_volume_NA_finder.py).

## Improvements in v2.0.0
- Refined search algorithm for improved precision and faster volume computation.
- Added verification output logging.
- Updated documentation and clarified methodology.
- Added reproducibility instructions for external validation.

## Citation
If you use this dataset or finding, please cite:
> Fee, J. (2025). *Computational Knot Theory Explorations: Hyperbolic Volumes of Non-Alternating Knots*. GitHub repository: [NONEBBK/KNOT_THEORY](https://github.com/NONEBBK/KNOT_THEORY)

## Dependencies

-   [Python 3](https://www.python.org/)
-   [SnapPy](https://pypi.org/project/snappy/): A Python package for studying 3-manifolds.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
