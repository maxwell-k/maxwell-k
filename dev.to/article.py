from sys import argv
from json import dumps

with open(argv[-1]) as file_:
    output = {"body_markdown": file_.read()}
print(dumps({"article": output}))
