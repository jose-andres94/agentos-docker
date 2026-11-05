"""
Basic Agent
===========

Minimal test agent: chats through LiteLLM and can use the calculator tool.
"""

from agno.agent import Agent
from agno.tools.calculator import CalculatorTools

from app.settings import default_model
from db import get_postgres_db

basic_agent = Agent(
    id="basic",
    name="Basic",
    model=default_model(),
    tools=[CalculatorTools()],
    instructions="Eres un asistente de prueba. Responde breve, en el idioma del usuario. Usa la calculadora para cualquier cuenta.",
    db=get_postgres_db(),
    add_history_to_context=True,
    num_history_runs=5,
    markdown=True,
)
