from actions.rp5_runner import Rp5Runner
from datetime import datetime
import properties
import logging
launches = 0
step = properties.LAUNCHES_DELETE_STEP

if __name__ == "__main__":
    runner = Rp5Runner()
    runner.auth()
    start = datetime.now()
    while True:
        try:
            runner.delete_first_n_launches_on_page(step)
            launches += step
            logging.info(f"deleted +{step} launches, total deleted: {launches}, time spent: {(datetime.now() - start)}")
        except BaseException as e:
            pass
