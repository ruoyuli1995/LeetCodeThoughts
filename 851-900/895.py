# 895. Maximum Frequency Stack

'''
---Description---

Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
 

Example 1:

Input: 
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].
 

Note:

Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
The total number of FreqStack.push calls will not exceed 10000 in a single test case.
The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.
'''

'''
---Thought---
At first I thought about using priority queue to solve it. But there is a question that the frequency number of the element of pq cannot be assigned easily.
Then when I tried to simulate the stack operations, I found that a) a poped element should be still in the stack if its frequency is not zero;
b) the order always matters.
So it is necessary to record all the elements and their order.
Then I should record the frequencies(for push operation) and the order of every frequency.
After my ac I found that the variable "max_frequency" is not necessary if "frequency_to_key_list" is changed from dict to list, since frequency must increase and decline 1 by 1.
'''

'''
---My solution---
'''

class FreqStack(object):

    def __init__(self):
        self.key_to_frequency, self.frequency_to_key_list, self.max_frequency = dict(), dict(), 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        fre = self.key_to_frequency.get(x, 0)
        fre += 1
        self.key_to_frequency[x] = fre
        self.max_frequency = max(self.max_frequency, fre)
        if fre not in self.frequency_to_key_list:
            self.frequency_to_key_list[fre] = []
        self.frequency_to_key_list[fre].append(x)

    def pop(self):
        """
        :rtype: int
        """
        temp = self.frequency_to_key_list[self.max_frequency]
        result = temp.pop()
        if not temp:
            self.max_frequency -= 1
        self.key_to_frequency[result] -= 1
        return result

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()

'''
---Official Solution---
Approach 1: Stack of Stacks
Intuition
Evidently, we care about the frequency of an element. Let freq be a Map from xx to the number of occurrences of xx.
Also, we (probably) care about maxfreq, the current maximum frequency of any element in the stack. This is clear because we must pop the element with the maximum frequency.
The main question then becomes: among elements with the same (maximum) frequency, how do we know which element is most recent? We can use a stack to query this information: the top of the stack is the most recent.
To this end, let group be a map from frequency to a stack of elements with that frequency. We now have all the required components to implement FreqStack.
Algorithm
Actually, as an implementation level detail, if x has frequency f, then we'll have x in all group[i] (i <= f), not just the top. This is because each group[i] will store information related to the ith copy of x.
Afterwards, our goal is just to maintain freq, group, and maxfreq as described above.

class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x

Complexity Analysis
Time Complexity: O(1) for both push and pop operations.
Space Complexity: O(N), where N is the number of elements in the FreqStack. 
'''

'''
---Discuss Solution---
Storing (count, index, number) in min-heap and keeping map of counts. Since its a min-heap, I am negating the count and index while pushing in the heap.

The intuition is, heap will always keep the element with max count on top, and if two elements have same count, the second element (index) will be considered while doing pop operation. Also, the count map, is useful when the new occurence of the exisiting element is pushed.

class FreqStack:

    def __init__(self):
        self.heap = []
        self.m = collections.defaultdict(int)
        self.counter = 0
        
    def push(self, x):
        self.m[x]+=1
        heapq.heappush(self.heap,(-self.m[x], -self.counter, x))
        self.counter+=1
    
    def pop(self):
        toBeRemoved = heapq.heappop(self.heap)
        self.m[toBeRemoved[2]]-=1
        return toBeRemoved[2]
'''
