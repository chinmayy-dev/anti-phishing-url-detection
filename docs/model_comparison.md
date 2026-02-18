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
