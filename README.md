# Aapt

Android Asset Packaging Tool for Python3

## Install

`pip3 install aapt`

Your can easily check your installation with `python -c "import aapt; print(aapt.version())"`.

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
# https://tea.xyz/what-is-this-file
---
version: 1.0.0
codeOwners:
  - '0xEbB4102D4561283a02a304d04C9BAC2204cEd944'
quorum: 1
