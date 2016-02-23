#!/usr/bin/env python

"""
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys
import string
import optparse
import colorama


def cmd_parser_setup():
    parser = optparse.OptionParser()

    parser.add_option('-f', '--file',
                      dest='filename',
                      help='Filename to hexdump')

    parser.add_option('-c', '--columns',
                      dest='columns',
                      default=16,
                      type=int,
                      help='Hex columns count')

    parser.add_option('', '--version',
                      dest='version',
                      default=False,
                      action="store_true",
                      help='Prints package version and exits')

    (opts, args) = parser.parse_args()
    return (opts, args)


def hexy_load_chunk(f, chunksize=32):
    while True:
        chunk = f.read(chunksize)
        if chunk:
            for b in chunk:
                yield b
        else:
            break


def hexy_view_file(filename, line_len = 16):
    result = 0
    special_yellow = [0x0D, 0x0A]

    # string.printable
    # string.whitespace
    try:
        with open(filename, "rb") as f:
            lint_cnt = 1
            line_print = ""
            for b in hexy_load_chunk(f):

                if ord(b) in special_yellow:
                    sys.stdout.write(colorama.Back.YELLOW)
                if ord(b) > 0x7F:
                    sys.stdout.write(colorama.Back.RED)
                sys.stdout.write("%02X"% ord(b))
                sys.stdout.write(colorama.Back.RESET)
                sys.stdout.write(" ")

                if b in string.printable and b not in string.whitespace:
                    line_print += b
                else:
                    if ord(b) in special_yellow:
                        line_print += colorama.Back.YELLOW
                    elif ord(b) > 0x7F:
                        line_print += colorama.Back.RED
                    line_print += " "
                    line_print += colorama.Back.RESET
                if lint_cnt == line_len:
                    print " | ", line_print
                    lint_cnt = 0
                    line_print = ""
                elif lint_cnt == line_len / 2:
                    sys.stdout.write("| ")
                lint_cnt += 1
            for i in range(line_len - lint_cnt + 1):
                sys.stdout.write("   ")
                if lint_cnt == line_len / 2:
                    sys.stdout.write("| ")
                lint_cnt += 1
            print " | ", line_print
    except Exception as e:
        print str(e)
        print "Error opening file..."
        result = -1
    return result

def hexy_main():
    errorlevel_flag = 0
    (opts, args) = cmd_parser_setup()

    colorama.init()

    if opts.filename:
        # print "open file %s..."% opts.filename
        errorlevel_flag = hexy_view_file(opts.filename, opts.columns)

    elif opts.version:
        import pkg_resources  # part of setuptools
        version = pkg_resources.require("hexy-viewer")[0].version
        print version
    else:
        pass

    sys.exit(errorlevel_flag)
