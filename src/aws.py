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
    try:
        req = requests.get(csv_url)
        url_content = req.content.decode("utf-8").split("\n")
        print(url_content[1])
        rows = [(row.strip()).split(",") for row in url_content]
        rows = rows[0:]
        return rows
    except Exception as e:
        raise ValueError(
            f"An error has occurred whilst pulling '{csv_url}' from bucket AWS"
        )