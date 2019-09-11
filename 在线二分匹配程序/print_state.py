
def print_state(left,right,edge,i):
    print("第",i,"轮")
    print(("左边"))
    for ii in range(len(left)):
        print(left[ii][0])
    print("右边")
    for ii in range(len(right)):
        print(right[ii][0])
    print("边值")
    for ii in range(len(edge)):
        print(edge[ii][0]," ",edge[ii][1]," ",edge[ii][2])
