## Phishing urls usually have:

- Longer URL length
- More than 2 dot count
- 2 or more than 2 Suspicious keywords
- Higher entropy
- Number of hyphen is unusually larger
- Has IP

* if from the above given points, if 2 or more than 2 things are present in a URL, there might be a potential risk.


## Random Forest:

- In Random forest, feature importance tells us how much that feature helped us in reducing impurity across all trees.
- Higher value = More influence in the decision making.

* The top 5 highest contributing features for the model were:
1. url_length - 0.419971
2. entropy - 0.281174
3. dot_count - 0.114114
4. has_https - 0.089157
5. hyphen_count - 0.079998