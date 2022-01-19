from flask import Flask, request, make_response, jsonify

# TODO check what __name__ return
# print(f"{__name__=}")

app = Flask(__name__)


@app.route("/")
def index():
    # print(request.headers)
    print(request.method)
    print(request.path)
    print(request.url)
    print(request.headers)
    print(request.headers["Authorization"])
    print(request.headers["Content-Type"])
    print(request.json)
    print(request.json["name"])
    print(request.json.get("age"))
    # response = make_response([{"id": 1, "title": "Title"}])
    # # set response header type to json
    # response.headers["Content-Type"] = "application/json"
    # jsonify automatically converts response to json
    response = jsonify([{"id": 1, "title": "Title"}])
    return response


if __name__ == '__main__':
    app.run(debug=True)
