#!/usr/bin/env python3
from vectorcloud import app

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host="0.0.0.0")