# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyparsing as pp

# Basic Elements from the output of FFmpeg

# A real number in the format 1111.2222
real_number = pp.Combine(pp.Word(pp.nums) + pp.Optional('.' + pp.Word(pp.nums)))

# Any string of alphanums and some special characters
str_any = pp.Word(pp.alphanums + ',.-;:_#\'+*~!"§$%&/()=?')

# a date in the format of yyyy-mm-dd
str_date = pp.Combine(pp.Word(pp.nums, max=4) + '-' + pp.Word(pp.nums, max=2) + '-' + pp.Word(pp.nums, max=2))

# a time in the format of hh:mm:ss.fffff
str_time = pp.Combine(pp.Word(pp.nums, max=2) + ':' + pp.Word(pp.nums, max=2) + ':' + pp.Word(pp.nums, max=2) +\
           pp.Optional('.' + pp.Word(pp.nums, max=10)))

# a FFmpeg file or stream identifier of the form #0:1
file_stream_id = pp.Combine('#' + pp.Word(pp.nums, max=2).setResultsName('File_ID') + \
                 pp.Optional(':' + pp.Word(pp.nums, max=2).setResultsName('Stream_ID')))

# FFmpeg input file-name (e.g. 'Filename.Extension')
file_name = pp.Literal('\'') + pp.Word(pp.alphanums + ' _-+').setResultsName('Name') + \
            pp.Literal('.') + pp.Word(pp.alphanums).setResultsName('Extension') + pp.Literal('\'')


# Input File line (e.g. Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'Dani Jensen - Submissive Slave.mp4':)
input_file = pp.Literal('Input') + pp.SkipTo(file_stream_id, include=True).setResultsName('Input_File_ID') + \
             pp.SkipTo(pp.Literal('from') + file_name, include=True).setResultsName('Input_File_Name')

input_stream = pp.Literal('Stream') + pp.SkipTo(file_stream_id, include=True).setResultsName('Stream') + \
               pp.SkipTo(pp.oneOf(['Video', 'Audio']), include=True).setResultsName('Streamtype')





inp_Input_line = """Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'Dani Jensen - Submissive Slave.mp4':"""
inp_Metadata_line = """creation_time   : 2013-09-19 19:33:20"""
inp_Duration_line = """Duration: 00:31:15.11, start: 0.000000, bitrate: 1101 kb/s"""
inp_Stream_line_1 = """Stream #0:0(eng): Video: h264 (High) (avc1 / 0x31637661), yuv420p, 750x420 [SAR 224:225 DAR 16:9], 1000 kb/s, 23.98 fps, 23.98 tbr, 1199 tbn, 47.96 tbc (default)"""
inp_Stream_line_2 = """Stream: #0:1(eng): Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 95 kb/s (default)"""