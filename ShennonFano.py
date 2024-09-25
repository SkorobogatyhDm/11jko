def ShennonFano(array, left, right, border_array):
    if left >= right:  
        return

    border_array.append(right)  
    print("Border_array =", border_array)
    border = delit(array, left, right)
    print("Border =", border)

    for i in array[left:border + 1]:
        i[2] += "1"
    for i in array[border + 1:right + 1]:  
        i[2] += "0"

    print(array)

    if border == left:  
        print("Слева 1 буква")
        return ShennonFano(array, border + 1, right, border_array)
    elif border + 1 == right:  
        print("Справа 1 буква")
        return array

    print("Слева несколько букв")
    ShennonFano(array, left, border, border_array)
    ShennonFano(array, border + 1, right, border_array)

def delit(array, left, right):
    sum_left = array[left][1]
    sum_right = array[right][1]

    while left < right - 1: 
        if sum_right <= sum_left:
            right -= 1
            sum_right += array[right][1]  
        else:
            left += 1
            sum_left += array[left][1] 
            
    return left

if __name__ == "__main__":
    array = [["a", 3, ""], ["b", 3, ""], ["c", 3, ""], ["d", 3, ""]]
    ShennonFano(array, 0, len(array) - 1, [])
    print(array)