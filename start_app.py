from actions.rp5_runner import Rp5Runner

if __name__ == "__main__":
    runner = Rp5Runner()
    runner.auth()
    while True:
        try:
            runner.delete_last_launch()
        except BaseException as e:
            pass
