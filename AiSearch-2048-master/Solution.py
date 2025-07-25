from Problem import Problem
from State import State
from datetime import datetime


class Solution:
    def __init__(self, state: State, problem: Problem, start_time):
        self.state = state
        self.problem = problem
        self.duration = datetime.now() - start_time

    def print_path(self):  # this for show path of every search how it's done
        queue = []
        state = self.state.parent
        while state is not None:
            queue.insert(0, state)
            state = state.parent
        print('Init State')
        self.problem.print_state(queue[0])
        for state in queue[1:]:
            print(state.selected_action)
            self.problem.print_state(state)
        print(self.state.selected_action)
        self.problem.print_state(self.state)
        print('Solution State\n')
        print('duration = ' + str(self.duration))
