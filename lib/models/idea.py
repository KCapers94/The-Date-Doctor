from models.__init__  import CURSOR, CONN
from models.category import Category


class Idea:

    all = {}

    def __init__(self, date_idea, category_id, date_details= None, id= None):
        self.id = id
        self.date_idea = date_idea
        self.category_id = category_id 
        self.date_details = date_details
       

    #def __repr__(self):
        #return (
            #f"{self.date_idea}-{self.restaurant_type}" 
        #)

    

    @property
    def date_idea(self):
        return self._date_idea
    
    @date_idea.setter
    def date_idea(self, date):
        if isinstance(date, str) and len(date):
            self._date_idea = date
        else:
            raise ValueError("Invalid input")
        
    @property
    def date_details(self):
        return self._date_details
    
    @date_details.setter
    def date_details(self, type):
        if isinstance(type, str) and len(type):
            self._date_details = type
        else:
            raise ValueError("Invalid input")
        
    @property
    def category_id(self):
        return self._category_id
    
    @category_id.setter
    def category_id(self, category_id):
        if type(category_id) is int and Category.find_by_id(category_id):
            self._category_id = category_id
        else:
            raise ValueError("category_id must reference an established category")
        


    @classmethod
    def create_table(cls):

        sql = """
            CREATE TABLE IF NOT EXISTS ideas (
            id INTEGER PRIMARY KEY,
            date_idea TEXT,
            category_id INTEGER,
            date_details TEXT,
            FOREIGN KEY (category_id) REFERENCES categories(id)
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):

        sql = """
            DROP TABLE IF EXISTS ideas;
        """

        CURSOR.execute(sql)
        CONN.commit()

    

    def save(self):

        sql = """
            INSERT INTO ideas (date_idea, category_id, date_details)
            VALUES(?, ?, ?)
        """

        CURSOR.execute(sql, (self.date_idea, self.category_id, self.date_details,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):

        sql = """
            UPDATE ideas
            SET date_idea = ?, category_id = ?, date_details = ?
            WHERE id = ?
        """

        CURSOR.execute(sql,( self.date_idea, self.category_id, self.date_details, self.id))

        CONN.commit()
    
    def delete(self):

        sql = """
            DELETE FROM ideas
            WHERE id = ?
        """

        CURSOR.execute(sql,(self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None


    @classmethod
    def create(cls, date_idea, category_id, date_details):

        idea = cls(date_idea, category_id, date_details)
        idea.save()
        return idea
    
    @classmethod
    def instance_from_db(cls, row):

        idea = cls.all.get(row[0])
        if idea:
            idea.date_idea = row[1]
            idea.category_id = row[2]
            idea.date_details = row[3]
        else:
            idea = cls(row[1], row[2], row[3])
            idea.id = row[0]
            cls.all[idea.id] = idea
        
        return idea
    
    @classmethod
    def get_all(cls):

        sql = """
            SELECT *
            FROM ideas
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]


    @classmethod
    def find_by_id(cls, id):

        sql = """
            SELECT *
            FROM ideas
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

    @classmethod
    def find_by_name(cls, date_idea):

        sql = """
            SELECT *
            FROM ideas
            WHERE date_idea is ?
        """

        row = CURSOR.execute(sql, (date_idea,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_category_id(cls, category_id):
        sql = """
            SELECT *
            FROM ideas
            WHERE category_id = ?
        """
        rows = CURSOR.execute(sql, (category_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]


    

    # Welcome

    #1)Categories
    #2)Exit program
    

    #1)Restaurant
         #view all ideas
         #add 
         #delete
         #exit

    #2)Activites
        #name
         #add
         #delete
         #exit
    #3)Gifts
        #name
         #add
         #delete
         #exit

    #a)Add Category 
    #d)Delete Category
    #0)exit