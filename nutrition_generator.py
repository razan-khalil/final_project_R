def generate_nutrition_facts_and_advice(meal_plan):
    meals_text = "\n".join([f"{meal}: {desc}" for meal, desc in meal_plan.items()])

    prompt = f"""
You are a professional nutritionist AI. Analyze the following meal plan and:

1. Estimate total daily Calories, Proteins (g), Carbs (g), Fats (g).
2. Provide one short health advice for this meal plan.

Meal Plan:
{meals_text}

Respond in this format:
Calories:
Proteins (g):
Carbs (g):
Fats (g):
Health Advice:
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a nutrition assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    nutrition_info = response.choices[0].message.content
    return nutrition_info
