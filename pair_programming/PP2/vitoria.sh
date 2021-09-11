for entry in `find . -type f -perm +u=x`; do 
   echo "($entry)"
done
