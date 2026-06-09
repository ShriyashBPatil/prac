import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8]
}

df = pd.DataFrame(data)

imputer = KNNImputer(n_neighbors=2)

df_imputed = imputer.fit_transform(df)

print(df_imputed)
