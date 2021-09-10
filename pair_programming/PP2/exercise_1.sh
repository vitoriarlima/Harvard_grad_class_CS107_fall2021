#1. Prompt user file for a file to commit

read -r -p "What file would you like to commit?" file_name

#2. Stage the file

git add $file_name #check why $

#3. Display the results of git status

git status

#4. Ask if the user wants to continue. If they respond N then exti

read -p "Do you want to continue dear? Type y or n " user_input

if [$user_input = "y"]
then 
git push
fi

if [$user_input = "n"]
then 
exit 1
fi 



 
