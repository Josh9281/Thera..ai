from uagents import Agent, Context
import pandas as pd

agent = Agent()

@agent.on_event("startup")
async def handle_summary_request(ctx: Context):
    """
    Handle summarization requests with hardcoded data for mood counts and emotion categories.
    """
    try:
        # Hardcoded dashboard data
        data = {
            "mood": ["happy", "sad", "neutral", "angry", "happy", "neutral"],
            "count": [15, 7, 10, 5, 20, 12],
            "emotion_category": ["positive", "negative", "neutral", "negative", "positive", "neutral"],
            "timestamp": pd.date_range(start="2023-01-01", periods=6, freq="D")
        }
        dataframe = pd.DataFrame(data)

        # Additional chronological dataset for in-depth analysis
        chronological_data = {
            "date": pd.date_range(start="2023-01-01", periods=6, freq="D"),
            "events": ["meeting", "holiday", "work", "personal", "work", "holiday"],
            "stress_level": [3, 2, 5, 4, 3, 1]
        }
        chronological_dataframe = pd.DataFrame(chronological_data)

        # Join datasets on timestamp/date
        merged_data = dataframe.merge(chronological_dataframe, left_on="timestamp", right_on="date")

        # Summarize the data
        summary = {
            "mood_summary": dataframe.groupby("mood")["count"].sum().to_dict(),
            "emotion_category_summary": dataframe.groupby("emotion_category")["count"].sum().to_dict(),
            "stress_level_avg": merged_data["stress_level"].mean(),
            "null_counts": merged_data.isnull().sum().to_dict(),
            "data_types": merged_data.dtypes.astype(str).to_dict(),
        }

        ctx.logger.info(summary)
    except Exception as e:
        await ctx.error(f"Error processing the request: {str(e)}")

if __name__ == "__main__":
    agent.run()

