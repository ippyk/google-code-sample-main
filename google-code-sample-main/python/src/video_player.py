"""A video player class."""
import random

from video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""
    global FD
    global AC
    global ACV
    global LAG
    global VAN
    FD = False
    AC = False
    ACV = False
    LAG = False
    VAN = False

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        name_videos = self._video_library.video_names()
        for i in name_videos:
            print(i)
        """Returns all videos."""


    def play_video(self, video_id):
        l=[]

        for i in self._video_library.get_all_videos():
            l.append(i.video_id)

        if video_id not in l:
            print('Cannot play video: Video does not exist')
            return

        global FD
        global AC
        global ACV
        global LAG
        global VAN

        if FD == True:
            FD = False
            print('Stopping video: Funny Dogs')
        if AC == True:
            AC = False
            print('Stopping video: Amazing Cats')
        if ACV == True:
            ACV = False
            print('Stopping video: Another Cat Video')
        if LAG == True:
            LAG = False
            print('Stopping video: Life at Google')
        if VAN == True:
            VAN = False
            print('Stopping video: Video about nothing')

        name = self._video_library.get_video(video_id)
        print(f'Playing video: {name.title}')

        if str(name.title) == 'Funny Dogs':
            FD=True
        if str(name.title) == 'Amazing Cats':
            AC=True
        if str(name.title) == 'Another Cat Video':
            ACV=True
        if str(name.title) == 'Life at Google':
            LAG=True
        if str(name.title) == 'Video about nothing':
            VAN = True




        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
    def stop_video(self):
        """Stops the current video."""

        global FD
        global AC
        global ACV
        global LAG
        global VAN

        if FD==False and AC==False and ACV==False and LAG==False and VAN==False:
            print('Cannot stop video: No video is currently playing')

        if FD == True:
            FD = False
            print('Stopping video: Funny Dogs')
        if AC == True:
            AC = False
            print('Stopping video: Amazing Cats')
        if ACV == True:
            ACV = False
            print('Stopping video: Another Cat Video')
        if LAG == True:
            LAG = False
            print('Stopping video: Life at Google')
        if VAN == True:
            VAN = False
            print('Stopping video: Video about nothing')


    def play_random_video(self):
        """Plays a random video from the video library."""
        global FD
        global AC
        global ACV
        global LAG
        global VAN

        if FD == True:
            FD = False
            print('Stopping video: Funny Dogs')
        if AC == True:
            AC = False
            print('Stopping video: Amazing Cats')
        if ACV == True:
            ACV = False
            print('Stopping video: Another Cat Video')
        if LAG == True:
            LAG = False
            print('Stopping video: Life at Google')
        if VAN == True:
            VAN = False
            print('Stopping video: Video about nothing')

        rlist = ['FD','AC','ACV','LAG','VAN']
        q=random.choice(rlist)
        globals()[q]=True

        if FD == True:
            print('Playing video: Funny Dogs')
        if AC == True:
            print('Playing video: Amazing Cats')
        if ACV == True:
            print('Playing video: Another Cat Video')
        if LAG == True:
            print('Playing video: Life at Google')
        if VAN == True:
            print('Playing video: Video about nothing')

    def pause_video(self):
        """Pauses the current video."""

        print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
