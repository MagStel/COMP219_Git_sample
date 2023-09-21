# test_code.py

def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    return data

file_name = "sample_data1.txt"
print(read_file(file_name))
