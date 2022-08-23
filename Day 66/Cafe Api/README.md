# Cafe Api Generation
We generate our own Api in this file you will understand how to generate REST api and CURD functionality like Create,Updata, read and Delete data from Api.

## Steps To follow
1. For cafes first generate a random cafe from database and When Someone do GET request to /random route then it fetch all data from database related to that random cafe.
2. Because our server is now acting as an API, we want to return a JSON. We do this through Serialization in which object convert into JSON. We use [jsonify()](https://www.adamsmith.haus/python/docs/flask.jsonify).
   When a GET request is made to this /all route, your server should return all the cafes in your database as a JSON.

           @app.route("/all")
             def get_all_cafes():
                cafes = db.session.query(Cafe).all()
                return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

3. Create a /search route to search for cafes at a particular location.

4. Use [POSTMAN](https://learning.postman.com/docs/publishing-your-api/documenting-your-api/) To check all your api functionality is working or not.

5. Create a PATCH request route in main.py to handle PATCH requests to our API. In order for our API to be RESTful, ideally, the route should be something like this:
/update-price/<cafe_id>. The following code used to update the id 22 price.
          
        localhost:5000/update-price/22
6. If Cafe is closed, DELETE request to our server and update the database it only work when a secret key is given to it. DELETE route to /report-closed/<cafe_id>
7. When someone makes a GET request to the /random route, our Flask server should fetch a random cafe from our database