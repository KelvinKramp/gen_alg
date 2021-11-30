import random


def difficult_formula(x,y,z):
    return (2*(x**2)) + (y) - (57)
    # return 6*x**3 + 9*y**2 + 90*z -25

def fitness(x,y,z):
    ans = difficult_formula(x,y,z)

    # ranking parameters with a reward
    if ans == 0:
        print("FOUND ANSWER")
        exit()
    else:
        return abs(1/ans) # if close to zero give high reward, take absolute because negative and close to zero should also be rewarded

def generate_starting_inputs():
    # generate x,y,z
    inputs = []
    for s in range(1000):
        inputs.append((random.uniform(0, 20), random.uniform(0, 20), random.uniform(0, 20))) # create list of tuples of three random numbers
    return inputs


def run_gen_algo():
    graph_data = []
    inputs = generate_starting_inputs()
    # loop of 10,000 iterations
    for i in range(2000):
        print("RUNNING ITERATION NUMBER", i)
        # ============
        # APPLY FITNESS FUNCTION
        # ============
        # create empty list "outputs" for outputs
        outputs = []
        # for each iteration go through all 1000 different 3 random number combinations of inputs and feed them to the fitness function
        for s in inputs:
            f = fitness(s[0],s[1],s[2])
            # save the list of outcomes of the fitness function in list "outputs"
            outputs.append((f, s))


        # ============
        # SELECTION
        # ============
        # sort the list of outputs
        outputs.sort()
        # rank according to the largest outcome first
        outputs.reverse()
        ranked_outputs = outputs
        # print(f"=== Gen {i} x,y,z leading to best solutions ===")
        # print(ranked_outputs[0])  # items in rankedoutputs are in form "(f, (x,y,z))"
        graph_data.append(ranked_outputs[0])
        bestsolutions = ranked_outputs[:100]

        # ============
        # CROSSOVER
        # ============
        # get x,y,z out of the best solutions and create lists out of it
        elements1, elements2, elements3 = [],[],[]
        for s in bestsolutions:
            elements1.append(s[1][0]) # -> list of x
            elements2.append(s[1][1]) # -> list of y
            elements3.append(s[1][2]) # -> list of z
            # elements = [x1,y1,z1,x2,y2,z2...]
            # if len(elements) == 6:
            #     print(elements)
            #     exit()

        # ============
        # MUTATION
        # ============
        # create new generation of inputs based on the elements of the previously selected 100 best solutions
        new_generation = []
        for i in range(1000):
            e1 = random.choice(elements1) * random.uniform(0.95, 1.05)
            e2 = random.choice(elements2) * random.uniform(0.95, 1.05)
            e3 = random.choice(elements3) * random.uniform(0.95, 1.05)
            new_generation.append((e1, e2, e3))
        inputs = new_generation

        # # STOP IF CERTAIN TRESHOLD IS REACHED
        # if ranked_outputs[0][0] > 100000:
        #     break

    x,y,z = [],[],[]
    results = []
    for i in graph_data:
        results.append(i[0])
        x.append(i[1][0])
        y.append(i[1][1])
        z.append(i[1][2])
    # print(results[0], x[0],y[0],z[0])
    return results, x, y, z

if __name__ == "__main__":
    results,x,y,z = run_gen_algo()