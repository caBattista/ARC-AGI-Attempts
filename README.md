# ARC-AGI-Attempts

The purpose of these attemts are to try to solve the ARC-AGI-Prize visually and 
learn about the tooling needed and get a better understanding of what active inference is all about.

# Ideas

The idea is to have an LLM interpret the problem and generate ideas as to how to solve it. It uses a recursive process consiting of:
  1) Naively generate a couple of ideas of how it could be solved
  2) Feed all these ideas back to the model and have it generalise or find commonground between them (constantly referencing the images)
  3) Have this generalisation fed back into a new set of new ideas
  4) Repeat this process until it is shure how to solve the problem
