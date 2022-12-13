#include <stdlib.h>
#include <stdio.h>


int count_lines(FILE *file_p) {
    char cr;
    size_t lines = 0;

    while(cr != EOF) {
        if (cr == '\n') {
            lines++;
        }
        cr = getc(file_p);
    }
    printf("Number of lines: %ld\n", lines); 
    rewind(file_p);

    return lines;
}



void print_file(char **file, size_t file_len) {
    for(size_t i = 0; i < file_len; i++) {
        printf("%s", file[i]);
    }
}

char** read_file(char *filename, size_t *file_len) {

    FILE *file_p = fopen(filename, "r");
    printf("Opened file: %s\n", filename); 

    *file_len = count_lines(file_p);
    
    char **data = malloc(sizeof(char *) * *file_len);

    for (size_t i = 0; i < *file_len; i++) {
        data[i] = NULL;
        size_t n = 0;

        getline(&data[i], &n, file_p);
    }

    // for (size_t i = 0; i < *file_len; i++) {
    //         printf("%s", data[i]);
    //         // free(data[i]);
    //     }

    // Close File
    fclose(file_p);

    return data;
}

void free_file(char **file, size_t file_len) {
    for(size_t i = 0; i < file_len; i++) {
        free(file[i]);
    }
    free(file);
}