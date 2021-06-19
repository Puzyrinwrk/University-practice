# Task_1
# You have the following function:
# def retrieve_age(person):
#   return int(person["age"])
# Modify this function to handle possible exceptions.

# Task_2
# Write a function to parse MP3's ID3v2 tag.
# Function signature: def parse_id3v2(file_path)

# Format description:

# ID3v2 tag contains metadata(artist, album name, song name, etc) of MP3 file.
# usually (otherwise, don't parse) MP3 files start with ID3v2 tag, then audio data follows
# ID3v2 tag consists of header and body, header (10 bytes in total):
#     ID3v2/file identifier      "ID3"
#     ID3v2 version              $04 00 (ID3v2 version 4), $03 00 (ID3v2 version 3)
#     ID3v2 flags                %abcd0000 (1 byte, if `b` is set - extended header present)
#     ID3v2 size             4 * %0xxxxxxx (4 bytes, first bit of each byte always 0, 28 effective bits in total)
# example:
# b'ID3\x03\x00\x00\x00\x00\x03\x19'
#     ID3v2/file identifier      b'ID3' (b'ID3' - the way Python handle binary data in ASCII range, equal to b'x49x44x33')
#     ID3v2 version              $03
#     ID3v2 flags                $00
#     ID3v2 size                 $00 00 03 19 = 409 bytes
# tag body consists of one or more frames, followed one after another
# tag frame consists of header and body (with actual data)
# header (10 bytes in total), size format differs for ID3v2 version 3 and version 4:
#     Frame ID      $xx xx xx xx  (four ASCII characters)
#     Size (v4)     4 * %0xxxxxxx
#     size (v3)     $xx xx xx xx  (32 effective bits in total)
#     Flags         $xx xx
# example:
# b'TYER\x00\x00\x00\x05\x00\x00\x002004'
# Frame ID       b'TYER'
# Size           $00 00 00 05 = 5 bytes
# Flags          $00 00
# Data           $00 b'2004' -- first byte - encoding (see below), followed by data (year of release)
# There are several frame types. One of them, text information frames (identified by Frame ID starting with 'T' as in example above) should be parsed and binary data converted to string.

# Text frame body format:

# first byte is encoding, values:
# $00 – ISO-8859-1 (LATIN-1, Identical to ASCII for values smaller than 0x80).
# $01 – UTF-16 (UCS-2) encoded Unicode with BOM, in ID3v2.2 and ID3v2.3.
# $02 – UTF-16BE encoded Unicode without BOM, in ID3v2.4.
# $03 – UTF-8 encoded Unicode, in ID3v2.4.
# then actual data follows
# To convert to string use `decode` function, e.g. in REPL:
# >>> b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82, Python 3!'.decode('UTF-8')
# 'Привет, Python 3!'

# Implementaion notes:

# this is educational task, don't implement all features described in specification, just what required in task
# ensure your file starts with ID3 tag
# ensure ID3v2's version is 3 or 4
# don't parse files with extended header
# realworld ID3 tags can be incorrectly constructed, be careful (use Python 'with' construct to open file, exceptions should be handled)
# if it's not possible to parse file (for any reason: file not exists, no file read access, bad format, etc) return empty list
# read only tag data from file, don't read it all, this decreases IO dramatically (2.5 VS 27 seconds on my 1.6 GB directory with MP3s)
# it's ok to use "magic numbers" while parsing structures, e.g. version (major) occupies byte 4 in ID3 header, so can be accessed in following way:  tag_header[3] (compare with  tag_header_offset = 3; tag_header[tag_header_offset])
# you may use hex editor or Python binascii module to investigate file content
# see attached doc for more details
# Your function should return list of tuples (in order of appearance) with tag data, tuple format:

# Frame ID
# size
# binary data
# for text fields data converted to string, otherwise None
# Examples:
# >>> parse_id3v2('ariya_ulitsa_roz.mp3')
# [(b'TIT2', 19, b'\x03\xd0\xa3\xd0\xbb\xd0\xb8\xd1\x86\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb7\x00', 'Улица роз\x00'), (b'TALB', 29, b'\x03\xd0\x93\xd0\xb5\xd1\x80\xd0\xbe\xd0\xb9 \xd0\xb0\xd1\x81\xd1\x84\xd0\xb0\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\x00', 'Герой асфальта\x00'), (b'TCON', 13, b'\x03Heavy Metal\x00', 'Heavy Metal\x00'), (b'TDRC', 6, b'\x001987\x00', '1987\x00'), (b'TRCK', 5, b'\x005/6\x00', '5/6\x00'), (b'TPE1', 10, b'\x03\xd0\x90\xd1\x80\xd0\xb8\xd1\x8f\x00', 'Ария\x00')]

# >>> parse_id3v2('01_epidemiya_pridumai_svetlii_mir_myzuka.me.mp3')
# [(b'TALB', 61, b'\x01\xff\xfe\x1f\x04@\x048\x044\x04C\x04<\x040\x049\x04 \x00A\x042\x045\x04B\x04;\x04K\x049\x04 \x00<\x048\x04@\x04 \x00(\x00S\x00i\x00n\x00g\x00l\x00e\x00)\x00', 'Придумай светлый мир (Single)'), (b'TCON', 25, b'\x01\xff\xfeP\x00o\x00w\x00e\x00r\x00 \x00M\x00e\x00t\x00a\x00l\x00', 'Power Metal'), (b'TIT2', 43, b'\x01\xff\xfe\x1f\x04@\x048\x044\x04C\x04<\x040\x049\x04 \x00A\x042\x045\x04B\x04;\x04K\x049\x04 \x00<\x048\x04@\x04', 'Придумай светлый мир'), (b'TPE1', 19, b'\x01\xff\xfe-\x04?\x048\x044\x045\x04<\x048\x04O\x04', 'Эпидемия'), (b'TRCK', 13, b'\x01\xff\xfe0\x001\x00/\x000\x004\x00', '01/04'), (b'TYER', 11, b'\x01\xff\xfe2\x000\x001\x006\x00', '2016'), (b'TSSE', 13, b'\x03Lavf51.12.1\x00', 'Lavf51.12.1\x00'), (b'APIC', 58516, b'\x00image/jpg\x00\x03\x00\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00`\x00`\x00\x00\xff\xfe\x00?CREATOR: gd-jpeg v1.0 (using IJG JPEG v80), default quality\n\x00\xff\xdb  ... #50kilobytes of hex data removed from example# ', None), (b'COMM', 34, b'\x01eng\xff\xfe\x00\x00\xff\xfe(\x00m\x00y\x00z\x00u\x00k\x00a\x00.\x00o\x00r\x00g\x00)\x00', None)]


# Task_1
class AgeException(Exception):
    def init(self, msg, age):
        super().init(msg)
        self.age = age


class TooYoungException(AgeException):
    def init(self, msg, age):
        super().init(msg, age)


class TooOldException(AgeException):
    def init(self, msg, age):
        super().init(msg, age)


def retrieve_age(person):
    try:
        if int(person["age"]) < 1:
            raise TooYoungException("Age " + str(int(person["age"])) + " too young", int(person["age"]))
        elif int(person["age"]) > 100:
            raise TooOldException("Age " + str(int(person["age"])) + " too old", int(person["age"]));
        print(int(person["age"]))
    except TooYoungException as e:
        print('TouYoungException:', e)
    except TooOldException as e:
        print('TouOldException:', e)
    except Exception as e:
        print('Exception:', e)


retrieve_age({"name": "Dmitriy", "age": 5})


# Task_2
def check_frame_id(byte_list):
    for byte in byte_list:
        if not chr(byte).isupper() and not chr(byte).isdigit():
            return False
    return True


def convert_to_int(byte_list, version):
    size = 0
    if version == 4:
        pows = [24, 16, 8, 0]
    else:
        pows = [21, 14, 7, 0]
    for i in range(4):
        size += byte_list[i] << pows[i]

    return size


def parse_id3v2(file_path):
    try:
        tags = list()
        with open(file_path, 'rb') as file:
            header_tag = file.read(10)
            version = header_tag[3]
            flags = header_tag[5]

            if [header_tag[0], header_tag[1], header_tag[2]] != [73, 68, 51]:
                raise Exception('Its not a ID3v2 Tag')

            if flags & (1 << 6):
                raise Exception('File with extended header')

            if not version in (3, 4):
                raise Exception('Version should be 3 or 4')

            encoding = {
                b'\x00': 'ISO-8859-1',
                b'\x01': 'UTF-16',
                b'\x02': 'UTF-16BE',
                b'\x03': 'UTF-8',
            }

            while True:
                frame_id = file.read(4)
                if not check_frame_id(frame_id):
                    break

                size = convert_to_int(file.read(4), version)
                _ = file.read(2)  # flags
                encoding_type = file.read(1)
                data = file.read(size - 1)
                converted_data = None

                if chr(frame_id[0]) == 'T':
                    converted_data = data.decode(encoding[encoding_type])

                tags.append((frame_id, size, data, converted_data))
        return tags
    except:
        return []


print(parse_id3v2('D:/ch14_aria_ulitsa_roz.mp3'))

 
