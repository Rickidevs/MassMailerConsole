#!/bin/bash

chmod +x "main.py"

sudo cp "main.py" /usr/local/bin/rickmail

if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Python3 is loading..."
    sudo apt-get install -y python3
fi

if ! python3 -c "import colorama" &> /dev/null; then
    echo "Colorama is not installed. Colorama is loading..."
    sudo pip install colorama
fi

python_modules=("time" "os" "smtplib")
for module in "${python_modules[@]}"; do
    if ! python3 -c "import $module" &> /dev/null; then
        echo "$module module not installed $module Loading module..."
        sudo pip install $module
    fi
done
