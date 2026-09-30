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


cat "$1" | grep -oE "[a-zA-Z_][a-zA-Z0-9_]*" | sort | uniq | tr '\n' ' '
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

nano make_archive

#!/bin/bash


if [ "$#" -ne 2 ]; then
    echo "Использование: $0 <директория> <расширение>"
    exit 1
fi

DIR="$1"
EXT="$2"

if [ ! -d "$DIR" ]; then
    echo "Ошибка: директория '$DIR' не найдена"
    exit 1
fi

ARCHIVE="archive_${EXT}.tar"


find "$DIR" -type f -name "*.$EXT" -print0 | tar -cf "$ARCHIVE" --null -T -

echo "Архив '$ARCHIVE' создан."

=============test
mkdir -p /tmp/archive_test/subdir
cd /tmp/archive_test

echo "test1" > a.txt
echo "test2" > b.txt
echo "test3" > subdir/c.txt
echo "не txt" > d.log
echo "с пробелом" > "my file.txt"

./make_archive /tmp/archive_test txt

задача 9:

nano spaces_to_tab

#!/bin/bash


if [ "$#" -ne 2 ]; then
    echo "Использование: $0 <входной файл> <выходной файл>"
    exit 1
fi

IN="$1"
OUT="$2"


if [ ! -f "$IN" ]; then
    echo "Ошибка: файл '$IN' не найден"
    exit 1
fi


sed 's/    /\t/g' "$IN" > "$OUT"

echo "Готово: $IN → $OUT"

============test
cat > /tmp/input.txt <<'EOF'
строка с 4 пробелами    конец
строка с 8 пробелами        конец
строка с 2 пробелами  конец
строка с табомвнутри
строка с 6 пробелами      конец
EOF


chmod +x spaces_to_tab

./spaces_to_tab /tmp/input.txt /tmp/output.txt
<img width="1385" height="448" alt="изображение" src="https://github.com/user-attachments/assets/d799082c-832b-400a-a938-4d9afcf523ba" />


задача 10:

 nano find_empty
                                              
                                                                                                     
#!/bin/bash


if [ -z "$1" ]; then
    echo "Использование: $0 <директория>"
    exit 1
fi


if [ ! -d "$1" ]; then
    echo "Ошибка: '$1' — не директория"
    exit 1
fi


while IFS= read -r -d '' file; do
    type=$(file -b "$file")
    
    if [[ "$type" == *text* ]] || [[ "$type" == "empty" ]]; then
    echo "$file"
    fi
done < <(find "$1" -type f -empty -print0) 

===================test
mkdir -p /tmp/empty_test/sub
cd /tmp/empty_test

touch empty1.txt          # пустой .txt
touch empty2              # пустой без расширения
touch sub/empty3.log      # пустой .log в подкаталоге
echo "hello" > notempty.txt   # непустой .txt
touch empty4.png          # пустой .png (с точки зрения file — тоже "empty")

chmod +x find_empty

./find_empty /tmp/empty_test

