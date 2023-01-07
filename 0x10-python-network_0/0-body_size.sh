#!/bin/bash
#A bash script that displayin length
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
