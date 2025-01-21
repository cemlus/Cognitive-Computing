'''
1. Create a List L that is defined as= [10, 20, 30, 40, 50, 60, 70, 80].
i. WAP to add 200 and 300 to L.
ii. WAP to remove 10 and 30 from L.
iii. WAP to sort L in ascending order.
iv. WAP to sort L in descending order.
'''
L = [10, 20, 30, 40, 50, 60, 70, 80]
L.append(200)
L.append(300)
L.remove(10)
L.remove(30)
L.sort()
print(L)
L.sort(reverse=True)
print(L)

'''
2. Create a tuple of marks scored as scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45) and
perform the following operations using tuple functions:
i. Identify the highest score and its index in the tuple.
ii. Find the lowest score and count how many times it appears.
iii. Reverse the tuple and return it as a list.
iv. Check if a specific score "76" (input by the user) is present in the tuple and
print its first occurrence index, or a message saying it’s not present.
'''

scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
maxScore = max(scores)
maxIndex = scores.index(maxScore)
print(maxScore, maxIndex)

minScore = min(scores)
minIndex = scores.index(minScore)
print(minScore, minIndex)

scoresList = list(scores)
scoresList.reverse()
print(scoresList)

score = int(input("Enter a score: "))
if score in scores:
    print(scores.index(score))
else:
    print("Score not found")

'''
3. WAP to create a list of 100 random numbers between 100 and 900. Count and print
the:
i. All odd numbers
ii. All even numbers
iii. All prime numbers
'''
import random
randomNumbers = [random.randint(100,900) for i in range(100)]
print(randomNumbers)

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

oddNumbers = [i for i in randomNumbers if i % 2 != 0]
print(oddNumbers)

evenNumbers = [i for i in randomNumbers if i % 2 == 0]
print(evenNumbers)

primeNumbers = [i for i in randomNumbers if isPrime(i)]
print(primeNumbers)

'''
4. Consider the following two sets, A and B, represenƟng scores of two teams in mulƟple
matches. A = {34, 56, 78, 90} and B = {78, 45, 90, 23}
WAP to perform the following operaƟons using set funcƟons:
i. Find the unique scores achieved by both teams (union of sets).
ii. IdenƟfy the scores that are common to both teams (intersecƟon of sets).
iii. Find the scores that are exclusive to each team (symmetric difference).
iv. Check if the scores of team A are a subset of team B, and if team B's scores are
a superset of team A.
v. Remove a specific score X (input by the user) from set A if it exists. If not, print
a message saying it is not present.
'''
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}
print(A.union(B))
print(A.intersection(B))
print(A.symmetric_difference(B))
print(A.issubset(B))
print(B.issuperset(A))
score = int(input("Enter a score: "))
if score in A:
    A.remove(score)
else:
    print("Score not found")
print(A)

