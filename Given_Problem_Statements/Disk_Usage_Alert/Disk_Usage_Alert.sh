#! /bin/bash

THRESHOLD=40

usage=$(df -hP / | awk 'NR==2 {gsub("%","",$5); print $5}')

# Validate numeric value
if [[ "$usage" -gt "$THRESHOLD" ]]; then
    echo "High disk usage: ${usage}%"
else
    echo "Disk usage is OK: ${usage}%"
fi