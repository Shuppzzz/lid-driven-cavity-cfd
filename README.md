# lid-driven-cavity-cfd
2D incompressible Navier–Stokes solver in Python for lid-driven cavity flow using the Finite Difference Method.
# Lid Driven Cavity CFD Solver

This project implements a **2D incompressible Navier–Stokes solver in Python** using the **Finite Difference Method (FDM)**. The solver simulates the classical **lid-driven cavity flow** problem, which is widely used for validating Computational Fluid Dynamics (CFD) codes.

---

## Problem Description

The lid-driven cavity problem consists of a square cavity filled with fluid.

- The **top wall moves with constant velocity**
- All other walls remain **stationary**
- This generates a **primary vortex inside the cavity**

This benchmark problem is commonly used to test CFD solvers.

---

## Governing Equations

The solver numerically solves the incompressible Navier–Stokes equations.

Continuity equation:

∂u/∂x + ∂v/∂y = 0

Momentum equations:

du/dt + u du/dx + v du/dy = -1/ρ dp/dx + ν(∂²u/∂x² + ∂²u/∂y²)

dv/dt + u dv/dx + v dv/dy = -1/ρ dp/dy + ν(∂²v/∂x² + ∂²v/∂y²)

A **Pressure Poisson Equation** is used to enforce incompressibility.

---

## Numerical Method

- Spatial discretization: **Finite Difference Method**
- Grid type: **Uniform structured grid**
- Time integration: **Explicit scheme**
- Pressure correction: **Pressure Poisson equation**

---

## Requirements

Install dependencies:

Required libraries:

- numpy
- matplotlib

---

## Running the Simulation

Run the Python solver:


The solver will simulate the flow and generate visualization plots.

---

## Results

The simulation produces:

- Velocity vector field
- Streamline plot showing vortex formation

Example result:

Primary vortex forms at the center of the cavity due to the moving lid.

---

## Project Structure

lid-driven-cavity-cfd
│
├── cavity_flow.py
├── results
│ ├── streamlines.png
│ ├── velocity_vectors.png
│
├── requirements.txt
└── README.md

---

## Future Improvements

- Grid refinement study
- Validation against Ghia et al. benchmark data
- Reynolds number variation
- Flow animation
- Pressure contour visualization

---

## Author

Anantha

Computational Fluid Dynamics Enthusiast

