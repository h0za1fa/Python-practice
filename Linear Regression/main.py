import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Linear Regression/Boston.csv')

def linear_decent(m_now, b_now, df, learning_rate):
    m_gradient = 0
    b_gradient = 0

    for i in range (len(df)):
        x = df.iloc[i].indus
        y = df.iloc[i].tax

        m_gradient += (-2/len(df)) * x * (y - (m_now * x + b_now)) 
        b_gradient += (-2/len(df)) *  (y - (m_now * x + b_now))
    m = m_now - (learning_rate * m_gradient)
    b = b_now - (learning_rate * b_gradient)
    return m,b


plt.xlabel('Industrial Proportion')
plt.ylabel('Taxes')
plt.title('Linear Regression: Industrial Proportion vs Taxes')
plt.scatter(df.indus, df.tax)

learning_rate = 0.00001
m = 0
b = 0

for i in range(1000):
    m, b = linear_decent(m , b, df, learning_rate)

plt.plot(list(range(0,30)), [m * x + b for x in range(0,30)])

plt.show()
