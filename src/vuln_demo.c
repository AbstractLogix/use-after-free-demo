#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void demonstrate_vulnerability();
void demonstrate_mitigation();

int main()
{
    printf("Demonstrating use-after-free vulnerability...\n");
    demonstrate_vulnerability();

    printf("\nDemonstrating mitigation...\n");
    demonstrate_mitigation();

    return 0;
}

// Function to demonstrate a use-after-free vulnerability
void demonstrate_vulnerability()
{
    char *buffer = malloc(100); // Allocate memory
    strcpy(buffer, "This is some text in the buffer.");
    printf("Before free: %s\n", buffer);

    free(buffer); // Free the memory

    // Use after free - attempting to use the buffer after it has been freed
    printf("After free: %s\n", buffer); // Undefined behavior: buffer is freed
}

// Function to demonstrate a basic mitigation technique
void demonstrate_mitigation()
{
    char *buffer = malloc(100); // Allocate memory
    strcpy(buffer, "This is safe text in the buffer.");
    printf("Before free: %s\n", buffer); // Show the buffer's content

    free(buffer);  // Free the memory
    buffer = NULL; // Mitigation: Nullify the pointer after freeing to prevent use after free

    // SAFE: check if buffer is NULL before using it
    if (buffer != NULL)
    {
        printf("After free: %s\n", buffer);
    }
    else
    {
        printf("After free: Buffer is nullified, preventing use-after-free.\n");
    }
}
