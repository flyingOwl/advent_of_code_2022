SCRIPTS = $(wildcard src/*.py)
INPUT = $(patsubst src/%.py, input/%.txt, $(SCRIPTS))
PUZZLES = $(patsubst src/%.py, puzzle_%, $(SCRIPTS))
url = $(shell echo $@ | sed -e "s/input\/0\?\([0-9]\+\).txt/2022\/day\/\1\/input/g")
num = $(shell echo $@ | sed -e "s/\(puzzle_\|example_\)//g")

all: $(PUZZLES)

input: $(INPUT)

input/%.txt: .session
	curl -H @.session https://adventofcode.com/$(url) > $@

puzzle_%: input/%.txt
	python src/$(num).py $^

example_%: input/example/%.txt
	python src/$(num).py $^
