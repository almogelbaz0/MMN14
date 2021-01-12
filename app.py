import murmurhash
import mmh3

def hash_them(input,m,k):
    results = []
    i = 0
    while i < k :
        num = mmh3.hash(input,i)
        results.append(num%m)
        i+=1
    return results

def create_hash_table(array,m,k):
    #O(n)
    T=[0] * m
    for input in array:
        hashedResults = hashThem(input,m,k)
        for i in hashedResults:
            T[i]=1
    return T

def create_array_from_file(file):
    #O(n)
    result = []
    for line in file.readlines():
        for word in line.split(","):
            result.append(word)
    return result
    
def get_m_k_from_user():
    f = 0
    while f == 0:
        try:
            print("Enter Size Of Hash Table: ")
            m = int(input())
            f = 1
        except:
            print("Value Must Be INT !")
    while f == 1:
        try:
            print("Enter Number Of Hashs To Do: ")
            k = int(input())
            f = 2
        except:
            print("Value Must Be INT !")
    while f == 2 :
        try:
            print("Enter File Path To Build Stracture: ")
            stract = open(input(),"r")
            # stract = open("./Examples/Example1.txt","r")
            f =3
        except:
            print("File Was Not Found Try Again")
    while f == 3 :
        try:
            print("Enter File Path To Check If In Stracture: ")
            file = open(input(),"r")
            # file = open("./Examples/Checks.txt","r")
            f =4
        except:
            print("File Was Not Found Try Again")
    return m , k ,stract,file

# check if a word is in the stract ( len(indexs)== k)
def check_if_cell_is_taken(array,indexs):
    #O(n)
    for i in indexs :
        if array[i] == 0 :
            return False
    return True


m,k,stract,file= get_m_k_from_user()
print(" ")
print(" ")
stractArray = create_array_from_file(stract)
hashedTable = createHashTable(stractArray,m,k)
checkArray = create_array_from_file(file)
for word in checkArray :
    indexs = hashThem(word, m, k)
    print("[{},{}]".format(word,check_if_cell_is_taken(hashedTable,indexs)),end=" ")
print(" ")
print(" ")
input("press any key to EXIT !")


