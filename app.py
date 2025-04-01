from app import app
from app import app
from app.routers.euler_router import euler_bp
from app.routers.status_router import status_bp

app.register_blueprint(euler_bp, url_prefix='/')
app.register_blueprint(status_bp, url_prefix='/status')

print(app.url_map)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
