# Aapt

Android Asset Packaging Tool for Python3

## Example

```python
import aapt

help = aapt.aapt('--help')
print(help)

ls = aapt.ls('./xx.apk')
print(ls)

apk_info = aapt.get_apk_info('./xxx.apk')
print(apk_info)

# save icon
from PIL import Image
apk_info = aapt.get_apk_and_icon('./xxx.apk')
byte_stream = io.BytesIO(apk_info['icon_byte_value'])
img = Image.open(byte_stream)
img.save('./1.png')

# upload file

requests.post(url, files={'file': apk_info['icon_byte_value']})

```

## API

* aapt(args)
* ls(file_path)
* dump(file_path, values)
* packagecmd(file_path, command)
* remove(file_path, files)
* add(file_path, files)
* crunch(resource, output_folder)
* single_crunch(input_file, output_file):
* version()
* get_apk_info(file_path)
