"""
Purpose: Analyzes the results of the vulnerability and mitigation demonstrations and provides visual feedback or summaries.
Contents: Analysis functions, result summarization, and optional visualization tools (e.g., generating charts or graphs to illustrate the effects of the vulnerability and its mitigation).
"""

import matplotlib.pyplot as plt


def save_graph(data, filename):
    """
    Generate a simple bar chart indicating the presence or absence of a vulnerability.
    'data' is a list with a single boolean value, where True indicates vulnerability/mitigation.
    """
    labels = ["Vulnerable", "Mitigated"]
    values = [
        1 - data[0],
        data[0],
    ] 

    plt.figure()
    plt.bar(labels, values, color=["red", "green"])
    plt.title("Vulnerability Analysis")
    plt.savefig(f"/app/graphs/{filename}")  # Save to the mounted volume directory
