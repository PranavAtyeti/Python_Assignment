from my_package.maths import add, subtract, multiply, divide
from my_package.logger_config import logger

def main():
    logger.info("Inside main")

    try:
        a, b = 10, 5
        logger.info(f"Performing operations on {a} and {b}")

        print(f"{a} + {b} = {add(a, b)}")
        print(f"{a} - {b} = {subtract(a, b)}")
        print(f"{a} * {b} = {multiply(a, b)}")
        print(f"{a} / {b} = {divide(a, b)}")
    except Exception as e:
        logger.error("An error occurred!", exc_info=True)
    finally:
        logger.info("Main application finished.")

if __name__ == "__main__":
    main()
