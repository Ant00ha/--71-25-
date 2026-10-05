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
-------------------------------------------------------------------------------
# Практическое занятие №2. Менеджеры пакетов
## Задача 1
```
pip show matplotlib
```
## Как получить пакет без менеджера пакетов, прямо из репозитория?
```
curl -s https://pypi.org/pypi/matplotlib/json | jq -r '.urls[] | select(.packagetype=="sdist") | .url' | xargs curl -O
tar -xzf matplotlib-*.tar.gz
cd matplotlib-*
python setup.py install
```
## Задача 2
```
npm view express
```
## Как получить пакет без менеджера пакетов, прямо из репозитория?
```
curl -s https://registry.npmjs.org/express/latest | jq -r '.dist.tarball' | xargs curl -O
tar -xzf express-*.tgz
cd package
```
## Задача 3
## matplotlib
```
digraph matplotlib_deps {
    rankdir=LR;
    node [shape=box, style=filled, color=lightblue];
    
    matplotlib [color=lightgreen];
    numpy;
    pillow;
    pyparsing;
    cycler;
    fonttools;
    kiwisolver;
    packaging;
    python_dateutil [label="python-dateutil"];

    matplotlib -> numpy;
    matplotlib -> pillow;
    matplotlib -> pyparsing;
    matplotlib -> cycler;
    matplotlib -> fonttools;
    matplotlib -> kiwisolver;
    matplotlib -> packaging;
    matplotlib -> python_dateutil;
}
```
## expess
```
digraph express_deps {
    rankdir=LR;
    node [shape=box, style=filled, color=lightyellow];
    
    express [color=lightgreen];
    accepts;
    body_parser [label="body-parser"];
    cookie;
    debug;
    qs;

    express -> accepts;
    express -> body_parser;
    express -> cookie;
    express -> debug;
    express -> qs;
}
```
## Задача 4
```
include "all_different.mzn";

array[1..6] of var 0..9: digits;

constraint all_different(digits);

constraint digits[1] + digits[2] + digits[3] = digits[4] + digits[5] + digits[6];

solve minimize digits[1] + digits[2] + digits[3];

output [
    "Билет: \(digits[1])\(digits[2])\(digits[3]) - \(digits[4])\(digits[5])\(digits[6])\n",
    "Сумма первой тройки: \(digits[1] + digits[2] + digits[3])\n",
    "Сумма второй тройки: \(digits[4] + digits[5] + digits[6])\n"
];
```
## Задача 5
```
var {0, 100, 110, 120, 130, 140, 150}: menu;
var {0, 180, 200, 210, 220, 230}: dropdown;
var {0, 100, 200}: icons;

constraint menu > 0;
constraint icons == 100;

constraint menu == 100 -> dropdown == 180;
constraint menu >= 110 -> dropdown >= 200;

constraint dropdown >= 200 -> icons == 200;

solve satisfy;

output [
  "menu: ", show(menu), "\n",
  "dropdown: ", show(dropdown), "\n",
  "icons: ", show(icons), "\n"
];
```
## Задача 6
```
var {0, 100}: root;
var {0, 100, 110}: foo;
var {0, 100}: left;
var {0, 100}: right;
var {0, 100, 200}: shared;
var {0, 100, 200}: target;

constraint root == 100;

constraint root == 100 -> (foo >= 100 /\ foo < 200 /\ target >= 200 /\ target < 300);

constraint foo == 110 -> (left >= 100 /\ left < 200 /\ right >= 100 /\ right < 200);

constraint left == 100 -> shared >= 100;

constraint right == 100 -> (shared > 0 /\ shared < 200);

constraint shared == 100 -> (target >= 100 /\ target < 200);

solve satisfy;

output [
  "root: ", show(root), "\n",
  "foo: ", show(foo), "\n",
  "left: ", show(left), "\n",
  "right: ", show(right), "\n",
  "shared: ", show(shared), "\n",
  "target: ", show(target), "\n"
];
```
## Задача 7
```
import asyncio
from minizinc import Instance, Model, Solver

PACKAGES_DB = {
    "root": {
        "1.0.0": {"foo": "^1.0.0", "target": "^2.0.0"}
    },
    "foo": {
        "1.0.0": {},
        "1.1.0": {"left": "^1.0.0", "right": "^1.0.0"}
    },
    "left": {
        "1.0.0": {"shared": ">=1.0.0"}
    },
    "right": {
        "1.0.0": {"shared": "<2.0.0"}
    },
    "shared": {
        "1.0.0": {"target": "^1.0.0"},
        "2.0.0": {}
    },
    "target": {
        "1.0.0": {},
        "2.0.0": {}
    }
}


def version_to_int(v_str: str) -> int:
    parts = list(map(int, v_str.split('.')))
    return parts[0] * 10000 + parts[1] * 100 + parts[2]


def int_to_version(v_int: int) -> str:
    if v_int == 0:
        return "Not Installed"
    major = v_int // 10000
    minor = (v_int % 10000) // 100
    patch = v_int % 100
    return f"{major}.{minor}.{patch}"


def parse_constraint(pkg_var: str, constraint_str: str) -> str:
    if constraint_str.startswith("^"):
        v = constraint_str[1:]
        base = version_to_int(v)
        major = int(v.split('.')[0])
        next_major = (major + 1) * 10000
        return f"({pkg_var} >= {base} /\\ {pkg_var} < {next_major})"
    elif constraint_str.startswith(">="):
        base = version_to_int(constraint_str[2:])
        return f"({pkg_var} >= {base})"
    elif constraint_str.startswith("<"):
        base = version_to_int(constraint_str[1:])
        return f"({pkg_var} > 0 /\\ {pkg_var} < {base})"
    elif constraint_str.startswith("=="):
        base = version_to_int(constraint_str[2:])
        return f"({pkg_var} == {base})"
    else:
        base = version_to_int(constraint_str)
        return f"({pkg_var} == {base})"


def generate_mzn_code(db: dict, root_pkg: str, root_ver: str) -> str:
    lines = []

    for pkg, versions in db.items():
        v_ints = [0] + [version_to_int(v) for v in versions.keys()]
        v_set = "{" + ", ".join(map(str, sorted(v_ints))) + "}"
        lines.append(f"var {v_set}: {pkg};")

    lines.append("")
    lines.append(f"constraint {root_pkg} == {version_to_int(root_ver)};\n")

    for pkg, versions in db.items():
        for v_str, deps in versions.items():
            v_int = version_to_int(v_str)
            if not deps:
                continue

            dep_conds = [parse_constraint(dep_pkg, expr) for dep_pkg, expr in deps.items()]
            full_deps = " /\\ ".join(dep_conds)
            lines.append(f"constraint {pkg} == {v_int} -> ({full_deps});")

    lines.append("\nsolve satisfy;")
    return "\n".join(lines)


async def main():
    target_package = "root"
    target_version = "1.0.0"

    mzn_code = generate_mzn_code(PACKAGES_DB, target_package, target_version)

    model = Model()
    model.add_string(mzn_code)
    
    solver = Solver.lookup("gecode")
    instance = Instance(solver, model)

    result = await instance.solve_async()

    if result.status.has_solution():
        for pkg in PACKAGES_DB.keys():
            val = result[pkg]
            print(f"{pkg}: {int_to_version(val)}")
    else:
        print("Unsatisfiable")

if __name__ == "__main__":
    asyncio.run(main())

```
