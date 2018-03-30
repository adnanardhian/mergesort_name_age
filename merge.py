def merge(left, right):
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i].split(' ')[1] < right[j].split(' ')[1]: #sort by age first
            result.append(left[i])
            i+= 1
        elif left[i].split(' ')[1] == right[j].split(' ')[1]: #if age is the same, sort by name
            if left[i] < right[j]:
                result.append(left[i])
                i+= 1
            else:
                result.append(right[j])
                j+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break 

    return result

def mergesort(list):
    if len(list) < 2:
        return list

    middle = int(len(list)/2)
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge(left, right)

file_object = open("PATH_TO_FILE/name_age.txt", "r")
input_file = file_object.read()
input_file = input_file.split('\n')
input_file = list(map(str, input_file))
sorted_file = mergesort(input_file)

file_output = open("PATH_TO_FILE/sorted_name_age.txt", "w")
file_output.write("============================")
file_output.write("\n")
for i in range(0,len(sorted_file)):
    file_output.write(str(sorted_file[i]))
    file_output.write("\n")
file_output.write("============================")
file_output.close()

