def create_sample_file(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)

def read_sample_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()
