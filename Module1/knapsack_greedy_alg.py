def greedy(items, max_weight, key_function):
    """Assumes items a list, max_weight >= 0,
       key_function maps elements of items to numbers"""
    items_copy = sorted(items, key=key_function, reverse=True)
    result = []
    total_value, total_weight = 0.0, 0.0
    
    for i in range(len(items_copy)):
        if (total_weight + items_copy[i].get_weight()) <= max_weight:
            result.append(items_copy[i])
            total_weight += items_copy[i].get_weight()
            total_value += items_copy[i].get_value()
    
    return (result, total_value)