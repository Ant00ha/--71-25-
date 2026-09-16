задача 1 : cut -d: -f1 /etc/passwd | sort
задача 2: grep -v '^#' /etc/protocols | sort -k2 -nr | head -n 5 | awk '{print $2, $1}'
задача 3: 
  GNU nano 8.7.1                                                 banner *                                                        

length=${#text}

line=$(printf '%*s' $((length + 2)) '' | tr ' ' '-')

echo "+${line}+"
echo "| ${text} |"
echo "+${line}+"
-------------------
./banner "Hello from RTU MIREA!"
задача 4:
задача 5:
задача 6:
задача 7:
задача 8:
задача 9:
задача 10:
