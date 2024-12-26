PlayerName=input("Enter name of the player")
score=int(input('Enter the score'))
result=""
if score==0:
    result="Deck Out"
elif score<=50:
    result="Below half centuary"   
elif score==50:
    result="Half Centuary"
elif 50<=score <=100:
    result="Above half Century"
    print("The name of player is {},his score is {},his result is{}".format(PlayerName,score,result)) 
    #print("The name of player is {2},his score is {0},his result is{1}".format(score,result ,PlayerName)) if attributrs are not in order
    #we give numbers
