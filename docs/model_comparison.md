Model Comparison

## Logistic Regression:
- Accuracy: 0.9404761904761905
- Precision: 0.9375
- Recall: 0.9574468085106383
- F1: 0.9473684210526315

## Random Forest:
- Accuracy: 0.9642857142857143
- Precision: 0.9583333333333334
- Recall: 0.9787234042553191
- F1: 0.968421052631579


## Observation:
- Random Forest outperformed Logistic Regression across all metrics.
- Recall improved from 0.957 to 0.979, indicating fewer phishing URLs were missed.
- Precision also improved, reducing false positives.
- The consistent improvement suggests that the dataset contains non-linear feature interactions that Random Forest captures more effectively.


## Overfitting

- Overfitting happens when model performs extremely well on training data but performs very poor on the unseen test data.
- That means the model memorized patterns instead of learning general rules.

- For our model we have: 
- Training accuracy (0.97) is slightly higher than test accuracy (0.94), indicating minor overfitting. However, the gap is small, suggesting the model generalizes well.
