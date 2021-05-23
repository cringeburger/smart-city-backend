from resources import app, host_val


if __name__ == "__main__":
    app.run(host_val, port=5000, debug=True)
