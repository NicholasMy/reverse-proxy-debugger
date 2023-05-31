import json
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"])
def index(path):
    r = request

    body = r.get_data()
    formatted_body = ""
    try:
        formatted_body = json.dumps(json.loads(body))
    except:
        try:
            formatted_body = body.decode("utf-8")
        except:
            formatted_body = "Unable to parse body"

    nice_data = {
        "url": r.url,
        "method": r.method,
        "path": r.path,
        "headers": dict(r.headers),
        "query_string": dict(r.args),
        "remote_addr": r.remote_addr,
        "remote_port": r.environ["REMOTE_PORT"],
        "raw_body": str(r.data),
        "formatted_body": formatted_body
    }
    raw_data = str(r.__dict__)

    print("===== Request Received =====")
    for k, v in nice_data.items():
        if k == "headers":
            print("headers:")
            for header, value in v.items():
                print(f"\t{header}: {value}")
        else:
            print(f"{k}: {v}")
    return render_template("index.html", nice=nice_data, raw=raw_data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
