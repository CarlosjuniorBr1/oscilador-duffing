import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#pode variar os parametros de forma que preferir 

#  Conjunto 1 (parâmetros suaves)
# delta = 0.2
# alpha = -1.0
# beta = 1.0
# A = 0.5
# phi = 1.2

# Conjunto 2 (mais caótico)
# delta = 0.1
# alpha = -1.0
# beta = 5.0
# A = 1.0
# phi = 1.5


# Conjunto 3 (parâmetros suaves)
delta = 0.2
alpha = -1.0
beta = 1.0
A = 0.5
phi = 1.2

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
