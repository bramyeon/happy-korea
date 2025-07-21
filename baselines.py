import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
import argparse



from datetime import datetime

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor

import xgboost as xgb
import lightgbm as lgb

import numpy as np
import torch

# Parameters
ROOT_DIR = '.'
DATA_DIR = 'data'
DATA_DIR = os.path.join(ROOT_DIR, DATA_DIR)
SEED = 20244078
lr = 1e-3

parser = argparse.ArgumentParser()
parser.add_argument('--data_name', type=str, help="Specify the data name")
args = parser.parse_args()
data_name = args.data_name

print(f"Data directory: {DATA_DIR}")
print(f"Seed: {SEED}")
print(f"Data name: {data_name}")

random.seed(SEED)
np.random.seed(SEED)

df_train = pd.read_csv(os.path.join(DATA_DIR, f"preprocessed/{data_name}-train.csv"))
df_test = pd.read_csv(os.path.join(DATA_DIR, f"preprocessed/{data_name}-test.csv"))

df_train['bias'] = -1.
df_test['bias'] = -1.

df_train_label = torch.tensor(df_train['happiness_ladder'].tolist(), dtype=torch.float)
df_test_label = torch.tensor(df_test['happiness_ladder'].tolist(), dtype=torch.float)

del df_train['happiness_ladder']
del df_test['happiness_ladder']

df_train_data = torch.tensor(df_train.values, dtype=torch.float)
df_test_data = torch.tensor(df_test.values, dtype=torch.float)

df_train_data.shape, df_train_label.shape, df_test_data.shape, df_test_label.shape

all_in = df_train_data.shape[1]
print(f'Number of input features: {all_in}')

def LinRegression(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def L1Regression(X_train, y_train):
    model = Lasso(alpha=0.1, random_state=SEED)
    model.fit(X_train, y_train)
    return model

def L2Regression(X_train, y_train):
    model = Ridge(alpha=1.0, random_state=SEED)
    model.fit(X_train, y_train)
    return model

def L2Regression(X_train, y_train):
    model = Ridge(alpha=1.0, random_state=SEED)
    model.fit(X_train, y_train)
    return model

def MLP(X_train, y_train):
    model = MLPRegressor(hidden_layer_sizes=(100,), max_iter=300, random_state=SEED)
    model.fit(X_train, y_train)
    return model

print("LinRegression...")
model = LinRegression(df_train_data, df_train_label)
df_test_pred = model.predict(df_test_data)
mse = mean_squared_error(df_test_label, df_test_pred)
rmse = np.sqrt(mse)
r2 = r2_score(df_test_label, df_test_pred)
print(f"Test RMSE : {rmse:.4f}")
print(f"Test R²   : {r2:.4f}\n")

print("L1Regression...")
model = L1Regression(df_train_data, df_train_label)
df_test_pred = model.predict(df_test_data)
mse = mean_squared_error(df_test_label, df_test_pred)
rmse = np.sqrt(mse)
r2 = r2_score(df_test_label, df_test_pred)
print(f"Test RMSE : {rmse:.4f}")
print(f"Test R²   : {r2:.4f}\n")

print("L2Regression...")
model = L2Regression(df_train_data, df_train_label)
df_test_pred = model.predict(df_test_data)
mse = mean_squared_error(df_test_label, df_test_pred)
rmse = np.sqrt(mse)
r2 = r2_score(df_test_label, df_test_pred)
print(f"Test RMSE : {rmse:.4f}")
print(f"Test R²   : {r2:.4f}\n")

print("MLP...")
model = MLP(df_train_data, df_train_label)
df_test_pred = model.predict(df_test_data)
mse = mean_squared_error(df_test_label, df_test_pred)
rmse = np.sqrt(mse)
r2 = r2_score(df_test_label, df_test_pred)
print(f"Test RMSE : {rmse:.4f}")
print(f"Test R²   : {r2:.4f}\n")

print("NeuralNetwork-4...")
df = pd.read_csv('./data/inference-korea-complex-4-200.csv')
mse = mean_squared_error(df['label'], df['output'])
rmse = np.sqrt(mse)
r2 = r2_score(df['label'], df['output'])
print(f"Test RMSE : {rmse:.4f}")
print(f"Test R²   : {r2:.4f}\n")