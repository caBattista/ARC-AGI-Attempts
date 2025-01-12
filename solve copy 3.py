from helpers import *
log("START ##################################################################################\n")

def generateHypotheses(help, i):
    if(help):
        help = "Use these concepts as your guide:" + help
    hypotheses = ""
    for i in range(4):
        idea = doImage(
        f"""Look at the puzzle provided in the image.
        On the left side there are examples of matrices with colored squares inside. 
        The inputs and outputs show an emerging pattern.
        This pattern needs to be applied in the output under test section with the usable colors. 
        It is urgent.
        {help}\n"""
        , base64_image)
        hypotheses += log(f"\nIdea {i+1}: ##########################################################################\n\n" 
                     + idea + "\n")
    return hypotheses

def integrate(conclusion, i):
    hypotheses = generateHypotheses(conclusion, i)
    conclusion = doImage(f"""Generalise the meaning for solving the puzzle in the image based on the Ideas. 
                    It is urgent.
                    Ideas:\n\n {hypotheses}""", base64_image)
    log(f"Conclusion {i}: ##########################################################################\n\n" + conclusion + "\n")
    integrate(conclusion, i+1)
integrate("", 0)


##Random Ideas

#Integrating parts of of conciousness

#PID

#Detect when its in loop local max

#Fall thingy that rotates around -> chaos pendulum

#Free energy priciple 
#reduce the dieference between engergies
#it needs to see the image with the guesses

#Tell the ideas that they are bad

#Have a hypothesis