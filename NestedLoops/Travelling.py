destination = input()

while destination != 'End':
    # ----------------- LOGIC --------------------
    money_needed = float(input())
    money_saved = 0

    while money_saved < money_needed:
        # ------------- END CONDITION ----------------
        add_money = float(input())
        money_saved += add_money

        # ----------------- LOGIC --------------------
        if money_saved >= money_needed:
            print(f'Going to {destination}!')
            break

    # ------------- END CONDITION ----------------
    destination = input()
