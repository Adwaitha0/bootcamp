def hello(name: str | None = None) -> str:
    target = name or "world"
    return f"hello, {target}"

