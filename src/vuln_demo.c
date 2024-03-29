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

// Utility function to write output to a file
void write_output(const char *filename, const char *output)
{
    FILE *file = fopen(filename, "w");
    if (file != NULL)
    {
        fprintf(file, "%s", output);
        fclose(file);
    }
    else
    {
        printf("Failed to open file for writing.\n");
    }
}

// Function to demonstrate a use-after-free vulnerability
void demonstrate_vulnerability()
{
    char *buffer = malloc(100); // Allocate memory
    strcpy(buffer, "This is some text in the buffer.");

    // Create a copy of buffer's address for demonstration
    char *buffer_copy = buffer;

    // Before freeing, show what's in the buffer
    char output_before[256];
    snprintf(output_before, sizeof(output_before), "Before free: %s\n", buffer);
    printf("%s", output_before); // Print to stdout for immediate feedback

    free(buffer); // Free the memory

    // Attempt to use buffer after it has been freed
    // WARNING: This is just for demonstration and is unsafe
    char output_after[256];
    snprintf(output_after, sizeof(output_after), "After free (UNSAFE): %s\n", buffer_copy);

    // Combine before and after free messages
    char combined_output[512];
    snprintf(combined_output, sizeof(combined_output), "%s%s", output_before, output_after);

    // Write combined output to a file
    write_output("vulnerability_output.txt", combined_output);
}

// Function to demonstrate a basic mitigation technique
void demonstrate_mitigation()
{
    char *buffer = malloc(100); // Allocate memory
    if (buffer == NULL)
    {
        printf("Memory allocation failed\n");
        return;
    }
    strcpy(buffer, "This is safe text in the buffer.");

    // Prepare the message to be written before freeing the buffer
    char output_before[256];
    snprintf(output_before, sizeof(output_before), "Before free: %s\n", buffer);

    free(buffer);  // Free the memory
    buffer = NULL; // Mitigation: Nullify the pointer after freeing to prevent use after free

    // Prepare the message after freeing and nullifying the buffer
    char output_after[256];
    snprintf(output_after, sizeof(output_after), "After free: Buffer is nullified, preventing use-after-free.\n");

    // Combine before and after free messages
    char combined_output[512];
    snprintf(combined_output, sizeof(combined_output), "%s%s", output_before, output_after);

    // Use the write_output function to write the combined message to a file
    write_output("mitigation_output.txt", combined_output);
}