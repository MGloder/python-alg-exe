# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        val_dic = {}

        def traverse(node):
            if node.val in val_dic:
                val_dic[node.val] += 1
            else:
                val_dic[node.val] = 1

            if node.left:
                traverse(node.left)

            if node.right:
                traverse(node.right)

        traverse(root)

        if len(val_dic.keys()) < 1:
            return []

        current_max_model = None
        current_max_model_count = 0

        for key in val_dic:
            if current_max_model is None:
                current_max_model = [key]
                current_max_model_count = val_dic[key]
            else:
                if val_dic[key] > current_max_model_count:
                    current_max_model = [key]
                    current_max_model_count = val_dic[key]
                elif val_dic[key] == current_max_model_count:
                    current_max_model.append(key)

        return current_max_model
