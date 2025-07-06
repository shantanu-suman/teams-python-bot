import os
import asyncio
from flask import Flask, request, Response
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

APP_ID = os.getenv("MICROSOFT_APP_ID")
APP_PASSWORD = os.getenv("MICROSOFT_APP_PASSWORD")

adapter_settings = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
adapter = BotFrameworkAdapter(adapter_settings)

@app.route("/api/messages", methods=["POST"])
def messages():
    activity = Activity().deserialize(request.json)

    async def handle_turn(turn_context: TurnContext):
        await turn_context.send_activity("👋 Hello! This is your local Python bot in Teams.")

    asyncio.run(adapter.process_activity(activity, "", handle_turn))
    return Response(status=202)

if __name__ == "__main__":
    app.run(port=3978)
