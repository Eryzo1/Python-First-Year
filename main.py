seating_chart = [
    ["Amy", "Sarah", "Brian"],
    ["Donald", "Jacob", "Zoey"],
    ["Amanda", "Bob", "Dora"],
]

for col_index in range(3):
    column = []
    for row_index in range(3):
        student = seating_chart[row_index][col_index]
        column.append(student)
    print("List of students at position ", col_index, ":", column)
