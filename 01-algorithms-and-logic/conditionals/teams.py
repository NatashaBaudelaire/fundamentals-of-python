def main():
    teams = {

        "Manchester United": 66,
        "Real Madrid": 95,
        "Barcelona": 92,
        "Bayern Munich": 80,
        "Juventus": 70,
        "Paris Saint-Germain": 50,
        "Liverpool": 65,
        "Chelsea": 60,
        "AC Milan": 58,
        "Ajax": 55,

        "FC Seoul": 10,
        "Jeonbuk Hyundai Motors": 12,
        "Ulsan Hyundai": 14,
        "Pohang Steelers": 11,
        "Suwon Samsung Bluewings": 9,
    }

    print("Choose a European or Asian football team:")
    for team in teams.keys():
        print(f"- {team}")

    choice = input("Enter the name of the chosen team: ")

    if choice not in teams:
        print("Team not found. Please choose one of the listed teams.")

if __name__ == "__main__":
    main()