from uagents import Agent, Context, Model, Field
from uagents.setup import fund_agent_if_low
from transformers import pipeline

# Initialize the translation model
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")

# Connect agent to Agentverse
AGENT_MAILBOX_KEY = "e094c679-90aa-44be-bc06-889a91d904fe"
agent = Agent(name="Zh-En translator", seed="senderAgent secret phrase1234134242_3", port=8001,
              mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai")

print(agent.address)

# Fund the agent if low on funds
fund_agent_if_low(agent.wallet.address())

# Define the payload schema using Pydantic
class TranslationPayload(Model):
    text: str

# Define the translation behavior
@agent.on_message(model=TranslationPayload)
async def handle_translate(ctx: Context, sender:str, payload: TranslationPayload):
    input_text = payload.text

    if not input_text:
        ctx.logger.error("No text provided for translation.")


    result = translator(input_text)
    translation = result[0]['translation_text']
    ctx.logger.info(translation)

# Run the agent
if __name__ == "__main__":
    print("Translator agent is running. Use another uAgent to send 'translate' requests.")
    agent.run()