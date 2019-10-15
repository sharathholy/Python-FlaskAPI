from flask import Flask, request 

app = Flask(__name__)
HTTP_BAD_REQUEST = 400

@app.route('/',methods=['POST'])
def api_called():
    response=request.get_json(force=True)
    print(response)
    print ("hello world")


if __name__ == '__main__':
    app.run(debug=False)
