file="GCS_3_problems_20221105"

if [ -f "$file" ];then

    if [ -s "$file" ]; then
        echo 0
    else
        echo 1
    fi
else
    echo 2
fi
