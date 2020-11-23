#!/usr/bin/env python3

import argparse
import pypact as pp


def main():
    # Command line argument support
    parser = argparse.ArgumentParser(description='Files file path changer')
    parser.add_argument('oldfile', type=argparse.FileType('r'),
                        help='The fispact files file to be read')
    parser.add_argument('newfile', type=argparse.FileType('w'),
                        help='The changed fispact files file to be written')
    parser.add_argument('oldpath', type=str, default='/opt/fispact/nuclear_data',
                        help='The old file path to change in old file')
    parser.add_argument('newpath', type=str, default='/nuclear_data',
                        help='The new file path to use in new file')
    args = parser.parse_args()

    old_file = args.oldfile.name
    new_file = args.newfile.name
    old_path = args.oldpath
    new_path = args.newpath
    
    ff = pp.FilesFile()
    pp.from_file(ff, old_file)
    
    # change paths here
    for k, v in ff.to_dict().items():
        if old_path in v:
            new_v = v.replace(old_path, new_path)
            ff.__setattr__(k, new_v)
    
    # validate new paths
    print(" * Invalid paths are: ")
    for k, p in ff.invalidpaths():
        print("Key: {}, Path: {}".format(k, p))
    
    pp.to_file(ff, new_file)


if __name__ == "__main__":
    main()
