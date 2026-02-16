Metric Deep Dive

## Accuracy

- Accuracy measures the overall percentage of correct predictions.
- For our model the accuracy turned out to be 0.9875! That's excellent.
- Used cross validation evaluation technique to assess model stability which.
- The cross validation accuracy is 0.9625

## Precision (Phishing Class)

- Precision answers that of all URLs predicted as phishing, how many were actually phishing?
- As per our classification report, our precision is actually 1.00
- This means that of all URLs predicted as phishing, 100% were actually phishing. No false positives!

## Recall (Phishing Class)

- Recall answers that of all actual phishing URLs, how many did the model correctly catch?
- As per our classification report, our recall is 0.98
- This means that 98% of phishing URLs were caught and 2% were missed. Since support = 46, 2% of 46 ≈ 1 URL

## Which Matters More?

- In phishing detection, recall is usually more important than precision.
- Reason:
- If the model misses a phishing URL (false negative), the user may be exposed to a dangerous site.
- A false positive (legit marked as phishing) is inconvenient.
- A false negative (phishing marked as legit) is dangerous.
- Therefore, high recall is critical.


## After introducing more realistic phishing URLs, model accuracy decreased from ~99% to ~94%. Cross-validation results show variation across folds (0.88–0.99), indicating the dataset contains harder samples. This suggests the model is more realistically evaluated and not overfitting to obvious phishing patterns. Precision dropped from 1.00 to 0.9375 and recall dropped from 0.98 to ≈ 0.96 -> This proves that only structural and lexical characteristics to classify a URL into phishing or legitimate is not enough.