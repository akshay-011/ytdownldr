class youtube(object):
    def __init__(self, link):
        from pytube import YouTube
        self.link = link
        self.yt = YouTube(self.link)
    def get_image(self):
            image = self.yt.thumbnail_url
            return image
    def get_title(self):
        title = self.yt.title
        return title
    def get_video_info(self):
        info = self.yt.streams.filter(file_extension="mp4")
        res = []
        for i in info:
            ch = str(i.resolution)
            if not ch in res and not ch == 'None':
                ch = int(ch[:-1])
                res.append(ch)
            res = list(set(res))
            res = sorted(res)
        return res[0:-1]
    def download_mp3(self, file_name, path):
        self.path = path
        self.file_name = file_name
        file = self.yt.streams.get_audio_only()
        file.download(filename=self.file_name, output_path=self.path)
    def download_mp4(self, path, file_name, res='720p' ):
        self.path = path
        self.res = res
        self.file_name = file_name
        try:
            file = self.yt.streams.get_by_resolution(resolution=self.res)
            file.download(filename=self.file_name, output_path=self.path)
        except:
            file = self.yt.streams.get_highest_resolution()
            file.download(filename=self.file_name, output_path=self.path)