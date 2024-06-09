n,k,a,b=map(int,input().split())

goal_floor=n-1
elvator = (goal_floor+(k-1))*b
stair=goal_floor*a

print(elvator,stair)