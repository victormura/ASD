from math import log
from test import test_all

def bubble_sort(input_list):
    if input_list:
        for i in range(len(input_list)):
            for j in range(len(input_list)):
                if input_list[i] < input_list[j]:
                    input_list[i], input_list[j] = input_list[j], input_list[i]
    return input_list

def count_sort(input_list):
    if input_list:
        min_number = min(input_list)
        max_number = max(input_list)
        count_dict = {key: 0 for key in range(min_number, max_number+1)}
        for number in input_list:
            count_dict[number] += 1

        output_list = []
        for key, value in count_dict.items():
            output_list.extend([key]*value)
        return output_list
    return input_list
 

# Radix sort
def split(input_list, base, digit_num):
    buckets =  [[] for i in range(base)]
    for num in input_list:
        get_digit = (num // base ** digit_num) % base
        buckets[get_digit].append(num)  
    return buckets
 
def merge(input_list):
    new_list = []
    for sublist in input_list:
       new_list.extend(sublist)
    return new_list
 
def split_by_sign(input_list):
    buckets = [[], []]
    for num in input_list:
        if num < 0:
            buckets[0].append(num)
        else:
            buckets[1].append(num)
    return buckets
 
def radix_sort(input_list, base):
    if input_list not in [None, []]:
        max_abs = max(abs(num) for num in input_list)
        passes = int(round(log(max_abs, base)) + 1) 
        new_list = list(input_list)
        for digit_num in range(passes):
            new_list = merge(split(new_list, base, digit_num))
        return merge(split_by_sign(new_list))
    return input_list


# Merge sort
def merge_sort(input_list):
    if input_list not in [None, []]:
        if len(input_list) > 1:
            mid = len(input_list) // 2
            left_list = input_list[:mid]
            right_list = input_list[mid:]

            left_list = merge_sort(left_list)
            right_list = merge_sort(right_list)

            i = j = k = 0
            while i < len(left_list) and j < len(right_list):
                if left_list[i] < right_list[j]:
                  input_list[k] = left_list[i]
                  i += 1
                else:
                    input_list[k] = right_list[j]
                    j += 1
                k += 1
            while i < len(left_list):
                input_list[k] = left_list[i]
                i += 1
                k += 1
            while j < len(right_list):
                input_list[k]=right_list[j]
                j += 1
                k += 1
    return input_list

# Quick sort
def chunked(input_list, chunk_size):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

def pick_pivot(input_list):
    assert len(input_list) > 0
    if len(input_list) < 5:
        return nlogn_median(input_list)

    chunks = chunked(l, 5)

    full_chunks = [chunk for chunk in chunks if len(chunk) == 5]
    sorted_groups = [sorted(chunk) for chunk in full_chunks]

    medians = [chunk[2] for chunk in sorted_groups]
    median_of_medians = quickselect_median(medians, pick_pivot)

    return median_of_medians

def quick_sort(input_list):
    if input_list not in [None, []]:
        lows = []
        equal = []
        highs = []

        if len(input_list) > 1:
            pivot = input_list[0]
            for x in input_list:
                if x < pivot:
                    lows.append(x)
                elif x == pivot:
                    equal.append(x)
                elif x > pivot:
                    highs.append(x)
            return quick_sort(lows) + equal + quick_sort(highs)  
    return input_list


sort_methods = {
    'bubble sort': bubble_sort,
    'count sort': count_sort,
    'radix sort (base64)': lambda l: radix_sort(l, base=64),
    'radix sort (base256)': lambda l: radix_sort(l, base=256),
    'merge sort': merge_sort,
    'quick_sort': quick_sort
}

test_all(sort_methods)