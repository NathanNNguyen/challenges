
def gradingStudents(grades):
    output = []
    for i in range(len(grades)):
        if grades[i] < 38:
            output.append(grades[i])
        else:
            if grades[i] % 5 == 0:
                output.append(grades[i])
            elif (grades[i] + 1) % 5 == 0:
                output.append(grades[i] + 1)
            elif (grades[i] + 2) % 5 == 0:
                output.append(grades[i] + 2)
            else:
                output.append(grades[i])
    return output
