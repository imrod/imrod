# Read from the file file.txt and output the tenth line to stdout.
solution1:
flag=1
while read line
do
    if [ $flag -eq 10 ]; then
        echo "$line"
        exit 0
    fi
    ((flag++))
done < file.txt

solution2:
cat file.txt | awk 'NR==10'
