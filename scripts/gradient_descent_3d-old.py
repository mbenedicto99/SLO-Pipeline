# gradient_descent_3d.py

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mlflow

print("✅ Iniciando experimento com Gradiente Descendente em 3D...")

# Função objetivo: z = x^2 + y^2 (paraboloide)
def func(x, y):
    return x**2 + y**2

def grad(x, y):
    return 2*x, 2*y

# Parâmetros do gradiente descendente
lr = 0.1
steps = 30
x, y = 5.0, 5.0  # ponto inicial
trajectory = [(x, y, func(x, y))]

# Executar gradiente descendente
for _ in range(steps):
    dx, dy = grad(x, y)
    x -= lr * dx
    y -= lr * dy
    z = func(x, y)
    trajectory.append((x, y, z))

trajectory = np.array(trajectory)

# Geração da superfície
X = np.linspace(-6, 6, 100)
Y = np.linspace(-6, 6, 100)
X, Y = np.meshgrid(X, Y)
Z = func(X, Y)

# Plotar superfície e trajetória
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis')
ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], color='r', marker='o', label="Descida")
ax.set_title("Gradiente Descendente em 3D")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
plt.tight_layout()
plt.savefig("gradient_descent_3d.png")
plt.show()

print("📉 Gráfico de gradiente descendente salvo como 'gradient_descent_3d.png'")

# Logar no MLflow
mlflow.set_experiment("GradientDescent_3D")
with mlflow.start_run():
    mlflow.log_param("learning_rate", lr)
    mlflow.log_param("steps", steps)
    mlflow.log_param("start_point", [5.0, 5.0])
    mlflow.log_param("end_point", [x, y])
    mlflow.log_artifact("gradient_descent_3d.png")

    print("✅ Experimento logado no MLflow com sucesso!")