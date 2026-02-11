from urllib.parse import urlparse
import re
import math
from collections import Counter

def extract_features(url):

    parsed = urlparse(url)
    features = {}

    features["url_length"] = len(url)
    features["dot_count"] = parsed.netloc.count(".")
    features["hyphen_count"] = parsed.netloc.count("-")

    # https is not equivalent to safe website

    features["has_https"] = bool(parsed.scheme == "https")


    ip_address = r"\b\d{1,3}(\.\d{1,3}){3}\b"
    features["has_ip"] = bool(re.search(ip_address, url))

    keywords = ["secure", "login", "verify", "accounts", "update", "check", "security"]
    features["suspicious_keyword_count"] = sum(word in url.lower() for word in keywords)

    # calculates URL entropy (randomness)
    counts = Counter(url)
    entropy = 0
    for char in counts:
        p = counts[char]/len(url)
        entropy -= p * math.log2(p)
    features["entropy"] = round(entropy, 2)

    # label
    
    return features
