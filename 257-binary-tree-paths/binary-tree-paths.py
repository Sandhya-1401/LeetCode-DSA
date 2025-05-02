class Solution:
    def binaryTreePaths(self, root):
        def dfs(node, path, paths):
            if not node:
                return
            
            path += str(node.val)
            
            if not node.left and not node.right:  # if it's a leaf
                paths.append(path)
            else:
                path += "->"
                dfs(node.left, path, paths)
                dfs(node.right, path, paths)
        
        result = []
        dfs(root, "", result)
        return result
