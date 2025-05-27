# oscilador-duffing
# Oscilador de Duffing — Simulações em Python

Este repositório contém as simulações numéricas realizadas para o **Trabalho 1 da disciplina de Equações Diferenciais Ordinárias (EDO)**, ministrada na Universidade Federal de Goiás (UFG).

## 🎓 Projeto Acadêmico
**Aluno:** Carlos Alberto Rodrigues da Silva Junior  
**Curso:** Ciência da Computação  
**Matrícula:** 202200498  
**Tema:** Oscilador de Duffing e Sensibilidade às Condições Iniciais  
**Professor:** Dr. Rodrigo Donizete Euzébio  

---

## 🧠 Descrição

O **Oscilador de Duffing** é um sistema dinâmico não linear que estende o modelo de mola-massa da Lei de Hooke, adicionando uma componente cúbica na força de restituição. Sua equação diferencial é:
      
      d²x/dt² + δ dx/dt + αx + βx³ = A cos(ϕt)


Este projeto visa:

- Analisar a não linearidade do sistema
- Observar comportamentos periódicos e caóticos
- Estudar a **sensibilidade às condições iniciais**
- Visualizar as soluções para diferentes conjuntos de parâmetros

---

## 🛠️ Tecnologias e Métodos Utilizados

- **Python 3.10+**
- Biblioteca `SciPy` – método de Runge-Kutta (`solve_ivp`)
- Biblioteca `Matplotlib` – geração de gráficos
- Biblioteca `NumPy`

---

## 📊 Simulações

Foram simulados diferentes conjuntos de parâmetros:

| Conjunto | δ   | α    | β    | A   | φ   |
|----------|-----|------|------|-----|-----|
| 1        | 0.2 | -1.0 | 1.0  | 0.5 | 1.2 |
| 2        | 0.1 | -1.0 | 5.0  | 1.0 | 1.5 |
| 3        | 0.1 | -1.0 | 8.0  | 1.2 | 1.3 |

Também foi realizada uma análise com **β ≈ 0** para comparação com o comportamento linear, além de simulações com variações pequenas nas **condições iniciais (ε)** para observar o surgimento de caos.


## 🌀 Resultados

As simulações revelam:

- Comportamento quase periódico em β baixos
- Aumento da complexidade com β altos
- Divergência das soluções com pequenas variações em ε
- Evidência de **comportamento caótico**

---

## 📥 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/CarlosjuniorBr1/oscilador-duffing.git
   cd oscilador-duffing
   
   pip install -r requisitos.txt
   python duffing_simulation.py

📚 Referências
Duffing, G. Erzwungene Schwingungen... (1918)

Strogatz, S. H. Nonlinear Dynamics and Chaos (2015)

Boyce, W.; DiPrima, R. Elementary Differential Equations

SciPy Docs: solve_ivp

Matplotlib: https://matplotlib.org


      

