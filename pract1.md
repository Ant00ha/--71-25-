задача 1 : cut -d: -f1 /etc/passwd | sort


задача 2: cat /etc/protocols | grep -v '^#' | sort -nr | head -n 5 | awk '{print $1, $2}'


задача 3: 
  GNU nano 8.7.1                                                                                                    

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

#!/bin/bash


if [ -z "$1" ]; then
    echo "Использование: $0 <путь>"
    exit 1
fi


find "$1" -type f \( -name "*.c" -o -name "*.js" -o -name "*.py" \) | while read -r file; do
   
    first_line=$(head -n 1 "$file")

    
    if grep -qE '^\s*(//|/\*|#)' <<< "$first_line"; then
        echo "$file: ЕСТЬ комментарий"
    else
done
=========================
mkdir -p /tmp/test_comments && cd /tmp/test_comments

echo "// Это C комментарий" > good.c
echo "int main() { return 0; }" > bad.c
echo "# Python комментарий" > good.py
echo "print('hello')" > bad.py
echo "// JS комментарий" > good.js
echo "var x = 5;" > bad.js
echo "Не подходит по расширению" > ignore.txt

=========================


./zadanie6 /tmp/test_comments



задача 7:

!/bin/bash


if [ -z "$1" ]; then
    echo "Использование: $0 <путь>"
    exit 1
fi


declare -A hashes


while IFS= read -r -d '' file; do
    
    hash=$(md5sum "$file" | cut -d' ' -f1)
    
    hashes["$hash"]+="$file"$'\n'
done < <(find "$1" -type f -print0)


for hash in "${!hashes[@]}"; do
    
    count=$(printf '%s' "${hashes[$hash]}" | grep -c '^')
    if [ "$count" -gt 1 ]; then
        echo "Дубликаты (хеш: $hash):"
        printf '%s' "${hashes[$hash]}"
        echo
    fi
done
==============

./dupes /tmp/dupes

==============result

Дубликаты (хеш: 09f7e02f1290be211da707a266f153b3):
/tmp/dupes/sub/file3.txt
/tmp/dupes/file2.txt
/tmp/dupes/file1.txt


задача 8:
задача 9:
задача 10:
