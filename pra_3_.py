##20CE112 Yash Patel
##Github Repository Link
##https://github.com/Yash-3122/Assignment3
##Find Captain's Room Number

N = int(input())

room = map(int, input().split())
room = sorted(room)

for i in range(len(room)):
    if(i != len(room)-1):
        if(room[i]!=room[i-1] and room[i]!=room[i+1]):
            print(room[i])
            break;
    else:
        print(room[i])

