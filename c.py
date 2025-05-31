import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X, [2 + 0.6*i for i in X], color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Linear Regression Concept')
plt.show()