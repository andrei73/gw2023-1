import sys
import os
import time

from typing import List

class Solver:
    @staticmethod
    def solve(args: List[str]) -> None:
        if args[0] == 'all':
            Solver.run_all()
        else:
            day = args[0]
            puzzle = args[1]
            Solver.run(day, puzzle)

    @staticmethod
    def run_all() -> None:
        start_time = time.time()
        files = sorted(filter(lambda x: x.startswith('Day'), os.listdir()))
        for file in files:
            day = file[3:]
            Solver.run(day, '1')
            Solver.info('')
            Solver.run(day, '2')
            Solver.info('')
        end_time = time.time()
        elapsed = round(end_time - start_time, 4)
        Solver.success(f"Completed all solutions in {elapsed} seconds.")

    @staticmethod
    def run(day: str, puzzle: str) -> None:
        class_name = f"Day{day}.Puzzle{puzzle}"
        try:
            module = __import__(class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
        except (ImportError, AttributeError):
            Solver.error(f"Could not find class to solve Day {day} Puzzle {puzzle}.")
            Solver.info(f"Tried to instantiate: {class_name}")
            sys.exit(1)
        
        instance = class_obj()
        if not callable(instance):
            Solver.error(f"Instantiated class is not callable: {class_name}")
            sys.exit(1)
        
        pretty_day = day.zfill(2)
        Solver.info(f"========= Day {pretty_day}, Puzzle {puzzle} =========")
        start_time = time.time()
        Solver.success(instance('input.txt'))
        end_time = time.time()
        elapsed = round(end_time - start_time, 4)
        Solver.info(f"Completed in {elapsed} seconds.")
        Solver.info('====================================')

    @staticmethod
    def success(message: str) -> None:
        print(f"\033[01;32m  {message}  \033[0m")

    @staticmethod
    def error(message: str) -> None:
        print(f"\033[01;31m  {message}  \033[0m")

    @staticmethod
    def info(message: str) -> None:
        print(f"  {message}  ")

# Main script
if __name__ == '__main__':
    args = sys.argv[1:]
    Solver.solve(args)
