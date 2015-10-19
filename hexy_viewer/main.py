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
import optparse


def cmd_parser_setup():
    parser = optparse.OptionParser()

    parser.add_option('', '--version',
                      dest='version',
                      default=False,
                      action="store_true",
                      help='Prints package version and exits')

    (opts, args) = parser.parse_args()
    return (opts, args)


def hexy_main():
    errorlevel_flag = 0
    (opts, args) = cmd_parser_setup()

    if opts.version:
        import pkg_resources  # part of setuptools
        version = pkg_resources.require("hexy-viewer")[0].version
        print version
    else:
        pass

    sys.exit(errorlevel_flag)
