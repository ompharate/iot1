from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://om:pharate11@cluster0.btaiygi.mongodb.net")  

db = client['pymongo']

collection = db['users']

def create_document():
    document = {
        "name": input("Enter name: "),
        "age": int(input("Enter age: ")),
        "city": input("Enter city: ")
    }
    result = collection.insert_one(document)
    print(f"Document inserted with ID: {result.inserted_id}")

def read_documents():
    cursor = collection.find({})
    for doc in cursor:
        print(doc)

def update_document():
    doc_id = input("Enter the ID of the document to update: ")
    field = input("Enter the field to update (name, age, city): ")
    new_value = input("Enter the new value: ")

    update_query = {"$set": {field: new_value}}
    result = collection.update_one({"_id": ObjectId(doc_id)}, update_query)
    if result.modified_count > 0:
        print(f"Document with ID {doc_id} updated.")
    else:
        print("No document updated.")


def delete_document():
    doc_id = input("Enter the ID of the document to delete: ")
    result = collection.delete_one({"_id": ObjectId(doc_id)})
    if result.deleted_count > 0:
        print(f"Document with ID {doc_id} deleted.")
    else:
        print("No document found with the given ID.")


def switch_case(choice):
    switch = {
        '1': create_document,
        '2': read_documents,
        '3': update_document,
        '4': delete_document
    }
  
    func = switch.get(choice, lambda: print("Invalid choice"))
    func()

if __name__ == '__main__':
    while True:
        print("\n--- MongoDB CRUD Operations ---")
        print("1. Create Document")
        print("2. Read Documents")
        print("3. Update Document")
        print("4. Delete Document")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Exiting...")
            break
        else:
            switch_case(choice)
