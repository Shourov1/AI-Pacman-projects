# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    state_stack = util.Stack()
    start = problem.getStartState()
    visited = set()
    #path_dic = {}
    state_stack.push((start, []))
    while not state_stack.isEmpty():
        cur_state, path = state_stack.pop()
        if cur_state in visited:
            continue
        if problem.isGoalState(cur_state):
            return path
            #break
        visited.add(cur_state)
        successors = problem.getSuccessors(cur_state)
        for successor in successors:
            suc_state, direction, step_cost = successor[0], successor[1], successor[2]
            if suc_state not in visited:
                state_stack.push((suc_state, path+[direction]))
            #path_dic[suc_state] = (cur_state, direction)
    #path = []
    #while cur_state != start:
    #    cur_state, direction = path_dic[cur_state]
    #    path.append(direction)
    #return path[::-1]
    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    state_queue = util.Queue()
    state_queue.push((problem.getStartState(), []))
    visited = set()
    while not state_queue.isEmpty():
        node,path = state_queue.pop()
        if node in visited:
            continue
        visited.add(node)
        if problem.isGoalState(node):
            return path
        successors = problem.getSuccessors(node)
        for successor in successors:
            suc_state, direction, step_cost = successor[0], successor[1], successor[2]
            if suc_state not in visited:
                state_queue.push((suc_state, path + [direction]))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    PriorityQueue = util.PriorityQueue()
    visited = set()
    distance = {}
    PriorityQueue.push((problem.getStartState(), []), 0)
    distance[problem.getStartState()] = 0
    while not PriorityQueue.isEmpty():
        cur_node, path = PriorityQueue.pop()
        if cur_node in visited:
            continue
        visited.add(cur_node)
        path_cost = distance[cur_node]
        if problem.isGoalState(cur_node):
            return path
        successors = problem.getSuccessors(cur_node)
        for successor in successors:
            suc_state, direction, step_cost = successor[0], successor[1], successor[2]
            if suc_state in distance and distance[suc_state] <= path_cost + step_cost:
                continue
            elif suc_state in distance:
                PriorityQueue.update((suc_state, path+[direction]), path_cost+step_cost)
            else:
                PriorityQueue.push((suc_state, path+[direction]), path_cost+step_cost)
            distance[suc_state] = path_cost + step_cost
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    PriorityQueue = util.PriorityQueue()
    visited = set()
    distance = {}
    start = problem.getStartState()
    PriorityQueue.push((start, []), 0+heuristic(start, problem))
    distance[start] = 0
    while not PriorityQueue.isEmpty():
        cur_node, path = PriorityQueue.pop()
        if cur_node in visited:
            continue
        visited.add(cur_node)
        path_cost = distance[cur_node]
        if problem.isGoalState(cur_node):
            return path
        successors = problem.getSuccessors(cur_node)
        for successor in successors:
            suc_state, direction, step_cost = successor[0], successor[1], successor[2]
            if suc_state in distance and distance[suc_state] <= path_cost + step_cost:
                continue
            elif suc_state in distance:
                PriorityQueue.update((suc_state, path+[direction]), path_cost+step_cost+heuristic(suc_state, problem))
            else:
                PriorityQueue.push((suc_state, path+[direction]), path_cost+step_cost+heuristic(suc_state, problem))
            distance[suc_state] = path_cost + step_cost

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
