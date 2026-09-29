задача 1 : cut -d: -f1 /etc/passwd | sort


задача 2: cat /etc/protocols | grep -v '^#' | sort -nr | head -n 5 | awk '{print $1, $2}'


задача 3: 
  GNU nano 8.7.1                                                 banner *                                                        

length=${#text}

line=$(printf '%*s' $((length + 2)) '' | tr ' ' '-')

echo "+${line}+"
echo "| ${text} |"
echo "+${line}+"
-------------------
chmod +x banner
./banner "Hello from RTU MIREA!"




задача 4:
nano identifilers
#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi


cat "$1" | grep -oE '...твоя регулярка...' | sort | uniq | tr '\n' ' '
echo "" 

chmod +x identifilers

./identifilers hello.c
задача 5:

c  GNU nano 8.7.1                                                                                 
#!/bin/bash
nano reg

chmod +x "$1"
sudo cp "$1" /usr/local/bin/


sudo ./reg banner  

задача 6:



задача 7:
задача 8:
задача 9:
задача 10:
