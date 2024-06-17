import random

def flip_coin():
    # Randomly choose either "Heads" or "Tails"
    outcome = random.choice(["Heads", "Tails"])
    return outcome

def main():
    # Simulate flipping the coin
    result = flip_coin()
    print(result)

if __name__ == "__main__":
    main()
