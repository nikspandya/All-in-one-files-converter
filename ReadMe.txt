# All in one file converter:

User can convert any file with  '.pdf', .jpg', '.png', '.bmp', '.ppm', '.gif', '.tiff' file extensions to '.jpg', '.png', '.bmp', '.ppm', '.gif', '.tiff' file formates. 


# Running App using docker
Install [docker](https://docs.docker.co) and [docker compose](https://docs.docker.com/compose/).

Then run the following cmd from the root folder

     docker-compose up or $ docker-compose -d to run in the background

This will start the backend to receive endpoint requests from the frontends.


# Running backend App manually  
Please use the following steps to use API manually 
1. Install [python 3.7](https://www.python.org/downloads/) or higher
2. Install and create new [conda](https://docs.conda.io/en/latest/miniconda.html) isolated env or [python virtual env](https://docs.python.org/3/tutorial/venv.html) 
3. Then from /app run `pip install -r requirements.txt`. it will install all required dependency
4. From /app run `test.py` for testing and `run.py` for App uses


# Usage

* After running the app go to the browser and open http://localhost:8610
* Select and upload files from allowed file types
* Select the output file formats
* Press the convert button which converts your file to the requested file formats
* Converted file will be stored in the `/app/api/example_files` folder
