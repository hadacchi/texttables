#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2017 hadacchi <master@hadacchi.com>
# This code is released under the license described in the LICENSE file

from unicodedata import east_asian_width

# This is for Japanese strings.
FULLWIDTH = 'FWA'
HALFWIDTH = 'HNa'

def fullchars(string):
    '''This function return the number of fullwidth characters in the sense of
    Japanese language.'''
    fulls = sum(width in FULLWIDTH
                for width in [east_asian_width(char) for char in string])
    return fulls

def utfwidth(string):
    '''This function return width of a string which includes multibyte chars of
    Japanese language. Japanese multibyte characters are fullwidth, i.e. twice
    of halfwidth.'''
    return len(string) + fullchars(string)

