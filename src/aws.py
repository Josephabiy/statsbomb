""" Interact with files in S3"""
import requests


def pull(csv_url):
    """
    Pulls Object from specified S3 bucket and removes header row

    Args:
            bucket (str): GCS Bucket
            obj_name (str):  Object name
    Return:
    """
    req = requests.get(csv_url)
    url_content = req.content.decode("utf-8").split("\n")
    rows = [row.split(",") for row in url_content]
    rows = rows[1:]
    return rows
