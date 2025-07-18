from functions.get_files_info import get_files_info

def test():
    result1 = get_files_info("calculator", ".")
    print("Results for current directory:")
    print(result1)
    result2 = get_files_info("calculator", "pkg")
    print("Results for 'pkg' directory:")
    print(result2)
    result3 = get_files_info("calculator", "/bin")
    print("Results for '/bin' directory:")
    print(result3)
    result4 = get_files_info("calculator", "../")
    print("Results for '../' directory:")
    print(result4)

test()