def dead_letter_queue(data):
    if not data.get("value"):
        return "sent to DLQ"
    return data

def stream_processor(data):
    return {"validated": True, "summary": "summary info"}

def process_and_save(data):
    return True