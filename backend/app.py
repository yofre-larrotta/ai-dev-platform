"""
Main Flask Application
"""
import logging
import os
from flask import Flask
from flask_cors import CORS
from integrations.code_executor import CodeExecutor
from integrations.git_integration import GitManager
from plugins.plugin_manager import PluginManager

# Configure logging
logging.basicConfig(
    level=os.getenv('LOG_LEVEL', 'INFO'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize managers
code_executor = CodeExecutor()
git_manager = GitManager()
plugin_manager = PluginManager()

def create_app():
    """Application factory"""
    app = Flask(__name__)
    CORS(app)
    
    app.config['JSON_SORT_KEYS'] = False
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    
    # Store managers in app context
    app.code_executor = code_executor
    app.git_manager = git_manager
    app.plugin_manager = plugin_manager
    
    # Register blueprints
    from routes.code_execution import code_bp
    from routes.git_operations import git_bp
    from routes.plugins import plugin_bp
    from routes.todos import todo_bp
    
    app.register_blueprint(code_bp, url_prefix='/api/execute')
    app.register_blueprint(git_bp, url_prefix='/api/git')
    app.register_blueprint(plugin_bp, url_prefix='/api/plugins')
    app.register_blueprint(todo_bp, url_prefix='/api/todos')
    
    # Health check endpoint
    @app.route('/api/health', methods=['GET'])
    def health_check():
        return {
            "status": "healthy",
            "service": "AI Dev Platform",
            "version": "1.0.0"
        }, 200
    
    logger.info("Flask application initialized")
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)