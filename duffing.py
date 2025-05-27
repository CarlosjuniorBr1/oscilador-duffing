import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parâmetros (sinta-se livre para alterar)
# Parâmetros mais caóticos
delta = 0.1
alpha = -1.0
beta = 5.0
A = 1.0
phi = 1.5






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
t_span = (0, 200)
t_eval = np.linspace(*t_span, 4000)

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


# Parte 3: Efeito de β pequeno
beta = 0.01  # Valor muito pequeno de beta

def duffing_beta_pequeno(t, y):
    x, dx = y
    ddx = -delta*dx - alpha*x - beta*x**3 + A*np.cos(phi*t)
    return [dx, ddx]

# Mesmas condições iniciais
sol_beta_pequeno = solve_ivp(duffing_beta_pequeno, t_span, y0, t_eval=t_eval)

# Gráfico comparativo com β pequeno
plt.figure(figsize=(10, 4))
plt.plot(sol_beta_pequeno.t, sol_beta_pequeno.y[0], label='β = 0.01')
plt.plot(sol.t, sol.y[0], '--', label='β = 1.0 (original)')
plt.title("Comparação da posição x(t) com β pequeno")
plt.xlabel("Tempo")
plt.ylabel("x(t)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# Parte 4: Sensibilidade às condições iniciais
epsilons = [0.0, 0.05, 0.15]
solucoes = []

for eps in epsilons:
    y_eps = [1.0 + eps, 2.0 + eps]
    sol_eps = solve_ivp(duffing, t_span, y_eps, t_eval=t_eval)
    solucoes.append((eps, sol_eps))

# Gráfico da posição x(t) para diferentes ε
plt.figure(figsize=(10, 4))
for eps, sol_eps in solucoes:
    plt.plot(sol_eps.t, sol_eps.y[0], label=f"ε = {eps}")
plt.title("Sensibilidade às Condições Iniciais – x(t)")
plt.xlabel("Tempo")
plt.ylabel("x(t)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

