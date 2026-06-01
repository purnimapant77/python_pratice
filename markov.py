def markov_chain(m):
    n=len(m)
    print("Matric:")
    for row in m:
        print(row)
        
    all_positive=True
    row_sum_one=True
    
    for i in range(n):
        for j in range(n):
            if m[i][j]<0 or m[i][j]>1:
                all_positive=False
                break
            
    for i in range(n):
        s=sum(m[i])
        print(f"Sum of row {i+1}:{round(s,2)}")
        
    if abs(s-1)>0.0001:
        row_sum_one=False
    if all_positive and row_sum_one:
        print("The givem matrix is markov chain")
    else:
        print("The given matrix is not markov chain")
        
        
m=[[1.0,3.0],[4.0,2.0]]
markov_chain(m)