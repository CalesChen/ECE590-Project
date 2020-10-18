"""
Math 560
Project 2
Fall 2020

project2.py

Partner 1: Xunyu Chu
Partner 2: Ke Chen
Date: 10/18 2020
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The shortest path from maze.start to maze.exit.
"""


##this Function will return the ans of BFS
def findpath(maze, index):
    # Create the ans struct
    ans = []
    node = maze.adjList[index]
    while (True):
        ans.append(node.rank)
        # When we find the start, we exit
        if (node.prev == None):
            break
        # Choose the previous one
        node = maze.adjList[node.prev]
    return ans


## reset the visited status

def reset(maze):
    for i in range(0, len(maze.adjList)):
        maze.adjList[i].visited = False
    return


def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    ### REset All of the Visited status
    reset(maze)
    ##### Your implementation goes here. #####
    # ans = []
    if (alg == 'DFS'):
        # Create the Stack
        sta = Stack()
        # Push the Start vertex
        sta.push(maze.start.rank)
        maze.start.dist = 0
        while (not sta.isEmpty()):
            curr = sta.pop()
            # if we have visited this node, skip
            if (maze.adjList[curr].visited == True):
                continue
            # Mark the visited vertex
            maze.adjList[curr].visited = True

            # Iterating over the adjMat to find the neighbor
            for i in range(0, len(maze.adjMat[0])):

                # Check if we need to execute on this vertex
                if (maze.adjMat[curr][i] == 1 and \
                        (not maze.adjList[i].visited)):

                    # Push the new Vertex
                    sta.push(i)
                    # distance plus one
                    maze.adjList[i].dist = maze.adjList[curr].dist + 1
                    # previous vertex rank
                    maze.adjList[i].prev = curr
                    # when we find the solution
                    if (i == maze.exit.rank):
                        ans = findpath(maze, i)
                        return ans[::-1]

    else:
        q = Queue()
        # Push The first vertex
        q.push(maze.start.rank)
        # Set the first Vertex distance
        maze.start.dist = 0
        # Iterate over the Queue when it is not empty
        while (not q.isEmpty()):
            lenth = q.numElems
            # Iterate over the Vertex with same distance
            for i in range(0, lenth):
                curr = q.pop()
                # Check if we need to visit this vertex
                if (maze.adjList[curr].visited == True):
                    continue
                # Mark the visited vertex
                maze.adjList[curr].visited = True

                # Find the Neighbor
                for j in range(0, len(maze.adjMat[0])):

                    # Check if we need to visit this vertex
                    if (maze.adjMat[curr][j] == 1 and \
                            (not maze.adjList[j].visited)):

                        # Push the new vertex
                        q.push(j)
                        # Update the detail information
                        maze.adjList[j].dist = maze.adjList[curr].dist + 1
                        maze.adjList[j].prev = curr
                        # Return Answer when find the exit
                        if (j == maze.exit.rank):
                            ans = findpath(maze, j)
                            return ans[::-1]

    return []
    ##### Your implementation goes here. #####


"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
