# --- Flatten Fonksiyonu ---
def flatten_list(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

# --- Reverse Fonksiyonu ---
def reverse_list(lst):
    reversed_lst = []
    for item in reversed(lst):
        if isinstance(item, list):
            reversed_lst.append(reverse_list(item))
        else:
            reversed_lst.append(item)
    return reversed_lst

# Test
input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten_list(input_list))
# Çıktı: [1,'a','cat',2,3,'dog',4,5]

input_list2 = [[1, 2], [3, 4], [5, 6, 7]]
print(reverse_list(input_list2))
# Çıktı: [[7,6,5],[4,3],[2,1]]
