from helpers import *
import os
import json

with open(fr'C:\Users\chris\Desktop\AI solution\ARC-AGI-master\data\training\0a938d79.json', 'r') as file:
    data = json.load(file)

log("START ##################################################################################\n")

def distill(help, i):
    if(help):
        help = "Use these concepts as your guide:" + help
    ideas = " "
    for x in range(5):
        idea = doText(
        f"""
        You are tasked with completing a puzzle which will include examples input-output pairs\n
        and then a test input for which you must generate the output. You must find the simple pattern of what is happening\n
        in each of the inputs and apply that same abstact apporach to solfing the test example.\n
        Do not provide code.
        ${help}

        Training:\n
        Input:\n
        [1,0,0,0]\n
        [0,1,0,0]\n
        [0,0,1,0]\n
        [0,0,0,1]\n

        Output:\n
        [1,0,0,0]\n
        [1,1,0,0]\n
        [1,1,1,0]\n
        [1,1,1,1]\n

        Test\n
        Input\n
        [0,0,0,1]\n
        [0,0,1,0]\n
        [0,1,0,0]\n
        [1,0,0,0]\n

        Output:?
        """)
        ideas += log(f"Idea {x+1}: ##########################################################################\n\n" + idea + "\n\n")

    bestidea = doText(f"""Evaluate the ideas to generalise the actual meaning for solving the puzzle.They are probably wrong. Give a single solution.\n {ideas} \n \n""")
    log(f"BestIdea {i}: ##########################################################################\n\n" + bestidea + "\n")
    return bestidea

def integrate(help, i):
    help = distill(help, i)
    integrate(help, i+1)
integrate("", 0)

##Integrating parts of of conciousness

#PID

#Detect when its in loop local max

# Fall thingy that rotates around
#chaos how to do it in code

# [[0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

# to

# [[0,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0],
#  [0,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0],
#  [0,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0],
#  [0,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0],
#  [0,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0],
#  [0,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0],
#  [0,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0],
#  [0,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0],
#  [0,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0],
#  [0,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0],
#  [0,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0,0,0,0,4,0,0,0,0,3,0]]