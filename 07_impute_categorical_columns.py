import pandas as pd
import numpy as np

data = {
    'City': ['Mumbai', np.nan, 'Pune', 'Delhi']
}

df = pd.DataFrame(data)

mode_value = df['City'].mode()[0]

df['City'].fillna(mode_value, inplace=True)

print(df)
