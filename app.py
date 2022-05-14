from flask import Flask, render_template, request, url_for, send_file
import os
app = Flask(__name__)
PATH = os.path.join(os.getcwd(), 'files')

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/download",methods=['POST'])
def download():
    try:
        from main import youtube
        link = request.form.get("link")
        yt = youtube(link)
        image = yt.get_image()
        title = yt.get_title()
        reses = yt.get_video_info()
        return render_template("download.html", image_link = image, title=title, reses=reses, link=link)
    except:
        return render_template("error.html")

@app.route("/download_mp4", methods=['POST'])
def download_mp4():
    from main import youtube
    global PATH
    link = request.form.get("link")
    res = request.form.get('res')
    yt = youtube(link)
    name = yt.get_title() + f"{res}.mp4"
    yt.download_mp4(PATH, name, res)
    return send_file(PATH+"/"+name, as_attachment=True)
@app.route("/download_mp3", methods=['POST'])
def download_mp3():
    from main import youtube
    global PATH
    link = request.form.get("link")
    yt = youtube(link)
    name = yt.get_title() + ".mp3"
    yt.download_mp3(name, PATH)
    return send_file(PATH+"/"+name, as_attachment=True)

if __name__ == "__main__":
    app.debug = True
    app.run()
