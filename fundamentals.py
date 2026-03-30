student_responses = [
    "My favourite this to do is read",
    "I like to ride bikes",
    "My favourite thing to do, is to watch cartoons"
]

answers2 = (student_responses)


answers3 = set(answers2)


numbers_list = [1, 2, 3, 4, 5,6,7]

def use_numList_element(num_list):
    """
    create a list 
    """
    num_elmnt = len(num_list)
    int_list = []
    count = 0
    for element in range(1, num_elmnt + 1):
        int_list.append(element)
        count += 1
        print(element)
    return int_list

list_tuple = tuple(numbers_list)
print(type(list_tuple))
for val in list_tuple:
    print(  val)

# print(use_numList_element(num_list = numbers_list)) 

capital_cities = {
    "Gauteng": "Johannesburg",
    "Western Cape": "Cape Town"

}

for key in capital_cities:
    print(key)


student_responses = [
    "My favourite this to do is read",
    "I like to ride bikes",
    "My favourite thing to do, is to watch cartoons"
]

def create_number_triangle(n):
    """
    Create a number triangle pattern.
    Example for n=4:
    1
    1 2
    1 2 3
    1 2 3 4
    Args:
        n (int): Number of rows
    Returns:
        str: String representation of the triangle
    """
    triangle = ""
    for i in range(0, n + 1):
        for j in range(0, i + 1):
            triangle += str(j) + " "
        triangle += "\n"
    return triangle.strip(" ")

print(create_number_triangle(5))

def create_multiplication_table(n):
    """
    Create a multiplication table up to n x n.
    Args:
        n (int): Size of the multiplication table
    Returns:
        str: String representation of the multiplication table
    """
    table = ""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            table += f"{i * j:4d} "
        table += "\n"
    return table.strip()
# Example usage:
result = create_multiplication_table(5)
print(create_multiplication_table(n = 27))
