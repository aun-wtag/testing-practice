from features.fetch import get_data
from features.transform import process

def run_pipeline():
    data = get_data()
    return process(data)