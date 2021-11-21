#!/usr/bin/python3
# 5-no_c.py
# Gedeon Obae Gekonge <gideonobae@gmail.com.com>


def no_c(my_string):
    return ("".join(c for c in my_string if c not in "Cc"))
