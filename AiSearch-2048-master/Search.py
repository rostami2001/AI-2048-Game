from Solution import Solution
from Problem import Problem
from datetime import datetime
from queue import PriorityQueue


def heuristic(neighbor, goal_number):
    pass

class Search:
    @staticmethod
    def bfs(prb: Problem) -> Solution:  # this method get a first state of Problem and do bfs for find solution if no
        # solution is find return None else return the solution
        start_time = datetime.now()
        queue = []
        state = prb.initState
        queue.append(state)
        while len(queue) > 0:
            state = queue.pop(0)
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.goal_test(c):
                    return Solution(c, prb, start_time)
                queue.append(c)
        return None

    @staticmethod
    def dfs(prb: Problem) -> Solution:
        start_time = datetime.now()
        stack = []
        visited = {}
        state = prb.initState
        stack.append(state)

        while len(stack) > 0:
            state = stack.pop()
            if prb.goal_test(state):
                return Solution(state, prb, start_time)
            visited[state.__hash__()] = True
            neighbors = prb.successor(state)
            for neighbor in reversed(neighbors):
                if neighbor.__hash__() not in visited:
                    stack.append(neighbor)
                    visited[neighbor.__hash__()] = True
        return None

    def gbfs(prb: Problem) -> Solution:
        start_time = datetime.now()
        priority_queue = PriorityQueue()
        exp = {}
        state = prb.initState
        priority = 0
        priority_queue.put((priority, state))
        while not priority_queue.empty():
            priority, state = priority_queue.get()
            if prb.goal_test(state):
                return Solution(state, prb, start_time)
            exp[state.__hash__()] = True
            neighbors = prb.successor(state)
            for neighbor in neighbors:
                if neighbor.__hash__() not in exp:
                    priority = heuristic(neighbor, prb.goal_number)
                    priority_queue.put((priority, neighbor))
                    exp[neighbor.__hash__()] = True
        return None

    @staticmethod
    def ids(prb: Problem, depth_limit=50) -> Solution:
        start_time = datetime.now()
        for depth in range(depth_limit):
            result = Search.dls(prb, depth)
            if result:
                return result
        return None

    @staticmethod
    def dls(prb: Problem, depth) -> Solution:
        start_time = datetime.now()
        stack = [(prb.initState, 0)]
        visited = {prb.initState.__hash__(): True}
        while stack:
            state, current_depth = stack.pop()
            if current_depth > depth:
                continue
            if prb.goal_test(state):
                return Solution(state, prb, start_time)
            neighbors = prb.successor(state)
            for neighbor in reversed(neighbors):
                if neighbor.__hash__() not in visited:
                    stack.append((neighbor, current_depth + 1))
                    visited[neighbor.__hash__()] = True
        return None

    @staticmethod
    def astar(prb: Problem) -> Solution:
        start_time = datetime.now()
        priority_queue = PriorityQueue()
        exp = {}
        state = prb.initState
        priority = 0
        priority_queue.put((priority, state))
        while not priority_queue.empty():
            priority, state = priority_queue.get()
            if prb.goal_test(state):
                return Solution(state, prb, start_time)
            exp[state.__hash__()] = True
            neighbors = prb.successor(state)
            for neighbor in neighbors:
                if neighbor.__hash__() not in exp:
                    priority = heuristic(neighbor, prb.goal_number)
                    priority_queue.put((priority, neighbor))
                    exp[neighbor.__hash__()] = True
        return None

    @staticmethod
    def idastar(prb: Problem) -> Solution:
        start_time = datetime.now()
        bound = heuristic(prb.initState, prb.goal_number)
        while True:
            result, new_bound = Search.dfs_idastar(prb, prb.initState, bound)
            if result:
                return result
            if new_bound == float('inf'):
                return None
            bound = new_bound

    @staticmethod
    def dfs_idastar(prb: Problem, state, bound) -> (Solution, float):
        start_time = datetime.now()
        f = heuristic(state, prb.goal_number)
        if f is None or bound is None:
            return None, float('inf')  # Replace None values with float('inf')
        if f > bound:
            return None, f
        if prb.goal_test(state):
            return Solution(state, prb, start_time), float('inf')
        min_cost = float('inf')
        neighbors = prb.successor(state)
        for neighbor in neighbors:
            result, new_bound = Search.dfs_idastar(prb, neighbor, bound)
            if result:
                return result, float('inf')
            if new_bound < min_cost:
                min_cost = new_bound
        return None, min_cost

