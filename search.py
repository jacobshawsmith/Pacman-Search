# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
     

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  fringe = util.Stack()
  visited = []
  fringe.push( (problem.getStartState(), []) )
  visited.append( problem.getStartState() )
  
  while fringe.isEmpty() == False:
      state, actions = fringe.pop()
      for next in problem.getSuccessors(state):
        newstate = next[0]
        newdirection = next[1]
        
        if newstate not in visited:
            if problem.isGoalState(newstate):
                #print 'Find Goal'
                return actions + [newdirection]
            
            else:
                fringe.push( (newstate, actions + [newdirection]) )
                visited.append( newstate )

  util.raiseNotDefined()

def breadthFirstSearch(problem):
  Fringe = util.Queue()
  Visited = []
  Fringe.push( (problem.getStartState(), []) )
  Visited.append( problem.getStartState() )
  
  while Fringe.isEmpty() == False:
      state, actions = Fringe.pop()
      for next in problem.getSuccessors(state):
        newstate = next[0]
        newdirection = next[1]
        
        if newstate not in Visited:
            if problem.isGoalState(newstate):
                #print 'Find Goal'
                return actions + [newdirection]
            
            else:
                Fringe.push( (newstate, actions + [newdirection]) )
                Visited.append( newstate )

  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  def update(Frontier, item, priority):
    for index, (p, c, i) in enumerate(Frontier.heap):
      if i[0] == item[0]:
          if p <= priority:
                break
          del Frontier.heap[index]
          Frontier.heap.append((priority, c, item))
          heapq.heapify(Frontier.heap)
          break
    else:
      Frontier.push(item, priority)
  
  Frontier = util.PriorityQueue()
  Visited = []
  Frontier.push( (problem.getStartState(), []), 0 )
  Visited.append( problem.getStartState() )

  while Frontier.isEmpty() == 0:
    state, actions = Frontier.pop()

    if problem.isGoalState(state):
      return actions

    if state not in Visited:
      Visited.append( state )

    for next in problem.getSuccessors(state):
      n_state = next[0]
      n_direction = next[1]
      if n_state not in Visited:
        update( Frontier, (n_state, actions + [n_direction]), problem.getCostOfActions(actions+[n_direction]) )
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  closedset = []
  pqueue = util.PriorityQueue()
  start = problem.getStartState()
  pqueue.push((start, list()), heuristic(start, problem))

  while not pqueue.isEmpty():
    node, actions = pqueue.pop()

    if problem.isGoalState(node):
      return actions

    closedset.append(node)

    for pos, dir, cost in problem.getSuccessors(node):
      if not pos in closedset:
        new_actions = actions + [dir]
        score = problem.getCostOfActions(new_actions) + heuristic(pos, problem)
        pqueue.push( (pos, new_actions), score)

  return []

  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch