import sys
from pathlib import Path
import markdown


def validate_input_path():
    return Path(sys.argv[2]).exists()

def validate_output_path():
    return Path(sys.argv[3]).parent.exists()


def validate_args():
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

def main():
    validate_args()
    input_path = sys.argv[2]
    output_path = sys.argv[3]
    
    with open(input_path, 'r') as f:
        html = markdown.markdown(f.read())

    with open(output_path, 'w') as f:
        f.write(html)

if __name__ == '__main__':
    main()
