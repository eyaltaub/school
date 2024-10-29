def counter(node, character):
    if node is None:
        return 0
    if character == node.value:
        count = 1
    else:
        count = 0
    count += counter(node.left, character)
    count += counter(node.right, character)
    return count

def all_in(node, string):
    def values_to_set(node1):
        if not node1:
            return set()

        values = {node1.value}
        values.update(values_to_set(node1.left))
        values.update(values_to_set(node1.right))
        return values

    values_set = values_to_set(node)
    for char in string:
        if char not in values_set:
            return False
    return True

