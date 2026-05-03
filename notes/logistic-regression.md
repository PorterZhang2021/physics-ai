# Logistic Regression

## 1. What is Logistic Regression?

Logistic Regression is a **classification algorithm** used to predict the probability that an input belongs to a particular category (class).

Despite its name containing "regression," it is **not** used for predicting continuous values like house prices. Instead, it solves **classification problems** such as:

- Email: Spam or Not Spam?
- Tumor: Malignant or Benign?
- Loan: Default or Not Default?

---

## 2. Why Not Use Linear Regression for Classification?

If we use linear regression for classification:
- The predicted value can be **any real number** (e.g., -200, 500).
- Classification needs output between **0 and 1** (probability).
- Linear regression is sensitive to outliers in classification tasks.

**Solution:** Use the **Sigmoid Function** to squeeze any value into the range (0, 1).

---

## 3. The Sigmoid (Logistic) Function

The sigmoid function is the heart of logistic regression:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

Where:
- $z = w^T x + b$ (linear combination of features)
- $e$ is Euler's number (~2.718)

**Properties:**
- If $z \to +\infty$, $\sigma(z) \to 1$
- If $z \to -\infty$, $\sigma(z) \to 0$
- If $z = 0$, $\sigma(z) = 0.5$

---

## 4. Decision Boundary

After getting the probability $\hat{y}$:

$$
\hat{y} =
\begin{cases}
1 & \text{if } \sigma(z) \geq 0.5 \\
0 & \text{if } \sigma(z) < 0.5
\end{cases}
$$

The value **0.5** is called the **decision threshold**. You can adjust it based on your problem.

---

## 5. Cost Function

Using Mean Squared Error (MSE) for logistic regression makes the cost function **non-convex**, so gradient descent might get stuck in local minima.

Instead, we use **Log Loss** (Cross-Entropy Loss):

$$
J(w, b) = -\frac{1}{m} \sum_{i=1}^{m} \left[ y^{(i)} \log(\hat{y}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)}) \right]
$$

Where:
- $m$ = number of training examples
- $y^{(i)}$ = actual label (0 or 1)
- $\hat{y}^{(i)}$ = predicted probability

**Intuition:**
- If $y = 1$ and $\hat{y} \approx 1$ → cost is near 0 ✓
- If $y = 1$ and $\hat{y} \approx 0$ → cost is very high ✗

---

## 6. Gradient Descent

To minimize the cost function, we update parameters $w$ and $b$:

$$
w := w - \alpha \frac{\partial J}{\partial w}
$$

$$
b := b - \alpha \frac{\partial J}{\partial b}
$$

Where $\alpha$ is the **learning rate**.

The derivatives are surprisingly similar to linear regression:

$$
\frac{\partial J}{\partial w} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)}) x^{(i)}
$$

$$
\frac{\partial J}{\partial b} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})
$$

---

## 7. Multi-Class Classification (Softmax)

For more than 2 classes, we use **Softmax Regression** (a generalization of logistic regression).

For class $j$:

$$
P(y = j | x) = \frac{e^{z_j}}{\sum_{k=1}^{K} e^{z_k}}
$$

Where $K$ is the total number of classes.

---

## 8. Key Assumptions

1. The dependent variable is **binary** (or categorical for softmax).
2. Observations are **independent** of each other.
3. There is **no multicollinearity** among features (or it is low).
4. There is a **linear relationship** between log-odds and features.

---

## 9. Pros and Cons

| Pros | Cons |
|------|------|
| Simple and fast | Assumes linear decision boundary |
| Easy to interpret | Can underfit complex data |
| Provides probabilities | Sensitive to outliers |
| Works well with linearly separable data | Requires feature scaling for best results |

---

## 10. Common Use Cases

- Medical diagnosis (disease: yes/no)
- Credit scoring (approve/reject loan)
- Marketing (will customer buy: yes/no)
- Spam detection

---

## 11. Quick Python Example (scikit-learn)

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Generate sample data
X, y = make_classification(n_samples=1000, n_features=4, random_state=42)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)

# Accuracy
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy:.2f}")
```

---

## 12. Key Terms Glossary

| Term | Meaning |
|------|---------|
| **Sigmoid** | Function that maps any value to (0, 1) |
| **Odds** | $p / (1 - p)$ — ratio of success to failure |
| **Log-odds (Logit)** | $\log(p / (1 - p))$ — linear in logistic regression |
| **Decision Boundary** | Line/surface separating classes |
| **Threshold** | Cutoff value (default 0.5) for classification |
| **Cross-Entropy** | Loss function for classification |

---

> **Tip:** Logistic regression is often the **first algorithm** you should try for any binary classification problem before moving to more complex models like neural networks!
