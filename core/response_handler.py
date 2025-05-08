import json

class ResponseHandler:
    def sanitize(self, text):
        return text.strip()

    def to_json(self, text):
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {"error": "Invalid JSON", "raw": text}
