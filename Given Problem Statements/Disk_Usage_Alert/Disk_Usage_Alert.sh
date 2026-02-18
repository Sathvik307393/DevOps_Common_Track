#! /bin/bash

usage=$(df -hP / | awk 'NR==2 {gsub("%","",$5); print $5}')

# Validate numeric value
if [[ "$usage" =~ ^[0-9]+$ ]]; then
    if [[ "$usage" -gt "$THRESHOLD" ]]; then
        echo "High disk usage: ${usage}%"
    else
        echo "Disk usage is OK: ${usage}%"
    fi
else
    echo "Error: Unable to determine disk usage."
    exit 1
fi
