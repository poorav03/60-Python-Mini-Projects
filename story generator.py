import random
when = ["A few years ago","Yesterday","Last Night","A long time ago","On 20th Jan"]
who = ["a rabbit","an elephant","a mouse","a turtle","a cat"]
name = ["Ali","Mimi","Danny","Daniels","Jhonny","StarBoy"]
residence = ["Barcelona","India","Germany","Ireland","Venice","England"]
went = ["cinema","university","seminar","school","laundry"]
happened = ["made a lot of friends","Eats a burger","found a secret key","solved a mistery","wrote a book"]
print(random.choice(when)+", "+random.choice(who)+" that lived in "+random.choice(residence)+" went to the "+random.choice(went)+" and "+random.choice(happened))
