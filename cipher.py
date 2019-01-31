#!/usr/bin/env python2
'''
Description - An auto-generated stub description.
'''

import argparse
import logging
import string

logger = logging.getLogger(__name__)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--keyword', default='heart')
    parser.add_argument('--rotate', type=int, default=4)

    subparsers = parser.add_subparsers(help='sub-command help')
    encode_parser = subparsers.add_parser('encode')
    encode_parser.set_defaults(func=encode)
    encode_parser.add_argument('data')

    decode_parser = subparsers.add_parser('decode')
    decode_parser.set_defaults(func=decode)
    decode_parser.add_argument('data')

    # If `argv` is None, `parse_args` will default to using `sys.argv`
    return parser.parse_args(args=argv)


def make_key(args, encode=True):
    alphabet = string.ascii_lowercase + string.digits
    key = args.keyword + alphabet.translate(None, args.keyword)
    if args.rotate:
        key = key[args.rotate:] + key[:args.rotate]
    if encode:
        return key, alphabet
    return alphabet, key


def process(data, key, alphabet):
    data = data.lower()
    ans = ''
    for c in data:
        if c not in alphabet:
            ans += c
            continue
        x = alphabet.index(c)
        ans += key[x]
    return ans

def encode(data, args):
    key, alphabet = make_key(args, encode=True)
    print("Key:      {}".format(key))
    print("Alphabet: {}".format(alphabet))
    return process(data, key, alphabet)


def decode(data, args):
    key, alphabet = make_key(args, encode=False)
    print("Key:      {}".format(key))
    print("Alphabet: {}".format(alphabet))
    return process(data, key, alphabet)


def main(argv=None):
    args = parse_args(argv)
    print(args.func(args.data, args))


if __name__ == '__main__':
    main()
