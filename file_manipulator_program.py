import sys
from pathlib import Path


def validate_input_path():
    return Path(sys.argv[2]).exists()

def validate_output_path():
    return Path(sys.argv[3]).parent.exists()


def validate_reverse_file_args():
    if len(sys.argv) != 4:
        print('input collect number of args')
        return False
    
    if not validate_input_path():
        print('input collect input file path')
        return False
    
    if not validate_output_path():
        print('input collect output file path')
        return False

    return True

def validate_copy_file_args():
    return validate_reverse_file_args()

def validate_duplicate_contents_args():
    if len(sys.argv) != 4:
        print('input collect number of args')
        return False

    if not validate_input_path():
        print('input collect input file path')
        return False

    try:
        n = int(sys.argv[3])
    except TypeError:
        print('n must be integer')
        return False
    return True

def validate_replace_string_args():
    if len(sys.argv) != 5:
        print('input collect number of args')
        return False

    if not validate_input_path():
        print('input collect input file path')
        return False

    return True

def reverse_file():
    input_path = sys.argv[2]
    output_path = sys.argv[3]

    with open(input_path, 'r') as f:
        content = f.read()
    
    with open(output_path, 'w') as f:
        f.write(content[::-1])
    

def copy_file():
    input_path = sys.argv[2]
    output_path = sys.argv[3]

    with open(input_path, 'r') as f:
        content = f.read()
    
    with open(output_path, 'w') as f:
        f.write(content)

def duplicate_contents():
    input_path = sys.argv[2]
    n = int(sys.argv[3])

    with open(input_path, 'r') as f:
        content = f.read()
    
    with open(input_path, 'w') as f:
        for i in range(n):
            f.write(content)

def replace_string():
    input_path = sys.argv[2]
    from_string = sys.argv[3]
    to_string = sys.argv[4]

    with open(input_path, 'r') as f:
        content = f.read()
    
    replace_content = content.replace(from_string, to_string)

    with open(input_path, 'w') as f:
        f.write(replace_content)


def main():
    if len(sys.argv) < 2:
        print('input collect number of args')
        return

    mode = sys.argv[1]
    match mode:
        case 'reverse':
            if validate_reverse_file_args():
                reverse_file()
        case 'copy':
            if validate_copy_file_args():
                copy_file()
        case 'duplicate-contents':
            if validate_duplicate_contents_args():
                duplicate_contents()
        case 'replace-string':
            if validate_replace_string_args():
                replace_string()
        case _:
            print('choose mode in [reverse, copy, duplicate-contents, replace-string]')



if __name__ == '__main__':
    main()