# skin_beauty_tips/manager.py

from skin_beauty_tips.makeup_artist import generate_makeup_advice
from skin_beauty_tips.skincare_consultant import generate_skincare_advice
from skin_beauty_tips.beauty_trends_expert import generate_beauty_trends
from skin_beauty_tips.product_recommender import generate_product_recommendations

async def Distributed_task(user_input: str):
    # Call all agents and collect responses
    makeup = await generate_makeup_advice(user_input)
    skincare = await generate_skincare_advice(user_input)
    trends = await generate_beauty_trends(user_input)
    products = await generate_product_recommendations(user_input)

    return {
        "Makeup Tips": makeup.final_output,
        "Skincare Advice": skincare.final_output,
        "Trends": trends.final_output,
        "Product Recommendations": products.final_output
    }
