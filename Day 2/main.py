"""
Main file, this is the file to run when you want to see day 2. This holds the 'main' function.
URL: https://adventofcode.com/2024/day/2#part2
"""
from parser import InputParser


def main() -> None:
    """
    Gets reports from the input (input.txt) file, parsed.

    Part 1:
        has a list called is_safe, which holds whether the corresponding report is safe. They have the same index, so
        that's how they are linked. Then it checks if the report is either descending or ascending, and holds it to
        that, marking it unsafe it doesn't follow that behavior. It then checks total distance between the current
        number, and next number. If the gap is more than 3, or less than 1, marks it unsafe.

    Part 2:
        Checks to see if the report was safe before dampened, and if was, mark it as safe. If not, iterate through
        the reports length and remove one item until gone through every bit of the list. If the report is valid (using
        the part 1 method) mark it as valid and move one.
    """
    reports: list[list[int]] = InputParser("input.txt").get_parsed_lists()

    # Part 1
    is_safe: list[bool] = []
    for report in reports:
        safe: bool = True
        is_ascending: bool = report[0] - report[1] > 0
        for num in range(len(report) - 1):
            distance: int = report[num] - report[num + 1]  # Distance between index & neighbour index
            if (is_ascending and distance > 0) or (not is_ascending and distance < 0):  # Ascend/Descend continuity
                safe = 1 <= abs(distance) <= 3
            else:
                safe = False

            if not safe:
                break

        is_safe.append(safe)

    total_safe_reports = is_safe.count(True)

    for i, report in enumerate(reports):
        print(f"{report} : {is_safe[i]}")
    print(f"Total Safe Reports: {total_safe_reports}")

    # Entering part 2
    print("\n|\n|\n| PART 2\n|\n|\n")

    problem_dampener_safe: list[bool] = []
    for j, report in enumerate(reports):
        if is_safe[j]:
            problem_dampener_safe.append(True)
            continue

        dampened_safe: bool = False
        for i in range(len(report)):
            dampened_report: list[int] = report.copy()
            dampened_report.pop(i)

            safe: bool = True
            is_ascending: bool = dampened_report[0] - dampened_report[1] > 0
            for num in range(len(dampened_report) - 1):
                distance: int = dampened_report[num] - dampened_report[num + 1]  # Distance between i & neighbour i
                if (is_ascending and distance > 0) or (not is_ascending and distance < 0):  # Ascend/Descend continuity
                    safe = 1 <= abs(distance) <= 3
                else:
                    safe = False

                if not safe:
                    break

            if safe:
                dampened_safe = True
                break

        problem_dampener_safe.append(dampened_safe)

    for i, report in enumerate(reports):
        print(f"{report} : {problem_dampener_safe[i]}")
    print(f"Total Safe Dampened Reports: {problem_dampener_safe.count(True)}")


# Running Main function, as if this language was normal
if __name__ == '__main__':
    main()
