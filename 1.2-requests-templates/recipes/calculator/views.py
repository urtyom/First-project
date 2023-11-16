from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def calculate_recipe(request):
    # Получить название рецепта из запроса, например: /recipe?name=omlet
    recipe_name = request.GET.get('name', None)
    
    # Получить количество порций из опционального параметра servings
    servings = int(request.GET.get('servings', 1))
    
    if recipe_name is None or recipe_name not in DATA:
        # Если название рецепта не указано или не найдено в данных
        context = {
            'recipe': None
        }
    else:
        # Иначе, получить рецепт из данных
        recipe = DATA[recipe_name]
        
        # Создать новый словарь с учетом количества порций
        adjusted_recipe = {}
        for ingredient, quantity in recipe.items():
            adjusted_quantity = quantity * servings
            adjusted_recipe[ingredient] = adjusted_quantity
        
        context = {
            'recipe': adjusted_recipe
        }
    
    return render(request, 'calculator/index.html', context)
