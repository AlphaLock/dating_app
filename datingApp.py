""" Write a dating program compatibility between 2 pple. the prog shd check the no of times TRUE AND LOVE occurs in their combined names """

print ("Welcome To Dating App")
print("="*21)

#prompt user to enter thier name and convert it into lower case
user_name= input('Enter your full name :').lower()
crush_name=input('Enter full name of your crush :').lower()

#concatenate the two names
combine_name = user_name + crush_name

#count the number of times true & love appeared in their combined names


t=combine_name.count('t')
r=combine_name.count('r')
u= combine_name.count('u')
e= combine_name.count('e')
true= t + r + u + e


l=combine_name.count('l')
o=combine_name.count('o')
v= combine_name.count('v')
e= combine_name.count('e')

love= l+ o+ v+ e
#convert love and score to strings and assign to varaible
love_score= str(true) + str(love)

#convert variable love_score into int for easy concatenation
love_score= int(love_score)

if love_score > 80:
   print ("You Are Compatible")
elif love_score > 50:
   print("You might be compatible")
else:
   print ('Hey.....! you guys are like coke and mentos')


