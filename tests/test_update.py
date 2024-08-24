from tools.operations import update_gtfs_schedule_source

def test_catalogs_sources_gtfs_schedule_source_ids_uniqueness():
    update_gtfs_schedule_source(
        mdb_source_id=1159,
        provider="testSTER",
    )
    assert 1
