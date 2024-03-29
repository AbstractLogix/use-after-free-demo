# mitigation_demo.py
from cffi_loader import demonstrate_mitigation

def run_mitigation_demo():
    """
    Executes the demonstration of mitigating a use-after-free vulnerability.
    This function calls the C function through CFFI that applies mitigation
    techniques to prevent the exploitation of freed memory, showcasing safe
    memory handling practices.
    """
    print("Starting Mitigation of Use-After-Free Vulnerability Demonstration...")
    try:
        # Call the C function that demonstrates the mitigation
        demonstrate_mitigation()
        print("Mitigation demonstration complete. Notice the safe handling of freed memory.")
    except Exception as e:
        print(f"An error occurred during the mitigation demonstration: {e}")

if __name__ == "__main__":
    run_mitigation_demo()
