# Docker with simple web app

2. In this directory, build the image:
```
docker build -t flask-app -f docker/Dockerfile .
```

3. Start it up:
```
docker run -p 8000:8000 flask-app
```

4. Go to http://localhost:8000 in your browser.