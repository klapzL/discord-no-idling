import logging
import time

from requests.sessions import Session

from config import TEXT_CHANNEL_ID, TOKEN, configure_logger
from utils import get_idle_time


def main():
    configure_logger()

    data = {
        "url": f"https://discord.com/api/v9/channels/{TEXT_CHANNEL_ID}/messages",
        "headers": {"Authorization": TOKEN},
        "json": {"content": "i'm here."},
    }

    session = Session()
    interval = 60 * 5

    try:
        while True:
            if (idle_time := get_idle_time()) > interval:
                response = session.post(**data)
                if response.status_code == 200:
                    logging.info("message sent 'n you're alive!")
                else:
                    logging.error(f"failed to send message! {response.json()}")

            logging.info(f"{idle_time=}")
            logging.info("sleeping...")
            time.sleep(interval)

    except KeyboardInterrupt:
        logging.info("quitting...")


if __name__ == "__main__":
    main()
