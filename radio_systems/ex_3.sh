#!/bin/bash
if [ $# -ne 2]; then
	echo "Usage: $0 <file> <word>"
	exit 1
fi
grep -w "$2" "$1"
