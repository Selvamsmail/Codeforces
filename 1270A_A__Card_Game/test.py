import subprocess

def run_test(input_path, output_path):
    with open(input_path) as f_in, open(output_path) as f_out:
        expected = f_out.read().strip()
        result = subprocess.run(['python3', 'main.py'], input=f_in.read(), text=True, capture_output=True)
        output = result.stdout.strip()
        assert output == expected, f"Failed: Expected {expected}, Got {output}"
        print(f'Success: Expected {expected}, Got {output}')

if __name__ == '__main__':
    run_test('input1.txt', 'output1.txt')
