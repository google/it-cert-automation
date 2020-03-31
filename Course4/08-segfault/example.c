/*
 * Copyright 2020 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** copy_parameters(int argc, char* argv[]) {
    char **parameters = malloc(sizeof(char *) * argc);

    for (int i = 0; i <= argc; i++) {
        size_t len = strlen(argv[i]) + 1;
        parameters[i] = malloc(len);
        strncpy(parameters[i], argv[i], len);
    }

    return parameters;
}

struct options {
    int verbosity;
    char *output;
    bool text;
    bool progress;
    int jobs;
};

typedef struct options options_t;

options_t process_parameters(int argc, char** parameters);

struct information {
    char **clients;
    char **providers;
    char **products;
    int *relations;
};

typedef struct information information_t;

information_t prepare_data(options_t *options);

void generate_output(information_t *data, options_t *options);

int main(int argc, char* argv[]) {

    // We are going to modify the arguments so we make a copy to keep the
    // original ones in argv.
    char **parameters = copy_parameters(argc, argv);

    options_t options = process_parameters(argc, parameters);

    information_t data = prepare_data(&options);

    generate_output(&data, &options);
}

options_t process_parameters(int argc, char** argv) {
    options_t options = { 0 };

    return options;
}

information_t prepare_data(options_t *options) {
    information_t data = { 0 };

    return data;
}

void generate_output(information_t *data, options_t *options) {
}
