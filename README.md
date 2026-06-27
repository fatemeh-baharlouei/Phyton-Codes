# Python Scripts — ANN Modeling & Learning Exercise

A collection of Python scripts including ANN surrogate model development for building performance prediction, alongside a hands-on learning exercise completed during Python training.

---

## 📁 Repository Structure

```
📁 Training ANN Models/
    ANN model architecture, training pipelines, and evaluation scripts
    for building energy and daylighting performance prediction.

📁 Daily To-Do List Project/
    A small project built during Python learning, covering core
    programming concepts and practical scripting exercises.
```

---

## ANN Surrogate Models

This folder contains Python scripts developed for training and evaluating Artificial Neural Network surrogate models as part of research on kinetic façade control and building performance simulation.

### What the models do
- Predict building energy and daylighting performance metrics
- Replace computationally expensive EnergyPlus/Radiance simulations with fast ANN predictions
- Support multi-objective optimization workflows for kinetic façade control

### Key result
- Achieved **R² = 0.98** on test data, confirming high surrogate model accuracy

### How to run
1. Install dependencies (see Requirements below)
2. Prepare your dataset as a `.csv` file
3. Run the training script:
   ```bash
   python train_model.py
   ```

---

## Daily To-Do List Project

A beginner-to-intermediate Python project built during structured Python training. It covers practical programming concepts including data handling with pandas, user input, and script structuring.

---

## Requirements

Install dependencies using pip:

```bash
pip install tensorflow scikit-learn pandas numpy matplotlib joblib tabulate
```

### ANN Models

| Library | Purpose |
|---|---|
| TensorFlow / Keras | Building and training ANN models |
| scikit-learn | Data splitting, scaling, and evaluation metrics |
| pandas | Data loading and preprocessing |
| NumPy | Numerical computations |
| matplotlib | Plotting training curves and results |
| joblib | Saving and loading scaler objects |

### Daily To-Do List Project

| Library | Purpose |
|---|---|
| tabulate | Formatting terminal table output |
| csv, sys, datetime | Built-in Python libraries, no installation needed |

> Python 3.8 or higher is recommended.

---

## Author

**Fatemeh (Bahar) Baharlouei**  
MSc in Building Science — Shahid Beheshti University  
📧 fa.baharlouei@gmail.com  
🔗 [linkedin.com/in/fatemehbaharlouei](https://linkedin.com/in/fatemehbaharlouei)
