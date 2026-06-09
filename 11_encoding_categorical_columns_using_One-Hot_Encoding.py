import pandas as pd

data = {
    'City': ['Mumbai', 'Pune', 'Delhi']
}

df = pd.DataFrame(data)

encoded_df = pd.get_dummies(df, columns=['City'])

print(encoded_df)
