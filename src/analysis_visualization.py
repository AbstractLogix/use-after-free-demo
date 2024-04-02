"""
Purpose: Analyzes the results of the vulnerability and mitigation demonstrations and provides visual feedback or summaries.
Contents: Analysis functions, result summarization, and optional visualization tools (e.g., generating charts or graphs to illustrate the effects of the vulnerability and its mitigation).
"""

import re
from collections import defaultdict
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


def parse_asan_output(log_file):
    leak_pattern = re.compile(
        r"Indirect leak of (\d+) byte\(s\).*allocated from:\n\s*#\d+ (\S+)"
    )
    leaks = defaultdict(int)

    with open(log_file, "r") as file:
        for match in re.finditer(leak_pattern, file.read()):
            bytes_leaked, source = match.groups()
            leaks[source] += int(bytes_leaked)

    return leaks


def generate_leak_summary_chart(leaks, output_file):
    # Sort leaks by byte size for the chart
    sorted_leaks = sorted(leaks.items(), key=lambda x: x[1], reverse=True)[
        :10
    ]  # Top 10 leaks
    sources, bytes_leaked = zip(*sorted_leaks)

    plt.figure(figsize=(10, 8))
    plt.barh(sources, bytes_leaked, color="skyblue")
    plt.xlabel("Bytes Leaked")
    plt.title("Top Memory Leaks by Source")
    plt.tight_layout()
    plt.savefig(output_file)
