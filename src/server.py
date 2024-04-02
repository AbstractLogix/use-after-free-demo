import os
import logging
from flask import Flask, render_template, request, send_from_directory
from cffi_loader import demonstrate_mitigation, demonstrate_vulnerability
import analysis_visualization as av

logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]",
)

app = Flask(__name__)
GRAPHS_DIR = os.path.join(app.root_path, "graphs")

VULNERABILITY_OUTPUT_FILE = os.path.join(GRAPHS_DIR, "vulnerability_output.txt")
MITIGATION_OUTPUT_FILE = os.path.join(GRAPHS_DIR, "mitigation_output.txt")


def clear_file_content(file_path: str):
    """Clears the content of a file.

    Args:
        file_path (str): The path to the file to be cleared.
    """
    open(file_path, "w").close()


# Log every request
@app.before_request
def before_request_logging():
    app.logger.debug("Received request: %s %s", request.method, request.url)


# Log every response
@app.after_request
def after_request_logging(response):
    app.logger.debug("Response status: %s", response.status)
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # Placeholder for authentication logic
    # WARNING: This example does not include secure authentication practices
    if username == "admin" and password == "password":
        return "Login Successful"
    else:
        return "Login Failed", 401


@app.route("/trigger-vulnerability")
def trigger_vulnerability():
    app.logger.info("Triggering vulnerability")
    output = demonstrate_vulnerability()
    is_vulnerable = "after free:" in output.lower()
    av.save_graph([int(is_vulnerable)], "vulnerability_graph.png")
    clear_file_content(VULNERABILITY_OUTPUT_FILE)
    return render_template(
        "result.html", text_output=output, graph_file="vulnerability_graph.png"
    )


@app.route("/trigger-mitigation")
def trigger_mitigation():
    app.logger.info("Triggering mitigation")
    output = demonstrate_mitigation()
    is_mitigated = "nullified" in output.lower()
    av.save_graph([int(is_mitigated)], "mitigation_graph.png")
    clear_file_content(MITIGATION_OUTPUT_FILE)
    return render_template(
        "result.html", text_output=output, graph_file="mitigation_graph.png"
    )


@app.route("/graphs/<filename>")
def serve_graph(filename):
    """
    Serve a graph image from the graphs directory.
    """
    return send_from_directory(GRAPHS_DIR, filename)


@app.route("/analyze-leaks")
def analyze_leaks():
    log_file = "/app/logs/container_output.log"
    output_file = "leak_summary.png"

    # Parse the AddressSanitizer log and generate a summary chart
    leaks = av.parse_asan_output(log_file)
    av.generate_leak_summary_chart(leaks, f"/app/graphs/{output_file}")

    # Clear the log file after analysis
    open(log_file, "w").close()

    # Display the result
    return render_template("analysis_result.html", graph_file=output_file)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
