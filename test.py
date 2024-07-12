def reformat_student_info(filename):
    with open(filename) as file:
        with open("studentInfoReformatted.txt", "w") as output:
            for line in file:
                line = line.replace(" ", "")
                line = line.replace(",", "")
                netid = ""
                currIndex = 0
                while not line[currIndex].isdigit():
                    netid += line[currIndex]
                    currIndex += 1
                while not line[currIndex].isalpha():
                    netid += line[currIndex]
                    currIndex += 1
                name = line[currIndex]
                currIndex += 1
                while not line[currIndex].isupper():
                    name += line[currIndex]
                    currIndex += 1
                name += " "
                name += line[currIndex]
                currIndex += 1
                while line[currIndex].isalpha():
                    name += line[currIndex]
                    currIndex += 1
                course_num = ""
                for i in range(3):
                    course_num += line[currIndex]
                    currIndex += 1
                gpa = line[currIndex:].strip()
                gpa = float(gpa)
                gpa = str(gpa)
                output_line = f"{netid}, {name}, {course_num}, {gpa}"
                output.write(output_line + "\n")