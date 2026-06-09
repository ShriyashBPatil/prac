import pandas as pd
import numpy as np

data = {
    'Marks': [90, np.nan, 85, 95]
}

df = pd.DataFrame(data)

median_value = df['Marks'].median()

df['Marks'].fillna(median_value, inplace=True)

print(df)
