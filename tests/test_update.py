import os
from tools.operations import update_gtfs_schedule_source
from pathlib import Path

def test_catalogs_sources_gtfs_schedule_source_ids_uniqueness():
    response = update_gtfs_schedule_source(
        mdb_source_id=1159,
        direct_download_url="https://eu.ftp.opendatasoft.com/star/gtfs/GTFS_1_20240820_20240901_20240819145156.zip",
    )
    file_path = "catalogs/sources/gtfs/schedule/fr-ile-de-france-star-gtfs-1159.json"
    contents = Path(file_path).read_text()
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f :
        print("Response: " + response + "\nContents: " + contents, file=f)
    assert 1
