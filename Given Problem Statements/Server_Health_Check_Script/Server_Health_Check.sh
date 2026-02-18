#!/bin/bash

echo "[CPU USAGE]"
cpu_idle=$(top -bn1 | grep "Cpu(s)" | awk '{print $8}' | cut -d'.' -f1)
cpu_usage=$((100 - cpu_idle))
echo "CPU Usage: $cpu_usage%"
echo

echo "[MEMORY USAGE]"
free -m | awk 'NR==2{printf "Memory Usage: %s/%s MB (%.2f%%)\n", $3, $2, $3*100/$2 }'
echo

echo "[DISK USAGE]"
df -h | grep -vE '^Filesystem|tmpfs|devtmpfs'
echo

echo "[TOP PROCESSES BY CPU USAGE]"
ps aux --sort=-%cpu | head -n 6
echo

echo "[ACTIVE NETWORK CONNECTIONS]"
if command -v netstat >/dev/null 2>&1; then
    netstat -tunapl | head -n 10
else
    ss -tunapl | head -n 10
fi
echo