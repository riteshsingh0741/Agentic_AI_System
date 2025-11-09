import os
import matplotlib.pyplot as plt

def read_metrics(file_path):
    """Reads the metrics report and returns a dictionary of values."""
    metrics = {}
    with open(file_path, "r") as f:
        for line in f:
            key, value = line.strip().split(": ")
            metrics[key] = float(value)
    return metrics

def visualize_results():
    report_path = "reports/metrics_report.txt"

    if not os.path.exists(report_path):
        print("⚠️ No metrics_report.txt found. Please run main.py first.")
        return

    # Read metrics
    metrics = read_metrics(report_path)
    avg_raw = metrics["average_raw_score"]
    avg_refined = metrics["average_refined_score"]
    improvement = metrics["improvement_percent"]

    print("\n📊 Story Refinement Metrics")
    print(f"Average Raw Score: {avg_raw:.2f}")
    print(f"Average Refined Score: {avg_refined:.2f}")
    print(f"Improvement: {improvement:.2f}%")

    # Plot comparison bar chart
    plt.figure(figsize=(6, 4))
    plt.bar(["Before Refinement", "After Refinement"], [avg_raw, avg_refined],
            color=["gray", "green"])
    plt.title("User Story Quality Improvement (INVEST-based)")
    plt.ylabel("Average Score (%)")
    plt.ylim(0, 100)

    # Label values above bars
    for i, v in enumerate([avg_raw, avg_refined]):
        plt.text(i, v + 2, f"{v:.2f}%", ha="center", fontweight="bold")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_results()
