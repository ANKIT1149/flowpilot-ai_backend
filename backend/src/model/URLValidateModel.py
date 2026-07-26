from pydantic import BaseModel, HttpUrl

class VideoRequest(BaseModel):
    url: HttpUrl


class VideoPreview(BaseModel):
    id: str
    title: str
    thumbnail: str
    duration: int
    channel: str
    channel_url: str | None
    webpage_url: str | None
    verified: bool
    views: int
    upload_date: str
    timestamp: int


class ChannelPreview(BaseModel):
    channel_id: str
    channel_name: str
    channel_url: HttpUrl

    subscriber_count: int | None = None
    video_count: int | None = None

    verified: bool = False
