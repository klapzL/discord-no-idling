import logging
import os

from dotenv import load_dotenv

load_dotenv()

TEXT_CHANNEL_ID = os.getenv("DISCORD_TEXT_CHANNEL_ID")
TOKEN = os.getenv("DISCORD_USER_TOKEN")


def configure_logger(level=logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)-3d%(levelname)-s - %(message)s",
    )
