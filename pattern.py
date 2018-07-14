def pattern(inputstr,table):
    l=len(inputstr) 
    print inputstr
    if l ==1:
        return table.get(inputstr,[])

    result_list=list()
    for index in range(l-1):
        print index
        sub_list=pattern(inputstr[index+1:],table)
        for suffix in sub_list:
            print "suffixes are:" +str(sub_list)
            print "key is {}".format(inputstr[0:index+1])
            output=table.get(inputstr[0:index+1],[])
            print output
            for prefix in output:
                result_list.append(prefix+suffix)
    
    return result_list

if __name__=="__main__":
    table={ '1': ['A', 'B', 'C'],
            '2': ['D', 'E'],
	    '12': ['X'],
	    '3': ['P', 'Q']}
    print(pattern('123',table))
