class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n+1)
        #base case 
        # n = 0, 0 node we have 1 tree
        # n = 1, 1 node we have 1 tree

        #we start from 2 is because n =0, 1 are all base cases
        for node_num in range(2, n+1):
            cur_total = 0

            # ex: numTree[4] = (numTree[ 0 ] * numTree[ 3 ]) + (numTree[ 1 ] * numTree[ 2 ]) + (numTree[ 2 ] * numTree[ 1 ]) + (numTree[ 3 ] * numTree[ 0 ] )
            for root in range(1,node_num+1):
                # left + right should == node_num - 1
                # since there is a root 
                left_node_num = root - 1
                right_node_num = node_num - root
                cur_total += dp[left_node_num] * dp[right_node_num]
            
            dp[node_num] = cur_total
        return dp[-1]