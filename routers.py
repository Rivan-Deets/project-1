"""
Router Placement Project

file contains:
1. A baseline router-placement algorithm
2. An optimal greedy router-placement algorithm
3. A function for checking whether all required rooms are covered
"""


def baseline_routers(required_rooms):
    """
    Baseline solution that places a router in every room that requires WiFi

    Parameters:
    required_rooms (list[int]):
        Sorted list of room numbers requiring WiFi

    Returns:
        list[int]:
            Room numbers where routers are placed
    """

    return required_rooms.copy()


def greedy_routers(required_rooms, N):
    """
    Greedy solution

    Processes required rooms from left to right.
    For the most uncovered room, place a router as far to the right as possible
    while still covering that room.

    Parameters:
        required_rooms (list[int]):
            Sorted list of room numbers requiring WiFi

        N (int):
            Highest room number in the building

    Returns:
        list[int]:
            Room numbers where routers are placed
    """

    routers = []
    i = 0

    while i < len(required_rooms):

        # Find the most uncovered required room
        room = required_rooms[i]

        # Place a router as far to the right as possible while still covering that room
        router = min(room + 1, N)

        routers.append(router)

        # Skips all required rooms covered by this router
        while (
            i < len(required_rooms)
            and required_rooms[i] <= router + 1
        ):
            i += 1

    return routers


def is_covered(required_rooms, routers):
    """
    Checks whether every required room is covered by
    at least one router

    A router in room i coveres i-1, i, and i+1

    Parameters:
        required_rooms (list[int]):
            Sorted list of rooms requiring WiFi

        routers (list[int]):
            Room numbers containing routers

    Returns:
        bool:
            True if every required room is covered
            False if otherwise
    """

    for room in required_rooms:

        covered = False

        for router in routers:

            if abs(room - router) <= 1:
                covered = True
                break

        if not covered:
            return False

    return True


if __name__ == "__main__":

    rooms = [1, 2, 4, 5, 8, 9, 10]
    N = 10

    baseline = baseline_routers(rooms)
    greedy = greedy_routers(rooms, N)

    print("Required rooms:")
    print(rooms)

    print("\nBaseline routers:")
    print(baseline)

    print("Number of baseline routers:")
    print(len(baseline))

    print("\nGreedy routers:")
    print(greedy)

    print("Number of greedy routers:")
    print(len(greedy))

    print("\nAre all rooms covered by the greedy solution?")
    print(is_covered(rooms, greedy))