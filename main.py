from ParseR import retrieveResults
from time import time
def main():
    """The Driver code for the IR system
    """
    query = "*"
    # Main is the Input-ouput processing file 
    while query!="EXIT":
        print("Give your query to get results/press EXIT to end the loop : ")
        query = input()
        if query!="EXIT":
            print()
            start = time()
            retrieveResults(query)
            print("Info retrieved in", time()-start,"sec")

main()