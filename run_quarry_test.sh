#!/bin/sh
curl -X POST http://127.0.0.1:5000/v1/validate_card -H "Content-Type: application/json" -d @./test_shc.json

