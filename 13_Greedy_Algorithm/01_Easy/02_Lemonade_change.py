'''
Each lemonade at a booth sells for $5. Consumers are lining up to place individual orders, following the billing order. Every consumer will purchase a single lemonade and may pay with a $5, $10, or $20 bill. Each customer must receive the appropriate change so that the net transaction is $5. Initially, there is no change available.



Determine if it is possible to provide the correct change to every customer. Return true if the correct change can be given to every customer, and false otherwise.



Given an integer array bills, where bills[i] is the bill the ith customer pays, return true if the correct change can be given to every customer, and false otherwise.


Examples:
Input : bills = [5, 5, 10, 5, 20]



Output : true



Explanation : Initially we have $0 available for change.

From first two customers, we will collect two $5 bills in order. After the first two customers we have two $5 bills available with us for change.

From the third customer , we collect bill of $10 and give back $5. After third customer we have one $5 and one $10 bill available with us for change.

From fourth customer , we collect $5 bill. After fourth customer we have two $5 and one $10 bills available with us for change if required.

From fifth customer , we collect bill of $20 and give back $15 (one $10 + one $5 bill).

Since all the customers did receive the change correctly , so we return true.

Input : bills = [5, 5, 10, 10, 20]



Output : false



Explanation : From first two customers, we will collect two $5 bills in order. After the first two customers we have two $5 bills available with us for change.

From third customer , we collect $10 and give back $5. After the third customer we have one $5 and one $10 bill available with us for change.

From fourth customer , we collect $10 and give back $5. After the fourth customer we have two $10 bill available with us for change.

From fifth customer , we collect $20 , we cannot give the $15 change as we have two $10 bills.

Since all the customers did not receive the change correctly , the we return false.

Input : bills = [5, 5, 10, 20]

Output:
true
Constraints:
1 <= bills.length <= 105
bills[i] = {5 , 10 , 20}

Intuition
If a customer pays with a $5 bill, it's easy because we don't need to give any change. When a customer pays with a $10 bill, we need to have a $5 bill on hand to give them the correct change.
Now, if someone pays with a $20 bill, we can give them change with one $10 bill and one $5 bill, or if we don't have a $10 bill, we need to have three $5 bills to make the change.
Approach
First, keep track of the number of $5 and $10 bills available. Start with zero bills.
As each customer pays, follow these steps:
If a customer pays with a $5 bill, simply keep it because no change is needed.
If a customer pays with a $10 bill, provide them with $5 in change. Ensure there is at least one $5 bill to do this. If there is, give the $5 bill and keep the $10 bill. If not, it is impossible to give the correct change, and the process should stop.
If a customer pays with a $20 bill, provide them with $15 in change. The preferred way is by giving one $10 bill and one $5 bill. If there is no $10 bill, give three $5 bills instead. If neither option is possible, providing the correct change is not feasible, and the process should stop.
If the correct change is given to all customers, the process is successful. If at any point providing the correct change is not possible, the process fails.
class Solution:
    """ Function to find whether each customer can 
    be provided with correct change """
    def lemonadeChange(self, bills):
        
        # Counter for $5
        five = 0 
        
        # Counter for $10
        ten = 0   
        
        # Iterate through each customer's bill
        for bill in bills:
            
            # If the customer's bill is $5
            if bill == 5:
                # Increment $5
                five += 1
            
            # If the customer's bill is $10
            elif bill == 10:
                # Check if there are $5 bills available to give change
                if five > 0:
                    # Use one $5
                    five -= 1
                    # Receive one $10
                    ten += 1
                else:
                    # If no $5 bill available, return false
                    return False
            
            # If the customer's bill is $20
            else:
                # Check if there are both $5 and $10 bills available to give change
                if five > 0 and ten > 0:
                    # Use one $5
                    five -= 1
                    # Use one $10
                    ten -= 1
                # If there are not enough $10 bills,
                # check if there are at least three $5 bills available
                elif five >= 3:
                    # Use three $5 bills
                    five -= 3
                else:
                    # If unable to give change, return false
                    return False
        
        # Return true
        return True

# Example usage
if __name__ == "__main__":
    bills = [5, 5, 5, 10, 20]
    print("Queues of customers: ", end="")
    for bill in bills:
        print(bill, end=" ")
    print()
    solution = Solution()
    ans = solution.lemonadeChange(bills)
    if ans:
        print("It is possible to provide change for all customers.")
    else:
        print("It is not possible to provide change for all customers.")

        
Complexity Analysis
Time Complexity: O(N) where N is the number of people in the queue or the number of bills to be processed. Each customer's bill is processed exactly once. The loop iterates N times, and the operations performed during each iteration are done in constant time.
Space Complexity: O(1) because no extra space is used.


'''
class Solution:
    def lemonadeChange(self, bills):
        five = 0 
        ten = 0   

        for bill in bills:
        
            if bill == 5:
                five += 1
            elif bill == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
