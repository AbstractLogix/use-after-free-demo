"""
Purpose: Analyzes the results of the vulnerability and mitigation demonstrations and provides visual feedback or summaries.
Contents: Analysis functions, result summarization, and optional visualization tools (e.g., generating charts or graphs to illustrate the effects of the vulnerability and its mitigation).
"""

import matplotlib.pyplot as plt


# Example function for saving a graph
def save_graph(data):
    plt.figure()
    plt.plot(data)
    plt.savefig("/app/graphs/my_graph.png")  # Save to the mounted volume directory
