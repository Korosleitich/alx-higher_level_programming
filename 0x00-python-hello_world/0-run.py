#!/bin/bash

file="$PYFILE"

if [ -f "$file" ];
    python "$file"
else
    echo "File not found: $file"
