# AprioriWithSequence
the apriori algorithm is a widely used method to find the most frequent and relevant patterns in large datasets. 
It generates candidate item sets of length k from item sets of length k-1.
Unfortunately, the algorithm can not distinguish the order relationship in the original sequence. 
For example, there are two travel sequences of tourists A and B, TA={S1, S2, S3}and TB={S1, S3, S2}. 
The two sequences will be treated as the same sequence in the apriori algorithm.
To make up for the shortcomings of the algorithm,an improved apriori algorithm has been proposed. 
It can identify frequent patterns while maintaining the sequence of subitems.

# How to use
In the function loadDataSet(), you should prepare your data in a two-dimensional array.
Such as data = [['1', '5', '1'], ['2', '4', '3'], ['1', '2', '5', '1','3'], ['2', '5', '1','2', '3']]

Then, the result will be generate after running the code. 
Frequent 1 itemset: ['1', '5', '2', '4', '3']
Frequent 1 itemset support: {'1': 0.75, '5': 0.75, '2': 0.75, '4': 0.25, '3': 0.75}
Frequent 2 itemset: ['1,5', '5,1', '2,4', '2,3', '4,3', '1,2', '1,3', '5,3', '2,1', '2,5', '5,2']
Frequent 2 itemset support: {'1,5': 0.5, '5,1': 0.75, '2,4': 0.25, '2,3': 0.75, '4,3': 0.25, '1,2': 0.5, '1,3': 0.5, '5,3': 0.5, '2,1': 0.5, '2,5': 0.5, '5,2': 0.25}
Frequent 3 itemset: ['1,5,1', '2,4,3', '1,5,3', '5,1,3', '1,2,3', '1,2,1', '1,2,5', '2,1,3', '2,5,1', '2,5,3', '5,1,2', '2,1,2', '2,5,2', '5,2,3']
Frequent 3 itemset support: {'1,5,1': 0.5, '2,4,3': 0.25, '1,5,3': 0.25, '5,1,3': 0.5, '1,2,3': 0.5, '1,2,1': 0.25, '1,2,5': 0.25, '2,1,3': 0.5, '2,5,1': 0.5, '2,5,3': 0.5, '5,1,2': 0.25, '2,1,2': 0.25, '2,5,2': 0.25, '5,2,3': 0.25}
Frequent 4 itemset: ['1,5,1,3', '1,2,1,3', '1,2,5,1', '1,2,5,3', '2,5,1,3', '2,5,1,2', '5,1,2,3', '2,1,2,3', '2,5,2,3']
Frequent 4 itemset support: {'1,5,1,3': 0.25, '1,2,1,3': 0.25, '1,2,5,1': 0.25, '1,2,5,3': 0.25, '2,5,1,3': 0.5, '2,5,1,2': 0.25, '5,1,2,3': 0.25, '2,1,2,3': 0.25, '2,5,2,3': 0.25}
Frequent 5 itemset: ['1,2,5,1,3', '2,5,1,2,3']
Frequent 5 itemset support: {'1,2,5,1,3': 0.25, '2,5,1,2,3': 0.25}
Frequent 6 itemset: []
Frequent 6 itemset support: {}
