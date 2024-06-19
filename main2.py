import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzE4NzkxMTk1LCJpYXQiOjE3MTg3OTA4OTUsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjU4NjQyNWU3LWFlZjAtNGFjNS1hNWE4LWUxNzBhZjFjMTMyMSIsInN1YiI6IlByYWhhcnNoLnNpbmdoQHMuYW1pdHkuZWR1In0sImNvbXBhbnlOYW1lIjoiQW1pdHkgVW5pdmVyc2l0eSIsImNsaWVudElEIjoiNTg2NDI1ZTctYWVmMC00YWM1LWE1YTgtZTE3MGFmMWMxMzIxIiwiY2xpZW50U2VjcmV0IjoiUVNNZlRub1Z6aEV1SnhsRCIsIm93bmVyTmFtZSI6IlByYWhhcnNoIFJhaiBTaW5naCIsIm93bmVyRW1haWwiOiJQcmFoYXJzaC5zaW5naEBzLmFtaXR5LmVkdSIsInJvbGxObyI6IkE2MDIwNTIyMTIyOCJ9.krkoIgRd3IyDSsSa0-wqzGtjus-7oQQ0vnGo951e3Mw"
headers = {'Authorization': f'Bearer {token}'}

companies = ["AMZ", "FLP", "SNP", "MYN", "AZO"]
categories = ["Phone", "Computer", "TV", "Earphone", "Tablet", "Charger", "Mouse", "Keypad", "Bluetooth",
              "Pendrive", "Remote", "Speaker", "Headset", "Laptop", "PC"]

@app.route('/test/companies/<string:companyname>/categories/<string:categoryname>/products', methods=['GET'])
def get_products(companyname, categoryname):
    top_n = request.args.get('top', type=int, default=10)
    min_price = request.args.get('minPrice', type=int, default=0)
    max_price = request.args.get('maxPrice', type=int, default=float('inf'))

    if companyname not in companies or categoryname not in categories:
        return jsonify({"error": "Invalid company or category"}), 400

    test_server_url = f"http://20.244.56.144/test/companies/{companyname}/categories/{categoryname}/products?top={top_n}&minPrice={min_price}&maxPrice={max_price}"
    response = requests.get(test_server_url,headers=headers)

    if response.status_code == 200:
        products = response.json()
        return jsonify(products)
    else:
        return jsonify({"error": "Error fetching data from test server"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)