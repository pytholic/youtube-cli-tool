from pytube import YouTube
from pytube.cli import on_progress


def download_video(link: str, save_path: str) -> None:
    """Utility to download youtube video with highest reolution.

    Parameters
    ----------
    link : str
        Address of th youtube video.
    save_path: str
        Location to save the output file.
    """
    try:
        # create youtube object
        yt = YouTube(
            link,
            on_progress_callback=on_progress,
        )
        # get highest resolution
        stream = yt.streams.get_highest_resolution()
        # download the video
        stream.download(output_path=save_path)
        print("Download completed successfully!")
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=9dSkvxS2EB0&ab_channel=YannicKilcher"
    save_path = "../tmp/"
    download_video(video_url, save_path)
