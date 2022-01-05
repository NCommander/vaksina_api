# Copyright 2021-2022 Michael Casadevall <michael@casadevall.pro>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import json
import os

from flask import render_template, request
from werkzeug.utils import send_from_directory
from vaksina_api import vaksina_api


@vaksina_api.route('/')
def root():
    v = vaksina_api.config['v']
    with open("../vaksina/example-01-f-qr-code-numeric-value-0.txt", "r") as f:
        vax_data = v.parse_card_data(f.read())

    print(vax_data[0].names[0])
    return vax_data[0].names[0]

@vaksina_api.route('/v1/validate_card', methods = ['POST'])
def validate_card():
    d = request.json
    v = vaksina_api.config['v']

    # currently not handling binary data
    if d['qr_data_type'] != "text":
        return 'unknown data type', 400
    
    try:
        vax_data = v.parse_card_data(d['qr_decode'])
    except Exception:
        return 'processing error', 400

    return json.dumps(vax_data.to_dict(), indent=2)
