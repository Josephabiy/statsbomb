import requests
import logging

def pull(csv_url):
    """
    Pulls Object from specified S3 bucket and removes header row

    Args:
        csv_url (str): S3 bucket URL 
    Return:
        rows (list): returns a list of rows
    """
    try:
        req = requests.get(csv_url)
        url_content = req.content.decode("utf-8").split("\n")
        rows = [(row.strip()).split(",") for row in url_content]
        rows = rows[1:]
        logging.info(f" Sample pulled row from AWS: {rows[0]}")
        return rows

    except Exception as e:
        raise ValueError(
            f"An error has occurred whilst pulling '{csv_url}' from bucket AWS"
        )