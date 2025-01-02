# join_backend_app/firestore_service.py
from django.conf import settings
from google.cloud.firestore import Client

# Reference Firestore client
FIRESTORE_DB: Client = settings.FIRESTORE_DB

# CRUD Functions for Firestore
def add_document(collection_name, data):
    """Add a document to a Firestore collection."""
    doc_ref = FIRESTORE_DB.collection(collection_name).document()
    doc_ref.set(data)
    return doc_ref.id

def get_documents(collection_name):
    """Retrieve all documents from a Firestore collection."""
    collection_ref = FIRESTORE_DB.collection(collection_name)
    return [doc.to_dict() for doc in collection_ref.stream()]

def update_document(collection_name, doc_id, data):
    """Update a Firestore document by ID."""
    doc_ref = FIRESTORE_DB.collection(collection_name).document(doc_id)
    doc_ref.update(data)

def delete_document(collection_name, doc_id):
    """Delete a Firestore document by ID."""
    doc_ref = FIRESTORE_DB.collection(collection_name).document(doc_id)
    doc_ref.delete()