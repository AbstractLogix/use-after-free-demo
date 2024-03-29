from cffi import FFI
import os

ffi = FFI()

ffi.cdef(
    """
    void demonstrate_vulnerability();
    void demonstrate_mitigation();
    """
)

lib = ffi.dlopen("./vuln_demo.so")


def read_output(file_path: str) -> str:
    """Reads the content of a file.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file.
    """
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "No output generated"


def demonstrate_vulnerability():
    """Call the C function to demonstrate the use-after-free vulnerability."""
    lib.demonstrate_vulnerability()
    return read_output("vulnerability_output.txt")


def demonstrate_mitigation():
    """Call the C function to demonstrate how the vulnerability can be mitigated."""
    lib.demonstrate_mitigation()
    return read_output("mitigation_output.txt")
