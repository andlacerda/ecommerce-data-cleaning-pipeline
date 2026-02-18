import kagglehub as kh
import os
import sys
import zipfile

def run_ingestion():
    try :
        # Set your Kaggle API token here
        TOKEN_NUMBER = "PLACE YOUR TOKEN NUMBER HERE..."

        # Token Configuration
        os.environ["KAGGLE_API_TOKEN"] = TOKEN_NUMBER

        # Download the File
        path = kh.dataset_download("olistbr/brazilian-ecommerce",
                                path="olist_orders_dataset.csv")
        destination = "../data/raw/olist_orders_dataset.zip"

        # Moving the File
        os.makedirs("../data/raw",exist_ok=True)

        # Remove existing file to avoid conflicts
        if os.path.exists(destination):
            os.remove(destination)

        # Move downloaded file to the raw data folder
        os.rename(path,destination)

        # Extract the zip file and then delete the zip
        with zipfile.ZipFile(destination, 'r') as zip_ref:
            zip_ref.extractall("../data/raw/")
            print(f"File Extracted Sucess.")
        
        if os.path.exists(destination):
            os.remove(destination)
            print("Zip file removed")

        print(f"Ingestion completed successfully: {destination}")

    except Exception as e:
        # Error handling: execute if the ingestion fails
        print(f"Error during ingestion process: {e}")
        # Terminate execution with error code
        sys.exit(1)

if __name__ == "__main__":
    run_ingestion()