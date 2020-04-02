import os

# replacement strings
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

for root, dir, files in os.walk('.'):
    for file_path in files:
        try:
            if (file_path.endswith('.py') or
                    file_path.endswith('.txt') or
                    file_path.endswith('.css')):
                file_path = os.path.join(root, file_path)

                with open(file_path, 'rb') as open_file:
                    content = open_file.read()

                content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

                with open(file_path, 'wb') as open_file:
                    open_file.write(content)
                print('Line ending changed for:', file_path)
        except FileNotFoundError:
            print('Skipped file:', file_path)
