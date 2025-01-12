from helpers import *
log("START ##################################################################################\n")

def generateHypothesis(help):
    if(help):
        help = "Use these higher concepts as your guide:" + help
    hypotheses = " "
    for i in range(5):
        hypothesis = doImage(
        f"""{help}"""
        , base64_image)
        hypotheses += log(f"Hypothesis {i+1}: ##########################################################################\n\n" + hypothesis + "\n")
    return hypotheses

currentHypothesis = ""
while True:
    hypotheses = generateHypothesis(currentHypothesis)
    currentHypothesis = doImage(f"""Integrate the following: \n {hypotheses} \n  into ###{currentHypothesis}### to solve the puzzle in the image.\n""", base64_image)
    log(f"\nCurrentHypothesis: ##########################################################################\n\n" + currentHypothesis + "\n")

##Integrating parts of of conciousness

#PID

#Detect when its in loop local max

# Fall thingy that rotates around

#Free energy priciple 
#reduce the dieference between engergies
#it needs to see the image with the guesses

#tell the ideas that they are bad

# Have a sing hypothesis