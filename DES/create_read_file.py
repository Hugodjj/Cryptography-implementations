def create_sample_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)
        
def read_sample_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()