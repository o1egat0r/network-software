# GraphQL-клиент (неделя 6). Проект: logs-s05

PROJECT_CODE = "logs-s05"


def build_payload(query: str, variables: dict) -> dict:
    """Формирует тело POST-запроса в формате GraphQL over HTTP."""
    return {"query": query, "variables": variables}
