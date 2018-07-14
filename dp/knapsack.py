#either we consider the last or do not
def knapsack(weights,values,maxwt):
    selection=[]
   return  optimal(selection,weights,values,maxwt)

def optimal(selection,weights,values,maxwt):
    #empty
    if len(weights) ==0:
        return 0
    if weights[-1] <= maxwt : 
        with_last=knapsack(selection,weights[:-1],values[:-1],maxwt-weights[-1])
    else
        with_last=0
    without_last=knapsack(selection,weights[:-1],values[:-1],maxwt)

    if with_last >without_last :
        selection.append(len(weights)-1)
        return with_last
    else
        return without_last


