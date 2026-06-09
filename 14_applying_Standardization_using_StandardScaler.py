import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {
    'Marks': [50, 60, 70, 80]
}

df = pd.DataFrame(data)

scaler = StandardScaler()

df['Standardized'] = scaler.fit_transform(df[['Marks']])

print(df)
