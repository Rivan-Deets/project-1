ROUTER PLACEMENT EVALUATION

1. Code Implementation

The problem asks for the minimum number of routers needed to provide WiFi to every room that requires it in a single-corridor dormitory.

A router placed in room i provides WiFi to room i, as well as rooms i - 1 and i + 1.

This implementation contains two solutions: Baseline and Greedy

- Baseline Solution

The baseline solution places a router in every room that requires WiFi. This solution is simple and guarantees coverage, but it does not attempt to reduce the number of routers.

ex. 
Required rooms: [1, 2, 4, 5, 8, 9, 10]
Baseline routers: [1, 2, 4, 5, 8, 9, 10]

- Greedy Solution

The greedy solution processes the required rooms from left to right. For the leftmost required room that has not been covered, the algorithm places a router as far to the right as possible while still covering that room.

For a room r, a router can cover it if placed at:

r - 1, r, or r + 1

Therefore, the algorithm attempts to place the router at r + 1. If r + 1 is outside the building, the router is placed in room N, the final room of the building. 

After placing the router, the algorithm skips every required room that is covered by that router.

ex. (from project description)
Required rooms: [1, 2, 4, 5, 8, 9, 10]
Greedy routers: [2, 5, 9]

The three routers cover all seven required rooms. This is because the leftmost uncovered room must be covered by a router located at r - 1, r, or r + 1. Choosing the furthest possible position to the right allows the router to cover as many future required rooms as possible. Repeating this process produces the minimum number of routers for this one-dimensional problem.

2. Testing Suite

A separate test suite was created in test_routers.py to verify that the algorithms work correctly.

The tests included:

- Empty input: Verifies that no required rooms produces no routers

- Single room: Tests the smallest non-empty input

- Consecutive rooms: Tests several rooms requiring WiFi in a row

- Two rooms with one gap: Verifies that one router can cover rooms such as [2, 4]

- Separated rooms: Tests rooms that cannot share a router

- Professor's example: Verifies the expected result [2, 5, 9]

- Large consecutive group: Tests a larger group of required rooms

- Baseline coverage: Verifies that the baseline covers every required room

- Greedy vs. baseline: Verifies that the greedy solution uses fewer routers on the example

- General coverage cases: Tests several different room arrangements

After running the test suite, all tests should pass. This confirms that the implemented algorithms correctly handles the tested normal cases and edge cases, and that the greedy solution produces valid coverage.

3. Benchmarking

The benchmarking script in benchmark.py measures the execution time of both algorithms as the number of required rooms increases.

Each input contains consecutive required rooms from 1 through N. Five trials were performed for each input size, and the average execution time was recorded.

The benchmark used the following input sizes:

100
1,000
10,000
100,000
1,000,000

- Benchmark Results

Input Size |   Baseline Time |     Greedy Time |  Baseline Routers |  Greedy Routers
------------------------------------------------------------------------------------
         100 |      0.00000428 |      0.00004386 |               100 |              34
       1,000 |      0.00000614 |      0.00043478 |             1,000 |             334
      10,000 |      0.00006426 |      0.00319088 |            10,000 |           3,334
     100,000 |      0.00139874 |      0.04637546 |           100,000 |          33,334
   1,000,000 |      0.01302324 |      0.28245638 |         1,000,000 |         333,334

The measured times show that both algorithms conotinue to run as the input size increases. The greedy algorithm takes more execution time than the baseline implementation in this benchmark, but it produces substantially fewer routers.

For one million required rooms, the baseline uses 1,000,000 routers, while the greedy algorithm uses 333,334 routers. The benchmark therefore demonstrates a trade-off between the simple baseline and the proposed solution: the baseline is faster in this particular implementation, while the greedy algorithm significantly reduces the number of routers.

4. Communicate Findings

- Correectness

The test suite confirmed that the greedy algorithm successfully covers every required room for all tested cases. The professor's example produces exactly the expected result:

Required rooms: [1, 2, 4, 5, 8, 9, 10]
Greedy routers: [2, 5, 9]

The greedy algorithm also correctly handles rooms at the beginning and end of the building and cases where one router can cover multiple required rooms.

- Greedy Optimality

The greedy strategy is optimal for this specific single-corridor problem. Consider the leftmost uncovered required room r. Any valid solution must place a router at r - 1, r, or r + 1 in order to cover r.

Placing the router at r + 1, when possible, covers the furthest rooms to the right while still covering r. Therefore, choosing this position cannot reduce the ability to cover the remaining rooms compared with choosing a router farther left.

After this choice, the same reasoning can be applied to the next uncovered required room. Thus, repeatedly making this choice results in a minimum number or routers.

- Performance

Both algorithms have linear time complexity when the required rooms are already sorted. The baseline creates a copy of the required-room list, requiring:

0(n)

time

The greedy algorithm processes the sorted list from left to right. Although it contains a nested while loop, the index only moves forward and never moves backward. Therefore, every required room is processed at most once, giving:

0(n)

time

The benchmark results are consistent with both algorithms scaling as the input size increases.

- Space Complexity

The baseline requires 0(n) space for its output list. The greedy algorthm also required 0(n) space in the worst case for the list of router locations. The coverage-checking function used by the tests does not change the algorithms themselves and is only used to verify the resulting router placements.

5. Summary

The project successfully implemented and tested both a baseline solution and an optimal greedy solution for the single-corridor router placement problem.

The baseline solution is straightforward because it places a router in every required room. The greedy solution is more effective at reducing the number of routers because it places each router as far to the right as possible while still covering the leftmost uncovered required room.

The testing suite passed all implemented tests, including the professor's example and several edge cases. The benchmark showed that both algorithms scale to inputs containing up to one million required rooms. In the largest benchmark, the baseline used 1,000,000 routers while the greedy solution used 333,3334 routers.

Overall, the implementation demonstrates that the greedy strategy provides the required minimum router placement for the one-dimensional dormitory problem while maintaining linear time complexity.