def MergeSort(Arr):
    if len(Arr)>1:
        Middle=len(Arr)//2
        Left=Arr[0:Middle]
        Right=Arr[Middle:]
        MergeSort(Left)
        MergeSort(Right)
        i=j=k=0
        while(i<len(Left) and j<len(Right)):
            if Left[i]<Right[j]:
                Arr[k]=Left[i]
                i+=1
            else:
                Arr[k]=Right[j]
                j+=1
            k+=1
        
        while(i<len(Left)):
            Arr[k]=Left[i]
            i+=1
            k+=1
        while(j<len(Right)):
            Arr[k]=Right[j]
            j+=1
            k+=1
    
