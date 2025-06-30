from functions.get_files_info import get_files_info, get_file_content, write_file, run_python_file


def test():
    # result = get_file_content("calculator", "main.py")
    # print("Result for main.py:")
    # print(result)
    # print("")

    # result = get_file_content("calculator", "pkg/calculator.py")
    # print("Result for 'pkg/calculator.py':")
    # print(result)

    # result = get_file_content("calculator", "/bin/cat")
    # print("Result for '/bin/cat':")
    # print(result)

    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))


if __name__ == "__main__":
    test()