"""
App Settings
============

Shared runtime objects for the platform. All models go through the
OpenAI-compatible gateway (LiteLLM / 9router).
"""

from os import getenv

from agno.models.openai.like import OpenAILike

GATEWAY_URL = getenv("LITELLM_BASE_URL", "http://host.docker.internal:4000/v1")


def _model(model_id: str) -> OpenAILike:
    return OpenAILike(id=model_id, base_url=GATEWAY_URL, api_key=getenv("LITELLM_API_KEY"))


def default_model() -> OpenAILike:
    """Fresh model instance per agent — avoids shared-state footguns."""
    return _model(getenv("DEFAULT_MODEL", "sdd-B-tier"))


def manager_model() -> OpenAILike:
    """Model for OS Manager and Company Product Manager."""
    return _model(getenv("MANAGER_MODEL", "sdd-B-tier"))
