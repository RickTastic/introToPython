import json

jsonEg = '{"name":"John", "age":30, "city":"New York"}'

# parse jsonEG

parsedJson = json.loads(jsonEg)

print(parsedJson["age"])