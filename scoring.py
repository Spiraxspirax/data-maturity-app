# scoring.py

import pandas as pd

def score_responses(responses_dict):
    scores = {}
    for domain, answers in responses_dict.items():
        domain_score = sum(answers) / len(answers)
        scores[domain] = round(domain_score, 2)
    return scores

def maturity_level(score):
    if score < 1.5: return "Level 1 – Initial"
    if score < 2.5: return "Level 2 – Developing"
    if score < 3.5: return "Level 3 – Defined"
    if score < 4.5: return "Level 4 – Managed"
    return "Level 5 – Optimized"

