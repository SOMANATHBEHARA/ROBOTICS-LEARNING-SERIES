import random
ans = input('enter your over:  ')
if ans.isdigit():
    ans = int(ans)
    over = 6*ans
else:
    print('enter a valid value, again start the game ')

comptarget = random.randint(1, over)
print(' competure scored', comptarget, 'your target is ', comptarget + 1)
ball = 1
batover = 1
csguess = random.randint(0, 6)
point = 0
cspoint = 0
run = None
print(' over ', batover, ' ball', ball)
while ball != 7 and batover != ans + 1:
    run = input('enter number to bat:  ')
    if run.isdigit() :
        run = int(run)
        if run > 0 and run < 7:
            point = point + run
            ball += 1
            csguess = random.randint(0, 6)
            print('competure number:  ', csguess)
            cspoint = cspoint + csguess
            if ball > 6:
                batover += 1
                ball = 1
                s = print('over', batover, 'ball', ball)
                if batover > ans:
                    print('game is over, your over is complete')
                    break
            elif run == csguess:
                print('sorry!! you lose... competure guessed your number')
                break
            elif comptarget < point :
                j = point - cspoint
                print('congratulation!!!you won, you reached the target')
                if j > 0 :
                    print('and you won the game with', j,'run ahead')
                break
        else:
            print('please enter the value between 1 to 6 only')
            
       
    
        
        
            
        
    else:
        print('enter a valid digit')

print('your total run is:  ', point)
print('competure total run is:  ', cspoint)



