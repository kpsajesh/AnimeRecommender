import pandas as pd
from utils.custom_exception import CustomException
from utils.logger import get_logger

logger = get_logger(__name__)

class AnimeDataLoader:
    def __init__(self, original_csv: str, processed_csv: str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        try:
            
            logger.info("Loading and processing csv...")

            df = pd.read_csv(self.original_csv, encoding='utf-8', on_bad_lines='skip').dropna()
            #df = pd.read_csv(self.original_csv, encoding='utf-8', error_bad_lines=False).dropna()
            required_columns = {'Name','Genres','sypnopsis'}
            logger.info(f"Read the csv")
            
            missing = required_columns - set(df.columns)
            if missing:
                raise ValueError(f"Missing required columns: {missing}")
                logger.info("Missing required columns in csv...")

            df['combined_info'] = (
                "Title: " + df['Name'] + ' Overview: ' + df['sypnopsis'] + " Genres: " + df['Genres'] 
            )
            df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8')
            logger.info("Processed csv and saved...")
            return self.processed_csv
        except Exception as e:
                logger.error(f"Failed to read and process csv {str(e)}", exc_info=True)
                raise CustomException("Error during pipeline " , e)
    