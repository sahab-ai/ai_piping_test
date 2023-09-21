import openai
from decouple import config
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()

OPENAI_API_KEY = config('OPEN_API_KEY')
openai.api_key = OPENAI_API_KEY

VALID_SEASONS = ["spring", "summer", "fall", "winter"]


class RecommendationRequest(BaseModel):
    country: str
    season: str


def generate_recommendations(country: str, season: str):
    if season.lower() not in VALID_SEASONS:
        raise HTTPException(status_code=400, detail="Invalid season. Must be one of: spring, summer, fall, winter")

    prompt = f"Recommend three things to do in {country} during {season}"

    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=250
        )

        recommendations = response.choices[0].text
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch recommendations from OpenAI: {str(e)}")


@app.get("/recommendations/")
def get_recommendations(country: str = Query(..., description="The country for recommendations"),
                               season: str = Query(..., description="The season for recommendations")):


    try:
        recommendations = generate_recommendations(country, season)
        return {"country": country, "season": season, "recommendations": recommendations}
    except HTTPException as e:
        raise e


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3000)
