#!/usr/bin/env python3
""" return"""


def index_range(page: int, page_size: int) -> tuple:
    """ define index"""
    tupla = ((page - 1) * page_size, page * page_size)
