"""
HQAI Universe Downloader
"""

from io import StringIO

import pandas as pd
import requests

from hqai.core.logger import log


class UniverseDownloader:

    URL = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"

    def download(self) -> pd.DataFrame:

        log.info("Connecting to NSE...")

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 Chrome/137.0 Safari/537.36"
            )
        }

        response = requests.get(
            self.URL,
            headers=headers,
            timeout=30,
        )

        response.raise_for_status()

        df = pd.read_csv(StringIO(response.text))

        log.info(f"Downloaded {len(df)} records")

        return df
