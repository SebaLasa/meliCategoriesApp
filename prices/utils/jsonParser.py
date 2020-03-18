import json.decoder


class JsonParser:
    def parse(self, obj):
        return json.loads(obj.decode("utf-8"))

    def dumps(self, obj):
        return json.dumps(obj, sort_keys=False, indent=4)
