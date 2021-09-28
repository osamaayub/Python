def Alpha_Beta(D,Index,Turn,Score,A,B):
    if D == 3:
        return Score[Index]
    if Turn:
        Best = Beta
        # Recur for left and right children
        for i in range(0, 2):
            V = Alpha_Beta(D+1,Index*2+i,False,Score,A,B)
            Best = max(Best, V)
            A= max(A,Best)
            # Alpha Beta Pruning
            if A>=B:
                break
        return Best
    else:
        Best = Alpha
        # Recur for left and right children
        for i in range(0, 2):
            V = Alpha_Beta(D+1,Index*2+i,True,Score,A,B)
            Best = min(Best,V)
            B= min(B,Best)
            # Alpha Beta Pruning
            if A>=B:
                break
        return Best
# Drive Code
Alpha, Beta = 1000, -1000
Scores = [3,5,6,9,1,2,0,-1]
print("The optimal value is :", Alpha_Beta(0,0,True,Scores,Beta,Alpha))

