for var in "$@"
do
    make py="$var" js
done

for i in simple_recipes/__target__/*.js; do
    # echo "$i"
    FNAME="$(basename "$i" .js)"
    make py="$FNAME" nd
done

