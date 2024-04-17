#Giveven an array nums. Define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums
#Input: nums = [1,2,3,4]
#Output: [1,3,6,10]

def runningSum(nums=list(),suma=0, output=list()):
    for element in nums:
        suma += element
        output.append(suma)
    print(output)

nums=[1,2,3,4]
runningSum(nums)

# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
# Input: accounts = [[1,2,3],[3,2,2]]
# Output: 7
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 2 = 7
# 2nd customer is considered the richest with a wealth of 7 each, so return 7.

            #0 #1 #2
costumers=  [[1,2,3],#0
            [3,2,2]] #1

def richiestCostumer(costumers=[[1,2,3],[3,2,2]],suma=0, output_c=list(), costumer_1_whealth=0, costumer_2_whealth=0):
    for x in costumers:
        for y in x:
            suma+=y 
        output_c.append(suma)
        suma=0

    if output_c[0] > output_c[1]:
        print(f"Customer 1 is considered the richest with a wealth of {output_c[0]}")
    elif output_c[1] > output_c[0]:
        print(f"Customer 2 is considered the richest with a wealth of {output_c[1]}")

richiestCostumer(costumers)