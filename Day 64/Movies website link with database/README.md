# Movies Website having Database and also we can delete and update details.


## Steps to follow:
1. Create an SQLite database with SQLAlchemy.The database needs to contain a "Movie" Table.

	We can create a database table by creating a class and columns as shown below. Movie is table name while id ,title etc are column in movies table.

        class Movie(db.Model):
            id = db.Column(db.Integer,primary_key=True)
            title = db.Column(db.String(250), unique=True, nullable=False)
        db.create_all()

    We can Add new movie by following code.

        new_movie = Movie(
        title="Phone Booth")
        db.session.add(new_movie)
        #db.session.commit()

    Our new movie data add in database.

2. Edit movie Rating and Review

    For this we create a WTFquick_form, which take data from html page and we do changes in database.

    Use following line of code to get data from database.
      
        Movie.query.get(movie_id)
    
    And geting data from FORM 

        form.rating.data

    Then do db.session.commit() for all changes.

3. For deleting Data from Database

        db.session.delete(movie)

    We use this query to delete.

4. For Sorting the list we use order_by query.

        Movie.query.order_by(Movie.rating).all()