# import yaml

# with open("example.yaml") as stream:
#     try:
#         print(yaml.safe_load(stream))
#     except yaml.YAMLError as exc:
#         print(exc)

from openapi_parser import parse
from openapi_parser.specification import DataType

specification = parse("example.yaml")

# print(specification)

# input fieldy
for path in specification.paths:
    print(f"{path.url}: ")
    for op in path.operations:
        print(f"\t{op.method}:")
        for res in op.responses:
            print(f"\t\t{res.code}")
            for c in res.content:
                if c.schema.type == DataType.ARRAY:
                    x = c.schema.items
                else:
                    x = c.schema.properties
                try:
                    if x.type == DataType.OBJECT:
                        x = x.properties
                except:
                    pass
                for s in x:
                    print(f"\t\t\t{s}")
