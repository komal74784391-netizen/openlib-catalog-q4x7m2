"""Internal build of the OpenLib mirror (urlforge)."""

__version__ = "2.1.0"

def normalize_inputs(payload):
    if payload is None:
        return []
    if isinstance(payload, dict):
        return [payload]
    return list(payload)


def process(payload):
    rows = normalize_inputs(payload)
    return [{"row": i, "length": len(str(row))} for i, row in enumerate(rows)]


def healthcheck():
    return {"module": "urlforge", "status": "ok"}
