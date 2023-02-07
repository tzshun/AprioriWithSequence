
def loadDataSet():
    return [['1', '5', '3'], ['5', '2','1', '4', '3'], ['1', '2', '5', '4','3'], ['2', '5', '1','4', '3']]

def createC1(dataSet):  
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    return C1

def issubset(father,child):
    isin=set(child).issubset(set(father))
    if isin:
        if len(child)==1:
            return True
        result = []
        for b1 in child:
            temp = [i for i, x in enumerate(father) if x == b1]
            result.append(temp)
        seq = []
        seq = getseq(result, seq, 0)
        isseq = False
        for s in seq:
            iss = True
            for a in range(len(s) - 1):
                iss = iss and s[a] < s[a + 1]
            if iss:
                isseq = True
                break
        return isseq
    return False

def scanD(D, Ck, minSupport):  
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if issubset(tid,can):
                can=','.join(can)
                if not can in ssCnt:
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numItems  
        if support >= minSupport: 
            retList.append(key)
        supportData[key] = support
    return retList, supportData


def aprioriGen(Lk, k): 
    lenLk = len(Lk)
    temp_list = [] 
    for i in range(lenLk):
        for j in range(lenLk):
            if i!=j:
                L1 = checkGen(Lk[i],Lk[j]) 
                if len(L1)>0:  
                    if not L1 in temp_list:  
                        temp_list.append(L1)
    return temp_list  

def checkGen(kl,kr):

    left = kl.split(',')
    right = kr.split(',')
    k = len(left)

    if k==1:
        return [left[0],right[0]]
    elif k==2:
        if left[-1]==right[0]:
            left.append(right[-1])
            return left
        else:
            return []
    else:
        if left[1:k]==right[0:k-1]:
            left.append(right[-1])
            return left
        else:
            return []

def getinfo(L,S):
    temp={}
    for l in L:
        temp[l]=S[l]
    return temp

def apriori(dataSet, minSupport=0.5):  
    C1 = createC1(dataSet)  
    D = dataSet
    L1, supportData = scanD(D, C1, minSupport) 
    print('Frequent 1 itemset:',L1)
    print('Frequent 1 itemset support:',getinfo(L1,supportData))
    L = [L1]
    k = 2
    while (len(L[k - 2]) > 0): 
        Ck = aprioriGen(L[k - 2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        print(f'Frequent {k} itemset:',Lk)
        print(f'Frequent {k} itemset support:',getinfo(Lk,supportData))
        L.append(Lk)
        k += 1
    return L, supportData

def getseq(result,seq,k):
    if k ==len(result):
        return seq
    if k==0:
        for i in result[k]:
            seq.append([i])
    else:
        temp=seq.copy()
        seq=[]
        for s in temp:
            for i in result[k]:
                ss=s.copy()
                ss.append(i)
                seq.append(ss)
    if k<len(result):
       return getseq(result,seq,k+1)


if __name__ == "__main__":

    dataSet = loadDataSet()
    L, suppData = apriori(dataSet,minSupport=0.5)

