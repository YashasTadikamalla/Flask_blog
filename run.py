from flaskblog import create_app

app=create_app() # uses by default the config class

if __name__ == '__main__':
    app.run(debug=True)
