from app import app
from app import app
from app.routers.euler_router import euler_bp

app.register_blueprint(euler_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
