import numpy as np
import pandas as pd
import random

def generate_random_rank_data(teams= 5, length= 10, seed= 0):
    random.seed(0)
    rows = [np.array(random.sample(range(1, teams + 1), teams)).reshape(1, -1) for i in range(length)]
    data = np.concatenate(rows, axis= 0)
    columns = [chr(i) for i in range(ord("a"), ord("a") + teams)]
    df = pd.DataFrame(data= data, columns= columns)
    return df