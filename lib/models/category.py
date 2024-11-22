# lib/models/Category.py
from models.__init__ import CURSOR, CONN

class Category:

    all = {}
    

    def __init__(self,name, id= None):
        self.id = id
        self.name = name
        

    def __repr__(self):
        return f"{self.id}: {self.name}"

    @property
    def name(self):
        return self._name



    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Input is invalid")
    

    @classmethod
    def create_table(cls):

        sql = """
            CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):

        sql = """
            DROP TABLE IF EXISTS categories;
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        

        sql = """
            INSERT INTO categories (name)
            VALUES(?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        print("Works fine now")

    @classmethod
    def create(cls, name):

        category = cls(name)
        category.save()

        return category
    
    def update(self):

        sql = """
            UPDATE categories
            SET name = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

    def delete(self):

        sql = """
            DELETE FROM categories
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None


    @classmethod
    def instance_from_db(cls, row):

        category = cls.all.get(row[0])
        if category:
            category.name = row[1]
        else:
            category = cls(row[1], id = row[0])
            cls.all[category.id] = category
        return category

    @classmethod
    def get_all(cls):

        sql = """
            SELECT *
            FROM categories
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    

    @classmethod
    def find_by_id(cls, id):

        sql = """
            SELECT *
            FROM categories
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):

        sql = """
            SELECT *
            FROM categories
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

    def ideas(self):

        from models.idea import Idea
        sql = """
            SELECT *FROM ideas
            WHERE category_id = ?
        """ 

        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Idea.instance_from_db(row) for row in rows
        ]





 