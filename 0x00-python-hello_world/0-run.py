#!/usr/bin/python3

file="$PYFILE"

if [ -f "$file" ];
    python "$file"
else
    echo "File not found: $file"
