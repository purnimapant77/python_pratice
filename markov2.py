def markov_chain(matrix):
    n=len(matrix)
    print("matrix:")
    for row in matrix:
        print(row)
        
    all_positive=True
    row_sum_one=True
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j]<0 or matrix[i][j]>1:
                all_positive=False
                break
    
    for i in range(n):
        s=sum(matrix[i])
        print(f"Sum of row {i+1}:{s}")
        if(abs(s-1)>-.0001):
            row_sum_one=False
            
    if all_positive and row_sum_one:
        print("The given matrix follow markov property")
    else:
        print("The given matrix doesnot follow markov property")
    
matrix=[[0.2,0.5,0.3],[0.3,0.3,0.4],[0.7,0.2,0.1]]
markov_chain(matrix)