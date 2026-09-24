PROBLEM FORMULATION

We’ll have the apartment buildings be represented as a graph with each neighboring apartment being represented by a vertex. Placing a router in an apartment will provide WiFi to not only the apartment it’s placed in, but also neighboring apartments adjacent to it. 

We’re going to determine the minimum number of routers needed so every apartment has access to WiFi.

INPUT

We’ll set the apartments as a dictionary. Each dictionary key represents an
apartment with its connected list containing its neighbors.


Ex. 
   Apartments = {
            apartment1:  [neighbor1, neighbor2, …],
            apartment2:  [neighbor1, neighbor3, …],
            …
               }


              {
               “A”:  [“B”, “C”],
               “B”:  [“A”, “D”],
               “C”:  [“A”],
               “D”:  [“B”],
             }

OUTPUT

The algorithm should return a set/list of apartments where routers should be 
placed. Every apartment should either have a router or have a neighboring
apartment  containing a router, leaving the amount of routers as small as possible.


CONSTRAINTS AND ASSUMPTIONS

For our theoretical formulation:
          
 - Each apartment is a vertex on the graph
 - Neighbor relationships are bidirectional
 - An apartment will be considered covered if it follows the output
 - Every apartment must be covered by the end
 - Routers all have the same coverage
 - Minimize the number of routers
 - The input as shown should have valid apartment identifiers and neighbor lists
 - Some apartments on the graph may have no neighbors


ALGORITHMIC STRATEGY

This problem can be solved using backtracking for small graphs. While keeping everything simple, the algorithm considers whether each apartment should contain a router or not. It’ll explore possible router placements while keeping notes of apartments that are already covered. 

Our algorithm will maintain:
   - covered: apartments that already have WiFi
   - chose: apartments where routers have been placed
   - best: the smallest router set found so far

If every apartment is covered, that means the current solution is valid, updating best if the current solution uses fewer routers. Otherwise, it’ll select an uncovered apartment and explore possible router placements that could cover it.

Pseudocode:

EXACT-ROUTERS(apartments):
    best = all apartments
    covered = empty set
    chosen = empty set

    SEARCH(apartments, covered, chosen, best)

    return best


SEARCH(apartments, covered, chosen, best)

   if every apartment is covered:
       if |chosen| < |best|:
           best = copy(chosen)
       return

   if |chosen| >= |best|:
       return

   choose an uncovered apartment V

   candidates = {V} union neighbors [V]

   for each apartment u in candidates:

       if u not in chosen:
           add u to chosen

           newly_covered = 
               {u} union neighbors[u]

           SEARCH(
            apartments,
            covered union newly_cpvered,
            chosen,
            best
           )

           remove u from chosen
           
When the algorithm selects an uncovered apartment, any valid solution must place a router at either the uncovered apartment or one of its neighbors. Otherwise, the uncovered apartment would remain without WiFi. The algorithm keeps the smallest valid router set found so the final result is an optimal solution.

Greedy Pseudocode:

GREEDY-ROUTERS(apartments):

    uncovered = set of all apartments
    routers = empty set

    while uncovered is not empty:

        choose apartment u that covers
        the largest number of apartments in uncovered

        add u to routers

        covered_by_u = {u} union neighbors[u]

        remove every apartment in covered_by_u
        from uncovered

   return routers

BASELINE SOLUTION

A simple baseline can use a greedy strategy. At every step, it would select the apartment whose router would cover the largest number of currently uncovered apartments. This doesn’t guarantee that the minimum possible number of routers, but it provides a simple solution that can be compared against the exact algorithm.

Baseline Purpose

The greedy algorithm provides a reference point for: running time, number of routers selected, and behavior on different graph structures. The exact algorithm can then be compared against the greedy algorithm to determine how often the greedy strategy finds the optimal number of routers.


COMPLEXITY ANALYSIS

Comparing both algorithms, the Exact Search is more optimal with its 
backtracking strategy and its worst-case time being (O(2^n(n+m))), compared to 
the Greedy algorithm, with a worst-case time of (O(n(n+m))) with its strategy of
selecting apartments covering uncovered ones. 

The exact algorithm is useful for determining the true minimum numbers of 
routers, while the greedy algorithm provides a faster baseline that can be used for 
performance comparison.
