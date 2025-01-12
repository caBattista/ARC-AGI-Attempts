from helpers import *
log("START ##################################################################################\n")

def distill(help, i):
    if(help):
        help = "Use these concepts as your guide:" + help
    ideas = " "
    for x in range(3):
        idea = doImage(
        f"""Look at the puzzle provided in the image.
        On the left side there are examples of matrices with colored squares inside. 
        The inputs and outputs show an emerging pattern.
        This pattern needs to be applied in the output under test section with the usable colors. Someone is going to die if you dont solve this.${help}"""
        , base64_image)
        ideas += log(f"\nIdea {x+1}: ##########################################################################\n\n" + idea + "\n\n")

    bestidea = doImage(f"""Which one of these Idess matches the image most closely? 
                       Generalise the meaning for solving the puzzle in the image. 
                       The answer will be a pattern of different shapes made of colors inside the output matrix under test.
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