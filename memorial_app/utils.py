from werkzeug.utils import secure_filename

def secure_file_name(filename):
    return secure_filename(filename)