#include <stdio.h>
#include <string.h>
#include <sys/personality.h>

int main(int argc, char** argv)
{
    char name[10];
    printf("%p\n", name);

    gets(name);

    printf("Hallo %s\n", name);
    return 0;
}
