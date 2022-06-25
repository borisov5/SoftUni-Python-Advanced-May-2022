def shopping_cart(*arguments):
    namePizza = "Pizza"
    nameSoup = "Soup"
    nameDessert = "Dessert"

    addedProductsCount = 0

    dicMealsMaxProducts = {
        "Pizza": 3,
        "Soup": 4,
        "Dessert": 2
    }

    posMealType = 0
    posProductType = 1

    dicMeals = {
        namePizza: [],
        nameSoup: [],
        nameDessert: []
    }

    for arg in arguments:
        if (arg == "Stop"):
            break
        strMealType = arg[posMealType]
        strProductType = arg[posProductType]

        if not (strProductType in dicMeals[strMealType]) and len(dicMeals[strMealType]) <= dicMealsMaxProducts[
            strMealType]:
            dicMeals[strMealType].append(strProductType)
            addedProductsCount = addedProductsCount + 1

    for lst in dicMeals.values():
        lst.sort()

    sortedByKey = sorted(dicMeals.items(), key=lambda item: item[0])
    sortedByValue = sorted(sortedByKey, key=lambda item: len(item[1]), reverse=True)

    if addedProductsCount == 0:
        return "No products in the cart!"
    else:
        result = ''
        for meal in sortedByValue:
            result += f'{meal[0]}:\n'
            products = meal[1]
            if products:
                for product in products:
                    result += f' - {product}\n'
        return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
