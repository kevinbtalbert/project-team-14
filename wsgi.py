from flaskr import create_app
from flaskr import config

# INITIALIZE APP WITH DEVELOPMENT CONFIGURATION
app = create_app(config.DevelopmentConfig)

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
