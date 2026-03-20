import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

data = pd.read_csv(os.path.join(BASE_DIR, '../data/student_data.csv'))

X = data[['hours', 'attendance']]
y = data['marks']

model = RandomForestRegressor()
model.fit(X, y)

with open(os.path.join(BASE_DIR, '../model/performance_model.pkl'), 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained")