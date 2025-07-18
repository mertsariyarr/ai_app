from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

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
    result = get_file_content("calculator", "lorem.txt")
    resul1 = get_file_content("calculator", "main.py")
    result2 = get_file_content("calculator", "pkg/calculator.py")
    result3 = get_file_content("calculator", "/bin/cat")
    result4 = get_file_content("calculator", "pkg/does_not_exist.py")

    print(result, resul1, result2, result3,result4)

if __name__ == "__main__":
    test()