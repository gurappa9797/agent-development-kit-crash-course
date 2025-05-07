from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.vetting_agent import vetting
from .sub_agents.coverage_agent import coverage
from .sub_agents.payment_agent import payment
from .sub_agents.refund_agent import refund
from .tools.tools import get_current_time

root_agent = LlmAgent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.

    You are responsible for delegating tasks to the following agent:
    - vetting
    - coverage
    - payment
    - refund
    -

    You also have access to the following tools:
    - get_current_time
    """,
    sub_agents=[vetting, coverage, payment, refund],
    tools=[
        AgentTool(),
        get_current_time,
    ],
)
