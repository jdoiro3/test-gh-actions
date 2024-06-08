import markdown_to_json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("value", type=str)
parser.add_argument("--header", type=str, default="Checkbox")

def is_checked(val: str) -> bool:
    start, end = val.index("["), val.index("]")
    return bool(val[start+1:end].strip())

if __name__ == "__main__":
    args = parser.parse_args()
    dictified = markdown_to_json.dictify(args.value.replace("\\n", "\n"))
    print("true" if is_checked(dictified[args.header][0]) else "false")