# Notes

## To research

AddressSanitizer, MemorySanitizer, UndefinedBehaviorSanitizer, Control Flow Integrity, libFuzzer, or AFL.

## MISC NOTES

Addressing Memory Leaks in vuln_demo.c
Review Memory Allocation and Deallocation: Start by reviewing vuln_demo.c for any memory allocations that may not be properly deallocated. Since you're demonstrating vulnerabilities, ensure that the demonstration includes how to properly manage memory to prevent leaks.

Use of Python C API: If your vuln_demo.c interacts with Python through the C API, make sure that any Python objects you create or manipulate have their reference counts managed correctly. Every Py_INCREF must be matched with a Py_DECREF to avoid leaking Python objects.

Sanitize Resource Management: Given the educational nature of your project, it's crucial to show correct handling of resources in the "mitigated" versions of your demonstrations. This includes properly freeing memory and correctly using the Python C API.

Integration with Python
Debugging and Analysis Tools: Utilize tools like Valgrind in addition to AddressSanitizer to analyze memory usage and potential leaks in your C code. These tools can provide insights into where memory is being allocated and not freed.

Educational Context: If the purpose of vuln_demo.c is educational, showing both vulnerable and fixed (mitigated) code versions, ensure that your demonstrations clearly communicate the importance of proper memory management. This can be an invaluable learning experience for those studying cybersecurity, software vulnerabilities, and memory management.

Python Side Considerations: On the Python side, make sure that any wrappers or interfaces used to interact with the C code properly manage the lifecycle of the objects they create or receive from C. This includes using constructs like with statements for managing resources more cleanly in Python.

General Advice
Code Review and Pair Programming: Since the project has educational goals, consider incorporating code reviews or pair programming sessions focused on security and resource management. These practices can help identify potential issues before they become problematic.
Documentation and Comments: Document both the intended use of the functions within vuln_demo.c and their correct integration with Python. Clear comments and documentation can help learners understand the demonstrations and the importance of proper memory management.
