#from heapq import *
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        N = len(A)
        #create a set to store visited permutations
        visited = set()
        #sort the arrays first
        A = sorted(A, reverse=True)
        B = sorted(B, reverse=True)
        result = []
        #build the heap
        heap = []
        #(0,0) is definitely the maximum
        visited.add((0, 0))
        #build the very first heap element
        heappush(heap, (-(A[0] + B[0]), (0, 0)))
        #we only need N items
        for _ in range(N):
            sum, (iA, iB) = heappop(heap)
            result.append(-sum)
            
            tuple1 = (iA + 1, iB)
            #Make sure we don't build duplicates
            if iA < N - 1 and tuple1 not in visited:
                heappush(heap, (-(A[iA + 1] + B[iB]), tuple1))
                visited.add(tuple1)
            
            tuple2 = (iA, iB + 1)
            if iB < N - 1 and tuple2 not in visited:
                heappush(heap, (-(A[iA] + B[iB + 1]), tuple2))
                visited.add(tuple2)
                
        return result

def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)

def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        #define parent position
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            #swap
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem
        
def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    #pop the last element
    lastelt = heap.pop()    
    # raises appropriate IndexError if heap is empty
    if heap:
        #take out the min element and replace it with the last element
        returnitem = heap[0]
        heap[0] = lastelt
        #call the heapify function and adjust positions
        _siftup(heap, 0)
        return returnitem
    #if lastelt is the only element in heap
    return lastelt
    
def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos #0
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)
