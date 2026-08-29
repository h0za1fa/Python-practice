import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def compute_model_output(x, w, b):
    m = len(x)
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b
    return f_wb



data = pd.read_csv('advertising.csv')
TV_spending = data['TV']
sales = data['Sales']

w_ = 0
b_ = 20

X_train = np.array(TV_spending)
y_train = np.array(sales)

tmp_f_wb = compute_model_output(X_train, w_, b_)
plt.plot(X_train, tmp_f_wb, color='blue', label='prediction')

# plotting the data
plt.scatter(X_train,y_train)
plt.title('TV spending vs sales')
plt.xlabel('TV spending')
plt.ylabel('sales')
plt.show()


