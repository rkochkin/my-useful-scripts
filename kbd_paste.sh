#!/bin/bash
A=$(xclip -o)
sleep 5s;
echo "$A" | xdotool type -- "$A"

