import pandas as pd
import numpy as np

data = {
    'Name': ['A', 'B', 'C'],
    'Marks': [90, np.nan, 85]
}

df = pd.DataFrame(data)

new_df = df.dropna()

print(new_df)
