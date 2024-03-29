def QuickSort(Elements,start,end):
    #as we are using recursive call our
    #code can change the value of start and end
    #so we start with a codition start<end 
    #if start is not smaller than end 
    #that means we have alredy sorted that part and we have 
    #reached at the end where the list cannot be divided further
    if start<end:
        #we find the position of pivot
        #i will call pivot as monitor
        Monitor=Sort(Elements,start,end)
        #So we have the position of Pivot in Monitor
        #and Monitor is standing at its correct place.
        #now as we know its position we sort the remaining elements
        #elements before pivot and elements after pivot
        QuickSort(Elements,start,Monitor-1)
        QuickSort(Elements,Monitor+1,end)

        
#now lets write the Sort function.
#This function returns the index of the Monitor
#and it also sorts the monitor from others 
def Sort(Elements,start,end):
    #we take an index to store smaller element call s
    s=start-1
    #we start s by s-1 because while we will be storing the elements we will
    #increment first and then store the elements
    Monitor=Elements[end]
    j=start
    while(j<end):
        if Elements[j]<Monitor:
            s+=1
            Elements[s],Elements[j]=Elements[j],Elements[s]
        j+=1
    #Now when we are out of the loop we have the position
    #s which is at the location where last smaller element
    #was added
    #so the position where out montior should be exzatly after this element
    #i.e at s+1
    #so we swap the element at s+1 position with the last elemet
    #i.e with our Monitor/Pivot element
    Elements[s+1],Elements[end]=Elements[end],Elements[s+1]
    #then we return the position of Monitor Which is  used by our QuickSort
    #function to call itself later
    return(s+1)
