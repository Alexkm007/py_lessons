
def inser_sort(A):
    """ сортировка списка А ваставками"""
    N = len(A)
    for top in range(1,N):
        k = top
        while k > 0 and A[k-1]>A[k]:
            A[k],A[k-1]= A[k-1],A[k]
            k-= 1


def chise_sort(A):
    """ сортировка списка А выбором"""
    pass

def bubble_sort(A):
    """ сортировка списка А методом пузырька"""
    pass

def test_sort(sort_algoritm):
    print("Тестируем: ", sort_algoritm.__doc__)
    print("testcase #1: ", end="")
    A = [4,2,5,1,3]
    A_sorted = [1,2,3,4,5]
    sort_algoritm(A)
    print("Ok" if A==A_sorted else "Fail")

    print("testcase #2: ", end="")
    A = list(range(10,20)) + list(range(0,10))
    A_sorted = list(range(20))
    sort_algoritm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algoritm(A)
    print("Ok" if A == A_sorted else "Fail")

if __name__ =="__main__":
    test_sort(inser_sort)
    test_sort(chise_sort)
    test_sort(bubble_sort)