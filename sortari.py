#RADIX SORT
def radix_sort(v,baz):
    p=1
    b=[[] for i in range(baz)]
    t=True
    while t==True:
        t=False
        for i in range(baz):
            del b[i][0:]
        for i in range(len(v)):
            a=v[i]//p
            u=a%baz
            b[u].append(v[i])
            if a>0:
                t=True
        p=p*baz
        del v[0:]
        for i in range(baz):
            v.extend(b[i])
    return v

#MERGE SORT
def merge(v,s,m,d):
    nr1=m-s+1
    nr2=d-m

    S=[0]*nr1 
    D=[0]*nr2

    for i in range(nr1):
        S[i]=v[i+s]

    for i in range(nr2):
        D[i]=v[i+m+1]

    i=j=0
    k=s
    while i<nr1 and j<nr2:
        if S[i]>D[j]:
            v[k]=D[j]
            j+=1
            k+=1
        else:
            v[k]=S[i]
            i+=1
            k+=1

    while i < nr1:
        v[k] = S[i]
        i += 1
        k += 1
 
    while j < nr2:
        v[k] = D[j]
        j += 1
        k += 1

def merge_sort(v,s,d):
    if s<d:
        m=(s+d)//2 
        merge_sort(v,s,m)
        merge_sort(v,m+1,d)
        merge(v,s,m,d)
    return v

#SHELL SORT
def shell_sort(v):
    n=len(v)
    gap=n//2
    while gap>0:
        for i in range(0,n-gap):
            while True:
                if v[i]>v[i+gap]:
                    v[i],v[i+gap]=v[i+gap],v[i]
                    i=i-gap
                    if i<0:
                        break
                else: break
        gap=gap//2
    return v

#HEAP SORT
def heap_sort(v):
    build_max_heap(v)
    l=len(v)
    for i in range(l-1,0,-1):
        # print(i)
        v[0],v[i]=v[i],v[0]
        heapify(v,i,0)

def build_max_heap(v):
    n=len(v)
    for i in range(n//2-1,-1,-1):
        heapify(v,n,i)


def heapify(v,n,i): 
    max=i
    st=2*i+1 
    dr=2*i+2

    if st<n and v[i]<v[st]:
        max=st
    if dr<n and v[max]<v[dr]:
        max=dr

    if max!=i:
        v[i],v[max]=v[max],v[i]
        heapify(v,n,max)

#COUNTING SORT 
def count_sort(v):
    m=max(v)
    fr=[0]*(m+1)
    for i in range(len(v)):
        fr[v[i]]+=1
    k=0
    for i in range(m+1):
        while fr[i]>0:
            v[k]=i
            k+=1
            fr[i]-=1
    return v

from time import perf_counter
import random

f=open("test.txt","r")
g=open("timp.txt","w")
T=int(f.readline())
# print(T)
for i in range(1,T+1):
    nr=f.readline().split()
    N=int(nr[0])
    MAX=int(nr[1])

    randomlist = [random.randint(0,MAX) for i in range(N+1)]
    g.write("N="+str(N) + " MAX=" + str(MAX)+'\n')
    start=perf_counter()
    radix_sort(randomlist,2**16)
    # time.sleep(3)
    end=perf_counter()
    g.write("radix sort:"+ str(int((end-start)*1000000) )+" micros"+'\n' )
    # print(f"radix sort: {(end-start)*1000} ms")

    start=perf_counter()
    merge_sort(randomlist,0,N-1)
    end=perf_counter()
    g.write("merge sort:"+ str(int((end-start)*1000000))+" micros"+'\n' )
    # print(f"merge sort: {(end-start)*1000} ms")

    start=perf_counter()
    shell_sort(randomlist)
    end=perf_counter()
    g.write("shell sort:"+ str(int((end-start)*1000000))+" micros"+'\n' )

    start=perf_counter()
    heap_sort(randomlist)
    end=perf_counter()
    g.write("heap sort:"+ str(int((end-start)*1000000))+"micros"+'\n' )

    start=perf_counter()
    randomlist.sort()
    end=perf_counter()
    g.write("python sort:"+ str(int((end-start)*1000000))+" micros"+'\n' )

    start=perf_counter()
    count_sort(randomlist)
    end=perf_counter()
    g.write("count sort:"+ str(int((end-start)*1000000) )+" micros"+'\n'+'\n' )



f.close()
g.close()

