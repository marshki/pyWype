#!/bin/bash

if [ "$OSTYPE" == "linux-gnu"* ]; then
  	printf "%s\n" "MEMORY: $(free -gh)"

fi
