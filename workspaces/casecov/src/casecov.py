"""Internal build of the OpenLib mirror (casecov)."""

__version__ = "6.2.1"

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
    return {"module": "casecov", "status": "ok"}
