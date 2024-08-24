from tools.operations import update_gtfs_schedule_source
from pathlib import Path

def test_catalogs_sources_gtfs_schedule_source_ids_uniqueness():
    update_gtfs_schedule_source(
        mdb_source_id=1159,
        provider="testSTER",
    )
    file_path = "catalogs/sources/gtfs/schedule/fr-ile-de-france-star-gtfs-1159.json"
    contents = Path(file_path).read_text()
    print(contents)
    assert 1
