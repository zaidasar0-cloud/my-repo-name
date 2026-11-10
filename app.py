import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# Sample initial data for houses
houses = [
    {
        "id": 1,
        "title": "Modern Suburban Villa",
        "price": "$250,000",
        "location": "Addis Ababa",
        "type": "For Sale",
    },
    {
        "id": 2,
        "title": "Cozy City Apartment",
        "price": "$120,000",
        "location": "Bole",
        "type": "For Sale",
    },
]


@app.route("/")
def index():
  return render_template("index.html", houses=houses)


@app.route("/add", methods=["POST"])
def add_house():
  title = request.form.get("title")
  price = request.form.get("price")
  location = request.form.get("location")
  listing_type = request.form.get("type")

  if title and price:
    new_house = {
        "id": len(houses) + 1,
        "title": title,
        "price": price,
        "location": location,
        "type": listing_type,
    }
    houses.append(new_house)

  return redirect(url_for("index"))


if __name__ == "__main__":
  # Use Render's dynamic port if available, otherwise default to 5000 locally
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)
