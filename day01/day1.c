#include <stdio.h>
#include <string.h>

#define MAX_LEN 36

int main(void)
{
    FILE* fp;
    fp = fopen("file.txt", "r");
    if (fp == NULL) {
      perror("Failed: ");
      return 1;
    }

    char buffer[MAX_LEN];
    while (fgets(buffer, MAX_LEN, fp))
    {
        // Remove trailing newline
        buffer[strcspn(buffer, "\n")] = 0;
        printf("%s\n", buffer);
    }

    fclose(fp);
    return 0;
}