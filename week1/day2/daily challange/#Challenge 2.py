#Challenge 2
#Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
#Examples

#user's word : "ppoeemm" ➞ "poem"

#user's word : "wiiiinnnnd" ➞ "wind"

#user's word : "ttiiitllleeee" ➞ "title"

#user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
#Notes
#Final strings won’t include words with double letters (e.g. “passing”, “lottery”).
s = input("Enter the string: ") 
newstr = '' 
for letter in s: 
	if letter not in newstr: 
		newstr += letter 
print("The string with duplicate letters removed:", newstr)