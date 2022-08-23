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
    
    return random_walk

