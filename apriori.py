
def loadDataSet():
    return [['1', '5', '1'], ['2', '4', '3'], ['1', '2', '5', '1','3'], ['2', '5', '1','2', '3']]
    # df = pd.read_csv(r'df_cn2.csv')
    # cn1 = []
    # for a in df['fnid_jq']:
    #     re = a.replace('\'', '')
    #     b = json.loads(re)
    #     if len(b) > 1:
    #         cn1.append(b)
    # cn = []
    # for a in cn1:
    #     numbers = [str(x) for x in a]
    #     cn.append(numbers)
    # return cn
def createC1(dataSet):  # 创造候选项集C1，C1是大小为1的所有候选项集的集合
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

def scanD(D, Ck, minSupport):  # 此函数计算支持度,筛选满足要求的项集成为频繁项集Lk，D是数据集，Ck为候选项集C1或C2或C3 ...
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
        support = ssCnt[key] / numItems  # 计算支持度
        if support >= minSupport:  # 如果支持度大于设定的最小支持度
            retList.append(key)
        supportData[key] = support
    return retList, supportData


def aprioriGen(Lk, k):  # 新版aproriGen
    lenLk = len(Lk)
    temp_list = []  # 临时字典，存储
    for i in range(lenLk):
        for j in range(lenLk):
            if i!=j:
                L1 = checkGen(Lk[i],Lk[j])  # 两两合并，执行了 lenLk！次
                if len(L1)>0:  # 如果合并后的子项元素有k个，满足要求
                    if not L1 in temp_list:  # 把符合的新项存到字典的键中，使用字典可以去重复，比如{1,2,3}和{3，1，2}是一样的项，使用了字典就可以达到去重的作用
                        temp_list.append(L1)
    return temp_list  # 把字典的键转化为列表

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

def apriori(dataSet, minSupport=0.5):  # 通过循环得出[L1,L2,L3..]频繁项集列表
    C1 = createC1(dataSet)  # 创造C1
    D = dataSet
    L1, supportData = scanD(D, C1, minSupport) #筛选出L1
    print('Frequent 1 itemset:',L1)
    print('Frequent 1 itemset support:',getinfo(L1,supportData))
    L = [L1]
    k = 2
    while (len(L[k - 2]) > 0):  # 创造Ck
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
    L, suppData = apriori(dataSet,minSupport=0.005)

