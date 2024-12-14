def prepare_payload(schema, payload):
    """Recursively construct a valid payload based on the schema."""
    if not schema:
        return None

    schema_type = schema.get("type")
    if schema_type == "string":
        return payload
    elif schema_type == "number":
        return 1
    elif schema_type == "boolean":
        return True
    elif schema_type == "array":
        item_schema = schema.get("items")
        return [prepare_payload(item_schema, payload)]
    elif schema_type == "object":
        properties = schema.get("properties", {})
        return {
            key: prepare_payload(sub_schema, payload)
            for key, sub_schema in properties.items()
        }
    return None
