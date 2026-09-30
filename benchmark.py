"""
Benchmarking Script for Router Placement Project

This script:
1. Generates large inputs
2. Runs the baseline and greedy algorithms
3. Measures the number of routers produced
4. Records the number of routers produced
5. Prints the results in a table
"""

import time

from routers import baseline_routers, greedy_routers


INPUT_SIZES = [
    100,
    1_000,
    10_000,
    100_000,
    1_000_000
]

TRIALS = 5


def generate_input(n):
    """
    Generates a sorted list containing n required rooms

    For this benchmark, every room from 1 through n
    requires WiFi

    Parameters:
        n (int):
            number of required rooms

    Returns:
        list[int]:
            Sorted list of required room numbers
    """

    return list(range(1, n + 1))


def measure_time(function, *args):
    """
    Measures how long a function takes to execute

    Parameters:
        function:
            Function being benchmarked

        *args:
            Arguments passed to the function

    Returns:
        tuple:
            The function's result and execution time
    """

    start = time.perf_counter()

    result = function(*args)

    end = time.perf_counter()

    elapsed = end - start

    return result, elapsed


def run_benchmark():
    """
    Runs th benchmark for every input size and prints
    the results
    """

    print(
        f"{'Input Size':>12} | "
        f"{'Baseline Time':>15} | "
        f"{'Greedy Time':>15} | "
        f"{'Baseline Routers':>17} | "
        f"{'Greedy Routers':>15}"
    )

    print("-" * 84)

    for n in INPUT_SIZES:

        rooms = generate_input(n)

        baseline_times = []
        greedy_times = []

        baseline_result = None
        greedy_result = None

        # Runs several trials to reduce timing noise
        for _ in range(TRIALS):

            baseline_result, baseline_time = measure_time(
                baseline_routers,
                rooms
            )

            greedy_result, greedy_time = measure_time(
                greedy_routers,
                rooms,
                n
            )

            baseline_times.append(baseline_time)
            greedy_times.append(greedy_time)

        # Calculates the average execution times
        average_baseline = sum(baseline_times) / TRIALS
        average_greedy = sum(greedy_times) / TRIALS

        print(
            f"{n:>12,} | "
            f"{average_baseline:>15.8f} | "
            f"{average_greedy:>15.8f} | "
            f"{len(baseline_result):>17,} | "
            f"{len(greedy_result):>15,}"
        )


if __name__ == "__main__":
    run_benchmark()