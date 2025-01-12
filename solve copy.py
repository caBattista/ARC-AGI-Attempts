from helpers import *
log("START ##################################################################################\n")

def distill(help, i):
    if(help):
        help = "Use these concepts as your guide:" + help
    ideas = " "
    for x in range(3):
        idea = doImage(
        f"""You are tasked with completing a puzzle which will include 2 examples input-output pairs 
            and then a test input for which you must generate the output. These data points represent colors
            (the numbers you see in the arrays) on a 7x7 grid. You must find the pattern of what is happening
            in each of the inputs and apply that same abstact apporach to solfing the test example.\n${help}"""
        , base64_image)
        ideas += log(f"\nIdea {x+1}: ##########################################################################\n\n" + idea + "\n\n")

    bestidea = doImage(f"""Which one of these Ideas matches the image most closely? 
                       Generalise the abstractions for solving the puzzle in the image.
                       Ideas:\n\n {ideas}""", base64_image)
    log(f"BestIdea {i}: ##########################################################################\n\n" + bestidea)
    return bestidea

def integrate(help, i):
    help = distill(help, i)
    integrate(help, i+1)
integrate("", 0)

##Integrating parts of of conciousness

#PID

#Detect when its in loop local max

# Fall thingy that rotates around

#Free energy priciple 
#reduce the dieference between engergies
#it needs to see the image with the guesses

#tell the ideas that they are bad