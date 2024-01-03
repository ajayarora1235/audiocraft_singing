import gdown

def download_model():
    url = 'https://drive.google.com/uc?id=1S79T3XlPFosbhXgVO8h3GeBJSu43Sk-O'
    output = 'model_ckpts/drumsep_ckpt.th'
    gdown.download(url, output, quiet=False)

download_model()
