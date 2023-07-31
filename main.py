import logging
from typing import List
from parts import PARTS_INFO


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


class PCPart:
    def __init__(self, name: str, price: int, tdp: str) -> None:
        self.name = name
        self.price = price
        self.TDP = tdp

    def get_name(self, search_name: str) -> List:
        try:
            logger.info(f"Searching for parts with name: {search_name}")
            names = []
            for part_id, info in PARTS_INFO.items():
                if search_name == info["name"]:
                    names.append(info)
            return names
        except Exception as error:
            logger.error(f"Error getting name: {error}")

    def get_price(self, search_price: int) -> List:
        try:
            logger.info(f"Searching for parts with price: {search_price}")
            prices = []
            for part_id, info in PARTS_INFO.items():
                if search_price == info["price"]:
                    prices.append(info)
            return prices
        except Exception as error:
            logger.error(f"Error getting price: {error}")

    def get_tdp(self, search_tdp: str) -> List:
        try:
            logger.info(f"Searching for parts with TDP: {search_tdp}")
            tdp = []
            for part_id, info in PARTS_INFO.items():
                if search_tdp == info["TDP"]:
                    tdp.append(info)
            return tdp
        except Exception as error:
            logger.error(f"Error getting TDP: {error}")


if __name__ == "__main__":
    pc_part = PCPart("Test Part", 100, 150)
    logger.info(pc_part.get_name("Intel HD Graphics 4600"))
    logger.info(pc_part.get_price("$190"))
    logger.info(pc_part.get_tdp("65 W"))
