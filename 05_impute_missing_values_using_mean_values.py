import pandas as pd
import numpy as np

data = {
    'Marks': [90, np.nan, 85, 95]
}

df = pd.DataFrame(data)

mean_value = df['Marks'].mean()

df['Marks'].fillna(mean_value, inplace=True)

print(df)
