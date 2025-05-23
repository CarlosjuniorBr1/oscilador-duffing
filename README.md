
# Oscilador de Duffing — Simulação Numérica com Python

Este repositório contém a simulação numérica do **Oscilador de Duffing**, um sistema dinâmico não linear com aplicações em física, engenharia e sistemas caóticos. A simulação é feita com Python usando o método de Runge-Kutta (`solve_ivp`) para resolver a equação diferencial de segunda ordem.

##  Equação do Oscilador de Duffing

\[
\frac{d^2x}{dt^2} + \delta \frac{dx}{dt} + \alpha x + \beta x^3 = A \cos(\varphi t)
\]

- \( \delta \): coeficiente de amortecimento
- \( \alpha \), \( \beta \): constantes da mola
- \( A \): amplitude da força externa
- \( \varphi \): frequência da força externa

## 🔧 Requisitos

- Python 3.8+
- Bibliotecas:

```bash
pip install numpy scipy matplotlib
