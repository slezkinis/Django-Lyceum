#!/bin/bash
echo $1 > test.txt
echo -e "$1" | python3 data/solution.py
# rm test.txt