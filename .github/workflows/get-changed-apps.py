import argparse

parser = argparse.ArgumentParser()
parser.add_argument("changed_files", type=str)

if __name__ == "__main__":
    args = parser.parse_args()
    print([v.strip() for v in args.changed_files.split(",")])
    print([v.strip() for v in args.changed_files.split(",")])
