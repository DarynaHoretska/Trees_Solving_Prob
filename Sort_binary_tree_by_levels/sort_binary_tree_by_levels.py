def tree_by_levels(node):
    if not node:
        return []
    queue = [node]
    result = []
    while queue:
        cur = queue.pop(0)
        result.append(cur.value)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return result