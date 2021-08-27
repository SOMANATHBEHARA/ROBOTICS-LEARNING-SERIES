import random
ans = input('enter your over:  ')       #enter your number of overs.
if ans.isdigit():
    ans = int(ans)                       # cheak the number weather it is a digit or not and if it is a digit then save it as integer.
    over = 6*ans
else:
    print('enter a valid value, again start the game ')
#make the competure to guess a value and print it with screen with target greater than one.and make variable and give them value .

comptarget = random.randint(1, over)
print(' competure scored', comptarget, 'your target is ', comptarget + 1)
ball = 1
batover = 1
csguess = random.randint(0, 6)
point = 0
cspoint = 0
run = None
#print the initial number of over and ball
print(' over ', batover, ' ball', ball)
#make a loop satisfing the above condition and write our program for given condition.
while ball != 7 and batover != ans + 1:
    run = input('enter number to bat:  ')
    if run.isdigit() :
        run = int(run)
        if run > 0 and run < 7:                   #it will decided if a input is in between 1 and 6 or not
            point = point + run
            ball += 1
            csguess = random.randint(0, 6)          #competure will also guess a number between 0 to 6
            
            print('competure number:  ', csguess)
            cspoint = cspoint + csguess
            
            
            if run == csguess  :
                print('sorry!! you lose... competure guessed your number')
                break
            elif comptarget < point :
                j = point - cspoint
                print('congratulation!!!you won, you reached the target')
                if j > 0 :
                    print('and you won the game with', j,'run ahead')
                break
            elif ball > 6:                               #after completing a over we should skip to the next over
                batover += 1
                ball = 1
                
                if batover > ans:
                    print('game is over, your over is complete')     # if a over complete then game should be over
                    break
            print('over', batover, 'ball', ball)
        else:
            print('please enter the value between 1 to 6 only')
               
        
    else:
        print('enter a valid digit')
# print the score
print('your total run is:  ', point)
print('competure total run is:  ', cspoint)
