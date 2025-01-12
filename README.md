# ARC-AGI-Attempts

The purpose of these attemts are to try to solve the ARC-AGI-Prize visually and 
learn about the tooling needed and get a better intuitive understanding of what active inference is all about.

# Ideas

The idea is to have an LLM interpret the problem and generate ideas as to how to solve it. It uses a recursive process consiting of:
  1) Naively have the llm generate a couple of hypothesis of how it could be solved
  2) Feed them back to the model and have it generalise or find commonground between them (eveluating all the diferent perspectives while referencing the images again)
  3) Have this generalisation fed back into a new set of new ideas to hopefully bring the idea generators on the right track
  4) Repeat this process until it is sure how to solve the problem

# Interpretation of the results
It seems to be inferencing with each feedback cycle but unfortunately there seems to be to much noise in the idea generation process for it to arrive at a sucessful conclusion.
