#capitals of indian states quiz
print('hello welcome to this quiz on capitals of states of india')
rounds=int(input('how many rounds do you want to play? '))
list_of_states=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands"]
list_of_capitals=['amaravati','itanagar','dispur','patna','Raipur','panaji','gandhi nagar','chandigarh','shimla','srinagar','ranchi','bengaluru','trivandrum','bhopal','mumbai','imphal','Shillong','Aizawl','Kohima','bhubaneshwar','chandigarh','jaipur','Gangtok','chennai','hyderabad','agartala','lucknow','dehradun','kolkata','port blair']
l2=list_of_capitals
l1=list_of_states
import random
points=0
for i in range(rounds):
    state=random.choice(l1)
    print('what is the capital city of:',state)
    capital=l2[l1.index(state)]
    ans=input('enter the capital:').lower()
    if capital.lower()==ans.lower():
        print('that is the correct answer')
        points+=1
    else:
        print('that was a wrong answer,the correct answer is',capital)
    l1.remove(state)
    l2.remove(capital)
print('that was the end of the game')
print('your total score was:',points,'out of a maximum',rounds)
