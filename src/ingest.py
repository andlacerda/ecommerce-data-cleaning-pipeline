import kagglehub as kh
import os

# Coloque seu token diretamente aqui
TOKEN_NUMBER = "PLACE YOUR TOKEN NUMBER HERE..."

# Token Configuration
os.environ["KAGGLE_API_TOKEN"] = TOKEN_NUMBER

# Download the File
path = kh.dataset_download("olistbr/brazilian-ecommerce",
                            path="olist_orders_dataset.csv")

print("Path to dataset files:", path)
