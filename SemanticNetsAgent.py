import copy
import queue 

from collections import deque

class SemanticNetsAgent:

    def __init__(self):
        #If you want to do any initial processing, add it here.            
        pass



    def solve(self, initial_sheep, initial_wolves):
            global const BOAT_LEFT = 0
            global const BOAT_RIGHT = 1
        class State(object):
            def __init__(self, left_sheep, left_wolf, right_sheep, right_wolf, boat):
                self.left_sheep=left_sheep
                self.left_wolf=left_wolf 
                self.right_sheep=right_sheep
                self.right_wolf=right_wolf
                self.boat = boat
                self.parent = None


            def check_position(self):
                if (self.left_sheep < 0 or self.left_wolf < 0 or self.right_sheep < 0 or self.right_wolf < 0)
                    return False 
                elif (self.left_sheep !=0 and self.left_wolf > left_sheep):
                    return False
                elif (self.right_sheep !=0 and self.right_sheep < self.right_wolf):
                    return False
                else:
                    return True

                
            def isGoalState(self):
                    if self.left_sheep == 0 and self.left_wolf == 0 and self.boat == BOAT_RIGHT:
                        return True
                    else:
                        return False  

        def findKids(currNode):
            children = []
            movesarray = [(2,0),(0,2),(1,1),(0,1),(1,0)]
            if currNode.boat == BOAT_LEFT:
                for moves in movesarray:
                    newState = State(currNode.left_sheep - moves[0], currNode.left_wolf - moves[1], currNode.right_sheep + moves[0], currNode.right_wolf + moves [1], BOAT_RIGHT )
                    if newState.check_position():
                        children.append(newState)
                        newState.parent = currNode
            else:
                for moves in movesarray:
                     newState = State(currNode.left_sheep + moves[0], currNode.left_wolf + moves[1], currNode.right_sheep - moves[0], currNode.right_wolf - moves [1], BOAT_LEFT )
                    if newState.check_position():
                        children.append(newState)
                        newState.parent = currNode
            return children


        goal_state = False
        root = State(initial_sheep, initial_wolf, 0, 0, BOAT_LEFT)
        open_states = deque([])
        open_states.append(root)
        closed_states = []
        while (goal_state == False and open_states):
            currState = open_states.popleft()
            if (currState.isGoalState()):
                goal_state = True
            else:
                closed_states.append(currState)
                newchildren = findKids(currState)
                for child in newchildren:
                    if child not in closed_states:
                        open_states.append(child)

        if goal_state == True:
            all_moves = []
            order_moves = []
            while currState.parent:
                move = (abs(currState.left_sheep-currState.parent.leftsheep), abs(currState.left_wolf=currState.parent.left_wolf))
                all_moves.append(move)
                currState=currState.parent
            for i in range(len(all_moves)):
                currMove = all_moves[len(all_moves)-i-1]
                order_moves.append(currMove)
            return order_moves
        else:
            return []



        



        











        #Add your code here! Your solve method should receive
        #the initial number of sheep and wolves as integers,
        #and return a list of 2-tuples that represent the moves
        #required to get all sheep and wolves from the left
        #side of the river to the right.
        #
        #If it is impossible to move the animals over according
        #to the rules of the problem, return an empty list of
        #moves.
        pass
