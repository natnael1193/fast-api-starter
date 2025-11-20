from src.utils.router import router

# Define the router for video-related endpoints
video_router = router(tag="Videos")



@video_router.get("/videos")
def get_videos():
    return {"message": "List of videos"}