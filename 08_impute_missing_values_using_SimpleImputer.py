import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data = {
    'Marks': [90, np.nan, 85, 95]
}

df = pd.DataFrame(data)

imputer = SimpleImputer(strategy='mean')

df['Marks'] = imputer.fit_transform(df[['Marks']])

print(df)
