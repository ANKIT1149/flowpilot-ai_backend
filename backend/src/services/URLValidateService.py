import yt_dlp
from fastapi import HTTPException
from backend.src.core.logging import logger
from backend.src.model.URLValidateModel import ChannelPreview, VideoPreview


async def validate_url(url: str):
    logger.info(f"Validating URL: {url}")
    ydl = yt_dlp.YoutubeDL(
        {
            "quiet": True,
            "extract_flat": True,
            "playlist_items": "0",
        }
    )

    logger.info(f"Extracting video information...: {ydl}")

    try:
        info = ydl.extract_info(url, download=False)
        info.get("_type")
        if info.get("_type") == "playlist":
            return ChannelPreview(
                channel_id=info["channel_id"],
                channel_name=info["channel"],
                channel_url=info["channel_url"],
                subscriber_count=info["channel_follower_count"],
                video_count=info.get("playlist_count") or info.get("n_entries"),
                verified=info["channel_is_verified"],
            )

        else:
            print(info.keys())
            print(info.get("_type"))

            logger.info(
                f"Video information extracted successfully: {info.get('player_url', 'N/A')}"
            )

            return VideoPreview(
                id=info["id"],
                title=info["title"],
                thumbnail=info["thumbnail"],
                duration=info["duration"],
                channel=info["channel"],
                channel_url=info.get("channel_url"),
                webpage_url=info.get("webpage_url"),
                verified=info["channel_is_verified"],
                views=info["view_count"],
                upload_date=info["upload_date"],
            )
    except Exception as e:
        logger.error(f"yt-dlp error: {e}")
        return HTTPException(
            status_code=400,
            detail="Invalid URL or unable to extract video information.",
        )
