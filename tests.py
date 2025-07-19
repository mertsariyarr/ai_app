from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def test():
    # result1 = get_files_info("calculator", ".")
    # print("Results for current directory:")
    # print(result1)
    # result2 = get_files_info("calculator", "pkg")
    # print("Results for 'pkg' directory:")
    # print(result2)
    # result3 = get_files_info("calculator", "/bin")
    # print("Results for '/bin' directory:")
    # print(result3)
    # result4 = get_files_info("calculator", "../")
    # print("Results for '../' directory:")
    # print(result4)
    ####
    # result = get_file_content("calculator", "lorem.txt")
    # resul1 = get_file_content("calculator", "main.py")
    # result2 = get_file_content("calculator", "pkg/calculator.py")
    # result3 = get_file_content("calculator", "/bin/cat")
    # result4 = get_file_content("calculator", "pkg/does_not_exist.py")

    # print(result, resul1, result2, result3,result4)

    # result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    # result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    # result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

    # print(result, result2, result3)
    ###

    result = run_python_file("calculator", "main.py")
    result2 = run_python_file("calculator", "main.py", ["3 + 5"])
    result3= run_python_file("calculator", "tests.py")
    result4 = run_python_file("calculator", "../main.py")
    result5 = run_python_file("calculator", "nonexistent.py")
    print(result, result2, result3, result4,result5)

if __name__ == "__main__":
    test()