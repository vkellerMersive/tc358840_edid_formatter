#!/usr/bin/python

import struct
import sys

# Pass the path to an edid binary and this script will output
# the edid format as expected by the tc358840.c file.

if __name__=='__main__':

    if len( sys.argv ) != 2:
        print( "Expecting path to EDID binary." )
        sys.exit( 1 )

    edid_path = sys.argv[1]

    prefix = "        "
    starting_byte = 0x8c00

    edid = open( edid_path, mode='rb' ).read()

    format_str = "I" * ( len( edid ) // 4 )

    edid_bytes = struct.unpack( format_str, edid )

    for b in edid_bytes:
        formatted_byte = "{0:#0{1}x}".format( b, 10 )
        print "{}{{{}, {}, H2C_DATA_32BIT}},".format( prefix, hex(starting_byte), formatted_byte )
        starting_byte += 4
