def find_repeating_elements(arr):
    count_dict = {}
    repeating_elements = []

    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num, count in count_dict.items():
        if count == 2:
            repeating_elements.append(num)

    return repeating_elements

# Example usage:
input_list = [4, 2, 4, 5, 2, 3, 1]
result = find_repeating_elements(input_list)
print("Repeating elements are:", result)
