import numpy as np

def random_dice_walk_func(n):
    random_walk = [0]

    for i in np.arange(n):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)

        if (dice <= 2):
            step = max(0, step - 1)
        elif (dice <= 5):
            step += 1
        else:
            step += np.random.randint(1, 7)
        
        random_walk.append(step)
    
    return np.array(random_walk)

def all_walks(n, m):
    all_walks_arr = []
    for i in np.arange(n):
        all_walks_arr.append(random_dice_walk_func(m))
    
    return np.array(all_walks_arr)
