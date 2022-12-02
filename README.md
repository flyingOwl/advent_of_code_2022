# Advent of Code 2022

This repository contains the python code I used to solve the [2022 Advent of Code](https://adventofcode.com/2022) puzzles. As a personal challenge, I tried not to use more than 500 bytes for each solution without looking at other peoples solution on reddit.

The python file for each day contains the solution for both parts. The scripts will only output a tuple or list with two elements: the answer for part 1 and for part 2.

## Makefile and .session

The Makefile can do two things:

- download the input files
- run the python scripts

To download the input files, you need to provide your Cookie in the `.session` file. You can find your session key by using the developer tools of your browser.

```
$ cat .session
Cookie: session=abc123abc123...abc123;
```

The Makefile will download the input files to `input/[day].txt`. To automatically download the input and run the script for the first day, e.g., just call:

```
$ make puzzle_01
```

Running `make` without arguments (or with `all`) will download and solve all puzzles.

To run the script with the example input, you need to provide the input via `input/example/[day].txt` and run `make example_[day]`.

