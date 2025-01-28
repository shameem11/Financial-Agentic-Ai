from phi.agent import Agent, RunResponse
from phi.model.groq import Groq

agent = Agent(
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    markdown=True
)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story.")
# print(run.content)

# Print the response in the terminal
agent.print_response("discribe about any car .")

