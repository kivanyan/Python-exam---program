import re


def get_data_file():

    with open(r'C:\Users\user\Desktop\Automation_testing_group\Python_Exam\Karine_Ivanyan_exam_last\Karine_Ivanyan_exam\Data.txt', 'r') as file:
        lines = file.readlines()
    for i in lines:
        if re.search(r"^#|^\n", i):
            pass
        else:
            if re.search(r"#+", i):
                part1, part2 = re.split(r"#", i)
                my_list = re.split(r":|\t", part1)


    my_dict = {}
    my_dict["userid"] = my_list[0]
    my_dict["title"] = my_list[1]
    my_dict["body"] = my_list[2]

    return(my_dict)

print(get_data_file())