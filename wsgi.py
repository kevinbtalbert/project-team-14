from flaskr import create_app
from flaskr import config

# INITIALIZE APP WITH DEVELOPMENT CONFIGURATION
application = create_app(config.ProductionConfig)

if __name__ == "__main__":
    application.run(host="localhost", port=8080, debug=True)
