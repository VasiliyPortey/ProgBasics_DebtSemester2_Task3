class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1
 
 
def isBalanced(root):
    if root is None:
        return True
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    if (abs(leftHeight - rightHeight) <= 1) and isBalanced(
            root.left) is True and isBalanced(root.right) is True:
        return True
    return False

root = TreeNode(1)
root.left = TreeNode(2)        #первый уровень
root.right = TreeNode(3)       #первый уровень
root.left.left = TreeNode(4)      #второй уровень (первый от левой ветки от корня)
root.left.right = TreeNode(5)      #второй уровень (первый от левой ветки от корня)
root.left.left.left = TreeNode(6)    #третий уровень (первый от левой ветки от левой ветки от корня)
root.right.left = TreeNode(7)       #второй уровень (первый от левой ветки от корня)
root.right.right = TreeNode(8)      #второй уровень (первый от левой ветки от корня)
root.right.right.right = TreeNode(9)      #третий уровень (уже разница в максимальной высоте +1)
root.right.right.right.left = TreeNode(10) #если удалить эту строчку (это, получается, четвёртый уровень от корня (корень считаю за нулевой))
if isBalanced(root):                       #то дерево будет сбалансированным (сейчас оно не сбалансированно, т.к. справа от корня в одну 
    print("Дерево сбалансированное!")    #сторону всего один уровень, а в другую уже три)
else:
    print("Дерево не сбалансированное(")