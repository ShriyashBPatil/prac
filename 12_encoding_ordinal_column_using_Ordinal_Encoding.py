import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

data = {
    'Grade': ['Low', 'Medium', 'High']
}

df = pd.DataFrame(data)

encoder = OrdinalEncoder(categories=[['Low', 'Medium', 'High']])

df['Grade_Encoded'] = encoder.fit_transform(df[['Grade']])

print(df)
