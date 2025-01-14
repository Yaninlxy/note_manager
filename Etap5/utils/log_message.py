def log_message(message, level="INFO"):
    """
    Логирует сообщение с указанным уровнем.
    """
    levels = {"INFO": "ℹ️", "WARNING": "⚠️", "ERROR": "❌"}
    prefix = levels.get(level.upper(), "ℹ️")
    print(f"{prefix} {message}")
