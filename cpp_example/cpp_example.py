import subprocess

# 1. g++ -o hello hello_world.cpp
# 2. ./hello
# 2.1. пишем метод run_cpp_program()


def run_cpp_program():
    try:
        # Запуск исполняемого файла
        result = subprocess.run('./hello', check=True, stdout=subprocess.PIPE, text=True)

        # Вывод результата
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    run_cpp_program()
