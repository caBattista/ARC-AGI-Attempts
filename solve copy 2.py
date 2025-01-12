from helpers import *

def generateHypotheses(help, i):
    if(help):
        help = "Use these concepts as your guide. They might be wrong.:" + help
    hypotheses = ""
    for i in range(4):
        hypothesis = doImage(f"""Do not give an answer for the solution. {help}\n""", base64_image)
        hypotheses += log(f"Hypotheses {i+1}: ##########################################################################\n\n" 
                    + hypothesis  + "\n")
    return hypotheses

def integrate(currentBelief, i):
    hypotheses = generateHypotheses(currentBelief, i)
    currentBelief = doImage(f"""Current Belief:\n{currentBelief}\nNew Hypotheses:\n{hypotheses}\n\n
    Generalise the meaning for solving the puzzle based on current belief and the new hypotheses into a single sentence. 
    But they might be wrong.""", base64_image)
    log(f"Current belief {i}: ##########################################################################\n\n" + currentBelief + "\n")
    integrate(currentBelief, i+1)

integrate("", 0)

#Random Ideas

#Integrating parts of of conciousness

#PID

#Detect when its in loop local max

#Fall thingy that rotates around -> chaos pendulum

#Free energy priciple 
#reduce the dieference between engergies
#it needs to see the image with the guesses

#Tell the ideas that they are bad

#Have a hypothesis

#Generate 4 ideas -> make a conclusion
#use conclusion again 4times