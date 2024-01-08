import tarfile


def zip_(directory_path, output_filename):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(directory_path, arcname="")

directory_path = "D:/Pycharm/ya_suo"
output_filename = "compressed.tar.gz"

zip_(directory_path, output_filename)
def untar_directory(output_directory, input_filename):
    with tarfile.open(input_filename, 'r:gz') as tar:
        tar.extractall(path=output_directory)

output_directory = 'D:/Pycharm/ya_suo'
input_filename = 'compressed.tar.gz'
untar_directory(output_directory, input_filename)
