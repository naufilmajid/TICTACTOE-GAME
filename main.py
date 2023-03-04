
def sum(a,b,c):
    return a+b+c
def printBoard(xstate,Zstate):
    zero='x' if xstate[0] else('O' if Zstate[0] else 0)
    one='x' if xstate[1] else('O' if Zstate[1] else 1)
    two='x' if xstate[2] else('O' if Zstate[2] else 2)
    three='x' if xstate[3] else('O' if Zstate[3] else 3)
    four='x' if xstate[4] else('O' if Zstate[4] else 4)
    five='x' if xstate[5] else('O' if Zstate[5] else 5)
    six='x' if xstate[6] else('O' if Zstate[6] else 6)
    seven='x' if xstate[7] else('O' if Zstate[7] else 7)
    eight='x' if xstate[8] else('O' if Zstate[8] else 8)

    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three}| {four} | {five} ")
    print(f"--|---|---")
    print(f"{six}| {seven} | {eight} ")
    pass
def checkwin(xstate,Zstate):
    xwins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in xwins:
        if(sum(xstate[win[0]],xState[win[1]],xstate[win[2]])==3):
            print("X won the match")
            return 1
        if(sum(Zstate[win[0]],ZState[win[1]],Zstate[win[2]])==3):
            print("O won the match")
            return 0
    return-1

if __name__=="__main__":
        xState=[0,0,0,0,0,0,0,0,0]
        ZState=[0,0,0,0,0,0,0,0,0]
        turn=1 # 1 for x and 0 for o
        print("Welcome to TIC TAC TOE")
        while(True):
            printBoard(xState,ZState)
            if(turn==1):
                print("X's Chance")
                value=int(input("please enter the value: "))
                xState[value]=1
            else:
                print("O's Chance")
                value=int(input("please enter the value: "))
                ZState[value]=1
            cwin=checkwin(xState,ZState)
            if (cwin!=-1):
                print("Match over")
                break
            
            turn=1-turn  

