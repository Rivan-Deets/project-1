"""
Test Suite for Router Placement Project

file tests:
1. Baseline algorithm
2. Greedy algorithm
3. WiFi coverage
4. Edge cases
5. Expected numbers of routers
"""


from routers import baseline_routers, greedy_routers, is_covered


def test_empty_input():
    """Tests that an empty list requires no routers"""

    rooms = []
    N = 0

    baseline = baseline_routers(rooms)
    greedy = greedy_routers(rooms, N)

    assert baseline == []
    assert greedy == []


def test_single_room():
    """Tests a building with only one required room"""

    rooms = [5]
    N = 5

    greedy = greedy_routers(rooms, N)

    assert len(greedy) == 1
    assert is_covered(rooms, greedy)


def test_consecutive_rooms():
    """Tests several consecutive rooms"""

    rooms = [1, 2, 3, 4, 5]
    N = 5

    greedy = greedy_routers(rooms, N)

    assert is_covered(rooms, greedy)
    assert len(greedy) == 2


def test_two_rooms_with_one_gap():
    """
    Tests rooms that can both be covered by a single
    router placed in the room between them
    """

    rooms = [2, 4]
    N = 4

    greedy = greedy_routers(rooms, N)

    assert greedy == [3]
    assert is_covered(rooms, greedy)
    assert len(greedy) == 1


def test_separated_rooms():
    """Tests rooms that require separate routers"""

    rooms = [1, 4, 7]
    N = 7

    greedy = greedy_routers(rooms, N)

    assert is_covered(rooms, greedy)
    assert len(greedy) == 3


def test_professor_example():
    """Tests the example provided in the project description"""

    rooms = [1, 2, 4, 5, 8, 9, 10]
    N = 10

    greedy = greedy_routers(rooms, N)

    assert greedy == [2, 5, 9]
    assert is_covered(rooms, greedy)
    assert len(greedy) == 3


def test_large_consecutive_group():
    """Tests a large group of consecutive required rooms"""

    rooms = list(range(1, 10))
    N = 9

    greedy = greedy_routers(rooms, N)

    assert is_covered(rooms, greedy)
    assert len(greedy) == 3


def test_baseline_covers_everything():
    """Verifies that the baseline solution covers all required rooms"""

    rooms = [1, 2, 4, 5, 8, 9, 10]

    baseline = baseline_routers(rooms)

    assert is_covered(rooms, baseline)


def test_greedy_uses_fewer_routers_than_baseline():
    """
    Verifies that the greedy solution uses fewer routers
    than the simple baseline for the professor's example
    """

    rooms = [1, 2, 4, 5, 8, 9, 10]
    N = 10

    baseline = baseline_routers(rooms)
    greedy = greedy_routers(rooms, N)

    assert len(greedy) < len(baseline)


def test_all_required_rooms_are_covered():
    """
    General coverage test using several groups of rooms
    """

    test_cases = [
        [1],
        [1, 2],
        [1, 3],
        [2, 4],
        [1, 2, 3, 4],
        [2, 3, 5, 6, 8],
        [1, 4, 7, 10],
    ]

    for rooms in test_cases:

        N = max(rooms)

        greedy = greedy_routers(rooms, N)

        assert is_covered(rooms, greedy)


if __name__ == "__main__":

    test_empty_input()
    test_single_room()
    test_consecutive_rooms()
    test_two_rooms_with_one_gap()
    test_separated_rooms()
    test_professor_example()
    test_large_consecutive_group()
    test_baseline_covers_everything()
    test_greedy_uses_fewer_routers_than_baseline()
    test_all_required_rooms_are_covered()

    print("All test passed!")