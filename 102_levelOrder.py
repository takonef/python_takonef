class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        
        result = []
        que = [root]
        ind = 0 
        
        while ind < len(que):
            size = len(que) - ind
            cur = []
            
            for _ in range(size):
                node = que[ind]
                ind += 1
                
                cur.append(node.val)
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            result.append(cur)
        
        return result