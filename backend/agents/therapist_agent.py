from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low


class ContextPrompt(Model):
    context: str
    text: str


class Response(Model):
    text: str

class TranslationPayload(Model):
    text: str

#Deifining and connecting Agent to Agentverse via Mailbox
#To get the AGENT_MAILBOX_KEY first leave the AGENT_MAILBOX_KEY empty and run the agent it will throw an error, copy the agent's address and go to Agentverse switch to Local Agent and then Connect Agent paste your agent address here and copy the generated mailbox key
AGENT_MAILBOX_KEY = "0ce1f369-7e4c-44ec-96e1-72e91c4d8cc7"
agent = Agent(name="Therapist", seed="therapist-seed-phrase3", port=8000,
              mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai")

print(agent.address)
#Add testnet funds to the agent's wallet for it to register on the network
fund_agent_if_low(agent.wallet.address())

AI_AGENT_ADDRESS = "agent1q0h70caed8ax769shpemapzkyk65uscw4xwk6dc4t3emvp5jdcvqs9xs32y" #OpenAI Agent
TRANSLATOR_AGENT_ADDRESS = "agent1qwcndkhen93258rjrqgph86j5w84xmdcfc8fmcphl2277lczsatxqzqwsth"

diary_text = """
    i am so sad 我失去我的朋友
    """

prompt = ContextPrompt(
    context="Act as a therapist and provide feedback and analysis on the diary's content",
    text=diary_text,
)


@agent.on_event("startup")
async def send_message(ctx: Context):
    await ctx.send(AI_AGENT_ADDRESS, prompt)


@agent.on_message(Response)
async def handle_response(ctx: Context, sender: str, msg: Response):
    ctx.logger.info(f"Received response from {sender}: {msg.text}")
    therapist_response=msg.text
    await ctx.send(TRANSLATOR_AGENT_ADDRESS, TranslationPayload(text=therapist_response))

if __name__ == "__main__":
    agent.run()


