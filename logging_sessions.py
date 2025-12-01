import logging
import os

# Clean up any previous logs
for log_file in ["logger.log", "web.log", "tunnel.log"]:
    if os.path.exists(log_file):
        os.remove(log_file)
        print(f"🧹 Cleaned up {log_file}")

# Configure logging with DEBUG log level.
logging.basicConfig(
    filename="logger.log",
    level=logging.DEBUG,
    format="%(filename)s:%(lineno)s %(levelname)s:%(message)s",
)

print("✅ Logging configured")

api_key = os.getenv("GEMINI_API_KEY")

from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools.agent_tool import AgentTool
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google.genai import types

print("ADK imported successfully")

retry_config = types.HttpRetryOptions(
    attempts=3,
    exp_base=7, # Delay multiplier
    initial_delay=1, # initial delay before first retry (seconds)
    http_status_codes=[429, 500, 503, 504] # Retry on these HTTP errors
)

google_search_agent = Agent(
    name="google_search_agent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    description="A simple agent that can answer general questions.",
    instruction="You are a helpful assistant that provides accurate and concise answers to user questions. Use Google Search for current info or if unsure.",
    tools=[google_search]
)

print("Root agent created successfully")

wellness_coach_agent = Agent(
    name="wellness_coach_agent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    description="An agent that provides wellness coaching and advice.",
    instruction="You are a wellness coach. Provide advice on mental and physical well-being. Use Google Search to find up-to-date information when necessary.",
    tools=[AgentTool(agent=google_search_agent)]
)

print("Wellness coach agent created successfully")

runner = InMemoryRunner(agent=nutrient_calculation_agent)

print("Runner created successfully")

response = await runner.run_debug("What is Agent Development Kit from Google and what languages is its SDK available in?")

!adk create nutrient_calculation_agent --model gemini-2.5-flash-lite --api_key $GEMINI_API_KEY

nutrient_calculation_agent = Agent(
    name="nutrient_calculation_agent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    description="An agent that calculates nutritional information based on user input.",
    instruction="""You are a nutritional expert.

    1. Ask the user for details about their meal (ingredients, quantities, etc.).
    2. Calculate the nutritional information based on the provided details.
    3. Provide the user with a detailed breakdown of the nutritional content.
    4. Compare the nutritional content with recommended daily values and provide suggestions for improvement if necessary."""
)
