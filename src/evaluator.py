import os

def evaluate_dataset(raw_scores, refined_scores):
    """Compute average improvement metrics and save them to reports/."""
    if not raw_scores or not refined_scores:
        return {"average_raw_score": 0, "average_refined_score": 0, "improvement_percent": 0}

    avg_raw = sum(raw_scores) / len(raw_scores)
    avg_refined = sum(refined_scores) / len(refined_scores)
    improvement = compute_improvement(avg_raw, avg_refined)

    metrics = {
        "average_raw_score": round(avg_raw, 2),
        "average_refined_score": round(avg_refined, 2),
        "improvement_percent": round(improvement, 2)
    }

    os.makedirs("reports", exist_ok=True)
    with open("reports/metrics_report.txt", "w") as f:
        for k, v in metrics.items():
            f.write(f"{k}: {v}\n")

    return metrics


def compute_improvement(raw_avg, refined_avg):
    """Calculate percent improvement between averages."""
    if raw_avg == 0:
        return 0
    return ((refined_avg - raw_avg) / raw_avg) * 100
