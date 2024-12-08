import logging
import time

from requests.sessions import Session

from config import TEXT_CHANNEL_ID, TOKEN, configure_logger


def main():
    configure_logger()

    data = {
        "url": f"https://discord.com/api/v9/channels/{TEXT_CHANNEL_ID}/messages",
        "headers": {"Authorization": TOKEN},
        "json": {"content": "i'm here."},
    }

    session = Session()
    interval = 60 * 5
    while True:
        response = session.post(**data)
        if response.status_code != 200:
            logging.error(f"failed to send message! {response.json()}")
        elif response.status_code == 200:
            logging.info("message sent 'n you're alive!")
        else:
            logging.info("something went wrong...")

        logging.info("sleeping for 5 minutes now...")
        time.sleep(interval)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("quitting...")
