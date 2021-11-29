import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Incorrect number of arguments,",
              "proper example: python3 get_json_from_demo.py <demo_path> <out_path>")
        exit(0)

    from csgo.parser import DemoParser

    out_dir, demo_id = os.path.split(sys.argv[2])

    demo_id = ".".join(demo_id.split(".")[:-1])

    demo_parser = DemoParser(demofile=sys.argv[1], outpath=out_dir, demo_id=demo_id, parse_rate=128)

    # Parse the demofile, output results to dictionary with df name as key
    data = demo_parser.parse()
