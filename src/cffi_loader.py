from cffi import FFI

ffi = FFI()

ffi.cdef(
    """
    void demonstrate_vulnerability();
    void demonstrate_mitigation();
    """
)

lib = ffi.dlopen("vuln_demo.dll")


def demonstrate_vulnerability():
    """Call the C function to demonstrate the use-after-free vulnerability."""
    lib.demonstrate_vulnerability()


def demonstrate_mitigation():
    """Call the C function to demonstrate how the vulnerability can be mitigated."""
    lib.demonstrate_mitigation()
