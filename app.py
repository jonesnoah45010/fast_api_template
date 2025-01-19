from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv

load_dotenv()

# Item model for single string processing
class Item(BaseModel):
	data: str

# Item model for list of strings processing
class ItemList(BaseModel):
	items: List[str]

app = FastAPI()


# Normal Post Endpoint
@app.post("/process_data")
def process_data(item: Item):
	processed_data = f"Received data: {item.data}"
	return {"message": "Data processed successfully", "processed_data": processed_data}



# POST endpoint for concurrent processing
@app.post("/process_data_concurrent")
def process_data_concurrent(item_list: ItemList):

	def process_item(item):
		return item + " was processed"

	with ThreadPoolExecutor() as executor:
		# Submit each item for processing in a separate thread
		future_to_item = {}
		for item in item_list.items:
			future = executor.submit(process_item, item)  # Submit the task
			future_to_item[future] = item  # Store the future and the item

		results = []
		for future in as_completed(future_to_item):
			result = future.result()
			results.append(result)
	return {"message": "Data processed successfully", "processed_data": results}


















