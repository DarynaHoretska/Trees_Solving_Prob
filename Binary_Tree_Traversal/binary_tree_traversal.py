# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)

# In-order traversal
def in_order(node):
    if node is None:
        return []
    prereverse = pre_order(node.right)
    reverse = prereverse[::-1]
    return pre_order(node.left) + [node.data] + reverse

# Post-order traversal
def post_order(node):
    if node is None:
        return []
    prereverse = pre_order(node.right)
    reverse = prereverse[::-1]
    return pre_order(node.left) + reverse + [node.data]
