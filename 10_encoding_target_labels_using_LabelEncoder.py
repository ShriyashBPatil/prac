from sklearn.preprocessing import LabelEncoder

data = ['Pass', 'Fail', 'Pass', 'Fail']

encoder = LabelEncoder()

encoded = encoder.fit_transform(data)

print(encoded)
