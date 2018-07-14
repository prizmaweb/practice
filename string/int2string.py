def int2str(val):
    mapping="0123456789" 
    result=""
    signed =0
    if val ==0:
        return "0"
    if  val <0:
        val *=-1
        signed=1
    while val >0:
        x=val %10
        result+=mapping[x]
        val//=10
    if signed:
        result +="-"
    return result[::-1]

if __name__ == '__main__':
    print(int2str(-1))

    
    
