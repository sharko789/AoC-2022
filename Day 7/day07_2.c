#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "txtio.h"

#define MAX_NAME_LENGTH 255

typedef struct _directory directory_t;
typedef struct _file file_t;

struct _file {
    int size;
    char name[MAX_NAME_LENGTH];
    directory_t *parent;
    file_t *next;
};

struct _directory {
    char name[MAX_NAME_LENGTH];
    int size;
    int files;
    file_t *first_file;
    file_t *last_file;
    int children;
    directory_t *first_child;
    directory_t *last_child;
    directory_t *parent;
    directory_t *next;
};



file_t* create_file(char *name, int size) {
    file_t *file = malloc(sizeof(file_t));
    file->size = size;
    strncpy(file->name, name, MAX_NAME_LENGTH);
    file->parent = NULL;
    file->next = NULL;

    return file;
}


directory_t* create_directory(char *name) {
    directory_t *directory = malloc(sizeof(directory_t));
    strncpy(directory->name, name, MAX_NAME_LENGTH);
    directory->size = 0;
    directory->files = 0;
    directory->first_file = NULL;
    directory->last_file = NULL;
    directory->children = 0;
    directory->first_child = NULL;
    directory->last_child = NULL;

    directory->parent = NULL;
    directory->next = NULL;

    return directory;
}


// add a file to the end of a directories file list
void add_file(file_t *file, directory_t *parent) {
    if(parent->first_file == NULL) {
        parent->first_file = file;
        parent->last_file = file;
    } else {
        parent->last_file->next = file;
        parent->last_file = file;
    }
    parent->files++;
    file->parent = parent;
} 


// add a directory to the end of a parent directories children list
void add_directory(directory_t *directory, directory_t *parent) {
    if(parent->first_child == NULL) {
        parent->first_child = directory;
        parent->last_child = directory;
    } else {
        parent->last_child->next = directory;
        parent->last_child = directory;
    }
    parent->children++;
    directory->parent = parent;
}


void build_path(directory_t *root, char **file, size_t file_len) {
    directory_t *current = root;

    for(size_t i = 1; i < file_len; i++) {
        if(file[i][0] == '$') {                         // line is a command
            if(file[i][2] == 'c') {                     // command is cd
                if(file[i][5] == '.') {                 // command is cd ..
                    current = current->parent;
                    printf("cd ..\n");
                } else {                                // command is cd <directory>
                    char *dirname = strrchr(file[i], ' ') + 1;
                    directory_t *dir = current->first_child;
                    for(int i = 0; i < current->children; i++) {
                        if(strcmp(dirname, dir->name) != 0) {
                            dir = dir->next;
                        } else {
                            break;
                        }
                    }
                    current = dir;
                    printf("cd %s", dir->name);
                }
            } else {                                    // command is ls
                continue;
            }
        } else {                                        // line is a response
            if((int) file[i][0] < 58) {                 // response is a file (57 = '9')
                char *filename = strrchr(file[i], ' ') + 1;
                int size = atoi(file[i]);

                file_t *file = create_file(filename, size);
                add_file(file, current);

                printf("added file %s(%d) to %s", filename, size, current->name);
            } else {                                    // response is a directory
                char *dirname = strchr(file[i], ' ') + 1;
                directory_t *new_directory = create_directory(dirname);
                add_directory(new_directory, current);

                printf("added dir %s to %s", dirname, current->name);
            }
        }
    }
}

void print_path(directory_t *root) {
    printf("%d\n", root->first_child->files);
    printf("%d\n", root->first_child->next->size);
    printf("%s", root->first_child-> next->name);
    printf("%d\n", root->first_child->next->first_file->size);

}

int calculate_directory_size(directory_t *dir) {
    file_t *file = dir->first_file;
    while (file != NULL) {
        dir->size += file->size;
        file = file->next;
    }

    directory_t *child = dir->first_child;
    while (child != NULL) {
        dir->size += calculate_directory_size(child);
        child = child->next;
    }
    return dir->size;
}

void solve(directory_t *dir, int *lower_bound, int *smallest_so_far) {
    if(dir->size > *lower_bound && dir->size < *smallest_so_far) {
        *smallest_so_far = dir->size;
    }

    directory_t *child = dir->first_child;
    while (child != NULL) {
        solve(child, lower_bound, smallest_so_far);
        child = child->next;
    }
    printf("%d\n", *smallest_so_far);
}

int main() {
    size_t file_len;
    char** file = read_file("input.txt", &file_len);
    
    directory_t *root = create_directory("/\n");
    build_path(root, file, file_len);
    calculate_directory_size(root);

    // print_path(root);

    int *i = malloc(sizeof(int));
    *i = 70000000 - root->size;
    printf("frei: %d\n", *i);
    *i = -1 * *i + 30000000;
    printf("benötigt: %d\n", *i);

    int *j = malloc(sizeof(int));
    *j = root->size;
    solve(root, i, j);
    
    free_file(file, file_len);
}
