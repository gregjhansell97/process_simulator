'''
parameters: l <list that represents a priority queue>, i <index>
purpose: moves the index further up the list until it's no longer
    larger than it's parent
'''
def bubble_up(l, i):
    parent = i/2
    if(l[parent] < l[i]):
        swap(l, parent, i)
        bubble_up(l, i/2)

'''
parameters: l <list that represesnts a priority queue>, i <index>
purpose: moves the index down in the list until it is less than
    its parents but larger than its children
'''
def sift_down(l, i):
    left_child = 2*i + 1
    right_child = 2*i
    if(is_index(l, left_child)):
        if(l[left_child] > l[i] and l[left_child] >= l[right_child]):
            swap(l, left_child, i)
            sift_down(l, left_child)
        elif(l[right_child] > l[i] and l[right_child] >= l[left_child]):
            swap(l, right_child, i)
            sift_down(l, right_child)
    elif(is_index(l, right_child)):
        if(l[right_child] > l[i]):
            swap(l, right_child, i)

'''
parameters: l <list>, index1 <first index>, index2 <second index>
purpose: swaps the indexes in list l. assumes both indecies are in range
'''
def swap(l, index1, index2):
    temp = l[index1]
    l[index1] = l[index2]
    l[index2] = temp

'''
parameters: l <list>, i <index>
purpose: checks to make sure i is a valid index in l
returns: boolean verifying whether or not its an index
'''
def is_index(l, i):
    return i >= 0 and i < len(l)

class Priority_Queue(object):
    '''
    parameters: <none>
    purpose: default constructor that creates an empty priority queue
    state variables:
        pq_list is a list that represents a priority queue
    '''
    def __init__(self):
        self.pq_list = [] #a list of values of a given type

    '''
    parameters: val <the value being added to the priority queue
    purpose: adds value to the end of pq_list and the function
        bubble_up then moves it to the appropriate index
    '''
    def push(self, val):
        self.pq_list.append(val)
        bubble_up(self.pq_list, len(self.pq_list) - 1)

    '''
    parameters: <none>
    purpose: removes the largest value from the priority queue and
        adjusts the list to maintain the priority queue properites
    returns: the popped value r
    '''
    def pop(self):
        swap(self.pq_list, 0, len(self.pq_list) - 1)
        r = self.pq_list.pop()
        sift_down(self.pq_list, 0)
        return r

class Queue(object):
    '''
    parameters: <none>
    purpose: default constructor that creates an empty queue
    state variables:
        q_list is a list that represents a queue
    '''
    def __init__(self):
        self.q_list = [] #a list of values of a given type

    '''
    parameters: val the value being added to the priority queue
    purpose: adds value to the end of q_list
    '''
    def push(self, val):
        self.q_list.append(val)

    '''
    parameters: <none>
    purpose: removes value in first index
    returns: the popped value r
    '''
    def pop(self):
        r = self.q_list.pop(0)
        return r