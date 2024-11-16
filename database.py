import pyrebase
from config import get_firebase_config

class Database:
    config = get_firebase_config()
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    # datapenduduk
    @staticmethod
    def get_all_products():
        try:
            products = Database.db.child("datapenduduk").get()
            if products.each():
                return [(product.key(), product.val()) for product in products.each()]
            return []
        except Exception as e:
            print(f"Error getting products: {e}")
            return []

    @staticmethod
    def add_product(product_data):
        try:
            return Database.db.child("datapenduduk").push(product_data)
        except Exception as e:
            print(f"Error adding product: {e}")
            raise e

    @staticmethod
    def update_product(product_id, product_data):
        try:
            return Database.db.child("datapenduduk").child(product_id).update(product_data)
        except Exception as e:
            print(f"Error updating product: {e}")
            raise e

    @staticmethod
    def delete_product(product_id):
        try:
            return Database.db.child("datapenduduk").child(product_id).remove()
        except Exception as e:
            print(f"Error deleting product: {e}")
            raise e
        
    # datacalonrt
    @staticmethod
    def get_all_calonrts():
        try:
            calonrts = Database.db.child("datacalonrt").get()
            if calonrts.each():
                return [(calonrt.key(), calonrt.val()) for calonrt in calonrts.each()]
            return []
        except Exception as e:
            print(f"Error getting calonrts: {e}")
            return []

    @staticmethod
    def add_calonrt(calonrt_data):
        try:
            return Database.db.child("datacalonrt").push(calonrt_data)
        except Exception as e:
            print(f"Error adding calonrt: {e}")
            raise e

    @staticmethod
    def update_calonrt(calonrt_id, calonrt_data):
        try:
            return Database.db.child("datacalonrt").child(calonrt_id).update(calonrt_data)
        except Exception as e:
            print(f"Error updating calonrt: {e}")
            raise e

    @staticmethod
    def delete_calonrt(calonrt_id):
        try:
            return Database.db.child("datacalonrt").child(calonrt_id).remove()
        except Exception as e:
            print(f"Error deleting calonrt: {e}")
            raise e
        
    # datacalonrw  
    @staticmethod
    def get_all_calonrws():
        try:
            calonrws = Database.db.child("datacalonrw").get()
            if calonrws.each():
                return [(calonrw.key(), calonrw.val()) for calonrw in calonrws.each()]
            return []
        except Exception as e:
            print(f"Error getting calonrts: {e}")
            return []

    @staticmethod
    def add_calonrw(calonrw_data):
        try:
            return Database.db.child("datacalonrw").push(calonrw_data)
        except Exception as e:
            print(f"Error adding calonrw: {e}")
            raise e

    @staticmethod
    def update_calonrw(calonrw_id, calonrw_data):
        try:
            return Database.db.child("datacalonrw").child(calonrw_id).update(calonrw_data)
        except Exception as e:
            print(f"Error updating calonrw: {e}")
            raise e

    @staticmethod
    def delete_calonrw(calonrw_id):
        try:
            return Database.db.child("datacalonrw").child(calonrw_id).remove()
        except Exception as e:
            print(f"Error deleting calonrw: {e}")
            raise e
        

    # login user dari Firebase
    @staticmethod
    def get_product_by_name(nama):
        try:
            # Ambil data pengguna berdasarkan nama (username) dari Firebase
            user_data = Database.db.child("datapenduduk").order_by_child("nama").equal_to(nama).get()
            if user_data.each():
                return user_data.each()[0].val()  # Ambil data pengguna pertama yang cocok
            return None
        except Exception as e:
            print(f"Error getting user by name: {e}")
            return None