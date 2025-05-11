import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parâmetros (sinta-se livre para alterar)
delta = 0.1
alpha = -1.0
beta = 8.0
A = 1.2
phi = 1.3




# Equação de Duffing convertida para sistema de 1ª ordem
def duffing(t, y):
    x, dx = y
    ddx = -delta*dx - alpha*x - beta*x**3 + A*np.cos(phi*t)
    return [dx, ddx]

# Condições iniciais
x0 = 1.0
dx0 = 0.0
y0 = [x0, dx0]

# Intervalo de tempo
t_span = (0, 50)
t_eval = np.linspace(*t_span, 2000)

# Solução numérica
sol = solve_ivp(duffing, t_span, y0, t_eval=t_eval)

# Plot x(t)
plt.figure(figsize=(10, 4))
plt.plot(sol.t, sol.y[0])
plt.title("Posição x(t) do Oscilador de Duffing")
plt.xlabel("Tempo")
plt.ylabel("x(t)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot x'(t)
plt.figure(figsize=(10, 4))
plt.plot(sol.t, sol.y[1])
plt.title("Velocidade x'(t) do Oscilador de Duffing")
plt.xlabel("Tempo")
plt.ylabel("x'(t)")
plt.grid(True)
plt.tight_layout()
plt.show()
