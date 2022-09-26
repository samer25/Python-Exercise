budget = float(input())
price_kg_flower = float(input())

eggs_price = price_kg_flower * 0.75

milk_l_price = price_kg_flower * 1.25

milk_fourth_price = milk_l_price / 4

price_one_cozonac = eggs_price + milk_fourth_price + price_kg_flower

cozonac_coount = 0
colored_eggs = 0

while True:
    if budget > price_one_cozonac:
        budget -= price_one_cozonac
        cozonac_coount += 1
        colored_eggs += 3

        if cozonac_coount % 3 == 0:
            colored_eggs -= cozonac_coount - 2

    else:
        print(cozonac_coount, colored_eggs, budget)
        break
