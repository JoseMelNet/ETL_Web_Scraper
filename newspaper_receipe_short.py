import argparse
import logging
from urllib.parse import urlparse
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(filename):
    logger.info('Starting cleaning process')
    
    logger.info('Reading file {}'.format(filename))
    df = pd.read_csv(filename)
    
    logger.info('Extracting newspaper uid')
    newspaper_uid = filename.split('_')[0]
    
    logger.info('Newspaper uid detected: {}'.format(newspaper_uid))
    
    logger.info('Filling newspaper_uid column with {}'.format(newspaper_uid))
    df['newspaper_uid'] = newspaper_uid
    
    logger.info('Extracting host from urls')
    df['host'] = df['url'].apply(lambda url: urlparse(url).netloc)
    
    return df
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='The path to the dirty data',
                        type=str)

    args = parser.parse_args()

    df = main(args.filename)
    print(df)