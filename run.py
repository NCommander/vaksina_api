#!/usr/bin/env python3

import json
import vaksina
import vaksina_api

def main():
    v = vaksina.Vaksina()

    with open("../vaksina/jwks.json", "r") as f:
        jwt_json = json.loads(f.read())
        v.import_signing_key("shc",
                             "https://spec.smarthealth.cards/examples/issuer",
                             jwt_json)

    with open("../vaksina/data/vaccine_info.json") as f:
        v.load_vaccine_info(f.read())

    vaksina_api.vaksina_api.config['v'] = v
    vaksina_api.vaksina_api.run()

if __name__ == "__main__":
    main()
