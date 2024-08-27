from app.utils.database import get_vocabulary_collection

def add_vocabulary(item):
    vocab_collection = get_vocabulary_collection()
    result = vocab_collection.insert_one(item.dict())
    return str(result.inserted_id)
