import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
    'Marks': [50, 60, 70, 80]
}

df = pd.DataFrame(data)

scaler = MinMaxScaler()

df['Normalized'] = scaler.fit_transform(df[['Marks']])

print(df)
