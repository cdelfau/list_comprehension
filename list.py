#Union function
def union(A, B):
    l = [x for x in A]
    l.extend([y for y in B if y not in A])
    return l
#test
#print union([1,2,3],[2,3,4])


#Intersection function
def intersection(A, B):
    return [x for x in A if x in B]
#test
#print intersection([1,2,3],[2,3,4])


#Set difference function
def set_difference(A, B):
    return [x for x in A if x not in B]
#test
#print set_difference([1,2,3],[2,3,4])
#print set_difference([2,3,4],[1,2,3])

#Symmetric difference function
def sym_difference(A, B):
    l = [x for x in A if x not in B]
    l.extend([y for y in B if y not in A])
    return l
#test
#print sym_difference([1,2,3],[2,3,4])


#Cartesian prodcut function
def cart_product(A, B):
    return [[x,y] for x in A for y in B]
#test
#print cart_product([1,2],["red","white"])
