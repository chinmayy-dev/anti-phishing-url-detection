import csv
from url_features import extract_features

def load_urls(filepath):
    with open(filepath, "r") as f:
        return [line.strip() for line in f if line.strip()]
    
phishing_urls = load_urls("data/phishing_urls.txt")
legit_urls = load_urls("data/legitimate_urls.txt")

with open("data/dataset_schema.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(
        [
            "url_length",
            "dot_count",
            "hyphen_count",
            "has_https",
            "has_ip",
            "suspicious_keyword_count",
            "entropy",
            "label"
        ]
    )

    for url in phishing_urls:
        features = extract_features(url)
        writer.writerow(
            [
                features["url_length"],
                features["dot_count"],
                features["hyphen_count"],
                int(features["has_https"]),
                int(features["has_ip"]),
                features["suspicious_keyword_count"],
                features["entropy"],
                1
            ]
        )
    for url in legit_urls:
        features = extract_features(url)
        print(features.keys())

        writer.writerow(
            [
                features["url_length"],
                features["dot_count"],
                features["hyphen_count"],
                int(features["has_https"]),
                int(features["has_ip"]),
                features["suspicious_keyword_count"],
                features["entropy"],
                0
            ]
        )
